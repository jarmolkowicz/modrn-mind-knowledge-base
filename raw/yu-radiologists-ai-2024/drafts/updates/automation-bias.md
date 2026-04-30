# Update: Automation Bias

## Source

[[yu-radiologists-ai-2024]]

## Proposed Additions

### To frontmatter `sources:`

Add: `- "Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849. https://doi.org/10.1038/s41591-024-02850-w"`

### To "Why It Matters" section (append after the Gonzalez et al. paragraph)

Yu et al. (2024) extend the team-level evidence into a specialist diagnostic context with an explicit dose-response. In a randomized two-design study of 140 board-certified radiologists across 324 chest X-ray cases and 15 pathologies, AI prediction error scaled the harm: more accurate AI yielded better radiologist treatment effects, and AI predictions with absolute error >80 (on a 0–100 probability scale) produced a treatment effect of −16.845 absolute-error points (95% CI: −24.288 to −9.403). Critically, the direction of AI error mattered too — predictions that *underestimated* ground-truth probabilities yielded better treatment effects than equally-erroneous predictions that *overestimated* them. Yu et al. interpret the underlying mechanism plainly: "radiologists struggle to consistently distinguish between accurate and inaccurate AI predictions and can be misled by inaccurate AI predictions" [p.11]. This is automation bias at expert scale: 140 specialists working in their domain, on their core task, still systematically followed AI into error.

### To "Key Insight" section (append after the Han et al. paragraph)

Yu et al. (2024) add a heterogeneity dimension to the feedback-loop description above. The same AI on the same tasks produced treatment effects ranging from −1.295 to +1.440 (IQR 0.797) on aggregated pathologies and up to −8.914 to +5.563 on individual high-prevalence tasks — meaning automation bias is not uniform across experts. Conventional predictors of who is most susceptible (years of experience, subspecialty, AI-tool familiarity, baseline diagnostic skill) all failed to identify which radiologists would be helped versus harmed. The practical implication: at the individual expert level, susceptibility to automation bias cannot be inferred from career stage or test scores; it must be measured per-radiologist under realistic deployment conditions before deciding who receives AI assistance. This is the strongest specialist-population evidence the KB has against the assumption that experts can self-calibrate their AI use.

### To "Related" section

Add: `- [[yu-radiologists-ai-2024]] — specialist dose-response evidence: AI absolute error >80 yields treatment effect of −16.845 in 140 board-certified radiologists; experience-based and skill-based predictors of automation-bias susceptibility all fail`

### To "Sources" section

Add: `- [[yu-radiologists-ai-2024]] — Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849.`
