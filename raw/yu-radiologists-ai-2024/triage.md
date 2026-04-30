# Triage: Yu et al. (2024) — Heterogeneity and Predictors of the Effects of AI Assistance on Radiologists

## Source
- Slug: `yu-radiologists-ai-2024`
- Type: `article` (peer-reviewed empirical paper, *Nature Medicine* 30:837–849, March 2024; DOI 10.1038/s41591-024-02850-w)
- Format: pdf, 27 pages, 16,056 words
- Path: `raw/yu-radiologists-ai-2024/source.md` (extracted), `raw/yu-radiologists-ai-2024/original.pdf` (binary)

## Summary

Yu, Moehring, Banerjee, Salz, Agarwal & Rajpurkar (Harvard Medical School + MIT + Stanford) report a large-scale diagnostic study of 140 board-certified radiologists across 324 patient cases and 15 chest X-ray pathologies, with and without AI assistance from a CheXpert-based DenseNet121 model. The study used two complementary experimental designs (a 107-radiologist non-repeated-measure setup and a 33-radiologist repeated-measure setup) to estimate per-radiologist *treatment effects* — the change in absolute error (calibration) and AUROC (discrimination) attributable to AI assistance.

The paper's three load-bearing findings: (1) **substantial heterogeneity** in treatment effects across radiologists — same AI, same tasks, treatment effects ranged from −1.295 to +1.440 (IQR 0.797) on aggregated pathologies, and up to −8.914 to +5.563 (IQR 3.245) on the high-prevalence "abnormal" task. (2) **Experience-based and skill-based predictors fail**: years of experience, subspecialty in thoracic radiology, experience with AI tools, and unassisted-error baseline performance all *failed* to reliably predict who benefits and who is harmed by AI assistance. Critically, lower-performing radiologists did *not* consistently benefit more from AI — counter to the common "AI as leveler" framing. (3) **AI error is the strongest predictor** of treatment effect direction: more accurate AI predictions yield better treatment effects (linear dose-response on aggregated pathologies); AI predictions with absolute error >80 produce a treatment effect of −16.845 (95% CI: −24.288 to −9.403). Direction matters too — AI predictions that *underestimate* ground-truth probabilities yield better treatment effects than equally-erroneous predictions that *overestimate* them.

The methodological contribution is sharper than the headline. Yu et al. show that without proper split sampling, a spurious "hallucinated association" between unassisted error and treatment effect appears (regression-to-the-mean artifact). This is a calibration warning for the AI-in-medicine evaluation literature: many existing claims about who benefits from AI may be statistical artifacts rather than substantive findings. Type: empirical (large-N RCT-style design with within-radiologist comparisons).

## Relevance
- Risk: yes — direct evidence that AI error degrades expert performance in a high-stakes specialist context (medical diagnosis); 6–11% "negative consultation" rate from Goddard et al. (2012) gets a quantitative companion: at high AI error, radiologist treatment effects average −16.8 absolute-error points.
- Erosion: yes — adds expert-population evidence (140 radiologists, real specialty work) to the KB's broader erosion literature; complicates the simple "novices over-rely, experts protected" frame.
- Preservation: yes — implication that targeted measurement of individual treatment effects under realistic deployment conditions is the only reliable predictor; supports the calibration practice and "AI-off drills" literature already in the KB.
- **Relevance**: HIGH

## Quality
- Evidence basis: large-scale randomized study (140 radiologists, 324 cases, 15 pathologies, two complementary designs); peer-reviewed in *Nature Medicine*; pre-registered companion paper (Agarwal et al. NBER 2023, ref 29) provides framework; empirical Bayes shrinkage to control sampling-error overestimation; split sampling to avoid regression-to-the-mean artifacts; multiple-testing correction (Benjamini–Hochberg) throughout.
- Originality: novel population-level evidence on heterogeneity. Compared against existing entries: [[goddard-automation-bias-2012]] is the closest prior — Goddard reviews 74 studies showing AI/CDSS users follow erroneous advice 26% more often; Yu provides experimental dose-response on a single specialist task (radiology) with 140 participants and quantifies how AI error magnitude scales the harm. Compared against [[bauer-discontinuing-ml-2022]]: Bauer shows skill-prevention via discontinuance; Yu shows skill-disruption via AI error during use. Compared against [[passalacqua-less-ai-2024]]: Passalacqua shows novice deskilling under full AI; Yu finds expert heterogeneity is *not* explained by experience level. The "lower-performing radiologists do not consistently benefit more" finding directly challenges the simple AI-as-leveler narrative encoded in [[novice-vulnerability]] and the broader literature.
- **Quality**: HIGH

## Extractable Elements
- Concepts: none NEW (article-type playbook default — paper applies established statistical constructs: treatment effect, calibration vs. discrimination, empirical Bayes shrinkage, split sampling)
- Methods: none NEW (the methodological lesson — measure individual treatment effects under realistic deployment before deploying — is a research-practice recommendation, not a transferable practitioner method)
- Claims (UPDATE candidates):
  - [[automation-bias]] — Yu provides specialist-context, dose-response evidence: as AI error rises, radiologist performance is degraded *more*, with AI absolute error >80 yielding treatment effect −16.845. Sharpens Goddard's 26% RR with a specialist-population effect-size curve.
  - [[human-ai-complementarity]] — Yu provides direct empirical evidence that human-AI team performance is *not* a default outcome of combining humans and AI. Same AI, same radiologists, same tasks: treatment effects span both improvement and degradation. Complementarity is heterogeneous and individual.
  - [[novice-vulnerability]] — Yu provides counter-evidence to the simple "AI helps lower-performers more" framing: lower-performing radiologists did not consistently benefit more from AI assistance. The simple skill-leveling story doesn't hold in this specialist context.
  - [[paradox-of-expertise]] — Yu's failure of experience-based predictors complicates the entry's claim about senior under-adoption being the dominant pattern. Not a contradiction, but a refinement: years of experience does not predict who benefits from AI.
  - [[upskilling-deskilling-paradox]] — Yu's direction-of-error finding (underestimation produces better outcomes than overestimation given same absolute error) adds texture: not all AI errors are equal in their effect on the human-AI workflow.

## Recommendation
**INCLUDE**

Reason: HIGH relevance + HIGH quality + non-duplicate (no Yu/radiology entry exists). Specialist-population, peer-reviewed, large-N evidence on the heterogeneity of AI's effect on expert performance — fills a gap the KB has had between general automation-bias literature and lab-scale studies. Multiple substantial UPDATE candidates; no NEW concepts per article-type playbook.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: AUTO-INCLUDE per rubric (Relevance=HIGH, Quality=HIGH, no duplicate). Re-triggered from prior DEFER. The paper provides the cleanest specialist-context evidence the KB has on heterogeneity of AI effect on expert performance, plus a methodological warning (regression-to-the-mean artifacts in unassisted-vs-treatment-effect studies) that strengthens the KB's calibration-and-evaluation literature. Decision matches recommendation.
