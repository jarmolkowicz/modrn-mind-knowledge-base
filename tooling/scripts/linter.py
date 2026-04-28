"""KB Linter — whole-KB health check over the Modern Mind Knowledge Base.

Runs a suite of pure-Python checks over every entry, aggregates findings into
a markdown report written to `private/lint-report.md`. No LLM calls — fast,
free, deterministic. Contradiction detection lives in a separate script
(`contradiction_scan.py`) because that one costs money.

## Checks

- broken_wikilinks  — [[links]] pointing to entries that don't exist
- orphans           — entries with zero inbound AND zero outbound wikilinks
                      (sources excluded — they're cited via frontmatter)
- uncited_sources   — source entries not referenced by any concept/method
- missing_related   — entry A mentions entry B's full title in body but
                      doesn't [[link]] to it
- frontmatter       — missing/invalid required fields

## Usage

    python tooling/scripts/linter.py                # full run, write report
    python tooling/scripts/linter.py --check orphans --check frontmatter
    python tooling/scripts/linter.py --stdout       # print to terminal
    python tooling/scripts/linter.py --json         # machine-readable output
"""

from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

# Allow running as a standalone script: add own directory to sys.path so
# `import kb_search` resolves even when there's no package context.
_DIR = Path(__file__).resolve().parent
if str(_DIR) not in sys.path:
    sys.path.insert(0, str(_DIR))

from kb_search import (  # noqa: E402
    KB_ROOT,
    VALID_AREAS,
    VALID_STATUSES,
    Entry,
    load_entries,
)

PRIVATE_DIR = KB_ROOT / "private"
REPORT_PATH = PRIVATE_DIR / "lint-report.md"


@dataclass
class Finding:
    check: str
    entry: str
    issue: str
    fix: str = ""


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


def check_broken_wikilinks(entries: dict[str, Entry]) -> list[Finding]:
    findings: list[Finding] = []
    for stem, entry in entries.items():
        for link in sorted(entry.wikilinks):
            if link not in entries:
                findings.append(
                    Finding(
                        check="broken_wikilinks",
                        entry=stem,
                        issue=f"links to [[{link}]] which does not exist",
                        fix=f"create '{link}' entry or fix typo in {Path(entry.path).name}",
                    )
                )
    return findings


def check_orphans(entries: dict[str, Entry]) -> list[Finding]:
    inbound: dict[str, set[str]] = {}
    for stem, entry in entries.items():
        for link in entry.wikilinks:
            inbound.setdefault(link, set()).add(stem)

    findings: list[Finding] = []
    for stem, entry in entries.items():
        if entry.type == "source":
            continue  # sources are checked separately
        has_in = bool(inbound.get(stem))
        has_out = bool(entry.wikilinks)
        if not has_in and not has_out:
            findings.append(
                Finding(
                    check="orphans",
                    entry=stem,
                    issue="no inbound or outbound wikilinks",
                    fix="add Related section, link from a related entry, or archive",
                )
            )
    return findings


def _normalize(s: str) -> str:
    """Lowercase + strip diacritics for robust substring matching."""
    return "".join(
        c for c in unicodedata.normalize("NFKD", s.lower()) if not unicodedata.combining(c)
    )


def check_uncited_sources(entries: dict[str, Entry]) -> list[Finding]:
    # Source stems follow `author-topic-year` convention. Concept/framework/
    # practice entries cite them either as [[wikilinks]] or as free-text
    # strings in the `sources:` frontmatter field (e.g. "Risko & Gilbert (2016)").
    # We match both patterns.
    wikilinked_sources: set[str] = set()
    citation_corpus_parts: list[str] = []
    for entry in entries.values():
        if entry.type == "source":
            continue
        wikilinked_sources.update(entry.wikilinks)
        for src in entry.sources:
            citation_corpus_parts.append(_normalize(src))
    citation_corpus = " \n ".join(citation_corpus_parts)

    findings: list[Finding] = []
    for stem, entry in entries.items():
        if entry.type != "source":
            continue
        if stem in wikilinked_sources:
            continue

        parts = stem.split("-")
        year_token = next(
            (p for p in reversed(parts) if p.isdigit() and len(p) == 4), None
        )
        author_token = _normalize(parts[0]) if parts else ""

        cited = False
        if year_token and author_token and len(author_token) >= 3:
            if year_token in citation_corpus and author_token in citation_corpus:
                cited = True

        if not cited:
            findings.append(
                Finding(
                    check="uncited_sources",
                    entry=stem,
                    issue="source not referenced via [[wikilink]] or sources: frontmatter",
                    fix=f"cite in a relevant entry's sources field, add [[{stem}]] wikilink, or archive",
                )
            )
    return findings


def check_missing_related(entries: dict[str, Entry]) -> list[Finding]:
    # Only match full multi-word titles to avoid false positives on short words.
    title_to_stem: dict[str, str] = {}
    for stem, entry in entries.items():
        if entry.type == "source":
            continue
        title = entry.title.strip()
        if len(title.split()) < 2:
            continue
        title_to_stem[title.lower()] = stem

    findings: list[Finding] = []
    for stem, entry in entries.items():
        body_lc = entry.body.lower()
        for title_lc, target_stem in title_to_stem.items():
            if target_stem == stem:
                continue
            if target_stem in entry.wikilinks:
                continue
            if title_lc in body_lc:
                findings.append(
                    Finding(
                        check="missing_related",
                        entry=stem,
                        issue=f"body mentions '{title_lc}' but has no [[{target_stem}]] link",
                        fix=f"add [[{target_stem}]] to Related section",
                    )
                )
    return findings


