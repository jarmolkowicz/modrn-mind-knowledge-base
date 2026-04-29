# Triage: Bartoš et al. (2026) — Effect of AI on Learning: A Meta-Meta-Analysis

## Source
- Slug: `bartos-et-al-2026-effect-of-artificial-intelligence-on-learning` (workbench); canonical KB slug: `bartos-ai-learning-meta-meta-2026`
- Type: paper (study-level meta-meta-analysis / "umbrella review with re-extracted study-level data")
- Format: pdf, 43 pages, 12,646 words
- Path: `raw/bartos-et-al-2026-effect-of-artificial-intelligence-on-learning/source.md` (extracted), `raw/.../original.pdf` (binary)
- Authors: František Bartoš, Oliwia Z. Bujak, Patrícia Martinková, Eric-Jan Wagenmakers (University of Amsterdam Psychological Methods + Czech Academy of Sciences + Charles University)
- Data + code: OSF https://osf.io/p3xah

## Summary

Bartoš and colleagues conducted a study-level meta-meta-analysis of 1,840 effect sizes drawn from 67 meta-analyses (in 41 articles) on the effect of AI/LLMs on learning. Rather than pool the published meta-analyses' headline numbers, they re-extracted the underlying study-level data — preferring tables, forest plots, supplementary material, and (when necessary) plot-digitized funnel plots — then re-analyzed everything under a single Bayesian model-averaged framework with state-of-the-art publication-bias adjustment (RoBMA-PSMA: selection models combined with PET-PEESE; sensitivity check via RoBMA-WF, weight-functions only). They also stratified estimates by ChatGPT era (≤2022 vs. >2022) and ran subgroup analyses by outcome type, educational field, educational level, and AI/LLM role.

The headline finding inverts the field's apparent consensus. The publication-bias-unadjusted pooled effect (SMD ≈ 0.629) collapses to SMD = 0.196 [95% CrI 0.000, 0.323] once bias is corrected — about one-third the published magnitude. Heterogeneity is extreme (τ = 0.869), so the prediction interval for true study effects spans −1.521 to 1.908, i.e., consistent with both substantial harm and substantial benefit. Subgroup analyses fail to identify any moderator (outcome, field, level, role) that yields consistent benefits or substantially reduces heterogeneity. Crucially, on the meta-analysis level: applying RoBMA-PSMA, **zero out of 44 individual meta-analyses with ≥10 effect sizes retain strong evidence for the effect** after publication-bias correction (vs. 41/44 in the unadjusted re-analysis). The authors conclude that broad claims of generalized learning gains from AI/LLMs are premature and that the current evidence base does not warrant firm policy or practice recommendations.

This is the highest-tier evidence document available on AI-and-learning effects: it does for the AI-education meta-analytic literature what well-known re-analyses (e.g., of the priming literature) did to other empirically embarrassed corners of psychology. It does not introduce a new construct; its contribution is *epistemic*: it tells the KB how much weight to put on the dozens of cited "AI improves learning by SMD ≈ 0.6–0.7" claims circulating in education, edtech, and consulting decks.

## Relevance
- Risk: yes — directly addresses the evidentiary basis for AI-in-education recommendations; quantifies how much existing claims are inflated by publication bias.
- Erosion: yes — the discussion explicitly frames known erosion mechanisms (Lee et al. 2025 task stewardship, Gerlich 2025 critical-thinking decline, Kosmyna et al. 2025 cognitive debt) as plausible explanations for why average effects fail to consolidate.
- Preservation: yes — the prescriptive implication ("integrate AI into the learning process; procedural vs. mastery-oriented use differentiates harm from benefit; conversation-based assessments instead of high-stakes exams") aligns with KB's preservation orientation.
- **Relevance**: HIGH

## Quality
- Evidence basis: highest available tier — meta-meta-analysis, study-level re-extraction (not just pooling reported pooled estimates), state-of-the-art publication-bias correction (RoBMA-PSMA + RoBMA-WF sensitivity), preregistered Bayesian framework, open data + code on OSF, reanalysis by senior methodologists (Wagenmakers; Martinková psychometrics).
- Originality: complementary, not duplicative, with existing KB entries. Extends `[[performance-paradox]]` and `[[novice-vulnerability]]` from individual studies (Bastani 2025, Fan 2025, Shen & Tamkin 2026) to the umbrella level — these are not contradicted but rather contextualized as "specific mechanisms behind a literature whose average effect is much weaker than reported." Strengthens `[[cognitive-debt]]`'s standing by providing umbrella-level absence-of-evidence for the simpler "AI helps learning" framing. No existing KB entry covers publication bias in AI-education research.
- **Quality**: HIGH

## Extractable Elements
- Concepts: none NEW (umbrella reviews rarely introduce constructs; this paper's contribution is methodological + epistemic). One borderline candidate — *evidence inflation* / *meta-analytic mirage* — does not reach the threshold for a standalone concept; the umbrella's findings function as evidence for existing concepts rather than naming a new phenomenon.
- Methods: none NEW (RoBMA-PSMA is a statistical technique outside the KB's scope of "structured guidance for human-AI work").
- Claims: 4 high-value UPDATE-grade claims:
  1. Bias-adjusted SMD = 0.196 [0.000, 0.323] vs. unadjusted 0.629 — published meta-analyses overstate AI-on-learning effects ~3×.
  2. Extreme between-study heterogeneity (τ = 0.869); 95% PI = [−1.521, 1.908]: a randomly chosen new study could plausibly find substantial harm or substantial benefit.
  3. No subgroup (outcome / field / level / role) shows consistent benefit or substantially reduced heterogeneity.
  4. After RoBMA-PSMA correction, 0/44 meta-analyses (with ≥10 effect sizes) retain strong evidence for an effect, vs. 41/44 unadjusted.

## Recommendation
**INCLUDE**

Reason: Highest-tier umbrella evidence on the central KB topic (AI's effect on learning). Source distillation is high-leverage (one citation can do the work of several individual meta-analyses' worth of UPDATE proposals across `[[performance-paradox]]`, `[[novice-vulnerability]]`, `[[metacognitive-laziness]]`, `[[cognitive-debt]]`, plus a meta-evidentiary update implicitly anchoring the broader KB voice on this topic). No NEW concept warranted — the paper's contribution is calibration of an existing literature, not a new construct.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: Overrides prior DEFER. Re-triggered for full ingestion as the highest-tier evidence on AI-and-learning. Source distillation + UPDATE proposals to performance-paradox, novice-vulnerability, metacognitive-laziness, cognitive-debt, leveling-effect. No NEW concept (umbrella reviews calibrate existing literatures rather than naming new phenomena).
