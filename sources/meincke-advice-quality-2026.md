---
status: solid
area: [risk, erosion]
type: paper
sources:
  - "Meincke, L., Nave, G., & Terwiesch, C. (2026). Advice quality and source disclosure shape trust in AI-generated ethical advice. Scientific Reports, 16, 11868. https://doi.org/10.1038/s41598-026-44258-1"
---

# Meincke, Nave & Terwiesch (2026) — Advice Quality and Source Disclosure Shape Trust in AI-Generated Ethical Advice

## Citation

Meincke, L., Nave, G., & Terwiesch, C. (2026). Advice quality and source disclosure shape trust in AI-generated ethical advice. *Scientific Reports*, 16, 11868. doi:10.1038/s41598-026-44258-1

(Wharton School, University of Pennsylvania + WHU–Otto Beisheim School of Management. Registered Report — Stage 1 protocol accepted 13/09/24, OSF DOI: 10.17605/OSF.IO/6FPW7. Open data at osf.io/pz2sf/.)

## Type

Paper (Registered Report; pilot N=187 + main study N=642; mixed logistic regression with random intercepts for participants and dilemmas)

## Key Insight

Once people see AI-generated ethical advice, they accept it: a-priori 72.6% preferred a human ethical advisor, but after seeing GPT-4 advice alongside an expert columnist's advice with sources disclosed, only 53.2% still preferred the human (46.8% AI). When the source label was hidden, AI preference rose to 53.7%. The same advice text, evaluated identically, is preferred ~7 percentage points more often when its AI origin is concealed — a domain-specific instance of the disclosure penalty operating in the most normatively loaded domain (ethics) where one would expect resistance to be strongest.

The corollary is that algorithm aversion in the ethical domain is highly malleable. Most of the gap between "I'd rather have a human" (a-priori) and "this AI advice is fine" (post-exposure) closes once people read the actual output — not because the AI got better, but because human resistance was operating on an *imagined* AI rather than the one in front of them.

## Key Passages

> "We find that people perceive the quality of AI-generated ethical advice to be on par with that of expert advice, with no significant difference in usefulness ratings between the two sources. When given a direct choice, 57% of participants preferred AI-generated advice."
> — Meincke, Nave & Terwiesch, [p.1] (abstract)

> "Before observing the advice, humans display a strong algorithm aversion in this context, with 72.6% of participants preferring to be advised ethically by humans. After being exposed to the quality of the AI-generated advice, however, algorithm aversion is reduced substantially to 53.2%. When hiding the source of the advice, algorithm aversion is further reduced to 46.3%."
> — Meincke, Nave & Terwiesch, [p.1] (abstract)

> "Trust in algorithmic ethical reasoning may be more malleable than previously assumed and could evolve as people gain direct exposure to AI's capabilities in moral decision-making."
> — Meincke, Nave & Terwiesch, [p.1]

> "When the source was visible (Condition B), expert advice was rated higher than AI advice... When the source was not disclosed, the point estimate of this effect became negative and did not reach statistical significance... when the source is disclosed, participants perceive the human expert advice to be more useful, but once the source is hidden AI is perceived on par with or even better than the expert."
> — Meincke, Nave & Terwiesch, [pp.7–8]

> "We propose that apart from the high quality of the advice, the nature of LLMs introduces a distinct pathway for trust formation compared to more quantitative AI systems... Because LLMs communicate in natural language complete with reasoning, argumentation, and rhetorical nuance, their advice may appear more human and their thought processes more transparent. This linguistic familiarity may soften initial skepticism and accelerate the development of trust."
> — Meincke, Nave & Terwiesch, [p.9]

> "Premature disclosure of its machine origin might, to some degree, inhibit its adoption, particularly in early stages of use. This presents a practical dilemma: how to balance the potential benefits of AI-generated ethical advice with the normative expectations around transparency and informed consent."
> — Meincke, Nave & Terwiesch, [p.9]

## Key Findings

