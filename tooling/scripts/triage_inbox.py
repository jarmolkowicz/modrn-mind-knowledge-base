"""
Triages raw/inbox/ by classifying each file as CANDIDATE (genuinely new) or
POSSIBLE_DUPLICATE (matches an already-ingested source by author+year).

Scope: top-level files + Articles and Opinions/ + Books/ + Papers/ + Reports/.
Excluded: Practical/ (practitioner ouevre — separate effort).

Moves files into:
  raw/inbox/candidates/<orig-name>           — proceed to /ingest
  raw/inbox/possible-duplicates/<orig-name>  — review, then either skip or override

Writes raw/inbox/triage-manifest.md with the full decision log.

Usage:
    uv run python tooling/scripts/triage_inbox.py            # dry-run
    uv run python tooling/scripts/triage_inbox.py --apply    # actually move
"""

import argparse
import shutil
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parents[2]
INBOX = KB_ROOT / "raw" / "inbox"
CANDIDATES = INBOX / "candidates"
DUPES = INBOX / "possible-duplicates"

# (relative-to-inbox path, classification, reason)
# classification: "CANDIDATE" or "POSSIBLE_DUPLICATE"
TRIAGE: list[tuple[str, str, str]] = [
    # --- Top level ---
    ("2503.04761v1.pdf", "CANDIDATE",
     "Handa et al. (Anthropic) — Which Economic Tasks Performed with AI? Not in sources/"),
    ("2601.20245v2.pdf", "POSSIBLE_DUPLICATE",
     "Shen & Tamkin (2026) — How AI Impacts Skill Formation. Already ingested as shen-skill-formation-2026"),
    ("2602.19141v1.pdf", "CANDIDATE",
     "Chandra, Kleiman-Weiner, Ragan-Kelley & Tenenbaum — Sycophantic Chatbots Cause Delusional Spiraling. Not in sources/"),
    ("Hermann, Puntoni & Morewedge (2025) - GenAI and the psychology of work.pdf", "CANDIDATE",
     "Not in sources/"),
    ("boyd-markowitz-2026-artificial-intelligence-and-the-psychology-of-human-connection.pdf", "POSSIBLE_DUPLICATE",
     "Already ingested as boyd-markowitz-human-connection-2026"),

    # --- Articles and Opinions ---
    ("Articles and Opinions/Appiah (2025)  - The Atlantic - The Age of De-Skilling.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Articles and Opinions/De Cremer & Koopman (2024) - HBR - Using AI Makes Us Lonelier.pdf", "CANDIDATE",
     "Not in sources/. Theme overlap with fang-ai-loneliness-2025 — verify it isn't a popularization of same study"),
    ("Articles and Opinions/Dolan (2025) - Users of generative AI struggle to accurately assess their own competence.pdf", "CANDIDATE",
     "Not in sources/. Theme overlap with he-illusion-competence-2023 / keshky-illusory-competence-2026"),
    ("Articles and Opinions/Guchait (2026) - Why Asking AI Feels So Good.pdf", "CANDIDATE", "Not in sources/"),
    ("Articles and Opinions/HBR (2026) - AI Brain Fry.pdf", "CANDIDATE", "Not in sources/"),
    ("Articles and Opinions/Holiday (2026) - This Simple Skill Will Put You Ahead In The Era Of AI _ LinkedIn.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Articles and Opinions/Nosta (2025) - The Impostor Phenomenon of Workplace Artificial Intelligence Augmentation.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) - AI and the New Impostor Syndrome.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) - Artificial Intelligence and the Passivity Problem _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) - The Curious Geometry of the Lived Experience _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) - The Curvature of Thought _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) - The Tragic Flaw in AI _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) - We’re Measuring AI on the Wrong Ruler _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) - When AI Becomes More You Than You _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) - When Answers Cost Less than Thought _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article. Theme overlap with nosta-frictionless-intelligence-2026 — verify"),
    ("Articles and Opinions/Nosta (2026) - When Expression Breaks Free From Intellect _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/Nosta (2026) -When Patterns Look Like Thought _ Psychology Today.pdf", "CANDIDATE",
     "Distinct Nosta article, not in sources/"),
    ("Articles and Opinions/O'Brien (2026) - Your AI strategy is undermining.pdf", "CANDIDATE", "Not in sources/"),

    # --- Books ---
    ("Books/Ganna Pogrebna Book.pdf", "CANDIDATE",
     "Not in sources/. Identify exact title at catalog time"),
    ("Books/Harari book.pdf", "CANDIDATE",
     "Not in sources/. Identify exact title at catalog time (likely Nexus 2024)"),
    ("Books/John Nosta Book.pdf", "POSSIBLE_DUPLICATE",
     "Likely The Borrowed Mind — already ingested as nosta-borrowed-mind-2026 (workbench exists, chapter-level work deferred)"),

    # --- Papers ---
    ("Papers/AI Assisted Learning System and Its Relation with Self Esteem and Metacognition.pdf", "CANDIDATE",
     "Author/year unidentified from filename — verify at catalog"),
    ("Papers/Ahmad & Arshad (2025) - Artificial Intelligence Dependency, Academic Self-Efficacy, and the Imposter Phenomenon in University Students.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Amayreh (2025).pdf", "CANDIDATE",
     "Title not in filename — identify at catalog"),
    ("Papers/Anderson et al. (2026) - Homogenizing Effect on Creative Diversity.pdf", "POSSIBLE_DUPLICATE",
     "Same author + topic as anderson-homogenization-2024. May be revised version; compare versions before re-ingesting"),
    ("Papers/Arif et al. (2025) - FROM AI DEPENDENCE TO IMPOSTOR SYNDROME.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Barcuai (2026) - ChatGPT as a cognitive crutch.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Bartos et al. (2026) Effect of Artificial Intelligence on Learning.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Cheng et al. (2026) - Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence.pdf", "CANDIDATE",
     "Was in v3 migration plan as INCLUDE but never re-ingested onto new pipeline. Strong candidate"),
    ("Papers/Domingo (2025) - Investigating the influence of AI-driven tools in ESL students’ experience of AI-induced  impostor syndrome and academic confidence.pdf", "CANDIDATE",
     "Not in sources/. Note: Reports/ has a 'Deloitte (2026)' file with the same subtitle — likely misnamed copy; flag at catalog"),
    ("Papers/Draxler et al. (2025) - The AI Ghostwriter Effect.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Hai et al. (2025) - The dark side of employee-generative AI collaboration in the workplace.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Hermann, Puntoni & Morewedge (2025) - GenAI and the psychology of work.pdf", "POSSIBLE_DUPLICATE",
     "Same file also at top-level of inbox — keep one copy as candidate, this one is the dup"),
    ("Papers/Hruschka & Appel (2026) - Reducing Political Polarization Through AI.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Hwang & Yu (2025) - AI and Creative Cognition.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Jia & Neary (2025) - Effect of GenAI Dependency on University Students’ Academic Achievement- The Mediating Role of Self-Efficacy and Moderating Role of Perceived Teacher Caring.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Kim & Lee (2026) - The mental health implications of artificial intelligence adoption- the crucial role of selfefficacy.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Kim et al., (20260 - The LLM Fallacy.pdf", "CANDIDATE",
     "Not in sources/. Filename has typo — year is 2026"),
    ("Papers/Kosmyna et al. (2026) - Brain on ChatGPT Cognitive Debt.pdf", "POSSIBLE_DUPLICATE",
     "Already ingested as mit-cognitive-debt-2025 (the MIT Brain on ChatGPT paper)"),
    ("Papers/Lee at al. (2026) - Relying on AI at work reduces self-efficacy, ownership, and meaning.pdf", "CANDIDATE",
     "Not in sources/. Theme overlap with nikolova-robots-meaning-2024"),
    ("Papers/Liu et al. (2026) - AI Assistance Reduces Persistence.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Mascanero et al. (2026) - When proximal collaboration with AI hinders innovation.pdf", "CANDIDATE",
     "Was in v3 migration plan as INCLUDE but never re-ingested onto new pipeline"),
    ("Papers/Matueny & Nyamai (2025) -  Illusion of Competence and Skill Degradation.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Meincke et al. (2026) - Advice quality.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Moon et al. (2024) - Homogenizing Effect on Creative Diversity.pdf", "POSSIBLE_DUPLICATE",
     "Same title as creativity-diversity-2024 stem — likely the same paper re-attributed. Compare authors at catalog before re-ingesting"),
    ("Papers/Pate et al. (2026) - Replicating Human Motivated Reasoning Studies with LLM.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Perry (2026) - In defense of social friction.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Shao et al. (2026) - Future of Work with AI Agents.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Sharma et al. (2026) - Who’s in Charge Disempowerment Patterns.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Shukla et al. (2026) De-skilling, Cognitive Offloading, and Misplaced Responsibilities.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Stanciu & Sava (2026) - Self-Esteem and the Use of Artificial Intelligence in Academic Settings.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Van Bavel et al. (2026) - Tyranny of the minority.docx", "CANDIDATE", "Not in sources/"),
    ("Papers/Vendrell & Johnston (2026) - Scaffolding Critical Thinking with Generative AI.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Wu et al. (2025) - Human-generative AI collaboration enhances task performance but undermines human’s intrinsic motivation.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Yu et al. (2026) - Heterogeneity and predictors of the effects of AI assistance on radiologists.pdf", "CANDIDATE",
     "Not in sources/"),
    ("Papers/Zhang et al. (2024) - AI Dependency Self-Efficacy Academic Stress.pdf", "CANDIDATE", "Not in sources/"),
    ("Papers/Zhao & He (2024) - The Impostor Phenomenon of Workplace Artificial Intelligence Augmentation.png", "CANDIDATE",
     "Not in sources/. WARNING: .png file — probably a screenshot rather than the paper. Verify before /ingest (extract.py won't handle images)"),
    ("Papers/Zindulka et al. (2025) - The AI Memory Gap.pdf", "CANDIDATE", "Not in sources/"),

    # --- Reports ---
    ("Reports/Building a Human Resilience Infrastructure for the AI Age.pdf", "CANDIDATE",
     "Author/year unidentified from filename"),
    ("Reports/Cyfrowy-Menedzer-2026-.pdf", "CANDIDATE", "Polish report; not in sources/"),
    ("Reports/Deloitte (2026) - Investigating the influence of AI-driven tools in ESL students’ experience of AI-induced  impostor syndrome and academic confidence.pdf", "POSSIBLE_DUPLICATE",
     "Same subtitle as Domingo (2025) in Papers/. Likely a misnamed copy of the academic paper, not a Deloitte report. Inspect before ingesting either"),
    ("Reports/EY (2025) - EY UK 2025 Impact Report.pdf", "CANDIDATE", "Not in sources/"),
    ("Reports/Ebook_Anthropic-Studies-Summary_v1.md", "CANDIDATE", "Not in sources/"),
    ("Reports/International AI Safety Report.pdf", "CANDIDATE", "Not in sources/"),
    ("Reports/Irrational Labs - AI Adoption in the Workplace Report.pdf", "CANDIDATE", "Not in sources/"),
    ("Reports/PWC (2025) - 2025 Global AI Jobs Barometer.pdf", "CANDIDATE", "Not in sources/"),
    ("Reports/Unlocking High Quality AI Adoption in the Workplace.pdf", "CANDIDATE", "Not in sources/"),
    ("Reports/diagnoza-mlodziezy_2026.pdf", "CANDIDATE", "Polish youth-diagnosis report; not in sources/"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="actually move files (default: dry-run)")
    args = ap.parse_args()

    if not INBOX.exists():
        print(f"error: {INBOX} not found", file=sys.stderr)
        return 2

    candidates: list[tuple[str, str]] = []
    dupes: list[tuple[str, str]] = []
    missing: list[str] = []

    for rel, cls, reason in TRIAGE:
        src = INBOX / rel
        if not src.exists():
            missing.append(rel)
            continue
        if cls == "CANDIDATE":
            candidates.append((rel, reason))
        elif cls == "POSSIBLE_DUPLICATE":
            dupes.append((rel, reason))
        else:
            print(f"error: unknown classification {cls} for {rel}", file=sys.stderr)
            return 2

    print(f"CANDIDATE:           {len(candidates)} files")
    print(f"POSSIBLE_DUPLICATE:  {len(dupes)} files")
    print(f"missing in inbox:    {len(missing)} files")
    if missing:
        for m in missing:
            print(f"  MISSING: {m}")
    print()

    if not args.apply:
        print("dry-run — pass --apply to move files")
        for rel, reason in candidates:
            print(f"  CANDIDATE -> {rel}")
        for rel, reason in dupes:
            print(f"  DUPLICATE -> {rel}")
        return 0

    CANDIDATES.mkdir(parents=True, exist_ok=True)
    DUPES.mkdir(parents=True, exist_ok=True)

    moved_candidates: list[tuple[str, str, str]] = []  # (orig_rel, dest_name, reason)
    moved_dupes: list[tuple[str, str, str]] = []

    for rel, reason in candidates:
        src = INBOX / rel
        dest = CANDIDATES / src.name
        if dest.exists():
            print(f"  skip (dest exists): {dest}")
            continue
        shutil.move(str(src), str(dest))
        moved_candidates.append((rel, src.name, reason))
        print(f"  moved -> candidates/{src.name}")

    for rel, reason in dupes:
        src = INBOX / rel
        dest = DUPES / src.name
        if dest.exists():
            print(f"  skip (dest exists): {dest}")
            continue
        shutil.move(str(src), str(dest))
        moved_dupes.append((rel, src.name, reason))
        print(f"  moved -> possible-duplicates/{src.name}")

    # Manifest
    manifest = INBOX / "triage-manifest.md"
    lines: list[str] = []
    lines.append("# Inbox triage manifest")
    lines.append("")
    lines.append("Generated by `tooling/scripts/triage_inbox.py`. Scope: top-level + Articles and Opinions/ + Books/ + Papers/ + Reports/. The `Practical/` subdirectory is excluded — it's a practitioner-content collection (~776 files) needing separate handling.")
    lines.append("")
    lines.append(f"## Candidates ({len(moved_candidates)})")
    lines.append("")
    lines.append("Genuinely new sources to feed through `/ingest`. Reasons noted below.")
    lines.append("")
    for orig_rel, dest_name, reason in moved_candidates:
        lines.append(f"- `{dest_name}` — _{reason}_")
        lines.append(f"  - was: `{orig_rel}`")
    lines.append("")
    lines.append(f"## Possible duplicates ({len(moved_dupes)})")
    lines.append("")
    lines.append("Suspect overlap with already-ingested sources. Inspect before deciding to skip or override.")
    lines.append("")
    for orig_rel, dest_name, reason in moved_dupes:
        lines.append(f"- `{dest_name}` — _{reason}_")
        lines.append(f"  - was: `{orig_rel}`")
    lines.append("")
    if missing:
        lines.append(f"## Missing from inbox ({len(missing)})")
        lines.append("")
        lines.append("Listed in triage table but not found at scan time:")
        lines.append("")
        for m in missing:
            lines.append(f"- `{m}`")
        lines.append("")
    manifest.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote manifest: {manifest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
