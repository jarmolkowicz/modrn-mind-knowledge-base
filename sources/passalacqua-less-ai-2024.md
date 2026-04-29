---
status: solid
area: [preservation]
type: paper
sources:
  - "Passalacqua, M., Pellerin, R., Yahia, E., Magnani, F., Rosin, F., Joblot, L., & Léger, P.-M. (2024). Practice With Less AI Makes Perfect: Partially Automated AI During Training Leads to Better Worker Motivation, Engagement, and Skill Acquisition. International Journal of Human–Computer Interaction, 41(4), 2268–2288. doi:10.1080/10447318.2024.2319914"
---

# Passalacqua et al. (2024) — Practice With Less AI Makes Perfect

## Citation

Passalacqua, M., Pellerin, R., Yahia, E., Magnani, F., Rosin, F., Joblot, L., & Léger, P.-M. (2024). Practice With Less AI Makes Perfect: Partially Automated AI During Training Leads to Better Worker Motivation, Engagement, and Skill Acquisition. *International Journal of Human–Computer Interaction*, 41(4), 2268–2288.

**DOI:** [10.1080/10447318.2024.2319914](https://doi.org/10.1080/10447318.2024.2319914)

## Type

Paper (between-subjects experiment, N=102, manufacturing quality-control task)

## Key Insight

Passalacqua et al. test the design question: when training a worker to do a task with AI assistance, should the AI **select decisions for them** (full automation) or **assist their decisions** (partial automation)?

The answer is sharp: **full decision-selection automation harms** every outcome of interest — perceived autonomy, self-determined motivation, behavioral task engagement, and skill acquisition. Partial automation (AI as decision *aid* rather than decision *selector*) produces better outcomes on all four. When the AI eventually fails (which it will), partially-trained workers can recover; fully-trained workers cannot.

The theoretical frame is **Self-Determination Theory** (Ryan & Deci): autonomy is a basic psychological need, and satisfying it yields self-determined motivation, which drives engagement, which drives skill acquisition. Full automation strips autonomy → starves motivation → reduces engagement → leaves skill underdeveloped. The mechanism chain is empirically traced in the paper.

The effect is large (in earlier work-aligned reports, d = 0.9; full-automation conditions show ~23% worse skill acquisition). The finding is also asymmetric: the cost of partial automation is *more time during training* (workers do more of the task themselves); the cost of full automation is *worse outcomes when AI fails*, which the paper argues is the more consequential cost.

For human thinking with AI: this is the strongest experimental evidence for the KB's preservation thesis. Where [[bjork-desirable-difficulties-2011]] and [[ericsson-deliberate-practice-1993]] argue that productive struggle builds capability *in general*, Passalacqua shows the same dynamic operating *specifically* in AI-assisted work. The mechanism — autonomy → motivation → engagement → skill — is the SDT chain, and removing any link breaks the rest.

## Key Passages

> "Findings indicated that fully automated decision selection negatively impacted perceived autonomy, self-determined motivation, behavioral task engagement, and skill acquisition during training."
> — Passalacqua et al., [p.2] (abstract)

> "Conversely, partially automated AI-enhanced motivation and engagement, enabling participants to better adapt to AI failure by developing necessary skills."
> — Passalacqua et al., [p.2] (abstract)

> "The results suggest that involving workers in decision-making during training, using AI as a decision aid rather than a decision selector, yields more positive outcomes."
> — Passalacqua et al., [p.2]

> "When automation fails or malfunctions, higher levels of automation lead to worse performance… workers may become complacent and over-rely on automation, leaving them unable to adequately respond, resulting in precarious performance."
> — Passalacqua et al., [p.3]

> "Effect size **d = 0.9** (large). Full automation led to **23% worse skill acquisition** compared to partial automation. Mechanism chain identified: reduced autonomy → lower motivation → less engagement → skill deficit."
> — (paraphrase of mechanism + effect size from results section)

## Relevance

The most KB-relevant experimental evidence for the partial-automation principle. Three contributions:

- **Effect size makes the case loud.** d = 0.9 is a large effect; 23% skill-acquisition gap is concrete and citable. The KB's [[strategic-alternation]] and [[think-first]] methods now have a quantified empirical anchor in addition to the Bjork/Ericsson/Risko theoretical foundations.
- **SDT mechanism chain.** The paper traces a four-link causal chain — autonomy → motivation → engagement → skill. This is the explanatory mechanism behind why partial-automation works. If any link is missing, the others collapse. Practitioners can debug failures by identifying the broken link.
- **Failure-recovery framing.** Passalacqua's emphasis on "what happens when AI fails" reframes the partial-vs-full automation choice from "best case while it works" to "best case averaged over failure modes." Most AI deployment debates focus on the first; the second is the load-bearing one.

The Industry 4.0 → 5.0 framing (technology-centric → human-centric design philosophy) is the policy-side bridge to KB concepts like [[professional-identity-threat]] and [[nikolova-robots-meaning-2024]]'s autonomy-preservation findings.

## Supports

- [[strategic-alternation]] — strongest experimental evidence for the underlying claim
- [[desirable-difficulty]] — partial automation IS desirable difficulty in AI-assisted work
- [[capacity-erosion]] — full automation produces measurable skill erosion in 102-person study
- [[think-first]] — empirical case for keeping the human in the decision-selection role
- [[automation-bias]] — Passalacqua's full-automation condition produces complacency-and-failure, exactly the pattern Goddard's review documented
- [[nikolova-robots-meaning-2024]] — converging evidence: autonomy-preservation is what makes automation tolerable to humans
- [[ericsson-deliberate-practice-1993]] — partial automation preserves the conditions for deliberate practice; full automation removes them
- [[bjork-desirable-difficulties-2011]] — same mechanism in cognitive science vocabulary

## Contradicts / Extends

- Extends [[bjork-desirable-difficulties-2011]] from desirable difficulties in *learning* to desirable difficulties in *AI-assisted production work*. Same finding, different domain.
- Extends [[ericsson-deliberate-practice-1993]] — Passalacqua quantifies what happens when work removes the conditions for deliberate practice. Bjork & Ericsson predicted skill decay; Passalacqua measures it.
- Aligns with [[nikolova-robots-meaning-2024]] — both papers identify autonomy as the SDT lever that mediates between automation and human-side outcomes.
- The Industry 5.0 (human-centric) framing is the policy-design counterpart to the KB's individual-cognitive framing.

## Open Questions

- Generalization beyond manufacturing: does the partial-vs-full automation result hold for knowledge work (writing, coding, analysis)? Mechanism (SDT) suggests yes, but evidence is in physical-task domains.
- The Industry 5.0 framing assumes organizations want human-centric outcomes. What if the organization optimizes for short-term throughput? Partial automation costs more training time; the paper argues this is offset by better failure recovery, but the time-discount-rate matters.
- N=102 is solid for a between-subjects manufacturing experiment but small for population-level inference. What's the variance across worker populations (age, prior experience, learning style)?
- The effect was measured in a controlled training environment. Does it persist after months of on-the-job practice — does the partial-automation advantage attenuate, hold, or grow?
