---
status: solid
area: [erosion]
type: paper
sources:
  - "Bauer, K., Nofer, M., Abdel-Karim, B. M., & Hinz, O. (2022). The Effects of Discontinuing Machine Learning Decision Support. SAFE Working Paper No. 370 (December 2022). doi:10.2139/ssrn.4299664"
---

# Bauer, Nofer, Abdel-Karim & Hinz (2022) — Discontinuing ML Decision Support

## Citation

Bauer, K., Nofer, M., Abdel-Karim, B. M., & Hinz, O. (2022). *The Effects of Discontinuing Machine Learning Decision Support*. SAFE Working Paper No. 370.

**DOI:** [10.2139/ssrn.4299664](https://doi.org/10.2139/ssrn.4299664)

## Type

Paper (incentivized online experiment, between-subjects design)

## Key Insight

Bauer et al. ran a clean experimental test of a counterintuitive prediction: **ML decision aids may improve performance while they're active but prevent the development of decision-making skills underneath — a deficit that only becomes visible when the system is discontinued.**

The design: participants solve logical puzzles. Treatment group: ML decision aid for the first half; system removed without warning for the second half. Control group: no aid throughout. Comparing post-discontinuance performance to control isolates whether skill development was disrupted during the aided phase.

The finding is sharp: treatment participants show a **performance drop after discontinuance** beyond what would be expected from simply losing the aid — they perform *worse than control participants who never had the aid*. The skill development that should have happened during the aided phase didn't occur. Crucially, this is not just atrophy of pre-existing skills (participants didn't have prior puzzle expertise) — it's **prevention of skill development**, which only manifests when the aid is removed.

A second finding adds a behavioral mechanism: **the degree of "blind trust"** in the ML predictions correlates with the size of the post-discontinuance performance drop. Participants who blindly trusted the aid built less skill underneath; participants who interrogated the aid built more. The implication: **practical interventions that signal AI imperfection may protect skill development**, even at the cost of slightly reduced in-the-moment performance.

For human thinking with AI: this is the cleanest experimental evidence the KB has for skill prevention (vs. erosion). And the discontinuance design generalizes — any context where AI is intermittent (system updates, retraining periods, model failures, moments of regulatory disablement) will reveal this hidden deficit. Organizations relying on continuous AI availability are accumulating an invisible vulnerability.

## Key Passages

> "The provision of ML-based predictions can adversely affect the development of decision-making skills that come to light when people lose access to the system."
> — Bauer et al., [p.2] (abstract)

> "We show that the initial provision of ML decision aids can latently prevent the development of decision-making skills which later becomes apparent when the system gets discontinued."
> — Bauer et al., [p.2]

> "We also find that the degree to which individuals 'blindly' trust observed predictions determines the ultimate performance drop in the post-discontinuance phase."
> — Bauer et al., [p.2]

> "Making it clear to people that ML decision aids are imperfect can have its benefits especially if there is a reasonable danger of (temporary) system discontinuances."
> — Bauer et al., [p.2]

> "Somewhat ironically, the development (and maintenance) of human decision-making skills is a complement to the successful implementation of ML-based decision support."
> — Bauer et al., [p.3]

## Relevance

Three load-bearing contributions:

- **Prevention vs. erosion.** Most KB sources document erosion of existing skills. Bauer et al. specifically shows *prevention* of new skill development — these are different mechanisms with different implications. Erosion can be reversed via practice; prevention means the skill never formed.
- **The discontinuance test.** Most AI-evaluation paradigms measure performance with the AI active. Bauer et al.'s contribution is methodological: hidden vulnerabilities only show up when the AI is removed. KB-relevant practices ([[strategic-alternation]], "AI-off drills") are validated by this finding.
- **Blind-trust moderation.** The finding that signaling AI imperfection improves the post-discontinuance outcome is an intervention lever. AI tools that explicitly flag uncertainty may protect skill formation even when otherwise unchanged.

## Supports

- [[cognitive-debt]] — Bauer's hidden-deficit-revealed-on-discontinuance is exactly the cognitive-debt mechanism
- [[capacity-erosion]] — provides experimental demonstration in the prevention variant
- [[confidence-competence-gap]] — blind-trust moderation finding
- [[automation-bias]] — over-reliance during the aided phase causes the post-discontinuance gap
- [[strategic-alternation]] — empirical justification for periodic AI-off practice
- [[think-first]] — interrogating AI predictions (rather than blind-trust) is the operational practice that protects skill development

## Contradicts / Extends

- Extends [[goddard-automation-bias-2012]]'s clinical-decision-support findings into the ML-specific context (vs. expert systems Goddard reviewed).
- Companion to [[passalacqua-less-ai-2024]] — both papers show full automation harms skill acquisition; Bauer specifically shows the harm is invisible until the AI is removed.

## Open Questions

- How long does the prevention deficit persist? Bauer et al. measured immediate post-discontinuance; longer-term recovery isn't tested.
- Generalization beyond logical puzzles to consequential professional work would strengthen the practical claim.
- The blind-trust moderation suggests interventions that flag AI imperfection help — but how should that flagging be designed? UX-level question the paper doesn't operationalize.
