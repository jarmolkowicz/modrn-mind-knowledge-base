"""Pass 1 of the legacy-source backfill.

For every binary sitting in raw/papers/, raw/articles/, raw/books/ (etc.),
match it to an existing sources/<slug>.md entry, then run extract.py to
produce raw/<slug>/{original.<ext>, source.md, source.json, log.md} with
source.json.status = "integrated".

This script does NOT do any LLM work. It's a structural migration:
existing KB entries are unchanged; only the per-source workbench is created
so every source has the new uniform shape going forward.

Sources flagged as AMBIGUOUS are reported and skipped — fix manually
(rename binary, override --slug, or hand-edit the mapping).

Usage:
    uv run python tooling/scripts/backfill.py --dry-run   # show plan, do nothing
    uv run python tooling/scripts/backfill.py --execute   # do the migration
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

KB_ROOT = Path.cwd()
SOURCES_DIR = KB_ROOT / "sources"
LEGACY_FOLDERS = ["papers", "articles", "books", "transcripts", "decks", "other"]


def list_source_slugs() -> set[str]:
    return {p.stem for p in SOURCES_DIR.glob("*.md")}


def list_legacy_files() -> list[Path]:
    files: list[Path] = []
    for sub in LEGACY_FOLDERS:
        d = KB_ROOT / "raw" / sub
        if not d.is_dir():
            continue
        for f in d.iterdir():
            if f.name == ".gitkeep" or not f.is_file():
                continue
            files.append(f)
    return files


STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "in", "on", "at", "to", "for", "with",
    "from", "by", "is", "as", "this", "that", "these", "those", "it", "its",
    "et", "al", "vs", "via", "how", "why", "when", "what",
}


def parse_filename(name: str) -> tuple[list[str], str | None, list[str]]:
    """Return (surname_candidates, year, title_tokens) parsed from a filename
    like 'Bjork & Bjork (2011) - Desirable Difficulties.pdf'.

    surname_candidates: 1-2 normalized lowercase ascii surname guesses
    (handles compound prefixes like 'de Mello' -> ['mello', 'demello']).
    title_tokens: significant lowercase words from the post-author part,
    used for disambiguation when multiple slugs match surname+year.
    """
    stem = Path(name).stem
    year_match = re.search(r"\b(19|20)\d{2}\b", stem)
    year = year_match.group(0) if year_match else None

    # Author chunk: everything before "(year)" or first "-" (whichever comes first)
    if year_match:
        author_chunk = stem[: year_match.start()]
    else:
        author_chunk = re.split(r"\s-\s", stem, maxsplit=1)[0]
    # Cut at first author boundary so we keep only the LEAD author:
    # "Bjork & Bjork" -> "Bjork", "Hermann, Puntoni & Morewedge" -> "Hermann",
    # "de Mello et al." -> "de Mello"
    author_chunk = re.split(r"\s*[&,]\s*|\s+et\s+al\.?", author_chunk, maxsplit=1, flags=re.IGNORECASE)[0]
    # Title chunk: post-author. Approximate: take everything after first "-" past the year.
    after_year = stem[year_match.end():] if year_match else ""
    title_part = re.sub(r"^[\s\-\(\)]+", "", after_year)

    # Lead author lookup: take the LAST run of alpha (handles compound names like "de Mello")
    head = re.sub(r"[^A-Za-z'\s]+", " ", author_chunk).strip()
    surnames: list[str] = []
    if head:
        words = head.split()
        last = words[-1].replace("'", "").lower()
        surnames.append(last)
        # If the surname is preceded by a particle (de, el, van, von, der, al, di, du, le),
        # also try the joined form (e.g. 'de Mello' -> 'demello' for slugs like 'demello-...')
        if len(words) >= 2 and words[-2].lower() in {"de", "el", "van", "von", "der", "al", "di", "du", "le", "la"}:
            joined = (words[-2] + words[-1]).replace("'", "").lower()
            surnames.append(joined)
        # Org-as-author fallback (e.g. "MIT Media Lab" -> 'mit'). Use first word too if it's
        # all-caps in the original or short.
        first = words[0].replace("'", "").lower()
        if first != last and (words[0].isupper() or len(first) <= 4):
            surnames.append(first)

    # Title tokens: lowercase, split by non-letters, drop stopwords, keep tokens >= 4 chars
    tokens = [t for t in re.split(r"[^A-Za-z]+", title_part.lower()) if t]
    title_tokens = [t for t in tokens if t not in STOPWORDS and len(t) >= 4]
    return surnames, year, title_tokens


def candidate_slugs(slugs: set[str], surnames: list[str], year: str | None) -> list[str]:
    if not (surnames and year):
        return []
    out = []
    for slug in slugs:
        if year not in slug:
            continue
        tokens = slug.split("-")
        if any(s in tokens for s in surnames):
            out.append(slug)
    return sorted(out)


def disambiguate(candidates: list[str], title_tokens: list[str]) -> str | None:
    """If multiple candidate slugs match surname+year, pick the one whose
    slug shares the most tokens with the filename's title. Return the best
    match if it's a unique winner, else None (ambiguous)."""
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    if not title_tokens:
        return None
    scores: dict[str, int] = {}
    for slug in candidates:
        slug_tokens = set(slug.split("-"))
        # Don't count year/surname tokens — those are already-matched
        score = sum(1 for t in title_tokens if t in slug_tokens)
        # Also count partial token matches (e.g. 'rebound' in slug 'ai-rebound')
        for t in title_tokens:
            for st in slug_tokens:
                if t != st and (t in st or st in t) and min(len(t), len(st)) >= 5:
                    score += 1
        scores[slug] = score
    best_score = max(scores.values())
    if best_score == 0:
        return None
    winners = [s for s, sc in scores.items() if sc == best_score]
    return winners[0] if len(winners) == 1 else None


