# Triage: Stadler, Bannert & Sailer (2024) — Cognitive Ease at a Cost

## Source
- Slug: `stadler-cognitive-ease-cost-2024` (renamed from `stadler-bannert-sailer-cognitive-ease-cost-2024` for citability)
- Type: `paper`
- Format: pdf, 7 pages, 7725 words
- Path: `raw/stadler-cognitive-ease-cost-2024/source.md` (extracted), `raw/stadler-cognitive-ease-cost-2024/original.pdf` (binary)
- Citation: Stadler, M., Bannert, M., & Sailer, M. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. *Computers in Human Behavior*, 160, 108386. https://doi.org/10.1016/j.chb.2024.108386
- License: CC BY (open access)

## Summary

Peer-reviewed RCT-style study (N=91 university students at a German university, between-subjects, randomization with prior-knowledge covariate) directly comparing LLM-based information gathering (ChatGPT-3.5) against traditional search engines (Google) on a 20-minute open-ended socio-scientific research task: produce a recommendation with justifications about whether a friend should use sunscreen with mineral nanoparticles. The study extends Kammerer et al. (2021)'s search-as-learning paradigm to compare it against LLM use.

Three pre-registered hypotheses tested. **H1 (cognitive load)**: LLM users showed significantly lower extraneous, intrinsic, and germane cognitive load (Klepsch et al. 2017 scale) — strongest effect for germane load (η² = 0.27). **H2 (justification quality)**: LLM users produced lower-quality justifications (1.20 vs 1.87 relevant arguments; F = 11.18, p = .001, η² = 0.11). The effect was **fully mediated by germane cognitive load** (β = 0.15, p = .020 indirect; β = 0.19, p = .095 direct) — i.e., the entire group difference in argument quality flows through reduced germane load. **H3 (homogeneity)**: contrary to expectation, LLM users did **not** show more homogeneous recommendations than search-engine users (χ²(2) = 1.78, p = .411).

The framing — "Cognitive ease at a cost" — is the paper's own naming for an effect that the KB captures across multiple concepts: AI's ease of use is the very thing that bypasses the effortful processing that produces deeper learning. Authors are established cognitive-load-theory researchers (Bannert is a major figure in CLT; Sailer in learning analytics).

## Relevance
- Risk: yes — empirical evidence that LLM use produces lower-quality reasoning under cognitive ease.
- Erosion: yes — direct demonstration that reduced cognitive load (especially germane load) translates to weaker argument construction; aligns with metacognitive-laziness, cognitive-debt, performance-paradox.
- Preservation: yes — establishes germane cognitive load as the *mediator* of the effect, which directly informs which difficulty-preserving interventions (search engines, retrieval prompts, generation effects) actually do work.
- **Relevance**: HIGH

## Quality
- Evidence basis: peer-reviewed RCT in *Computers in Human Behavior* (CHB), one of the better-respected journals in the human-AI-interaction space; preregistered hypotheses; mediation analysis; two-rater coding with κ = 0.92 / 0.89 inter-rater agreement; OSF-hosted instructions.
- Originality: not introducing a new construct; instead, providing direct empirical anchor for the "cognitive ease at a cost" pattern that [[fluency-bias]], [[desirable-difficulty]], and [[metacognitive-laziness]] collectively describe. Compared against [[fluency-bias]], [[desirable-difficulty]], [[cognitive-debt]], [[metacognitive-laziness]], [[performance-paradox]], [[cognitive-friction]], [[social-friction]] — each gets a corroborating empirical leg, none gets a new label.
- Limitations to declare: small sample (N=91), single-session, single domain (nano-particles), university-student sample (high digital literacy), no post-task knowledge-test for retention, no think-aloud, ChatGPT-3.5 specifically (now superseded). Authors acknowledge all in §7.1.
- **Quality**: HIGH

## Extractable Elements

- **Concepts**: none NEW. Strong UPDATE candidates: [[fluency-bias]], [[desirable-difficulty]], [[cognitive-debt]], [[metacognitive-laziness]], [[performance-paradox]], [[cognitive-friction]]. Mention only in [[social-friction]] is not warranted (the homogeneity null is about *output diversity*, not *interpersonal feedback*).
- **Methods**: none. The study uses Kammerer et al. (2021)'s sunscreen socio-scientific task — that's a study-design choice not generalizable enough to warrant its own KB method entry.
- **Claims**:
  - LLM use reduces all three CLT cognitive-load components (ECL, ICL, GCL) significantly vs. search engines, strongest effect on GCL [p.4, Table 2].
  - LLM use produces lower-quality justifications, fully mediated by reduced germane cognitive load [p.5].
  - LLM use does **not** narrow the diversity of recommendations [p.5, Table 3] — empirical counter-evidence to homogenization concerns at the *output-decision* level.

## Recommendation
**INCLUDE**

Reason: HIGH relevance, HIGH quality, no duplicate. Peer-reviewed CHB 2024; mediation analysis (germane load fully mediates the effect of LLM access on justification quality) is the kind of mechanistic anchor multiple existing KB concepts currently lack. Conservative: no NEW concepts — paper provides corroboration, not new constructs.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: AUTO-mode re-triage. Original DEFER overridden per task brief. HIGH/HIGH/no-duplicate triggers auto-INCLUDE; full GCL-mediation result strengthens multiple KB concepts (fluency-bias, desirable-difficulty, metacognitive-laziness, cognitive-debt, performance-paradox, cognitive-friction) at this granularity.
