---
status: solid
area: [preservation]
type: paper
sources:
  - "Hatano, G., & Inagaki, K. (1986). Two courses of expertise. Research and Clinical Center for Child Development, Hokkaido University, Annual Report 6, 27-36. (Also: in H. Stevenson, H. Azuma, & K. Hakuta (Eds.), Child Development and Education in Japan, pp. 262-272. Freeman.)"
---

# Hatano & Inagaki (1986) — Two Courses of Expertise

## Citation

Hatano, G., & Inagaki, K. (1986). Two courses of expertise. *Research and Clinical Center for Child Development, Annual Report* 6, 27–36. Hokkaido University. Also published in H. Stevenson, H. Azuma, & K. Hakuta (Eds.), *Child Development and Education in Japan* (pp. 262–272). Freeman.

**Hokkaido eprint:** [eprints.lib.hokudai.ac.jp/dspace/handle/2115/25206](https://eprints.lib.hokudai.ac.jp/dspace/handle/2115/25206)

## Type

Book chapter (theoretical, with cross-cultural application)

## Key Insight

Hatano and Inagaki distinguish **two courses of expertise development**:

- **Routine expertise** — accumulating procedural knowledge (decision rules + executive strategies + skills) through observation, instruction, feedback, and supervision. The skill works in familiar environments. The expert performs it efficiently. They cannot necessarily explain why it works, modify it for new constraints, or invent variations. Knowledge here is *transmitted from culture to individual*.
- **Adaptive expertise** — routine expertise *plus* **conceptual knowledge**: a model of why the procedure works, what its variations are, what counts as appropriate or inappropriate variation, and how to modify the skill when the constraints change. The adaptive expert can verbalize the principle, judge variants, invent new procedures, and predict outcomes in unfamiliar situations.

Two component knowledges are required to construct the conceptual layer:
1. **Empirical knowledge** — observed covariations between variables (action ↔ consequence; dimension ↔ outcome). Variations may be naturally produced, socially produced, or intentionally probed.
2. **Preconceptual model** — even a vague, tentative one — that constrains which variables to attend to. Often borrowed from another domain via analogy.

The two interact reciprocally: data suggests which model fits; the adopted model shapes what data are noticed.

The motivating example: a farmer with conventional skills may, through years of growing rice and observing covariations, build a conceptual model of plants. With it, the farmer adapts to unusual weather or disease — handles the *unfamiliar*. Without it, only trial-and-error or empirical minor adjustment is available when the original procedure stops working.

For human thinking with AI: this is the foundational distinction the KB inherits. AI-supported work tends to build *routine expertise* — pattern matching, applying procedures, executing fluent outputs — while leaving the conceptual layer underbuilt. The AI handles the procedural part; the human is rarely required to construct the underlying model. When AI fails or context changes (the "unusual weather" of professional work), the AI-supported worker has only the procedure, not the principles. This is the distillation of why AI substitution is a long-term capability problem, even when short-term performance looks fine.

## Key Passages

> "Adaptive experts… not only perform procedural skills efficiently but also understand the meaning of the skills and nature of their object."
> — Hatano & Inagaki, [p.2]

> "It is when the performer can explain why it works, i.e., verbalize the principle involved; or at the least, when he/she can judge, in addition to the conventional version of the skill, its variations as appropriate or inappropriate, and/or can modify the skill according to changes in constraints."
> — Hatano & Inagaki, [p.3]

> "Without [conceptual knowledge], what is possible, when the original version has appeared to reach its limits of effectiveness, is just trial-and-error, or empirical minor adjustment."
> — Hatano & Inagaki, [p.3]

> "External feedback serves only as a cue for interpretation; internal feedback is brought about by reorganizing pieces of prior knowledge."
> — Hatano & Inagaki, [p.4]

> "Even young children can construct some conceptual knowledge through repeated practice in a procedural skill in a 'meaningful' context and that this conceptual knowledge can not only invest the procedure with meaning (the how and the why), but also enable them to make predictions in unfamiliar situations and to invent new strategies."
> — Hatano & Inagaki, [p.4]

## Relevance

A foundational distinction for the KB's preservation cluster. Three load-bearing contributions:

- **Names the right target.** The KB's preservation argument isn't "preserve all skill" — it's preserve **adaptive** expertise. Routine expertise can be safely automated; adaptive expertise has to be cultivated. This is a useful conceptual sharpening.
- **Specifies the mechanism.** Conceptual knowledge requires both empirical observation and a preconceptual model. AI substitution often supplies neither — it gives the answer, not the data-and-model that build the conceptual layer. The mechanism for why AI undermines adaptive expertise is therefore precise: it short-circuits the data-collection and model-building loop.
- **Provides the failure mode.** When the original procedure fails (which happens in any non-stationary domain — and AI's deployment context is highly non-stationary), the routine-only expert has trial-and-error; the adaptive expert has principles to reason from. This is the real cost of AI substitution.

## Supports

- [[strategic-alternation]] — alternation builds the conceptual layer that pure AI use leaves underbuilt
- [[desirable-difficulty]] — Bjork's framing in cognitive vocabulary; Hatano & Inagaki's framing in expertise vocabulary; same underlying claim
- [[ericsson-deliberate-practice-1993]] — Ericsson's deliberate practice produces what Hatano & Inagaki call adaptive expertise
- [[bjork-desirable-difficulties-2011]] — variation-of-conditions builds the empirical-knowledge half of adaptive expertise
- [[capacity-erosion]] — capacity erosion is specifically the loss of the conceptual layer; routine skills can persist
- [[judgment]] — adaptive expertise is the substrate of professional judgment in novel situations
- [[gentner-markman-analogy-1997]] — [[analogical-reasoning|analogical reasoning]] is one mechanism by which preconceptual models get borrowed across domains

## Contradicts / Extends

- Foundational; extended by [[ericsson-deliberate-practice-1993]] (mechanism of how the conceptual layer gets built) and [[bjork-desirable-difficulties-2011]] (cognitive conditions that favor it).
- Cross-cultural angle (Japanese vs. Western trajectories of expertise) is mostly outside KB scope but supports the claim that "adaptive expertise" is a generalizable construct, not a culture-specific artifact.

## Open Questions

- AI as *external* conceptual knowledge: can AI supply the model layer rather than just the procedure? In principle yes (AI can verbalize principles, predict, invent variations) — but only if the human queries it for that, which most workflows don't. Would explicit prompting for "explain why this works" recover some of the conceptual-knowledge construction?
- The empirical-knowledge half requires *observed covariations*. AI-mediated work often hides the variations (the AI handles edge cases; the human sees only the smooth surface). Is there a workflow design that re-exposes the variations the AI is handling silently?
- Hatano & Inagaki argue conceptual knowledge construction is *endogenous* — driven by intrinsic motivation for understanding. If AI satisfies the immediate procedural need, does the intrinsic motivation to understand "why" attenuate? This is testable.
