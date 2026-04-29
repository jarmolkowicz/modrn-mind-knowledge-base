---
status: solid
area:
- risk
- erosion
- preservation
type: paper
sources:
  - "Bartoš et al. (2026)"
---

# Bartoš et al. (2026) — Effect of AI on Learning: A Meta-Meta-Analysis

## Citation

Bartoš, F., Bujak, O. Z., Martinková, P., & Wagenmakers, E.-J. (2026). *Effect of Artificial Intelligence on Learning: A Meta-Meta-Analysis.* University of Amsterdam, Czech Academy of Sciences, Charles University. Data and code: https://osf.io/p3xah

## Type

Paper (study-level meta-meta-analysis with publication-bias-adjusted Bayesian model averaging; preregistered framework, 1,840 effect sizes from 67 meta-analyses across 41 articles).

## Key Insight

The published meta-analytic literature on AI and learning is overstated by roughly a factor of three. Once publication bias is corrected, the average effect of AI/LLMs on learning shrinks from SMD ≈ 0.629 to SMD = 0.196 [0.000, 0.323], with extreme heterogeneity (prediction interval −1.521 to 1.908) consistent with both substantial harm and substantial benefit. No subgroup — outcome type, educational field, educational level, or AI/LLM role — shows consistent benefits. The umbrella's epistemic conclusion: the current evidence base does not warrant firm policy or practice recommendations about deploying AI in teaching.

## Key Passages

> "Publication bias-adjusted analyses reveal model-averaged effects approximately one-third the magnitude of unadjusted estimates (standardized mean difference, SMD = 0.196, 95% credible interval from 0.000 to 0.323), along with wide prediction intervals spanning both large negative and positive effects (−1.521 to 1.908)."
> — Bartoš et al. (2026), abstract, [p.2]

> "In the complete data set, a three-level RoBMA-PSMA finds strong evidence for an overall effect (BF₁₀ = 13.3). The model-averaged effect size of SMD = 0.196 [0.000, 0.323] is approximately three times lower than the publication bias-unadjusted estimate of SMD = 0.629 [0.572, 0.685]."
> — Bartoš et al. (2026), Results, [pp.12-13]

> "Crucially, the model-averaged estimate is accompanied by extreme between-study heterogeneity, τ = 0.869 [0.822, 0.926] (BF heterogeneity > 1.00 × 10⁶). Consequently, the prediction interval (PI) of true study effects ranges from −1.521 to 1.908, spanning large negative and positive treatment effects."
> — Bartoš et al. (2026), Results, [p.13]

> "While the publication bias unadjusted BMA meta-analysis finds strong evidence for the presence of the effect (BF₁₀ > 10) in 41 out of 44 meta-analyses with at least 10 effect size estimates, ... the publication bias adjustment with RoBMA-PSMA does not find any meta-analysis with at least 10 effect sizes estimates and strong evidence in favor of the effect of AI/LLMs on learning."
> — Bartoš et al. (2026), Results, [pp.20-21]

> "Subgroup analyses by outcome type, educational field, educational level, and the role of AI/LLMs failed to substantially reduce this heterogeneity or identify subgroups with consistent benefits."
> — Bartoš et al. (2026), Discussion, [p.21]

> "Although our meta-meta-analysis estimates the direct effects of AI and LLM use on learning outcomes, these estimates capture only a narrow subset of the total educational impact... null or heterogeneous average effects may signal a misalignment between systemic changes and current measurement tools rather than limited educational value."
> — Bartoš et al. (2026), Discussion, [p.23]

> "While we believe it is a priori plausible that AI/LLMs may have a positive impact on learning, the current empirical evidence base is insufficiently diagnostic and does not warrant concrete recommendations for educational practice or policy."
> — Bartoš et al. (2026), Discussion, [pp.23-24]

## Relevance

This is the highest-tier evidence document on AI-and-learning effects available to the KB. Three contributions matter for downstream KB use:

**1. Calibration of the broader literature.** The KB cites a number of individual studies (Bastani et al. 2025, Fan et al. 2025, Shen & Tamkin 2026, Liu et al. 2026) showing harm or zero effect on durable learning. The mainstream education-and-edtech narrative cites meta-analyses claiming SMD ≈ 0.6–0.7. Bartoš et al. demonstrate that the published meta-analytic effect is largely a publication-bias artefact: when corrected, the central estimate falls into the band where individual rigorous studies find their results, and the prediction interval explicitly admits the harm patterns documented by `[[performance-paradox]]` and `[[novice-vulnerability]]`. This sets the KB's voice on AI-and-learning claims to "evidence-based, not hype-based" with a citable umbrella anchor.

**2. Heterogeneity as a structural feature, not a sampling problem.** τ = 0.869 with subgroup analyses unable to reduce it [Inference] strongly suggests the relevant moderators are not the surface-level study features captured in published meta-analyses (outcome type, education level, AI role) but the moderators KB entries already emphasise — guardrails (Bastani 2025), mode of use (Lee, Yin et al. 2026), apprenticeship sequencing (Kosmyna 2025), assessment design (Kovanović 2025 cited in Discussion p.23). The umbrella's failure to find structural benefits is consistent with the KB's existing framing: AI's effect on learning depends on *how* it is integrated, not whether it is available.

**3. An evidentiary standard for the KB itself.** The paper documents that 11 of 67 meta-analyses had to be discarded for unrecoverable data, that 9 had funnel-plot extractions too imprecise to use, and that ≥66% of constituent meta-analyses (where assessable) showed at least moderate evidence for publication bias. This implicitly recommends a default skepticism toward "AI improves X" headline numbers in the secondary education-AI literature — a stance that aligns with the KB's existing voice guardrail against hype.

