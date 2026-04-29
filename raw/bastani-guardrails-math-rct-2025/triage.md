# Triage: Generative AI without guardrails can harm learning

## Source
- Slug: `bastani-guardrails-math-rct-2025`
- Type: `paper`
- Format: pdf, 8 pages, 7,555 words
- Path: `raw/bastani-guardrails-math-rct-2025/source.md` (extracted)

## Summary

Bastani, Bastani, Sungu, Ge, Kabakcı & Marimane (2025, *PNAS* 122(26): e2422633122). Preregistered field RCT in a large Turkish high school during Fall 2023-24, ~1,000 9th-11th grade students across ~50 classrooms, 4 sessions covering ~15% of the math curriculum. Three-arm randomization at the classroom level: **GPT Base** (vanilla ChatGPT-style interface on GPT-4), **GPT Tutor** (GPT-4 with teacher-curated prompts: includes correct solutions in the prompt to mitigate hallucinations + instructions to give hints not answers + common-mistake response patterns), and **Control** (textbooks only).

Each session had two phases: (1) assisted practice with treatment-arm AI access, (2) unassisted exam with no AI. The preregistered primary outcome was unassisted exam performance.

Headline results:
- **Practice (assisted) performance**: GPT Base +48%, GPT Tutor +127% vs control.
- **Exam (unassisted) performance**: GPT Base −17% vs control (statistically significant, p<0.05); GPT Tutor essentially equal to control (no effect).
- **Mechanism**: GPT Base students treated the AI as a "crutch" — predominantly asking "What is the answer?" and copying solutions. GPT Tutor students predominantly attempted answers and asked for help. Two analyses (GPT-error-rate vs subsequent performance + student-engagement message classification) jointly support crutch-mechanism over hallucination-induced misinformation as the dominant harm pathway.
- **Self-perception**: students in the GPT Base arm did not perceive they had learned less; GPT Tutor students perceived they had learned more (despite no exam-score advantage). Performance/learning dissociation is invisible to the learner.
- **Heterogeneity**: minimal; the harm is broadly distributed.
- **Skill gap**: GPT Base + GPT Tutor reduced grade dispersion during assisted practice (consistent with prior literature on AI as a leveler), but the dispersion-reduction did not persist in the unassisted exam.

This is currently the strongest field-experimental evidence in the KB for AI-induced learning harm and for guardrail-design as the mitigating lever.

## Relevance
- Risk: yes — quantifies harm magnitude (-17%) and mechanism (crutch behavior)
- Erosion: yes — the performance/learning dissociation is the central finding
- Preservation: yes — guardrail design with teacher-curated prompts substantially mitigates the harm
- **Relevance**: HIGH

## Quality
- Evidence basis: preregistered RCT (https://aspredicted.org/4DL_Q3J), N≈1,000, classroom-level randomization, ITT analysis, robustness checks, multiple specifications. PNAS-published.
- Originality: novel two-arm AI design (Base vs Tutor) cleanly isolates the guardrail-design contribution. The crutch-mechanism analysis (error-rate × engagement classification) is a substantive contribution to the empirical literature.
- **Quality**: HIGH

## Extractable Elements
- Concepts:
  - DUPLICATE / UPDATE: [[performance-paradox]] — Bastani is a clean field-experimental case; the existing entry should cite this as the strongest evidence to date.
  - DUPLICATE / UPDATE: [[novice-vulnerability]] — high schoolers learning new material is the canonical novice case; the +48% practice / -17% exam dissociation is the canonical novice-vulnerability pattern.
  - DUPLICATE / UPDATE: [[metacognitive-laziness]] — the crutch mechanism matches Fan et al.'s definition. Bastani's "students don't perceive they learned less" is the perception-gap variant.
  - Possible NEW: "crutch behavior" or "AI-as-crutch" — Bastani uses the term explicitly throughout. But this is adjacent enough to cognitive-offloading and metacognitive-laziness that it's probably better as a body-text term in those entries rather than a new atomic concept.
- Methods: candidate NEW: "guardrail design" or "teacher-curated AI prompts" — but the paper presents one specific instantiation, not a generalized method. Probably fits inside existing scaffolding/think-first cluster as a body-text addition.
- Claims: (1) unfettered AI access can produce performance-without-learning at large effect sizes; (2) guardrails (specifically: teacher-curated solutions + hint-not-answer prompts) substantially mitigate harm; (3) learners cannot self-detect the dissociation.

## Recommendation
**INCLUDE**

Reason: Highest-quality field-experimental evidence in the KB for AI-induced learning harm with a clear mechanism story and a clean intervention contrast. Source distillation + UPDATE proposals to performance-paradox, novice-vulnerability, and metacognitive-laziness.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-29
- **Reason**: Auto-decided per librarian rubric: Relevance=HIGH, Quality=HIGH, not a duplicate. Paper-branch path: source distillation + 3 UPDATE proposals (performance-paradox, novice-vulnerability, metacognitive-laziness). No new concepts (existing entries cover the phenomena; this paper is the strongest empirical evidence for several of them).
