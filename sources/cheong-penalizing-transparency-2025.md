---
status: emerging
area: [risk]
type: paper
sources:
  - "Cheong, I., Guo, A., Lee, M., Liao, Z., Kadoma, K., Go, D., Chang, J. C., Henderson, P., Naaman, M., & Zhang, A. X. (2025). Penalizing Transparency? How AI Disclosure and Author Demographics Shape Human and AI Judgments About Writing. arXiv:2507.01418v1."
---

# Cheong et al. (2025) — Penalizing Transparency

## Citation

Cheong, I., Guo, A., Lee, M., Liao, Z., Kadoma, K., Go, D., Chang, J. C., Henderson, P., Naaman, M., & Zhang, A. X. (2025). Penalizing Transparency? How AI Disclosure and Author Demographics Shape Human and AI Judgments About Writing. *arXiv:2507.01418v1* (CHIWORK 2025 Workshop on Generative AI Disclosure).

**URL:** [arXiv preprint](https://arxiv.org/abs/2507.01418)

## Type

Paper (pre-registered factorial experiment, n=1,970 human raters + 2,520 LLM evaluations)

## Key Insight

A 2×3×3 factorial design (AI disclosure × race × gender) shows that **disclosing AI assistance produces a measurable penalty in writing-quality judgments — among both human and LLM evaluators**. The disclosure penalty is modest in absolute terms (less than 0.15 points on a 7-point scale, p<0.05) but consistent.

The more disturbing finding is **"vanishing alignment"** in LLM raters: GPT-4o-mini and Qwen2.5-7B-Instruct each showed fairness-oriented preferences in the control condition (GPT favored Black authors, +0.137 vs. Asian; Qwen favored women, +0.133 vs. men, both p<0.001), but those preferences **disappeared when AI assistance was disclosed**. The same identical article, judged by the same model, gets a different demographic-fairness adjustment depending on whether it carries an "AI was used" label.

This matters because LLM evaluators are increasingly the gatekeepers of high-stakes decisions: 99% of Fortune 500 companies use automated screening in hiring; Texas grades standardized-test essays with AI; AI-based performance reviews are deploying. If LLM fairness behaviors are conditional and unstable across surface contextual cues, "AI alignment" is far more fragile than its training metrics suggest. The KB should treat alignment-by-RLHF as a contextually-triggered behavior, not a stable property.

For human thinking with AI: this is an erosion-of-fairness mechanism, not a [[capacity-erosion|capacity erosion]] mechanism. AI disclosure asymmetrically burdens marginalized groups under LLM evaluation, while doing so uniformly under human evaluation. The same transparency norm has different equity consequences depending on who's reading.

## Key Passages

> "We find that both human and LLM raters consistently penalize disclosed AI use. However, only LLM raters exhibit demographic interaction effects: they favor articles attributed to women or Black authors when no disclosure is present. But these advantages disappear when AI assistance is revealed."
> — Cheong et al., [p.1] (abstract)

> "Both models presented statistically significant AI disclosure penalty (-0.112 points, p = 0.002 for GPT-4o-mini and -0.133 points, p = 0.026 for Qwen2.5-7B-Instruct). However, unlike humans, the AI models demonstrated distinct demographic preferences in the control condition."
> — Cheong et al., [p.3]

> "Both favored groups — Black authors and women — are historically marginalized. These preferences may reflect an alignment-driven over-correction, in which models trained with human feedback disproportionately reward underrepresented identities. However, when AI disclosure is present, these fairness-oriented preferences vanish. We term this dynamic a form of 'vanishing alignment,' where the social and ethical calibration of model behavior becomes fragile under changing contextual cues."
> — Cheong et al., [p.4]

> "Beneath these questions lies a desire to calibrate judgments to discern the boundary between human insight and synthetic fluency."
> — Cheong et al., [p.1]

> "If reader perceptions about AI disclosure are filtered through gendered, racialized, or other socio-epistemic cues, then the burden of openness becomes asymmetrical. … the groups historically under-resourced and under-represented face the greatest risk of stigmatization for using AI."
> — Cheong et al., [p.2]

## Methodology

- 1,970 human raters via pre-registered between-subjects design
- 2,520 LLM ratings: 1,260 each from GPT-4o-mini and Qwen2.5-7B-Instruct
- Single human-authored news article; only the author's photo, biography, and disclosure statement varied across 18 conditions (2 disclosure × 3 races × 3 genders)
- Dependent measures: trustworthiness, comprehensiveness, writing quality, share likelihood (7-point Likert; mean = perception score)
- Manipulation checks: only 1.1% of participants correctly guessed the study purpose

## Relevance

Two distinct contributions for the KB:

- **Disclosure-penalty quantification.** Adds rigorous numbers to the existing [[disclosure-penalty]] concept. Effect is real but modest (<0.15/7), pre-registered, and replicates across humans and LLMs. Makes [[transparency-paradox]] testable rather than assertion.
- **Vanishing alignment.** A fresh and load-bearing concept the KB should integrate. RLHF-trained fairness preferences in LLMs are *contextually triggered*, not stable. The mere presence of an AI-disclosure cue toggles the model out of its fairness-oriented mode. This generalizes beyond the disclosure case: any surface contextual signal might rearrange whose voices a model amplifies. Connects to Hofmann et al. (2024)'s "covertly racist decisions" finding that alignment behaviors are surface-only.

## Supports

- [[disclosure-penalty]] — quantifies the effect with pre-registered N=1,970
- [[transparency-paradox]] — provides empirical grounding
- [[raj-disclosure-penalty-2026]] — converging evidence (Raj et al. follow-up work in the same space)
- [[automation-bias]] — LLMs as evaluators amplify the same dynamic Goddard documented for clinical decision support
- [[fluency-bias]] — readers calibrate against "synthetic fluency"; the disclosure cue partially counteracts the fluency-truth coupling

## Contradicts / Extends

- Extends [[raj-disclosure-penalty-2026]] — Cheong et al. add the demographic-interaction angle that Raj's design didn't include.
- Surfaces a tension with the standard "AI alignment" claim: alignment behaviors observed in benign contexts may not survive contextual perturbation. Worth a new concept entry on "vanishing alignment" as a mechanism that intersects with [[automation-bias]] and the [[ai-moralization]] cluster.

## Open Questions

- The effect was tested on news articles (a genre with strong objectivity expectations). Does the disclosure penalty hold for genres where AI assistance is normalized (marketing copy, code documentation, entertainment writing)?
- "Vanishing alignment" was demonstrated for two models on demographic dimensions. What's the breadth of contextual cues that toggle alignment behaviors? (Authorship signals? Topic? Politeness markers?)
- The study cannot disentangle whether the disclosure penalty is from perceived authorship dilution, perceived effort reduction, or epistemic stigma per se. Each implies a different intervention.
