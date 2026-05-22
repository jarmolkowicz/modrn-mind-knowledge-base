# Triage: When combinations of humans and AI are useful: A systematic review and meta-analysis

## Source
- Slug: `vaccaro-human-ai-meta-analysis-2024`
- Type: `paper` (extractor heuristic said `article`; corrected — peer-reviewed Nature Human Behaviour meta-analysis)
- Format: pdf, 14 pages, 10,552 words
- Path: `raw/vaccaro-human-ai-meta-analysis-2024/source.md` (extracted), `raw/vaccaro-human-ai-meta-analysis-2024/original.pdf` (binary)

## Summary

Vaccaro, Almaatouq & Malone (MIT Center for Collective Intelligence) conduct a preregistered
systematic review and meta-analysis of human-AI collaboration, published in *Nature Human
Behaviour* (vol. 8, 2293–2303, Dec 2024). From an initial pool of 5,126 papers they identified
106 experimental studies (published Jan 2020–Jun 2023) that each evaluated three conditions —
human alone, AI alone, and the human-AI combination — yielding 370 unique effect sizes analysed
in a three-level random-effects meta-analytic model.

The headline finding is a corrective to the common "human + AI = better" assumption. On average,
human-AI combinations performed *significantly worse* than the best of human-or-AI alone (Hedges'
g = -0.23; 95% CI -0.39 to -0.07) — i.e. no human-AI *synergy* on average. However, against the
weaker baseline of the human alone, combinations did help: *human augmentation* was positive and
medium-to-large (g = 0.64; 95% CI 0.53 to 0.74). Two moderators were significant: (1) task type —
decision tasks showed losses (g = -0.27) while creation tasks showed gains (g = 0.19, n=34, not
significant on its own but significantly different from decision tasks); (2) relative human/AI
performance — when humans outperformed AI alone, the combination gained (g = 0.46); when AI
outperformed humans, it lost (g = -0.54). Notably, the presence of AI explanations and AI
confidence displays did *not* significantly moderate performance — a null result against features
much of the field has emphasised.

This is high-quality meta-analytic evidence: preregistered, PRISMA-compliant, with publication-bias
diagnostics (Egger's regression, rank correlation), outlier/influence sensitivity analyses, and
leave-one-out robustness checks. The evidence type is quantitative synthesis of experimental
literature.

## Relevance
- Risk: yes — directly quantifies when human-AI collaboration produces *performance losses*, and shows the loss pattern (decision tasks, AI-stronger contexts).
- Erosion: partial — not about skill erosion per se, but about over/under-reliance dynamics that the discussion explicitly invokes.
- Preservation: yes — identifies the conditions under which the combination *does* add value (creation tasks, human-stronger contexts), informing how to design for it.
- **Relevance**: HIGH

## Quality
- Evidence basis: peer-reviewed *Nature Human Behaviour*; preregistered (OSF); 106 studies / 370 effect sizes; three-level meta-analytic model with robust variance estimation; full bias and sensitivity diagnostics. Among the strongest empirical evidence the KB could hold on this question.
- Originality: this is the empirical anchor the KB's existing `[[human-ai-complementarity]]` concept and `[[complementarity-framework]]` method currently lack — both are `status: speculative` and the complementarity concept currently asserts "meta-analyses show that human-AI teams can outperform either party alone," a claim this paper directly qualifies (synergy is the *exception*, not the rule). Compared against `[[dellacqua-jagged-frontier-2023]]` (single-firm field experiment) and `[[yu-radiologists-ai-2024]]` (single-domain RCT), this is the broad cross-task synthesis those point-studies sit inside.
- **Quality**: HIGH

## Extractable Elements
- Concepts:
  - human-AI synergy vs. human augmentation — the two-baseline distinction (combination beats best-of-both vs. combination merely beats human alone). Candidate NEW concept; likely overlaps with `[[human-ai-complementarity]]` (synergy ≈ complementarity) — the augmentation/synergy *distinction* itself may be the novel atomic idea.
- Methods: none new — the paper's findings update the existing `[[complementarity-framework]]`.
- Claims: combinations underperform best-of-both on average (g=-0.23); augmentation positive (g=0.64); decision-task losses / creation-task gains; relative-performance moderator; explanation & confidence null results.

## Recommendation
**INCLUDE**

Reason: Peer-reviewed, preregistered meta-analysis of 106 studies — the strongest cross-task
empirical evidence available on human-AI complementarity, and a direct corrective to a claim
currently stated in an existing KB concept.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-05-22
- **Reason**: User confirmed the recommendation. Strongest cross-task empirical evidence available on human-AI complementarity; proceed to distill with source entry + updates to existing complementarity concept/method.