## Supports

- [[performance-paradox]] — umbrella confirms that published "AI improves learning" effects collapse under bias correction; reinforces individual studies (Bastani 2025) showing scaffolded performance ≠ durable learning. The Discussion explicitly cites the Lee et al. (2025) "task stewardship" mechanism and Kosmyna et al. (2025) cognitive-debt finding as plausible reasons average effects fail to consolidate [pp.22-23].
- [[novice-vulnerability]] — wide prediction interval (−1.521 to 1.908) explicitly admits substantial-harm trajectories alongside benefits; subgroup absence-of-benefit at primary/secondary education levels is consistent with novice-population vulnerability documented elsewhere in the KB. The umbrella does not contradict the novice-vulnerability claim; it shows the field-level data are too noisy to test it.
- [[metacognitive-laziness]] — the umbrella's discussion explicitly invokes Lee et al. (2025) task stewardship and Gerlich (2025) critical-thinking decline as candidate explanations for non-consolidation [p.22]; reinforces the Bastani+Fan field/lab pair already cited in the concept.
- [[cognitive-debt]] — Kosmyna et al. (2025) is cited approvingly in the Discussion [pp.22-23] as evidence for why short-term AI assistance during writing predicts worse memory encoding and engagement; the umbrella positions cognitive debt as part of the explanation for the non-effect.
- [[leveling-effect]] — Bartoš shows the leveling pattern documented by Dell'Acqua et al. (2023) at the meta-analytic level disappears when publication bias is corrected and prediction intervals are inspected. Subgroup analysis by educational level finds no robust pattern.
- [[fluency-bias]] — Bartoš's Discussion frames the inflated published effects partly as a product of "broad claims of generalized learning gains" being uncritically accepted [p.2]; the KB's existing fluency-bias entry explains why fluent meta-analytic narratives propagate even when underlying evidence is weak [Inference].
- [[capacity-erosion]] — the −1.521 lower bound of the prediction interval explicitly admits large negative effects on durable learning, providing umbrella-level statistical room for capacity-erosion patterns documented in individual KB entries.
- [[cognitive-offloading]] — the umbrella's Discussion explicitly invokes cognitive offloading (via Gerlich 2025) as a candidate mechanism behind the non-consolidation of average effects [p.22].

## Contradicts / Extends

- Extends: [[bastani-guardrails-math-rct-2025]] — Bastani's classroom-RCT finding of negative durable-learning effects under unguardrailed AI is now reframed as a plausible point in a broader (umbrella-confirmed) heterogeneity distribution rather than an outlier. The umbrella's prediction interval [−1.521, 1.908] explicitly admits the Bastani finding as part of the distribution rather than as a statistical anomaly.
- Extends: [[fan-metacognitive-laziness-2025]] — Fan's lab finding of performance/learning dissociation is positioned by the umbrella as part of the "task stewardship / cognitive offloading" mechanism cited in the Discussion [p.22] as why average effects do not consolidate.
- Extends: [[kosmyna-cognitive-debt-2025]] — directly cited in the Discussion as an exemplar of the cognitive cost mechanism; the umbrella thereby anchors Kosmyna into the broader empirical conversation rather than leaving it as an isolated EEG finding.
- Contradicts (the consensus, not a KB entry): the dominant published meta-analytic narrative of SMD ≈ 0.6–0.7 effects of AI on learning. The KB should treat any future claim of large benefits from individual published meta-analyses (e.g., Wang & Fan 2025) as overstated unless the source explicitly applies Bartoš-grade publication-bias correction.

## Open Questions

- **Mode-of-use moderators not measured.** The umbrella could not test the moderators KB entries already emphasise — guardrails, mode of use (active vs. passive), assessment design, sequencing of unaided practice before AI assistance — because the constituent meta-analyses did not extract them. Bartoš explicitly notes this limitation [pp.7-8]: study-level moderator information was unavailable for many included meta-analyses. *The KB needs primary studies (Bastani 2025; Lee, Yin et al. 2026; Kosmyna 2025) to fill this gap; the umbrella anchors the field, but does not resolve "what works."*
- **Pre/post-ChatGPT comparison.** No substantial difference between studies published before vs. after January 2023 (publication-bias-adjusted SMDs of 0.018 [−0.007, 0.222] and 0.108 [0.000, 0.395] respectively) suggests modern LLMs have not produced a categorically different pattern from earlier AI-tutor work. [Inference] This challenges the popular "ChatGPT changed everything" narrative for learning outcomes, but the post-2023 sample is still small (518 estimates from a young literature).
- **What the umbrella cannot resolve.** Bartoš et al. note (Discussion, [pp.22-23]) that "AI/LLMs also transform education indirectly by reshaping metacognition, instructional practices, feedback processes, and assessment systems, effects that often escape detection by short-term achievement measures." The umbrella's null average effect on direct learning outcomes is therefore not the final word on AI's educational impact; it bounds the *direct, short-term, achievement-test* layer, which may be the wrong layer to optimise [Inference].
- **What it would take to update the estimate.** "Extending the meta-meta-analysis with an additional effect size estimate from a hypothetical study of infinite sample size would add less than three observations worth of effective sample size" [pp.21-22]. The path to a more diagnostic estimate is not more studies but better-designed studies — preregistered, large-scale, with standardized outcome measures and registered replication reports.
