# Update: Complementarity Framework

## Source

[vaccaro-human-ai-meta-analysis-2024]

## Context

The framework's `sources:` list is currently empty — its primary source was removed
pending verifiable access. Vaccaro et al. (2024) does not test the framework as a unified
model, but it is peer-reviewed meta-analytic evidence for two of the framework's named
"Factors Shaping Complementarity" (task characteristics, relative ability) and a caution
on a third (the interrogation/interface emphasis). It gives the entry a real empirical
anchor without overstating support for the framework as a whole.

## Proposed Additions

### To "Factors Shaping Complementarity" section

Append to the **Task characteristics** bullet:

> Vaccaro et al.'s (2024) meta-analysis of 106 experiments empirically confirms this: creation tasks (open-response content) showed performance gains, while decision tasks (choosing among fixed options) showed losses — and relative ability mattered most of all, with synergy appearing when the human was the stronger party and reversing into losses when the AI was.

Append to the **Trust calibration** bullet:

> A caution from the same meta-analysis: AI explanations and AI confidence displays — features the framework's interrogation and interface principles lean on — did *not* significantly improve human-AI performance across the 106 experiments. Surfacing AI reasoning is not sufficient on its own to produce calibrated trust; the framework's interrogation principle needs more than explanation-provision to deliver complementarity.

### To "Related" section

- [[vaccaro-human-ai-meta-analysis-2024]] — meta-analytic evidence for the task-type and relative-ability factors; null result on AI explanations and confidence
- [[augmentation-synergy-gap]] — the framework targets synergy; the gap names what a framework that settles for mere augmentation leaves on the table

### To "Sources" section

The "## Sources" section currently holds only the note about the removed primary source.
Add the Vaccaro entry as a genuine source above (or below) that note:

- [[vaccaro-human-ai-meta-analysis-2024]] — Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303.

## New Source for Frontmatter

Change `sources: []` to a list containing:

- "Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1"

## Note for reviewer

The method's `status` is `speculative`, partly because it lost its primary source. Vaccaro
et al. grounds *some* of its factors empirically but does not validate the framework as a
unified model, so this update alone does not justify promoting it to `emerging`. Status
left unchanged unless the reviewer decides otherwise.
