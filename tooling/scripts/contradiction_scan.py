"""Contradiction scan — one-off LLM pass to surface logical conflicts in the KB.

Separate from linter.py because this one costs money. Intended to be run
manually when you want a fresh pass. Findings are advisory — the LLM can be
wrong, and "partial contradiction" often means productive tension, not error.

## What it does

For each pair of non-source entries where one [[wikilinks]] to the other,
ask Haiku: "do these two entries contradict each other?"

Verdicts: clear / partial / none. Non-"none" pairs are written to
`dist/contradiction-report.md` with the reasoning.

## Cost

At ~150 pairs × ~1500 tokens per call, a full run is roughly $0.20–0.40 on
Haiku. Hard cap enforced via --budget (default $1.00) and --max-pairs
(default 200).

## Usage

    python tooling/scripts/contradiction_scan.py --dry-run       # list pairs, no API calls
    python tooling/scripts/contradiction_scan.py                 # full run
    python tooling/scripts/contradiction_scan.py --max-pairs 20  # quick sample
    python tooling/scripts/contradiction_scan.py --budget 0.10
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

# Allow running as a standalone script.
_DIR = Path(__file__).resolve().parent
if str(_DIR) not in sys.path:
    sys.path.insert(0, str(_DIR))

from dotenv import load_dotenv  # noqa: E402
from kb_search import KB_ROOT, Entry, load_entries  # noqa: E402

# Load .env from the KB repo root (two levels up from this file).
# override=True because some shells (and `uv run`) pre-set ANTHROPIC_API_KEY
# to an empty string, which would otherwise block the value from .env.
load_dotenv(dotenv_path=KB_ROOT / ".env", override=True)

MODEL = "claude-haiku-4-5-20251001"
# Haiku pricing (USD per 1M tokens) — mirrors budget.py::MODEL_PRICING
INPUT_PRICE_PER_MTOK = 0.80
OUTPUT_PRICE_PER_MTOK = 4.00

DIST_DIR = KB_ROOT / "dist"
REPORT_PATH = DIST_DIR / "contradiction-report.md"
LOG_PATH = DIST_DIR / "contradiction-scan.log.json"


SYSTEM_PROMPT = """\
You are a coherence reviewer for a structured knowledge base on how AI affects \
human thinking. Given two KB entries, determine whether they contradict each \
other — where contradiction means they make claims that cannot both be true, \
use the same term with incompatible meanings, or prescribe mutually \
inconsistent guidance.

Productive tension is NOT contradiction. Two entries can describe different \
facets of the same phenomenon, different contexts, or trade-offs without \
contradicting. Default to 'none' unless the conflict is clear.

## Output format
Return valid JSON only, no markdown wrapping:

