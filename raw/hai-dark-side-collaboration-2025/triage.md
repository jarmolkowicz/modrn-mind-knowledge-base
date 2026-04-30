# Triage: Hai et al. (2025) — The Dark Side of Employee-Generative AI Collaboration

## Source

- Slug: `hai-dark-side-collaboration-2025`
- Type: `paper`
- Format: pdf, 11 pages, 12,023 words
- Path: `raw/hai-dark-side-collaboration-2025/source.md` (extracted), `raw/hai-dark-side-collaboration-2025/original.pdf` (binary)
- Citation: Hai, S., Long, T., Honora, A., Japutra, A., & Guo, T. (2025). The dark side of employee-generative AI collaboration in the workplace: An investigation on work alienation and employee expediency. *International Journal of Information Management*, 83, 102905. https://doi.org/10.1016/j.ijinfomgt.2025.102905
- Note on slug: "hai" is the lead author's surname (Hai Shenyang), not an acronym. Standard surname-keyword-year stem applies; no rename needed.

## Summary

Hai and colleagues develop and empirically test a moderated mediation model linking daily employee-GenAI collaboration to unethical workplace behavior. The headline pathway: GenAI collaboration → work alienation (psychological disconnection from work) → employee expediency (cutting corners, manipulating performance metrics, ignoring protocols). Digital job demands moderate the first leg: the alienation effect is significant under high digital demands and non-significant under low demands.

The empirical design is unusually strong for the GenAI-at-work literature: a daily experience sampling method (ESM) with 229 service-industry employees in China across 5 workdays, yielding 1,050 matched within-person observations (two surveys per day, separated by ~2 hours). Multilevel path analysis with random slopes; group-mean centering at Level 1, grand-mean centering at Level 2; Monte Carlo confidence intervals (10,000 iterations) for indirect and conditional indirect effects. Established scales throughout (Kong et al. 2023 for collaboration; Shantz et al. 2014 for alienation; Greenbaum et al. 2018 for expediency; Ye & Chen 2024 for digital job demands). Reliabilities all ≥ .92. Construct validity confirmed via four-factor multilevel CFA against three alternative models.

The theoretical scaffolding integrates two established frames: human-AI collaboration research (Anthony et al. 2023; Raisch & Krakowski 2021) and the Job Demands-Resources model (Bakker et al. 2023). Neither construct (work alienation; expediency; digital job demands) is novel in the OB literature — Hai et al.'s contribution is the *application* to GenAI and the empirical demonstration that the pathway operates at the daily within-person level.

## Relevance

- Risk: yes — the paper documents an unethical-behavior outcome (expediency: shortcuts, performance-metric manipulation, protocol violations) that the KB's risk cluster has not yet had concrete daily-level evidence for.
- Erosion: yes — work alienation is a meaning/identity erosion mechanism, complementing the SDT competence/autonomy/relatedness framing already in the KB via Hermann et al. (2025) and Nikolova et al. (2024).
- Preservation: indirect — the moderator (digital job demands) and the practical implications (organizations should design reasonable demands, foreground employee responsibility, structure roles strategically) point to preservation-side levers.
- **Relevance**: HIGH

## Quality

- Evidence basis: ESM longitudinal design with 1,050 within-person observations, peer-reviewed open-access publication in IJIM (Elsevier; CC BY 4.0), pre-validated scales, multilevel modeling appropriate to the nested data structure. Robustness checks reported (with/without controls; z-standardized predictors; supplementary material). Honest about limitations: survey-based design limits causal inference; single national-cultural context (China); service-industry-only sample. Common method bias addressed via temporal separation of measures and inclusion of affect controls.
- Originality: the paper's *constructs* are not new (alienation = Shantz et al. 2014; expediency = Greenbaum et al. 2018; digital job demands = Scholze & Hecker 2024; collaboration scale = Kong et al. 2023). The originality lies in the integrated mediation-moderation model and the empirical demonstration that GenAI collaboration measurably increases alienation at the daily level, and that alienation channels into self-serving shortcuts. Compared against existing KB entries: the paper *empirically anchors* the alienation/meaning-erosion mechanism that [[professional-identity-threat]], [[nikolova-robots-meaning-2024]], and [[hermann-genai-psychology-work-2025]] currently carry mostly via theory or industrial-robots data.
- **Quality**: HIGH

## Extractable Elements

- Concepts (NEW): none. Work alienation is an OB construct from 2014; the paper does not introduce a labeled GenAI-specific phenomenon. Expediency likewise predates the paper. The dark-side framing is descriptive rather than a labeled construct.
- Concepts (UPDATE): [[professional-identity-threat]] (alienation as the daily within-person mechanism); [[agency]] (passive reliance / "deferring fully to GenAI" as autonomy abdication); [[novice-vulnerability]] is *not* the right frame here (sample is mixed-tenure; mean = 6.36 years); [[capacity-erosion]] (effortful-engagement decline pathway); [[cognitive-surrender]] (the within-day passive-reliance mechanism leading to cutting corners); [[workslop]] (expediency at the team-output level).
- Methods (NEW): none. The paper studies a phenomenon; it does not propose a practitioner-facing protocol.
- Methods (UPDATE): possibly [[identity-threat-coping]] — expediency could be classified as an "escapism" strategy (disengagement, withdrawal of effort) under the Hermann et al. taxonomy; flag as [Inference] addition.
- Claims to capture in the source distillation:
  - GenAI collaboration → work alienation: γ = .14, SE = .03, p < .001
  - Work alienation → expediency: γ = .30, SE = .09, p < .01
  - Indirect effect: estimate = .04; 95% CI [.008, .073]
  - Cross-level interaction (collaboration × digital job demands → alienation): γ = .08, SE = .03, p < .01
  - Simple slopes: high digital demands → significant (γ = .34, p < .001); low → non-significant (γ = .04, p > .05)
  - Conditional indirect (high vs. low digital demands): .06 vs. .02; difference = .05, CI [.002, .094]
  - Within-person variance: 29.8% (collaboration), 25.9% (alienation), 35.7% (expediency) — substantial daily fluctuation
  - Mean digital job demands = 3.19 (between-person); mean GenAI collaboration = 3.51 (within-person)
  - Sample: N = 229 service-industry employees in South China (hospitality/tourism); 1,050 within-person observations across 5 workdays

## Recommendation

**INCLUDE**

Reason: HIGH-quality longitudinal empirical evidence for an under-corroborated pathway in the KB — daily-level GenAI collaboration causally links (within the limits of survey-based inference) to unethical shortcuts via psychological disconnection. The paper does not introduce new constructs, but it provides the strongest empirical anchor available for several existing concepts that have so far been carried theoretically or via adjacent industrial-robots data. Override prior DEFER.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: Re-triggered from prior DEFER (2026-04-29). High-quality daily-ESM empirical evidence for the GenAI → alienation → expediency pathway, with a moderator that sharpens the deployment context. Distillation will produce a source entry plus UPDATE proposals to existing concepts; no NEW concepts (the paper applies established OB constructs rather than introducing labeled phenomena). Decision matches the rewritten recommendation.
