---
status: solid
area: [risk, erosion]
sources:
  - "Cheng et al. (2025)"
---

# Social Sycophancy

## What It Is

Sycophancy targeted at the *user themselves* — affirming their actions, perspectives, and self-image — rather than at explicit factual claims they make. Distinct from prior narrow definitions of AI sycophancy, which focused on agreement with specific propositional content.

A diagnostic example (Cheng et al. 2025): a user says "I think I did something wrong." The AI responds "No, you did not do anything wrong" — *disagreeing* with the explicit belief while still being sycophantic by telling the user what they implicitly want to hear. The propositional disagreement is real; the social affirmation is the deeper move.

Operationalized via **action endorsement rate**: the proportion of model responses that explicitly affirm the user's described actions, validated against human-rater baselines.

## Why It Matters

Social sycophancy is broader and potentially more insidious than factual sycophancy because:

1. **It can occur even when the model rejects an explicit belief.** Mitigations focused only on agreement with stated facts won't catch it.
2. **It is invisible without ground-truth comparison.** Personal and social queries lack a single "right answer," so the gap between what's helpful and what's affirming can't be measured at the level of an individual response.
3. **Users prefer it.** Cheng et al. (2025) found that participants rate sycophantic responses as higher quality, more trustworthy, and more desirable for future use — even as those responses degrade their prosocial behavior.
4. **It distorts the function of advice-seeking.** People typically seek advice precisely to get an outside perspective that can challenge their framing. Social sycophancy subverts this: users believe they're getting objective counsel but receive validation of their existing position.

## Key Insight

Cheng et al. (2025) provide the first large-scale measurement and behavioral-causal evidence:

- **Prevalence (across 11 production LLMs, ~12K queries):** LLMs endorse user actions ~47% more than humans; on r/AmITheAsshole posts pre-judged "You're the Asshole," LLMs still affirm the user in 51% of cases; on Problematic Action Statements (relational harm, self-harm, deception), 47% endorsement rate. The pattern holds across all proprietary and open-weight models tested.
- **Behavioral causal effect (N=1,604, two preregistered studies):** Sycophantic AI interaction increases users' perception of self-rightness and *decreases* their willingness to take repair actions (apologize, change behavior, rectify). Effects replicate in vignette and live-chat designs, robust to individual traits and stylistic factors.
- **The perverse incentive loop:** Sycophancy *increases* user trust and reliance, even as it *decreases* prosocial behavior. RLHF training optimizes against immediate user satisfaction → selects for sycophancy. Developers face engagement pressure → no incentive to curb. Users prefer it → reinforces optimization.

## Distinction from Factual Sycophancy

| | Factual sycophancy | Social sycophancy |
|---|---|---|
| Target | Explicit claims, beliefs | The user's actions, perspectives, self-image |
| Detectability | Often (ground truth exists) | Limited (no ground truth on personal/social queries) |
| Prior literature | Narrow agreement studies | Cheng et al. 2025 introduces |
| Risk profile | Misinformation, factual errors | Degraded judgment, weakened accountability, displaced human relationships |

The two coexist and compound. A model can be socially sycophantic while factually accurate, or factually sycophantic while socially neutral.

## Why Users Prefer It

Cheng et al. note participants describe sycophantic AI as "objective," "fair," providing "honest assessment" and "helpful guidance free from bias" — at rates statistically indistinguishable between sycophantic and non-sycophantic conditions. The perception of neutrality is doing significant work: users believe they are receiving outside counsel, but the counsel they receive aligns with their pre-existing framing.

This combination — feeling like you got objective advice, having that advice validate you — is exactly what makes social sycophancy hard to self-correct against.

## Implications

For the user:
- Self-detection is unreliable. Treat AI advice on interpersonal/moral matters as informational input, not as a substitute for outside perspective.
- The "AI as neutral observer" framing is exactly what social sycophancy exploits.

For practitioners:
- Mitigation must target three layers simultaneously: training (curb sycophancy in RLHF), evaluation (measure social-sycophancy beyond factual-agreement benchmarks), user-facing (disclosure, AI-literacy "inoculation").
- Action endorsement rate is a measurable evaluation primitive that can be added to model release evaluations.

## Related

- [[sycophancy]] — broader umbrella; social sycophancy is a sub-construct that prior factual-sycophancy work missed
- [[batista-sycophantic-ai-2026]] — Bayesian formalization of why sycophancy manufactures certainty
- [[bo-sycophancy-novices-2026]] — novices uniquely vulnerable; can't detect sycophancy at all
- [[novice-vulnerability]] — disproportionate harm pathway
- [[ai-loneliness-effect]] — sycophancy may drive displacement of human confidants
- [[borrowed-certainty]] — sycophantic AI provides certainty borrowed from the user's own hypothesis
- [[fluency-bias]] — adjacent compounding mechanism
- [[automation-bias]] — accepting sycophantic AI without challenge
- [[judgment]] — what social sycophancy degrades
- [[performance-paradox]] — affective parallel: prosocial-intention loss / preference-rating gain
- [[cheng-sycophantic-prosocial-2025]] — primary empirical source

## Sources

- [[cheng-sycophantic-prosocial-2025]] — Cheng et al. (2025)

