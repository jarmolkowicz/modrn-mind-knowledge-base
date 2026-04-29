---
status: solid
area: [preservation]
type: paper
sources:
  - "Gentner, D., & Markman, A. B. (1997). Structure mapping in analogy and similarity. American Psychologist, 52(1), 45–56. doi:10.1037/0003-066X.52.1.45"
---

# Gentner & Markman (1997) — Structure Mapping in Analogy

## Citation

Gentner, D., & Markman, A. B. (1997). Structure mapping in analogy and similarity. *American Psychologist*, 52(1), 45–56.

**DOI:** [10.1037/0003-066X.52.1.45](https://doi.org/10.1037/0003-066X.52.1.45)

## Type

Paper (theoretical synthesis)

## Key Insight

Gentner and Markman argue that analogy and similarity are **the same process operating over different proportions of relational vs. attribute matches** — both involve **structural alignment and mapping** between mental representations. The slogan is "similarity is like analogy."

Three psychological constraints define the process:

1. **Structural consistency** — matching relations must have matching arguments (parallel connectivity), and each element matches at most one element in the other representation (one-to-one correspondence).
2. **Relational focus** — common *relations* drive the analogy; common *objects* don't. Kepler's planets ↔ boatman analogy holds because relations between planet and motive force mirror relations between boat and current — even though planets and boats look nothing alike.
3. **Systematicity** — the comparison process favors *connected systems* of relations (with higher-order constraining relations) over equal numbers of unconnected relations. This is what lets analogies generate inferences: once a system aligns, further statements connected to it in the base domain can be projected as candidate inferences in the target.

The classic illustration is **cross-mapping**: in `1:3 :: 3:9`, the surface-identical 3s get *separated* to preserve relational structure (the 1↔3 and 3↔9 mappings preserve the ratio). Surface similarity is overridden by relational structure when the two conflict — and this is what genuine analogy looks like.

For human thinking with AI: LLMs excel at the *surface* end of the similarity spectrum — high attribute overlap, pattern completion, "this looks like that." They struggle systematically with structural alignment that requires *suppressing* surface similarity to preserve deep relational structure. The child saying "Where the white door?" after generalizing the color↔key↔door system is doing exactly the kind of structural alignment that lifts cognition above pattern completion. The KB's preservation case rests in part on protecting this kind of reasoning from being substituted by AI's surface-similarity gloss.

## Key Passages

> "Analogy and similarity are often viewed as quite separate: Analogy is a clever, sophisticated process used in creative discovery, whereas similarity is a brute perceptual process that we share with the entire animal kingdom. … We suggest that the process of carrying out a comparison is the same in both cases. The general idea is summarized by the slogan 'similarity is like analogy.'"
> — Gentner & Markman, [p.1]

> "Common relations are essential to analogy; common objects are not. This promoting of relations over objects makes analogy a useful cognitive device, for physical objects are normally highly salient in human processing — easy to focus on, recognize, encode, retrieve, and so on."
> — Gentner & Markman, [p.2]

> "The systematicity principle captures a tacit preference for coherence and causal predictive power in analogical processing. We are not much interested in analogies that capture a series of coincidences, even if there are a great many of them."
> — Gentner & Markman, [p.3]

> "A cross-mapping is a comparison in which two analogous scenarios contain similar or identical objects that play different relational roles in the two scenarios. … In `1:3::3:9`, the obvious possibility of matching the two identical 3s is dismissed because to do so would misalign the relational roles of the terms."
> — Gentner & Markman, [p.3]

> "These candidate inferences are only guesses: Their factual correctness must be checked separately. … Any process capable of producing novel true inferences is also capable of generating false inferences."
> — Gentner & Markman, [p.3]

## Relevance

The foundational specification of what *deep* reasoning looks like — and therefore the criterion against which AI pattern-matching can be evaluated. Three load-bearing contributions:

- **Distinguishes pattern-completion from analogical reasoning.** Surface similarity (LLMs are great at it) and structural alignment (LLMs are inconsistent at it) are different processes operating over different representational substrates. Treating their outputs as interchangeable is a category error.
- **Names the inference engine.** Systematicity is what lets a human reason from a known analogy to *new* discoveries in the target domain. Kepler's planets-as-boatmen analogy didn't just describe the planets — it generated falsifiable predictions about how the motive power must behave. AI completion that lacks systematic-relational structure can produce plausible-sounding statements but not novel-yet-correct ones.
- **Diagnostic for cross-mapping failures.** When human and AI reasoning disagree on a hard case, the structural-alignment view predicts AI is more likely to over-weight surface similarity (matching the identical 3s) where humans correctly suppress it. This is testable.

## Supports

- [[analogical-reasoning]] — primary theoretical source
- [[metacognition]] — recognizing whether you're doing surface matching vs. structural alignment
- [[think-first]] — the case for unaided reasoning when the task requires structural alignment
- [[fluency-bias]] — surface similarity is precisely what fluent AI output amplifies
- [[judgment]] — analogical reasoning is core to professional judgment in novel situations

## Contradicts / Extends

- Foundational; extended by subsequent computational implementations (Falkenhainer, Forbus, & Gentner 1989, the Structure-Mapping Engine; Holyoak & Thagard 1989). The KB doesn't have those source entries; this paper is the canonical reference.
- Compatible with [[bjork-desirable-difficulties-2011]] — both papers share the underlying claim that *productive struggle* (here: working out a structural alignment when surface cues mislead) builds something AI substitution doesn't.

## Open Questions

- Empirical question with sharper teeth in the AI era: how do current LLMs perform on cross-mapping tasks where surface and structural similarity conflict? (Existing benchmarks tend to lean on surface similarity.)
- Does AI-assisted reasoning preserve the human's ability to do structural alignment, or does prolonged use of pattern-completion tools degrade it (per the [[capacity-erosion]] hypothesis)?
- Gentner & Markman's framework predicts that humans suppress surface matches when structure demands it. Do AI-mediated reasoning settings (where surface matches are abundant and immediate) make that suppression harder?
