# Update: Human-AI Complementarity

## Source

[[yu-radiologists-ai-2024]]

## Proposed Additions

### To frontmatter `sources:`

Add: `- "Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849. https://doi.org/10.1038/s41591-024-02850-w"`

### To "Key Insight" section (append after the Handa et al. paragraphs)

Yu et al. (2024) provide the cleanest specialist-context evidence the KB has on the heterogeneity of complementarity. In a randomized two-design study of 140 board-certified radiologists across 324 chest X-ray cases and 15 pathologies, the same AI assistance (a CheXpert-based DenseNet121 model) produced treatment effects spanning both substantial improvement and substantial degradation: −1.295 to +1.440 (IQR 0.797) on aggregated pathologies, and up to −8.914 to +5.563 (IQR 3.245) on the high-prevalence "abnormal" task [p.2]. Same model, same patient population, same expert pool — yet the human-AI team outperformed the human alone for some radiologists and underperformed for others. None of the conventional predictors of who would benefit (years of experience, thoracic subspecialty, prior AI-tool experience, unassisted-error baseline) reliably identified which radiologists fell on which side of zero [p.4–5].

This is the empirical version of the entry's existing "complementarity is a design problem, not an inevitability" claim. Yu et al.'s finding pushes the implication further: complementarity is not even reliably a *population-level* design problem — it is an individual-level one. The paper's operational recommendation: "without reliable predictors, it is necessary to measure radiologists' response to AI assistance under realistic simulations of deployment settings before deciding whether to provide AI assistance to different radiologists" [p.11]. This is a stronger requirement than current AI-deployment practice typically meets — most clinical AI deployments use population-level studies to justify rollout to all clinicians in a role, not per-clinician measured benefit.

The strongest predictor Yu et al. did identify is AI error itself: more accurate AI yields better treatment effects, with a roughly linear dose-response on aggregated pathologies and a treatment effect of −16.845 when AI absolute error exceeds 80 (on a 0–100 scale) [p.9]. Direction of error matters too — AI predictions that underestimate ground-truth probabilities produce better treatment effects than equally-erroneous predictions that overestimate them. The complementarity sweet spot in this expert specialist context depends not just on task structure (the entry's existing framing) but on the AI model's specific failure-mode profile: a low-error AI that tends to underestimate is more complementary than a higher-error AI that tends to overestimate, even on the same diagnostic task.

### To "Related" section

Add: `- [[yu-radiologists-ai-2024]] — specialist-context evidence that complementarity is heterogeneous at the individual-expert level; same AI, same tasks, same expert pool yields treatment effects spanning improvement and degradation; AI error magnitude and direction shape the complementarity outcome`

### To "Sources" section

Add: `- [[yu-radiologists-ai-2024]] — Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849.`
