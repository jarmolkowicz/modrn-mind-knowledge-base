# Triage: Fernandes et al. (2026) — AI Makes You Smarter But None the Wiser

## Source
- Slug: `fernandes-metacognition-2025`
- Type: `paper` (peer-reviewed empirical, two studies)
- Format: pdf, 18 pages, ~18,682 words
- Path: `raw/fernandes-metacognition-2025/source.md` (extracted), `raw/fernandes-metacognition-2025/original.pdf` (binary)
- Citation: Fernandes, D., Villa, S., Nicholls, S., Haavisto, O., Buschek, D., Schmidt, A., Kosch, T., Shen, C., & Welsch, R. (2026). AI makes you smarter but none the wiser: The disconnect between performance and metacognition. *Computers in Human Behavior*, 175, 108779. https://doi.org/10.1016/j.chb.2025.108779

## Summary

Two large-sample empirical studies (Study 1 N=246; Study 2 N=452) examining how generative-AI use affects metacognitive monitoring on logical-reasoning tasks (LSAT items). Study 1 compared an AI-using group against an open no-AI dataset (Jansen et al., 2021); Study 2 ran a randomized AI vs. no-AI comparison with monetary incentives for accurate metacognition. Both studies measured metacognitive bias (estimate–performance gap), metacognitive sensitivity (AUC from confidence ratings), and AI literacy via the SNAIL scale (three subscales: Technical Understanding, Critical Appraisal, Practical Application). A Bayesian computational model decomposed performance estimates into bias and noise components.

Three principal findings: (1) AI use improved task performance by ~3 points but inflated self-estimates by ~4 points — robust overestimation in both studies. (2) The Dunning–Kruger Effect *disappeared* under AI use: the Bayesian model's noise parameter σ collapsed to ~1 (95% HDI [0.84, 1.19]) for the AI group versus σ ≈ 1.78 for the no-AI group, indicating that AI levels skill differences and produces uniform overconfidence rather than skill-scaled miscalibration. (3) Higher self-rated AI literacy correlated with *lower* metacognitive accuracy (r = .21, p < .01 in Study 1; r = .20, p < .01 in Study 2 between SNAIL Technical Understanding and overestimation), with the Technical Understanding subscale carrying the strongest effect — counterintuitive evidence against the assumption that AI literacy is uniformly protective.

The authors interpret these results through an "augmentation hypothesis" (AI compresses skill-based variance in performance and metacognitive judgment) and connect them to the illusion of explanatory depth (Fisher & Oppenheimer, 2021). Monetary incentives in Study 2 did not correct overestimation, suggesting low effort is not the primary driver. Mean AUC fell below the conventional .70 acceptable benchmark for metacognitive sensitivity in both AI and no-AI groups, but participants used AI shallowly (46% issued only one prompt per question; 8% used >3) — consistent with copy-paste behavior rather than reflective engagement. Design recommendations include "explain-back" micro-tasks before answer submission, AI uncertainty visualization, and post-task reflection prompts.

## Relevance
- Risk: yes — direct empirical evidence on overconfidence and erosion of self-monitoring under AI use; quantifies the size of the effect across two large samples.
- Erosion: yes — DKE flattening and AUC decline give the KB its first computational-model decomposition of metacognitive bias and noise under AI.
- Preservation: yes — Table 6 provides specific design-principle countermeasures (confidence calibration, uncertainty visualization, cognitive forcing, explain-back).
- **Relevance**: HIGH

## Quality
- Evidence basis: peer-reviewed, *Computers in Human Behavior* (Elsevier; high-tier HCI/behavioral journal). Two studies, large N (246 + 452), preregistered analysis path implied by the open data on OSF (https://osf.io/svax9/). Bayesian computational model (Stan/HMC, R-hat < 1.1, ESS > 1000). Includes randomized arm in Study 2 with monetary incentives — strongest design among the existing metacognition-under-AI evidence in the KB.
- Originality: provides the *primary empirical anchor* for findings already partially captured via secondary sources — `[[dolan-competence-assessment-2025]]` (PsyPost summary, currently DEFER) explicitly cites this paper as the underlying study. Substantively complements `[[tankelevitch-metacognitive-demands-2023]]` (theoretical/conceptual) by providing the empirical investigation Tankelevitch et al. called for. Adds quantification and a Bayesian decomposition the KB does not yet have. Compared against `[[he-illusion-competence-2023]]`, `[[shaw-cognitive-surrender-2026]]`, `[[bastani-guardrails-math-rct-2025]]`, `[[leonardi-artificial-certainty-2026]]`, `[[keshky-illusory-competence-2026]]`, `[[reich-artificial-confidence-2026]]`: each captures a different angle of the confidence-competence gap; none provide the bias/noise decomposition or the AI-literacy paradox that Fernandes does.
- **Quality**: HIGH

## Extractable Elements
- **Concepts**:
  - Likely no NEW concept entry. Fernandes does not introduce a novel named phenomenon; it provides empirical evidence supporting existing concepts (`[[confidence-competence-gap]]`, `[[metacognition]]`). The "AI literacy paradox" finding is striking but is reported as an empirical observation, not a labeled construct in the paper. Recommend conservative path: capture as UPDATE rather than NEW.
- **Methods**: none NEW. Table 6's "explain-back micro-task" and "uncritical-reliance design principles" are interesting but documented as one-row design recommendations rather than developed protocols — best surfaced inside the source distillation's Key Findings rather than as a standalone method entry.
- **Claims** (for source distillation):
  1. AI use improves logical-reasoning task performance (~3 points) but inflates self-estimates (~4 points) — overconfidence persists in both studies.
  2. The Dunning–Kruger Effect is eliminated under AI use: the Bayesian model's noise parameter σ_AI ≈ 1 vs. σ_noAI ≈ 1.78, indicating skill-scaled miscalibration disappears with AI.
  3. Higher AI literacy (especially the SNAIL Technical Understanding subscale) correlates with greater performance overestimation — counterintuitive against the assumption that AI literacy is purely protective.
  4. Monetary incentives for accurate metacognition do not correct overestimation (Study 2, +£0.50 ≈ 8% bonus).
  5. Metacognitive sensitivity (AUC) fell below the .70 acceptable threshold in both AI and no-AI groups — confidence ratings only weakly distinguish correct from incorrect responses.
  6. Most participants used AI shallowly: 46% issued one prompt per question; only 8% exceeded three prompts.
  7. Three design principles surface from the studies: confidence calibration with uncertainty visualization, cognitive forcing functions, and "explain-back" micro-tasks before answer submission.

## Recommendation
**INCLUDE**

Reason: peer-reviewed primary source, two large studies including a randomized arm, directly empirically anchors several existing KB concepts (`[[confidence-competence-gap]]`, `[[metacognition]]`) that currently rely on secondary or theoretical citations. Provides the first computational-model decomposition of metacognitive bias and noise under AI use in the KB. Resolves the DEFER queued at `[[dolan-competence-assessment-2025]]`.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: Auto-INCLUDE under the librarian rubric (Relevance=HIGH, Quality=HIGH, not a duplicate). Resolves the DEFER on `dolan-competence-assessment-2025`. Distillation will produce the source entry plus UPDATE proposals for `confidence-competence-gap` and `metacognition`. No new concept or method entries planned; the AI-literacy-overconfidence finding is significant but is an empirical observation rather than a novel named construct.
