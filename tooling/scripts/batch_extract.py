"""Batch Stage 1: run extract.py on every file in raw/inbox/candidates/.

extract.py auto-derives canonical slugs via derive_canonical_slug (clean
filename → type-aware PDF content template → fallback slugify). No per-file
override map needed in this script — pass `--slug X` per file to extract.py
manually for the rare case the auto-derivation gets it wrong.

Skips files where raw/<slug>/ already exists (use --force to re-extract).

Prints a summary report with: slug, extractor used (opendataloader-pdf /
pypdf / pdfplumber / ocr / failed), word count, source_type detected.

Usage:
    uv run python tooling/scripts/batch_extract.py            # extract all
    uv run python tooling/scripts/batch_extract.py --dry-run  # show plan only
    uv run python tooling/scripts/batch_extract.py --force    # re-extract existing
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parents[2]
CANDIDATES = KB_ROOT / "raw" / "inbox" / "candidates"
EXTRACT_PY = KB_ROOT / "tooling" / "scripts" / "extract.py"

# Files to skip entirely (e.g., images / unsupported formats that extract.py
# can't process)
SKIP_FILES: set[str] = {
    "Zhao & He (2024) - The Impostor Phenomenon of Workplace Artificial Intelligence Augmentation.png",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="show plan, don't extract")
    ap.add_argument("--force", action="store_true", help="re-extract even if raw/<slug>/ exists")
    ap.add_argument("--limit", type=int, default=None, help="extract at most N files (for testing)")
    args = ap.parse_args()

    files = sorted(CANDIDATES.iterdir())
    files = [f for f in files if f.is_file() and f.name not in SKIP_FILES]

    if args.limit:
        files = files[: args.limit]

    print(f"Found {len(files)} files in {CANDIDATES.relative_to(KB_ROOT)}")
    print()

    extracted: list[tuple[str, str, int, str]] = []  # (slug, extractor, word_count, source_type)
    skipped: list[tuple[str, str]] = []  # (filename, reason)
    failed: list[tuple[str, str]] = []  # (filename, error)

    py_exe = sys.executable
    for i, f in enumerate(files, start=1):
        cmd = [py_exe, str(EXTRACT_PY), str(f)]
        if args.force:
            cmd.append("--force")

        if args.dry_run:
            # In dry-run, we don't actually extract — just preview the file.
            # extract.py auto-derives the slug at runtime, so we don't predict
            # it here. (The previous SLUG_OVERRIDES dict is gone; slug derivation
            # is now centralized in extract.py:derive_canonical_slug.)
            print(f"[{i:>2}/{len(files)}] DRY {f.name}")
            continue

        print(f"[{i:>2}/{len(files)}] {f.name} ...", end=" ", flush=True)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(KB_ROOT))
        if result.returncode != 0:
            failed.append((f.name, result.stderr.strip()[:200]))
            print(f"FAILED: {result.stderr.strip()[:120]}")
            continue

        # Parse stdout for slug + extractor + word_count
        lines = result.stdout.strip().splitlines()
        actual_slug = ""
        for line in lines:
            if line.startswith("cataloged: ") or line.startswith("re-extracted: "):
                actual_slug = Path(line.split(":", 1)[1].strip()).name

        if actual_slug:
            sj_path = KB_ROOT / "raw" / actual_slug / "source.json"
            if sj_path.exists():
                meta = json.loads(sj_path.read_text(encoding="utf-8"))
                extracted.append((
                    actual_slug,
                    meta.get("extractor", "?"),
                    meta.get("word_count", 0),
                    meta.get("source_type", "?"),
                ))
                print(f"{meta.get('extractor', '?')} ({meta.get('word_count', 0)} words, {meta.get('source_type', '?')})")
            else:
                print("? (source.json missing)")
        else:
            print("? (couldn't parse slug)")

    # --- Summary ---
    print()
    print(f"=== Summary ===")
    print(f"  extracted:   {len(extracted)}")
    print(f"  skipped:     {len(skipped)}")
    print(f"  failed:      {len(failed)}")
    print()

    if extracted:
        by_extractor: dict[str, int] = {}
        for _, ext, _, _ in extracted:
            by_extractor[ext] = by_extractor.get(ext, 0) + 1
        print("Extractor breakdown:")
        for ext, n in sorted(by_extractor.items(), key=lambda x: -x[1]):
            print(f"  {ext:>20}: {n}")
        print()

    if failed:
        print("Failures:")
        for fname, err in failed:
            print(f"  {fname}\n      {err}")
        print()

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
