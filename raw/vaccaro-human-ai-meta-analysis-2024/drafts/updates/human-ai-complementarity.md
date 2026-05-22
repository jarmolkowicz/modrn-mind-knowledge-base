# Update: Human-AI Complementarity

## Source

[vaccaro-human-ai-meta-analysis-2024]

## Proposed Revision

### To "Why It Matters" section

The section currently reads:

> The assumption that "human + AI = better" is widespread but empirically unsupported as a general claim. Meta-analyses show that human-AI teams can outperform either party alone, but only when collaboration is well-calibrated and humans understand when and how to rely on AI input. Poorly designed interaction or overreliance on AI can produce worse outcomes than either working independently. This means complementarity is a design problem, not an inevitability.

The second sentence overstates what meta-analytic evidence shows. Vaccaro et al. (2024) — the largest meta-analysis on the question — found the *opposite* on average. Proposed replacement (preserving the section's voice and its closing point):

> The assumption that "human + AI = better" is widespread but empirically unsupported as a general claim. The largest meta-analysis to date (Vaccaro et al. 2024; 106 experiments) found that, on average, human-AI combinations performed *worse* than the best of human-or-AI alone — genuine synergy occurred in a minority of cases and only under specific conditions. Poorly designed interaction or overreliance on AI can produce worse outcomes than either working independently. This means complementarity is a design problem, not an inevitability.

## Proposed Additions

### To "Key Insight" section

Add as the first empirical paragraph, immediately before the existing "Handa et al. (2025) provide the first production-scale empirical map..." paragraph:

> Vaccaro et al. (2024) provide the meta-analytic anchor for this concept. Synthesizing 106 experiments (370 effect sizes) that each measured human-alone, AI-alone, and human-AI performance, they found that combinations *underperformed* the best of human-or-AI alone on average (Hedges' g = −0.23); only 42% of effect sizes showed genuine synergy. Complementarity is therefore not the typical outcome of pairing a human with an AI — it is a conditional minority result. Two factors predicted it: task type (creation tasks gained, decision tasks lost) and relative ability — synergy appeared when the human was the stronger party (g = 0.46) and reversed into losses when the AI was stronger (g = −0.54). This sharpens the entry's existing "uncertain middle ground" claim: the sweet spot is not merely tasks of uncertain difficulty but specifically tasks where the human's standalone ability still exceeds the AI's. Once the AI alone is the stronger party, adding a human tends to subtract value — which is why complementarity is a design target rather than a default.

### To "Related" section

- [[augmentation-synergy-gap]] — the distinction between merely beating the human (augmentation) and beating both parties (synergy); complementarity is synergy achieved
- [[vaccaro-human-ai-meta-analysis-2024]] — meta-analytic anchor: synergy is a conditional minority result, not the average outcome

## New Source for Frontmatter

Add to `sources:` list:

- "Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1"

And add the matching `[[vaccaro-human-ai-meta-analysis-2024]]` line to the "## Sources" section at the bottom of the entry.