{
  "verdict": "clear" | "partial" | "none",
  "reason": "one concise sentence explaining the verdict",
  "quoted_a": "short direct quote from entry A (or empty)",
  "quoted_b": "short direct quote from entry B (or empty)"
}
"""


@dataclass
class PairFinding:
    a: str
    b: str
    verdict: str
    reason: str
    quoted_a: str = ""
    quoted_b: str = ""
    cost_usd: float = 0.0


def find_pairs(entries: dict[str, Entry]) -> list[tuple[str, str]]:
    """Return sorted unique pairs of non-source entries linked via wikilinks."""
    pairs: set[tuple[str, str]] = set()
    for stem_a, entry_a in entries.items():
        if entry_a.type == "source":
            continue
        for target in entry_a.wikilinks:
            if target == stem_a:
                continue
            if target not in entries:
                continue
            if entries[target].type == "source":
                continue
            pair = tuple(sorted([stem_a, target]))
            pairs.add(pair)
    return sorted(pairs)


def _build_user_msg(entry_a: Entry, entry_b: Entry) -> str:
    return (
        f"## Entry A: {entry_a.stem}\n"
        f"Type: {entry_a.type}    Status: {entry_a.status}\n\n"
        f"{entry_a.body.strip()[:2500]}\n\n"
        f"---\n\n"
        f"## Entry B: {entry_b.stem}\n"
        f"Type: {entry_b.type}    Status: {entry_b.status}\n\n"
        f"{entry_b.body.strip()[:2500]}\n\n"
        f"---\n\n"
        f"Do these contradict? Respond with JSON only."
    )


def _extract_json(text: str) -> dict:
    raw = text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
        if raw.endswith("```"):
            raw = raw[: raw.rfind("```")]
    return json.loads(raw)


def check_pair(client, entry_a: Entry, entry_b: Entry) -> tuple[PairFinding, int, int]:
    import anthropic

    user_msg = _build_user_msg(entry_a, entry_b)
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
        )
        data = _extract_json(response.content[0].text)
        finding = PairFinding(
            a=entry_a.stem,
            b=entry_b.stem,
            verdict=str(data.get("verdict", "none")).lower(),
            reason=str(data.get("reason", "")),
            quoted_a=str(data.get("quoted_a", "")),
            quoted_b=str(data.get("quoted_b", "")),
        )
        return finding, response.usage.input_tokens, response.usage.output_tokens
    except (json.JSONDecodeError, anthropic.APIError, KeyError, IndexError) as exc:
        finding = PairFinding(
            a=entry_a.stem,
            b=entry_b.stem,
            verdict="error",
            reason=f"scan failed: {exc}",
        )
        return finding, 0, 0


def render_markdown(findings: list[PairFinding], total_pairs: int, total_cost: float) -> str:
    non_none = [f for f in findings if f.verdict not in ("none", "error")]
    errors = [f for f in findings if f.verdict == "error"]

    lines = [
        "# KB Contradiction Scan Report",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Model: {MODEL}",
        f"Pairs checked: {len(findings)} / {total_pairs}",
        f"Conflicts surfaced: {len(non_none)}",
        f"Errors: {len(errors)}",
        f"Total cost: ${total_cost:.4f}",
        "",
        "_Advisory output. The LLM can be wrong. Review before acting. 'Partial' often means productive tension, not a real conflict._",
        "",
    ]

    for verdict in ("clear", "partial"):
        items = [f for f in findings if f.verdict == verdict]
        lines.append(f"## {verdict.title()} ({len(items)})")
        lines.append("")
        if not items:
            lines.append("_none_")
            lines.append("")
            continue
        for f in items:
            lines.append(f"### `{f.a}`  ↔  `{f.b}`")
            lines.append(f"- **Reason:** {f.reason}")
            if f.quoted_a:
                lines.append(f"- Quote from A: _{f.quoted_a}_")
            if f.quoted_b:
                lines.append(f"- Quote from B: _{f.quoted_b}_")
            lines.append("")

    if errors:
        lines.append(f"## Errors ({len(errors)})")
        lines.append("")
        for f in errors:
            lines.append(f"- `{f.a}` ↔ `{f.b}`: {f.reason}")
        lines.append("")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="contradiction_scan",
        description="LLM pass over wikilinked entry pairs to surface contradictions.",
    )
    parser.add_argument("--max-pairs", type=int, default=200, help="Hard cap on pairs checked")
    parser.add_argument("--budget", type=float, default=1.00, help="USD budget cap; scan halts when exceeded")
    parser.add_argument("--dry-run", action="store_true", help="list pairs without calling the API")
    parser.add_argument("--out", default=str(REPORT_PATH))
    parser.add_argument("--log", default=str(LOG_PATH))
    args = parser.parse_args(argv)

    entries = load_entries()
    pairs = find_pairs(entries)

    if args.dry_run:
        print(f"Found {len(pairs)} wikilinked pairs across {len(entries)} entries")
        print(f"Would check: {min(len(pairs), args.max_pairs)} pairs")
        avg_tokens_per_call = 1500
        est_cost = (
            min(len(pairs), args.max_pairs)
            * avg_tokens_per_call
            * INPUT_PRICE_PER_MTOK
            / 1_000_000
        ) + (
            min(len(pairs), args.max_pairs)
            * 200
            * OUTPUT_PRICE_PER_MTOK
            / 1_000_000
        )
        print(f"Estimated cost: ~${est_cost:.4f}  (rough, assumes ~1500 input + ~200 output tokens per pair)")
        print()
        for a, b in pairs[: args.max_pairs]:
            print(f"  {a}  <->  {b}")
        return 0

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in environment", file=sys.stderr)
        return 2

    import anthropic

    client = anthropic.Anthropic()

    pairs_to_check = pairs[: args.max_pairs]
    print(
        f"[contradiction] Checking {len(pairs_to_check)}/{len(pairs)} pairs "
        f"(model={MODEL}, budget=${args.budget:.2f})"
    )

    findings: list[PairFinding] = []
    total_cost = 0.0
    total_input = 0
    total_output = 0

    for i, (stem_a, stem_b) in enumerate(pairs_to_check, 1):
        if total_cost >= args.budget:
            print(f"[contradiction] Budget ${args.budget:.2f} reached after {i - 1} pairs")
            break

        entry_a = entries[stem_a]
        entry_b = entries[stem_b]

        finding, in_tok, out_tok = check_pair(client, entry_a, entry_b)
        cost = (
            in_tok / 1_000_000 * INPUT_PRICE_PER_MTOK
            + out_tok / 1_000_000 * OUTPUT_PRICE_PER_MTOK
        )
        finding.cost_usd = round(cost, 6)
        total_cost += cost
        total_input += in_tok
        total_output += out_tok
        findings.append(finding)

        marker = {
            "clear": "!!",
            "partial": "?.",
            "none": " .",
            "error": "XX",
        }.get(finding.verdict, "??")
        print(
            f"  [{i:3d}/{len(pairs_to_check)}] {marker}  {stem_a}  <->  {stem_b}  "
            f"(${cost:.4f} total=${total_cost:.4f})"
        )

    report = render_markdown(findings, len(pairs), total_cost)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")

    log_path = Path(args.log)
    log_path.write_text(
        json.dumps(
            {
                "model": MODEL,
                "total_pairs_found": len(pairs),
                "pairs_checked": len(findings),
                "total_cost_usd": round(total_cost, 6),
                "total_input_tokens": total_input,
                "total_output_tokens": total_output,
                "budget_usd": args.budget,
                "findings": [asdict(f) for f in findings],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    non_none = sum(1 for f in findings if f.verdict not in ("none", "error"))
    print()
    print(f"[contradiction] Wrote report to {out_path}")
    print(f"[contradiction] Wrote log to {log_path}")
    print(f"[contradiction] Conflicts surfaced: {non_none}")
    print(
        f"[contradiction] Cost: ${total_cost:.4f}  "
        f"(tokens: {total_input} in, {total_output} out)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
