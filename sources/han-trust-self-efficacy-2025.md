---
status: emerging
area: [erosion, risk]
type: paper
sources:
  - "Han, Z., Song, G., Zhang, Y., & Li, B. (2025). Trust the Machine or Trust Yourself: How AI Usage Reshapes Employee Self-Efficacy and Willingness to Take Risks. Behavioral Sciences, 15(8), 1046. doi:10.3390/bs15081046"
---

# Han, Song, Zhang & Li (2025) — Trust the Machine or Trust Yourself

## Citation

Han, Z., Song, G., Zhang, Y., & Li, B. (2025). Trust the Machine or Trust Yourself: How AI Usage Reshapes Employee Self-Efficacy and Willingness to Take Risks. *Behavioral Sciences*, 15(8), 1046.

**DOI:** [10.3390/bs15081046](https://doi.org/10.3390/bs15081046)

## Type

Paper (three-wave longitudinal survey, N=442 Chinese employees, moderated mediation model)

## Key Insight

Han et al. test how AI usage affects two outcomes — **employee self-efficacy** and **willingness to take risks** — using a three-wave longitudinal survey grounded in **Social Cognitive Theory** (Bandura). The findings:

1. **AI usage significantly enhances self-efficacy** (B = 0.524, p < .001). Employees who use AI more report higher confidence in their own abilities.
2. **AI usage significantly enhances willingness to take risks** (B = 0.493, p < .001).
3. **Self-efficacy partially mediates** the AI → risk-taking path (indirect effect = 0.122, 95% CI [0.071, 0.176]).
4. **Learning goal orientation moderates the chain.** Employees high in learning goal orientation translate AI-boosted efficacy into genuine risk-taking. Employees *low* in learning goal orientation show **no significant mediated effect** — their AI-boosted self-efficacy doesn't translate.

The fourth finding is the load-bearing one for the KB. The AI-boost-to-self-efficacy effect appears in everyone, but only translates into actual risk-taking behavior in those with high learning orientation. This pattern is consistent with the interpretation that **low-orientation employees attribute AI-aided success externally** (the AI did it, not me) — so their inflated self-efficacy is shallow and doesn't generalize to unaided contexts. High-orientation employees, by contrast, internalize AI-aided success as growth.

For human thinking with AI: this is the longitudinal-mechanism counterpart to [[ai-self-efficacy-erosion]]. The two findings *appear* contradictory — Han et al. show AI *enhances* self-efficacy; Alessandro et al. show AI *erodes* it — but the tension is structural. AI-as-tool (Han's framing) tends to enhance via mastery experiences. AI-as-evaluator (Alessandro's framing) tends to erode via downward comparison. The directionality depends on the interaction mode.

The risk-taking finding also raises a concern the paper doesn't fully address: if AI inflates *willingness* to take risks via *inflated* (rather than genuine) self-efficacy, AI use could amplify overconfident decision-making. Especially in the low-learning-orientation group whose efficacy boost is shallow.

## Key Passages

> "AI usage significantly enhances employees' willingness to take risks; … self-efficacy serves as a partial mediator in the connection between AI usage and the willingness to take risks; … learning goal orientation moderates both the relationship between AI usage and self-efficacy, as well as the mediating effect."
> — Han et al., [p.1] (abstract)

> "When employees use AI to assist in decision-making, the data analysis and predictive capabilities provided by the system may reduce uncertainty, thereby increasing their confidence in taking risks."
> — Han et al., [p.3]

> "Said et al. (2023) demonstrated that individuals with greater confidence in AI knowledge tend to amplify potential benefits while underestimating risks, which may enhance employees' willingness to take risks in AI-assisted decision-making contexts. This cognitive bias toward optimistic risk assessment suggests that AI familiarity creates a psychological environment conducive to bolder decision-making."
> — Han et al., [p.4]

> "When employees become proficient in using AI tools and receive positive feedback, they may attribute this success to an enhancement of their abilities, thereby increasing their self-efficacy."
> — Han et al., [p.4]

## Methodology

- Three-wave longitudinal survey (N = 442 Chinese employees)
- Moderated mediation model (PROCESS macro)
- Variables: AI usage frequency, self-efficacy (Bandura scale), willingness to take risks (Dewett 2006), learning goal orientation (VandeWalle scale)
- Tested via SEM-style mediation analysis with bootstrapping for indirect-effect CIs

## Relevance

Three load-bearing contributions for the KB:

- **Provides the AI-as-tool side of the self-efficacy story.** The KB's existing [[ai-self-efficacy-erosion]] entry leans on Alessandro et al.'s finding that AI erodes self-efficacy. Han et al. show the opposite when AI is used as a tool rather than an evaluator. The two papers together specify the *directionality conditions* — same construct, opposite outcomes depending on interaction mode.
- **Identifies a moderator that matters for design.** Learning goal orientation isn't innate-fixed — it's a workplace-cultivable trait. If the AI-to-genuine-self-efficacy translation requires high learning orientation, organizations can intervene at the orientation level to make AI's psychological effects benign rather than shallow. This is the KB's preservation cluster talking to organizational design.
- **Risk-taking concern.** Increased willingness to take risks via inflated rather than genuine self-efficacy is a structural concern the paper raises. This connects the self-efficacy literature to the [[automation-bias]] / [[confidence-competence-gap]] cluster — same dynamic at the decision-making level.

## Supports

- [[ai-self-efficacy-erosion]] — provides contrasting evidence; AI-as-tool boosts efficacy while AI-as-evaluator erodes it
- [[confidence-competence-gap]] — low-orientation employees' non-significant mediation suggests their boost is externally attributed
- [[agency]] — self-efficacy mediates AI's effect on risk-taking
- [[automation-bias]] — inflated efficacy + increased risk-taking maps to overreliance dynamics
- [[calibration]] — distinguishing genuine from AI-attributed efficacy is a calibration challenge
- [[scan]] — Tsim & Gutoreva's framework predicts the difference: Complement-zone use should boost real efficacy; Substitute-zone use should boost only attributed efficacy

## Contradicts / Extends

- **Apparent tension with [[alessandro-self-efficacy-2025]]**: Alessandro shows AI use *erodes* self-efficacy and free-will beliefs. Han shows AI use *enhances* self-efficacy and risk-taking. Both N>400, both rigorous. The reconciliation is interaction mode (AI-as-evaluator vs. AI-as-tool) and population (chronic users in Alessandro's frame; workplace tool users in Han's). Worth a separate KB note synthesizing the two.
- Extends [[passalacqua-less-ai-2024]] — Passalacqua showed full automation harms autonomy and motivation; Han shows AI-as-tool boosts efficacy, but only translates to genuine behavior change when learning orientation is high. Together: tool-use can be beneficial *if* the orientation is preserved.

## Open Questions

- Population: Chinese employees in a specific cultural-work context. Generalization to Western contexts is plausible but not tested.
- The "AI-as-tool vs. AI-as-evaluator" distinction is implicit in the design but not formally measured. A study that explicitly manipulates the role of AI would clarify.
- The low-learning-orientation group's inflated-but-shallow efficacy is a concerning predicted pattern but not directly measured (the absence of mediation is consistent with it but not proof). Direct tests of attribution would resolve.
- Long-term durability: three waves over what timeframe? If the AI-boost is short-term and decays, the practical implications shift.