def check_frontmatter(entries: dict[str, Entry]) -> list[Finding]:
    findings: list[Finding] = []
    for stem, entry in entries.items():
        if not entry.status:
            findings.append(
                Finding(
                    check="frontmatter",
                    entry=stem,
                    issue="missing status field",
                    fix=f"set status to one of {VALID_STATUSES}",
                )
            )
        elif entry.status not in VALID_STATUSES:
            findings.append(
                Finding(
                    check="frontmatter",
                    entry=stem,
                    issue=f"invalid status: {entry.status!r}",
                    fix=f"use one of {VALID_STATUSES}",
                )
            )
        if not entry.area:
            findings.append(
                Finding(
                    check="frontmatter",
                    entry=stem,
                    issue="missing area field",
                    fix=f"add area tag from {VALID_AREAS}",
                )
            )
        else:
            for a in entry.area:
                if a not in VALID_AREAS:
                    findings.append(
                        Finding(
                            check="frontmatter",
                            entry=stem,
                            issue=f"invalid area: {a!r}",
                            fix=f"use one or more of {VALID_AREAS}",
                        )
                    )
        if entry.type != "source" and not entry.sources:
            findings.append(
                Finding(
                    check="frontmatter",
                    entry=stem,
                    issue="no sources cited in frontmatter",
                    fix="add at least one source citation",
                )
            )
    return findings


CHECKS = {
    "broken_wikilinks": check_broken_wikilinks,
    "orphans": check_orphans,
    "uncited_sources": check_uncited_sources,
    "missing_related": check_missing_related,
    "frontmatter": check_frontmatter,
}


CHECK_DESCRIPTIONS = {
    "broken_wikilinks": "Wikilinks pointing to entries that don't exist",
    "orphans": "Entries with no inbound or outbound wikilinks",
    "uncited_sources": "Source entries not wikilinked from any concept/method",
    "missing_related": "Entries whose body mentions another entry's title without linking",
    "frontmatter": "Missing or invalid required frontmatter fields",
}


def run_checks(names: list[str] | None, entries: dict[str, Entry]) -> list[Finding]:
    selected = names or list(CHECKS.keys())
    findings: list[Finding] = []
    for name in selected:
        check_fn = CHECKS[name]
        findings.extend(check_fn(entries))
    return findings


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def render_markdown(findings: list[Finding], total_entries: int, selected: list[str]) -> str:
    by_check: dict[str, list[Finding]] = {name: [] for name in selected}
    for f in findings:
        by_check.setdefault(f.check, []).append(f)

    lines: list[str] = []
    lines.append("# KB Lint Report")
    lines.append("")
    lines.append(f"Generated: {date.today().isoformat()}")
    lines.append(f"Entries scanned: {total_entries}")
    lines.append(f"Total findings: {len(findings)}")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append("| Check | Count | Description |")
    lines.append("|---|---:|---|")
    for name in selected:
        count = len(by_check.get(name, []))
        desc = CHECK_DESCRIPTIONS.get(name, "")
        lines.append(f"| {name} | {count} | {desc} |")
    lines.append("")

    for name in selected:
        items = by_check.get(name, [])
        lines.append(f"## {name}  ({len(items)})")
        lines.append("")
        lines.append(f"*{CHECK_DESCRIPTIONS.get(name, '')}*")
        lines.append("")
        if not items:
            lines.append("_No findings._")
            lines.append("")
            continue
        # Group by entry for denser output
        by_entry: dict[str, list[Finding]] = {}
        for f in items:
            by_entry.setdefault(f.entry, []).append(f)
        for entry_stem in sorted(by_entry.keys()):
            lines.append(f"### `{entry_stem}`")
            for f in by_entry[entry_stem]:
                lines.append(f"- **Issue:** {f.issue}")
                if f.fix:
                    lines.append(f"  - Fix: {f.fix}")
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="linter",
        description="Run health checks over the Modern Mind KB.",
    )
    parser.add_argument(
        "--check",
        action="append",
        choices=list(CHECKS.keys()),
        help="run only specific checks (repeatable). Default: all.",
    )
    parser.add_argument(
        "--out",
        default=str(REPORT_PATH),
        help=f"output path for markdown report (default: {REPORT_PATH})",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="print report to stdout instead of writing to file",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit findings as JSON to stdout (suppresses markdown report)",
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="print only the summary table to stdout (on top of file write)",
    )
    args = parser.parse_args(argv)

    entries = load_entries()
    selected = args.check or list(CHECKS.keys())
    findings = run_checks(selected, entries)

    if args.json:
        print(json.dumps([asdict(f) for f in findings], indent=2))
        return 0

    report = render_markdown(findings, total_entries=len(entries), selected=selected)

    if args.stdout:
        print(report)
    else:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote {len(findings)} findings across {len(selected)} checks to {out_path}")
        if args.summary_only or True:
            print()
            print("Summary:")
            by_check: dict[str, int] = {name: 0 for name in selected}
            for f in findings:
                by_check[f.check] = by_check.get(f.check, 0) + 1
            width = max(len(n) for n in selected)
            for name in selected:
                print(f"  {name:<{width}}  {by_check.get(name, 0):>4}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
