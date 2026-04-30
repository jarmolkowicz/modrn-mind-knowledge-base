---
status: solid
area: [erosion, risk, preservation]
type: paper
sources:
  - "Stadler, M., Bannert, M., & Sailer, M. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. Computers in Human Behavior, 160, 108386. https://doi.org/10.1016/j.chb.2024.108386"
---

# Stadler, Bannert & Sailer (2024) — Cognitive Ease at a Cost

## Citation

Stadler, M., Bannert, M., & Sailer, M. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. *Computers in Human Behavior*, 160, 108386.

**DOI:** [10.1016/j.chb.2024.108386](https://doi.org/10.1016/j.chb.2024.108386)
**License:** CC BY 4.0 (open access)
**OSF:** [osf.io/jpxyt](https://osf.io/jpxyt) (instructions, scales)

## Type

Paper (between-subjects RCT, N=91 university students; ANCOVA controlling for prior knowledge; mediation analysis on the LLM → justification-quality pathway through germane cognitive load).

## Key Insight

Stadler et al. extend Kammerer et al.'s (2021) socio-scientific search-as-learning paradigm by adding an LLM condition. 91 university students were randomly assigned to research the safety of nano-particles in sunscreen using either Google or ChatGPT-3.5 for 20 minutes, then write a recommendation with justifications without notes. The design lets the team isolate the effect of the *information-gathering tool* on both subjective cognitive load (Klepsch et al. 2017's three-facet CLT scale: extraneous / intrinsic / germane) and an external rating of justification quality.

The headline finding is the **dissociation**: LLM users experienced lower cognitive load on every facet (η² = 0.09 for ECL, 0.15 for ICL, 0.27 for GCL) and produced lower-quality justifications (1.20 vs. 1.87 relevant arguments out of 7 possible; F = 11.18, p = .001, η² = 0.11). Cognitive ease and learning quality moved in opposite directions.

The mediation result is what makes this paper KB-load-bearing: **the entire group difference in justification quality is mediated by germane cognitive load** (β = 0.15, p = .020 indirect; β = 0.19, p = .095 direct, n.s.). Germane load is the CLT construct for cognitive resources devoted to active processing — schema construction, inference, integration. The paper provides direct evidence that what LLMs strip out is precisely the load that produces durable understanding.

A secondary but important finding is the *null* on H3: LLM users did not show more homogeneous recommendations than search-engine users (χ² = 1.78, p = .411; distributions essentially equivalent — see Table 3, [p.4]). The authors had hypothesized LLM convergence on a single answer. They didn't find it. This is empirical counter-evidence against the "LLMs collapse output diversity" framing at the level of final decisions, even when LLMs reduce the diversity of *information* the user encounters during research.

The framing the paper provides — "cognitive ease at a cost" — is a clean linguistic hook for the broader pattern: the affordance that AI offers (effortless answers) is mechanistically the same thing that bypasses the processing that builds understanding. Several KB concepts already capture pieces of this (fluency-bias, desirable-difficulty, metacognitive-laziness, cognitive-debt, performance-paradox, cognitive-friction). Stadler et al. provide the cleanest CLT-anchored empirical demonstration the KB has — and a mediator (GCL) that gives the cluster a shared mechanistic vocabulary.

## Key Passages

> "Results indicated that students using LLMs experienced significantly lower cognitive load. However, despite this reduction, these students demonstrated lower-quality reasoning and argumentation in their final recommendations compared to those who used traditional search engines."
> — Stadler et al., [p.1, abstract]

> "The strongest difference was found for GCL, the smallest for ECL."
> — Stadler et al., [p.5]

> "We found a significant indirect effect (β = 0.15; p = 0.020) and no significant direct effect (β = 0.19; p = 0.095) indicating a full mediation of the effect of the different research conditions on the quality of the arguments and reasoning presented through GCL."
> — Stadler et al., [p.5]

> "Contrary to H3, students using LLMs did not show less variation in their recommendations than students using traditional search engines (χ²(2) = 1.78; p = 0.411). In fact, the distribution of recommendations was similar for the two groups."
> — Stadler et al., [p.5]

> "While LLMs can reduce the cognitive load, which is theoretically beneficial for learning, the nature of the content delivered and the interaction required to engage with that content also play crucial roles. The ease of obtaining answers from LLMs does not necessarily translate to deeper learning or better-quality outcomes."
> — Stadler et al., [p.5]

> "Specifically, the results point towards the importance of inferring cognitive processes (e.g., reorganizing, reflecting; Chi & Wylie, 2014) when using digital technologies that are associated with higher learning outcomes (Sailer et al., 2024). While recall of knowledge from LLMs might more closely be related to shallow learning processes, inferring knowledge from different sources might more closely be related to deep learning processes."
> — Stadler et al., [p.5]

## Relevance

The cleanest CLT-anchored empirical case in the KB. Three load-bearing contributions:

- **Mediator-level evidence.** The full mediation of justification-quality differences by germane cognitive load is the most mechanism-specific finding the KB has on the cognitive-ease-at-a-cost pattern. Where Kosmyna et al. (2025) measure neural correlates and Bastani et al. (2025) measure post-task performance, Stadler et al. measure the *intermediate variable* — what is bypassed during the task — and show it accounts for the entire downstream effect on output quality. This makes germane cognitive load the shared currency in which several KB concepts (fluency-bias, desirable-difficulty, metacognitive-laziness, cognitive-debt) can be linked at the same level of explanation.
- **Faithful titling.** "Cognitive ease at a cost" is the paper's own framing — and it captures, in plain English, the structural pattern the KB has been articulating across multiple concept entries. Useful linguistic anchor; less jargon-laden than "fluency bias" or "desirable difficulty."
- **The H3 null is itself useful.** The paper expected output homogeneity from LLM use and didn't find it. Final decisions remained diverse even when the information-gathering process was constrained. This refines the homogenization concern: AI may narrow the *informational substrate* without narrowing the *decision distribution*. KB entries on AI-driven sameness should distinguish between the two (e.g., [[anderson-homogenization-2024]] found group-level homogeneity in *idea* generation but not individual-level — a parallel resolution).

## Supports

- [[fluency-bias]] — direct empirical demonstration: lower cognitive load (the felt-easiness of LLM output) translates to lower-quality reasoning
- [[desirable-difficulty]] — the search-engine condition is the "more difficult" condition that produced better outcomes; germane load is the CLT-side label for what desirable difficulty engages
- [[cognitive-debt]] — converging behavioral evidence for the construct: LLM use → reduced engagement → weaker output
- [[metacognitive-laziness]] — reduced germane load is the operational signature of metacognitive bypass; LLM users invested less in active processing of the content
- [[performance-paradox]] — cognitive-load dimension of the paradox: easier tools, weaker outcomes
- [[cognitive-friction]] — search engines impose the friction that generates meaning; LLMs strip it; phenomenologically experienced as lower CL
- [[cognitive-offloading]] — adds CLT-mediator evidence: what gets offloaded is precisely the germane processing
- [[capacity-erosion]] — single-session evidence that even brief LLM use bypasses the active processing that builds capacity

## Contradicts / Extends

- Extends [[kosmyna-cognitive-debt-2025]] — Kosmyna measured neural connectivity (EEG) and produced *self-reports* of low ownership; Stadler et al. supply the cognitive-load mediator that connects "weaker neural engagement" to "weaker output." The two findings are at different measurement levels but tell the same story: AI use reduces engagement, engagement is what produces quality.
- Extends [[bastani-guardrails-math-rct-2025]] — Bastani measured post-task exam scores and inferred crutch behavior from interaction logs; Stadler et al. measure the during-task subjective load directly. Bastani's inferred mechanism gets a measured-mediator counterpart.
- Extends [[fan-metacognitive-laziness-2025]] — Fan demonstrated reduced metacognitive transitions in process-mining; Stadler et al. demonstrate reduced germane load on a validated CLT scale. Two different operationalizations of the same underlying disengagement.
- Refines [[anderson-homogenization-2024]] and the broader "AI homogenizes outputs" framing — Stadler et al.'s H3 null shows that LLM use can narrow *information exposure* without narrowing *final decisions*. The homogenization concern needs to specify which level it operates at (idea generation, information gathering, group-level pooling, individual decision).

## Open Questions

- Single-session, no retention test. The paper does not measure whether what was learned (or not learned) during the 20-minute task transfers to later unaided performance. The complement to this paper would be a Bastani-style design with a delayed unassisted assessment.
- ChatGPT-3.5 (April–May 2023) is now several model generations old. Modern LLMs cite sources, perform retrieval, and offer step-by-step reasoning that may invoke higher germane load. The mediator-level finding (GCL → quality) should generalize, but the absolute load levels may not.
- The N=91 sample is small for a mediation analysis; replication at scale would strengthen the GCL-mediator claim.
- No prompt-pattern moderation. Authors acknowledge in §7.1 that prompting strategies may fundamentally change the result. This suggests the cognitive-ease effect is *specific to default LLM use* and may be modulated by interaction patterns that re-introduce engagement (Socratic prompting, explanation requests) — connecting to Shen & Tamkin (2026)'s six-pattern typology.
- The H3 null on homogeneity opens a question: does LLM exposure narrow recommendations *over time* (longitudinal repeated exposure) even if it doesn't narrow them in a single session? The single-shot design cannot answer this.
- No measure of subjective confidence or ownership. Kosmyna et al. found low ownership in LLM users; whether Stadler's lower-load LLM users also reported less ownership of their justifications is untested but plausible.