def status_integrated_patch(source_json_path: Path) -> None:
    """After extract.py runs, set status to 'integrated' to reflect that the
    KB entry already exists for this source."""
    data = json.loads(source_json_path.read_text(encoding="utf-8"))
    data["status"] = "integrated"
    data.setdefault("decisions", []).append({
        "stage": "backfill",
        "outcome": "structurally_backfilled",
        "by": "tooling/scripts/backfill.py",
        "at": data.get("ingested_at"),
        "reason": "Source ingested before the new pipeline. Audit trail (triage/distill/critique) is permanently incomplete; only structural metadata + extracted text are recorded.",
    })
    source_json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def append_backfill_log(log_path: Path) -> None:
    note = (
        "\n## backfilled\n"
        "- Migrated from legacy raw/<type>/ folder to per-source workbench.\n"
        "- Stages 2-5 audit trail not available (this source pre-dates the new pipeline).\n"
        "- KB entry already exists in concepts/, methods/, sources/.\n"
    )
    with log_path.open("a", encoding="utf-8") as f:
        f.write(note)


def plan(slugs: set[str]) -> tuple[list[tuple[Path, str]], list[Path]]:
    """Return (matches, ambiguous). matches: (binary_path, slug). ambiguous:
    binaries with no unique match."""
    matches: list[tuple[Path, str]] = []
    ambiguous: list[Path] = []
    for f in list_legacy_files():
        surnames, year, title_tokens = parse_filename(f.name)
        cands = candidate_slugs(slugs, surnames, year)
        winner = disambiguate(cands, title_tokens)
        if winner:
            matches.append((f, winner))
        else:
            ambiguous.append(f)
    return matches, ambiguous


def run_extract(binary: Path, slug: str) -> None:
    """Shell out to extract.py with the chosen slug."""
    cmd = [
        sys.executable,
        str(KB_ROOT / "tooling" / "scripts" / "extract.py"),
        str(binary),
        "--slug", slug,
        "--force",  # always overwrite if a partial dir exists
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"extract.py failed for {binary.name} -> {slug}:\n"
            f"  stdout: {result.stdout}\n"
            f"  stderr: {result.stderr}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="show plan without changes")
    parser.add_argument("--execute", action="store_true", help="apply the migration")
    args = parser.parse_args()

    if not args.dry_run and not args.execute:
        parser.error("pick one: --dry-run or --execute")

    slugs = list_source_slugs()
    matches, ambiguous = plan(slugs)

    print(f"Backfill plan:")
    print(f"  legacy folders scanned: {LEGACY_FOLDERS}")
    print(f"  source slugs in KB:     {len(slugs)}")
    print(f"  matched (unique):       {len(matches)}")
    print(f"  ambiguous (skip):       {len(ambiguous)}")
    print()

    if matches:
        print("=== Matched (one slug per binary) ===")
        for f, slug in sorted(matches, key=lambda t: t[1]):
            rel = f.relative_to(KB_ROOT)
            print(f"  {rel}\n    -> raw/{slug}/")
        print()

    if ambiguous:
        print("=== Ambiguous (manual fix required) ===")
        for f in ambiguous:
            surnames, year, title_tokens = parse_filename(f.name)
            cands = candidate_slugs(slugs, surnames, year)
            rel = f.relative_to(KB_ROOT)
            print(f"  {rel}")
            print(f"    parsed: surnames={surnames!r}, year={year!r}, title_tokens={title_tokens!r}")
            if cands:
                print(f"    candidates: {cands}")
            else:
                print(f"    no slug matches any of {surnames!r} with year {year!r}")
        print()

    if args.dry_run:
        print("(dry-run; no files modified)")
        return 0

    # --execute path
    print(f"Executing backfill for {len(matches)} sources…")
    failures: list[tuple[Path, str, str]] = []
    for f, slug in matches:
        try:
            run_extract(f, slug)
            sj = KB_ROOT / "raw" / slug / "source.json"
            log = KB_ROOT / "raw" / slug / "log.md"
            status_integrated_patch(sj)
            append_backfill_log(log)
            # extract.py copied the binary; remove the legacy original
            f.unlink()
            print(f"  ✓ {slug}")
        except Exception as e:
            print(f"  ✗ {slug} ({f.name}): {e}", file=sys.stderr)
            failures.append((f, slug, str(e)))

    # Clean up empty legacy folders
    for sub in LEGACY_FOLDERS:
        d = KB_ROOT / "raw" / sub
        if not d.is_dir():
            continue
        remaining = [x for x in d.iterdir() if x.name != ".gitkeep"]
        if not remaining:
            # remove .gitkeep then dir
            (d / ".gitkeep").unlink(missing_ok=True)
            try:
                d.rmdir()
                print(f"  removed empty {d.relative_to(KB_ROOT)}/")
            except OSError:
                pass

    # Also retire raw/processing/ if empty
    proc = KB_ROOT / "raw" / "processing"
    if proc.is_dir():
        remaining = [x for x in proc.iterdir() if x.name != ".gitkeep"]
        if not remaining:
            (proc / ".gitkeep").unlink(missing_ok=True)
            try:
                proc.rmdir()
                print(f"  removed empty raw/processing/")
            except OSError:
                pass

    if failures:
        print(f"\n{len(failures)} failures — fix and re-run.", file=sys.stderr)
        return 1
    print(f"\nBackfilled {len(matches)} sources.")
    if ambiguous:
        print(f"{len(ambiguous)} ambiguous remain — handle manually.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