- **Pilot (N=187):** No significant difference in usefulness ratings between GPT-4 and Kwame Anthony Appiah (NYT *The Ethicist*) advice on 20 dilemmas (B=0.11, 95% CI [-0.26, 0.48]; d=0.08; p=.56). In the relative-choice condition, 57% of participants overall preferred AI advice (B=0.29, OR=1.34, p<.035). Effect strongest among Prolific laypeople (59.6% AI-preferring, p<.003); MBA students (51.3%) and ethics experts (55.5%) directionally similar but not statistically significant given lower sample sizes.
- **Main study (N=642), Condition A (a-priori, N=219):** 27.4% chose AI advice over a human expert *before* seeing either piece of advice. 72.6% algorithm aversion baseline.
- **Main study, Condition B (full disclosure, N=211):** AI preference rose to 46.8% after seeing both pieces of advice with sources labeled (B=0.96, OR=2.62, p<.001 vs. Condition A).
- **Main study, Condition C (no disclosure, N=212):** AI preference rose further to 53.7% when source labels were hidden (B=0.32, OR=1.38, p=.005 vs. Condition B).
- **Source-x-disclosure interaction in usefulness ratings (Conditions B+C, N=4,230 ratings, 423 participants):** Significant interaction (B=-0.39, d=-0.25, p<.001). When source was disclosed, expert advice was rated higher than AI (B=0.28, d=0.18, p<.001). When source was hidden, the point estimate reversed (B=-0.11, d=-0.07, p=.082, n.s.) — AI rated on par with or slightly better than expert.
- **Stimulus-level boundary condition:** 4 of 20 dilemmas showed effect reversal — *less* AI preference after seeing AI's advice. Qualitative analysis: these dilemmas were less emotionally loaded and the human expert provided clearer directives where AI's response was more abstract.

## Methodological Notes

- Registered Report — Stage 1 protocol accepted prior to data collection. Pre-registered hypotheses and analysis plan.
- All 20 dilemmas were published in NYT *after* GPT-4's training cutoff (March 2023), avoiding the contamination risk in prior work using overlapping training data (Dillion et al., GPT-4o, partial overlap).
- GPT-4 was seeded with one example reply of Appiah's writing to control for stylistic differences; without this, prior work has shown style alone can drive perceived-source effects.
- Mixed logistic regression with random intercepts for participants and dilemmas; >95% statistical power for the registered effect-size threshold (5% change from a 60% baseline).
- Protocol deviations (transparently reported in Declarations): N=658 vs. registered 618; preference question wording in Conditions B/C asked "which is more useful" rather than the registered "which would you prefer to follow"; due to programming error, post-dilemma attention checks were not administered. Authors flag the wording change as a possible source of A→B/C effect inflation but note B-vs-C remains a clean test of source disclosure.

## Relevance

The paper anchors three KB-relevant claims with a Registered Report design:

1. **Domain-specific disclosure penalty.** Adds an ethics-domain instance to the disclosure-penalty literature dominated so far by [[reimann-schilke-disclosure-2025]] (general workplace tasks) and [[raj-disclosure-penalty-2026]] (creative writing). Strengthens the [[transparency-paradox]] claim that disclosure costs are not a creative-domain artifact — they appear even in moral advice, where transparency is most ethically demanded.

2. **Malleability of algorithm aversion in moral domains.** Prior literature ([[automation-bias]], algorithm aversion per Dietvorst et al. 2015, [[ai-moralization]]) often treated moral reasoning as a domain where AI resistance is structurally elevated and stable. Meincke et al. show the resistance is largely *anticipatory* — it collapses by ~26 percentage points on direct exposure (45 / 73 ≈ 63% of the baseline aversion). The fixed-disposition framing is wrong; the resistance is highly contingent on direct experience.

3. **A pathway for fluency-bias-driven trust formation.** The paper's proposed mechanism for why trust forms quickly with LLM advice — "natural language complete with reasoning, argumentation, and rhetorical nuance... may appear more human and their thought processes more transparent" — is the [[fluency-bias]] mechanism applied to a normatively loaded domain. The empirical result (AI rated equal to or better than expert when source is hidden) is consistent with this: when the source label is removed, fluent AI output is indistinguishable from or superior to fluent expert output.

The combination matters: people *prefer* AI ethical advice when blinded to the source, even though independent literature ([[cheng-sycophantic-prosocial-2025]], [[chandra-sycophantic-delusional-2026]], [[batista-sycophantic-ai-2026]]) shows AI ethical advice tends toward sycophantic patterns that degrade prosocial outcomes. Meincke et al. document the preference; the sycophancy literature documents the cost. Both can be true.

## Supports

