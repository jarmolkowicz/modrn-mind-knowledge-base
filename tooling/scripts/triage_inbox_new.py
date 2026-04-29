"""One-shot triage for the inbox/new/ batch added 2026-04-29.

Same logic as triage_inbox.py but for the 26 files in raw/inbox/new/.
Moves into raw/inbox/candidates/ and raw/inbox/possible-duplicates/,
appends an addendum to triage-manifest.md, removes the now-empty
raw/inbox/new/ directory.
"""

import shutil
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parents[2]
NEW = KB_ROOT / "raw" / "inbox" / "new"
CANDIDATES = KB_ROOT / "raw" / "inbox" / "candidates"
DUPES = KB_ROOT / "raw" / "inbox" / "possible-duplicates"

TRIAGE = [
    ("1-s2.0-S0360131524002380-main.pdf", "CANDIDATE",
     "Deng, Jiang, Yu, Lu & Liu (2024) - Does ChatGPT enhance student learning? Systematic review and meta-analysis. Computers & Education."),
    ("1-s2.0-S0747563224002541-main.pdf", "CANDIDATE",
     "Stadler, Bannert & Sailer (2024) - Cognitive ease at a cost: LLMs reduce mental effort. Computers in Human Behavior."),
    ("1-s2.0-S2590291125010186-main.pdf", "POSSIBLE_DUPLICATE",
     "Barcaui - ChatGPT as a cognitive crutch (journal version). Same paper as 'Barcuai (2026) - ChatGPT as a cognitive crutch.pdf' already in candidates/ (note name spelling differs). SHA-256 differs (probably preprint vs published)."),
    ("2025.11.07.687207v1.full.pdf", "CANDIDATE",
     "Horowitz-Kraus et al. (2025) - fMRI study of children using ChatGPT: lower cognitive control, attention, creativity. Technion."),
    ("2410.03017v2.pdf", "CANDIDATE",
     "Wang, Ribeiro, Robinson, Loeb & Demszky (2024) - Tutor CoPilot: Human-AI Approach for Scaling Real-Time Expertise. Stanford."),
    ("2503.07599v2.pdf", "CANDIDATE",
     "Baradari, Kosmyna, Petrov, Kaplun & Maes - NeuroChat: Neuroadaptive AI Chatbot. MIT Media Lab. Distinct from kosmyna-cognitive-debt-2025."),
    ("2503.17473v2.pdf", "CANDIDATE",
     "Fang, Liu, Danry, Lee, Chan, Pataranutaporn, Maes et al. (MIT/OpenAI) - How AI and Human Behaviors Shape Psychosocial Effects of Extended Chatbot Use. Different first author from fang-ai-loneliness-2025; theme adjacent."),
    ("Beware-of-metacognitive-laziness-Effects-of-generative-artificial-intelligence-on-learning.pdf", "CANDIDATE",
     "Fan et al. (2025, BJET) - Beware of metacognitive laziness. HIGH PRIORITY: cited in 2 concept entries (metacognition, metacognitive-laziness) but never ingested as a source - bringing it in resolves an uncited reference."),
    ("IDU-c09f40d8-9ff8-42dc-b315-591157499be7.pdf", "CANDIDATE",
     "De Simone, Tiberti, Barron Rodriguez, Manolio, Mosuro & Dikoru (2025) - From Chalkboards to Chatbots: GenAI in Nigerian classrooms. World Bank Policy Research Working Paper 11125."),
    ("PI_2025.12.09_Teens-Social-Media-AI_REPORT.pdf", "CANDIDATE",
     "Pew Research (Faverio & Sidoti, Dec 2025) - Teens, Social Media and AI Chatbots 2025."),
    ("PS_2025.9.15_AI-and-its-impact_report.pdf", "CANDIDATE",
     "Pew Research (Kennedy et al., Sept 2025) - AI and its impact."),
    ("bastani-et-al-2025-generative-ai-without-guardrails-can-harm-learning-evidence-from-high-school-mathematics.pdf", "CANDIDATE",
     "Bastani, Bastani, Sungu, Ge, Kabakci & Marimane (2025, PNAS) - Generative AI without guardrails can harm learning: Turkish high school math RCT."),
    ("dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf", "POSSIBLE_DUPLICATE",
     "Dell'Acqua et al. (2026) - Navigating the Jagged Technological Frontier. PUBLISHED version (Organization Science 2026) of the working-paper version already in KB as dellacqua-jagged-frontier-2023. Decide whether to upgrade workbench to the published edition."),
    ("folk-dunn-2026-how-does-turning-to-ai-for-companionship-predict-loneliness-and-vice-versa.pdf", "CANDIDATE",
     "Folk & Dunn (2026, Psychological Science) - How does turning to AI for companionship predict loneliness and vice versa? Theme overlap with fang-ai-loneliness-2025."),
    ("fpsyg-15-1259845.pdf", "CANDIDATE",
     "Dergaa, Ben Saad, Glenn et al. (2024, Frontiers in Psychology) - From tools to threats: AI chatbots on cognitive health. Opinion article naming 'AICs-induced cognitive atrophy'."),
    ("fpsyg-16-1508383.pdf", "CANDIDATE",
     "Wang, Tao, Ma, Li & Wu (Frontiers in Psychology) - EEG assessment of AI-generated content impact on student creative performance. Chinese product-design students."),
    ("latikka-et-al-2025-individual-and-well-being-factors-associated-with-social-chatbot-usage-a-six-country-study.pdf", "CANDIDATE",
     "Latikka, Bergdahl, Savolainen et al. (2025, Journal of Social and Personal Relationships) - Six-country study of social chatbot usage and well-being."),
    ("learnLM_nov25.pdf", "CANDIDATE",
     "LearnLM Team (Google + Eedi, 2025) - AI tutoring RCT in UK classrooms. Industry research."),
    ("lee_2025_ai_critical_thinking_survey.pdf", "CANDIDATE",
     "Lee, Sarkar, Tankelevitch, Sellen et al. (2025, CHI) - Impact of GenAI on critical thinking: survey of knowledge workers. CMU + Microsoft Research. Shares Tankelevitch with the metacognitive-demands paper already in KB."),
    ("s41539-025-00311-8.pdf", "CANDIDATE",
     "Yin, Xu, Pan & Hu (2025, npj Science of Learning) - Effects of different AI-driven Chatbot feedback on learning outcomes and brain activity."),
    ("s41598-025-19212-2.pdf", "CANDIDATE",
     "Folk, Heine & Dunn (2025, Scientific Reports) - Individual differences in anthropomorphism help explain social connection to AI companions. Companion paper to folk-dunn-2026 above."),
    ("s41598-025-97652-6.pdf", "CANDIDATE",
     "Kestin, Miller, Klales, Milbourne & Ponti (2025, Scientific Reports) - AI tutoring outperforms in-class active learning: RCT with novel research-based design."),
    ("s41599-026-07019-z_reference.pdf", "CANDIDATE",
     "Wu, Zhu, Zhang, Yin et al. (2026) - ChatGPT's impact on student learning outcomes: meta-analysis of 35 experimental studies. Humanities & Social Sciences Communications."),
    ("s44387-025-00063-1.pdf", "CANDIDATE",
     "Rossi, Fraccaro & Manzotti (2025, npj AI Comment) - The brain side of human-AI interactions: the '3R principle'. Neuroplasticity / cognitive erosion comment."),
    ("sciadv.adn5290.pdf", "POSSIBLE_DUPLICATE",
     "Doshi & Hauser (2024, Science Advances) - Generative AI enhances individual creativity but reduces collective diversity. PUBLISHED version of same paper already in KB as doshi-hauser-creativity-diversity-2024 (SHA-256 differs but content identical). Decide whether to upgrade workbench to this canonical PDF."),
    ("ssrn-6097646.pdf", "POSSIBLE_DUPLICATE",
     "Shaw & Nave - Thinking Fast/Slow/Artificial: Cognitive Surrender. CONFIRMED IDENTICAL SHA-256 to raw/shaw-cognitive-surrender-2026/original.pdf - true duplicate, can be deleted."),
]


