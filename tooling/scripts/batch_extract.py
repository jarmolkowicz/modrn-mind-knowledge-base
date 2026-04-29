"""Batch Stage 1: run extract.py on every file in raw/inbox/candidates/.

For files with cryptic publisher-style filenames (1-s2.0-..., s41598-..., arXiv
IDs), provides an explicit slug. For files with already-readable
"Author (Year) - Title.pdf" names, lets extract.py auto-slugify.

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

# Explicit slug overrides for files where the filename doesn't carry author/year
# in a slugify-friendly way. Sourced from the triage manifest identifications.
SLUG_OVERRIDES: dict[str, str] = {
    "1-s2.0-S0360131524002380-main.pdf": "deng-chatgpt-meta-analysis-2024",
    "1-s2.0-S0747563224002541-main.pdf": "stadler-bannert-sailer-cognitive-ease-cost-2024",
    "2025.11.07.687207v1.full.pdf": "horowitz-kraus-fmri-children-chatgpt-2025",
    "2410.03017v2.pdf": "wang-tutor-copilot-2024",
    "2503.04761v1.pdf": "handa-economic-tasks-claude-2025",
    "2503.07599v2.pdf": "baradari-neurochat-2025",
    "2503.17473v2.pdf": "fang-chatbot-psychosocial-2025",
    "2602.19141v1.pdf": "chandra-sycophantic-delusional-2026",
    "Beware-of-metacognitive-laziness-Effects-of-generative-artificial-intelligence-on-learning.pdf": "fan-metacognitive-laziness-2025",
    "IDU-c09f40d8-9ff8-42dc-b315-591157499be7.pdf": "desimone-chalkboards-chatbots-nigeria-2025",
    "PI_2025.12.09_Teens-Social-Media-AI_REPORT.pdf": "pew-teens-ai-chatbots-2025",
    "PS_2025.9.15_AI-and-its-impact_report.pdf": "pew-ai-impact-2025",
    "bastani-et-al-2025-generative-ai-without-guardrails-can-harm-learning-evidence-from-high-school-mathematics.pdf": "bastani-guardrails-math-rct-2025",
    "folk-dunn-2026-how-does-turning-to-ai-for-companionship-predict-loneliness-and-vice-versa.pdf": "folk-dunn-companionship-loneliness-2026",
    "fpsyg-15-1259845.pdf": "dergaa-tools-to-threats-2024",
    "fpsyg-16-1508383.pdf": "wang-eeg-creative-design-2025",
    "latikka-et-al-2025-individual-and-well-being-factors-associated-with-social-chatbot-usage-a-six-country-study.pdf": "latikka-six-country-chatbot-2025",
    "learnLM_nov25.pdf": "learnlm-uk-tutoring-rct-2025",
    "lee_2025_ai_critical_thinking_survey.pdf": "lee-critical-thinking-survey-2025",
    "s41539-025-00311-8.pdf": "yin-chatbot-feedback-brain-2025",
    "s41598-025-19212-2.pdf": "folk-heine-dunn-anthropomorphism-2025",
    "s41598-025-97652-6.pdf": "kestin-ai-tutoring-rct-2025",
    "s41599-026-07019-z_reference.pdf": "wu-chatgpt-meta-analysis-2026",
    "s44387-025-00063-1.pdf": "rossi-3r-principle-2025",
    # Files in the older candidates batch with cryptic names
    "AI Assisted Learning System and Its Relation with Self Esteem and Metacognition.pdf": "ai-assisted-learning-self-esteem-metacognition",
    "Amayreh (2025).pdf": "amayreh-2025",
    "Cyfrowy-Menedzer-2026-.pdf": "cyfrowy-menedzer-2026",
    "Building a Human Resilience Infrastructure for the AI Age.pdf": "human-resilience-infrastructure-ai",
    "Ebook_Anthropic-Studies-Summary_v1.md": "anthropic-studies-summary-2025",
    "International AI Safety Report.pdf": "international-ai-safety-report-2025",
    "Irrational Labs - AI Adoption in the Workplace Report.pdf": "irrational-labs-ai-adoption-workplace-2025",
    "PWC (2025) - 2025 Global AI Jobs Barometer.pdf": "pwc-ai-jobs-barometer-2025",
    "Unlocking High Quality AI Adoption in the Workplace.pdf": "unlocking-high-quality-ai-adoption-2025",
    "diagnoza-mlodziezy_2026.pdf": "diagnoza-mlodziezy-2026",
    "EY (2025) - EY UK 2025 Impact Report.pdf": "ey-uk-impact-report-2025",
    "HBR (2026) - AI Brain Fry.pdf": "hbr-ai-brain-fry-2026",
    "Holiday (2026) - This Simple Skill Will Put You Ahead In The Era Of AI _ LinkedIn.pdf": "holiday-simple-skill-ai-2026",
    # Zhao & He (2024) is a .png file - we'll skip extraction (image, not extractable)
}

# Files to skip entirely (e.g., images that aren't extractable)
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
        slug = SLUG_OVERRIDES.get(f.name)
        cmd = [py_exe, str(EXTRACT_PY), str(f)]
        if slug:
            cmd.extend(["--slug", slug])
        if args.force:
            cmd.append("--force")

        # Detect existing slug to skip cleanly when not forcing
        if not args.force:
            test_slug = slug or _slugify_for_check(f.stem)
            if (KB_ROOT / "raw" / test_slug).exists():
                skipped.append((f.name, f"raw/{test_slug}/ exists"))
                print(f"[{i:>2}/{len(files)}] SKIP {f.name} -> raw/{test_slug}/ already exists")
                continue

        if args.dry_run:
            print(f"[{i:>2}/{len(files)}] DRY {f.name} -> slug={slug or '(auto)'}")
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


def _slugify_for_check(stem: str) -> str:
    """Mirror the slugify in extract.py to predict the auto-slug for skip-check."""
    import re
    s = stem.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


if __name__ == "__main__":
    sys.exit(main())