- [[disclosure-penalty]] — domain-specific evidence: in ethical advice, disclosed AI is preferred 46.8% vs. blinded AI 53.7% — a ~7 percentage-point penalty for the source label, holding advice content constant.
- [[transparency-paradox]] — extends pattern to ethics. People simultaneously want disclosure (normative expectation) and punish it (when given identical advice with vs. without source labels, they prefer the unlabeled version).
- [[fluency-bias]] — proposed mechanism: AI's natural-language reasoning makes it *appear* more human and transparent, accelerating trust. Once source label is removed, fluency does its work and AI is rated equal to or better than expert.
- [[ai-moralization]] — complement: moralized resistance is strong a-priori (72.6% prefer human) but largely collapses on exposure (53.2%). Suggests moralization operates partly through unfamiliarity rather than fixed normative stance.
- [[demello-moralization-2026]] — extends: moralization may be a real but contingent reaction; direct exposure to high-quality AI ethical advice substantially weakens it.
- [[automation-bias]] — adjacent: Meincke et al. document acceptance under demonstrated quality, not error. Worth contrasting with classical automation-bias studies where users follow AI *into* error.
- [[social-sycophancy]] / [[sycophancy]] — tension: users prefer the advice that the sycophancy literature suggests may be socially suboptimal, particularly when blinded.
- [[confidence-competence-gap]] — adjacent: ratings of AI advice are equal to or higher than expert ratings in the no-disclosure condition. Users cannot distinguish quality reliably between the two and likely use fluency as a proxy.
- [[novice-vulnerability]] — pilot effects strongest among laypeople (59.6% AI preference) and weakest in ethics experts (55.5%, n.s.) and MBA students (51.3%, n.s.); consistent with novice-skewed pattern.

## Contradicts / Extends

- Extends [[reimann-schilke-disclosure-2025]] — Reimann & Schilke established the disclosure penalty across general work outputs (writing, analytics, hiring); Meincke et al. extend to the ethical-advice domain, where one might expect transparency norms to be strongest. Same pattern holds.
- Extends [[raj-disclosure-penalty-2026]] — Raj et al. measured a ~6.2% penalty in creative writing evaluations (d=0.24). Meincke et al. measure a comparable ~7 percentage-point penalty in ethics advice preferences (Condition B 46.8% → Condition C 53.7%). Different measurement scale, similar effect size.
- Extends [[cheong-penalizing-transparency-2025]] — converging evidence that disclosure imposes a measurable cost.
- Extends [[demello-moralization-2026]] — adds a contingency dimension: moralized AI resistance reduces sharply on direct exposure to high-quality output.
- Tension with prior algorithm-aversion theory (Dietvorst et al. 2015) — that work documented algorithm aversion *increasing* after observing algorithmic errors. Meincke et al. show the inverse for high-quality LLM ethical advice: aversion *decreases* after observing the advice. The two are reconcilable if one notes Dietvorst studied numerical-prediction algorithms with visible errors, while Meincke et al. study natural-language ethical reasoning with no obvious errors flagged. The takeaway is that the direction of post-exposure change depends on what the user observes.
- Aligns with Howe et al. (2023, *Front. Psychol.* 14: 1281255) — earlier converging finding (not in KB) that ChatGPT's advice is perceived as better than professional advice columnists. Meincke et al. extend by adding the source-disclosure manipulation and methodologically rigorous post-cutoff dilemmas.
- Tension with [[cheng-sycophantic-prosocial-2025]] — Cheng et al. show AI ethical advice tends sycophantic and degrades prosocial repair. Meincke et al. show users prefer this advice when blinded. The two combined sharpen the worry: people prefer the advice the sycophancy literature suggests may damage them, especially when blinded to the source — the conditions under which the disclosure penalty drives them most strongly toward unlabeled AI.

## Open Questions

- The paper measures stated preference in a single survey session. Does the ex-post acceptance pattern persist over weeks/months of use, or does naturalistic exposure surface failure modes that re-engage aversion? Longitudinal designs needed.
- Stimulus-level effect reversals (4 of 20 dilemmas: less AI preference after exposure) suggest a boundary condition — AI advice being more abstract while human expert provides directives. What kinds of dilemmas does this generalize to? When does directive concreteness matter more than fluent argumentation?
- The protocol-deviation wording change ("more useful" vs. "would prefer to follow") may inflate the A→B/C effect. The clean B-vs-C contrast (the disclosure-penalty test) is unaffected. But the headline "algorithm aversion drops from 72.6% to 53.2%" should be read with this caveat in mind.
- The paper is silent on long-run sycophancy and prosocial-behavior costs documented by [[cheng-sycophantic-prosocial-2025]] and [[chandra-sycophantic-delusional-2026]]. The authors discuss limitations of single-session preferences but do not connect to that literature. Bridging is worth doing in synthesis.
- Practitioner question: the authors propose presenting AI advice alongside human expert opinions, allowing users to engage with arguments before learning their source. They flag that this raises "difficult ethical questions about disclosure, manipulation, and epistemic fairness." Worth tracking how organizations actually navigate this in practice.