def main() -> int:
    if not NEW.exists():
        print(f"error: {NEW} not found", file=sys.stderr)
        return 2
    CANDIDATES.mkdir(parents=True, exist_ok=True)
    DUPES.mkdir(parents=True, exist_ok=True)

    candidates_moved: list[tuple[str, str]] = []
    dupes_moved: list[tuple[str, str]] = []
    missing: list[str] = []

    for fname, cls, reason in TRIAGE:
        src = NEW / fname
        if not src.exists():
            missing.append(fname)
            continue
        dest_dir = CANDIDATES if cls == "CANDIDATE" else DUPES
        dest = dest_dir / fname
        if dest.exists():
            print(f"  skip (dest exists): {dest}")
            continue
        shutil.move(str(src), str(dest))
        if cls == "CANDIDATE":
            candidates_moved.append((fname, reason))
        else:
            dupes_moved.append((fname, reason))
        print(f"  {cls} -> {fname}")

    print(f"\nmoved -> candidates/: {len(candidates_moved)}")
    print(f"moved -> possible-duplicates/: {len(dupes_moved)}")
    if missing:
        print(f"MISSING from inbox/new/: {missing}")

    manifest = KB_ROOT / "raw" / "inbox" / "triage-manifest.md"
    addendum: list[str] = [
        "\n\n## Addendum: inbox/new/ batch (2026-04-29)\n",
        "\n26 files added to `raw/inbox/new/` after the initial triage. Classified and moved into the same `candidates/` and `possible-duplicates/` folders as the first batch.\n",
        f"\n### New candidates ({len(candidates_moved)})\n",
    ]
    for f, r in candidates_moved:
        addendum.append(f"- `{f}` - _{r}_\n")
    addendum.append(f"\n### New possible duplicates ({len(dupes_moved)})\n")
    for f, r in dupes_moved:
        addendum.append(f"- `{f}` - _{r}_\n")
    with manifest.open("a", encoding="utf-8") as fh:
        fh.writelines(addendum)
    print(f"manifest updated: {manifest}")

    remaining = list(NEW.iterdir())
    if not remaining:
        NEW.rmdir()
        print(f"removed empty {NEW}")
    else:
        print(f"NOTE: {NEW} still has {len(remaining)} files; not removing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
