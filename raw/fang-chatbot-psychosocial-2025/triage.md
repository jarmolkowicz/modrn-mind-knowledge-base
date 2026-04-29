# Triage: fang-chatbot-psychosocial-2025

## Source
- Slug: `fang-chatbot-psychosocial-2025`
- Type: `paper`
- Format: pdf, 70 pages, 23,462 words
- Path: `raw/fang-chatbot-psychosocial-2025/source.md` (extracted), `raw/fang-chatbot-psychosocial-2025/original.pdf` (binary, arXiv:2503.17473v2, 2 Oct 2025)

## Summary

Fang, Liu, Danry, Lee, Chan, Pataranutaporn, Maes (MIT Media Lab) and Phang, Lampe, Ahmad, Agarwal (OpenAI). "How AI and Human Behaviors Shape Psychosocial Effects of Extended Chatbot Use: A Longitudinal Randomized Controlled Study." arXiv:2503.17473v2, Oct 2025.

A 4-week randomized controlled trial (n=981, >300,000 messages) crossing three interaction modalities (text, neutral voice, engaging voice) with three conversation types (open-ended, non-personal, personal) in a 3x3 factorial design. Participants were assigned to use OpenAI's GPT-4o for at least five minutes daily. Weekly surveys tracked four psychosocial outcomes: loneliness, real-world socialization, emotional dependence on AI, and problematic AI use. Automated classifiers extracted affective/behavioral signals from conversation logs. Empirical evidence — large-scale longitudinal RCT.

This is the **same paper** already integrated as `[[fang-ai-loneliness-2025]]`. The existing KB entry was extracted from arXiv:2503.17473v1 (March 2025); this workbench's PDF is v2 (October 2025). Title differs only by the inserted word "Extended"; authors, n, message count, factorial design, findings — all identical.

## Relevance
- Risk: yes — emotional dependence, problematic use
- Erosion: yes — socialization decreases with usage
- Preservation: not directly
- **Relevance**: HIGH

## Quality
- Evidence basis: largest-scale longitudinal RCT on chatbot psychosocial effects to date
- Originality: paper is highly original; **but this workbench is a duplicate** of the v1 already integrated as `[[fang-ai-loneliness-2025]]`
- **Quality**: HIGH (paper); N/A (duplicate workbench)

## Extractable Elements
- Concepts: already extracted via `[[ai-loneliness-effect]]`; supports `[[capacity-erosion]]`, `[[green-yellow-red-monitoring]]`
- Methods: none new
- Claims: already covered by existing `[[fang-ai-loneliness-2025]]` source distillation

## Recommendation
**DUPLICATE-SKIP**

Reason: Same paper as `[[fang-ai-loneliness-2025]]` (arXiv:2503.17473). The integrated entry was extracted from v1; this workbench is v2 (minor revision, "Extended" added to title; nearly identical word count: 23,558 vs 23,462). Hash differs only because v1 vs v2 PDFs differ. No new content to extract. The existing `[[fang-ai-loneliness-2025]]` source distillation already covers the headline findings (dose-dependent psychosocial effects, voice-modality benefits diminishing at high usage, individual vulnerability factors). Keeping a second workbench would create duplicate citations in the KB graph.

## Decision

- **Outcome**: SKIP
- **Date**: 2026-04-30
- **Reason**: Duplicate of `[[fang-ai-loneliness-2025]]` (same arXiv ID 2503.17473, v1 already integrated; this is v2). Overrides prior 2026-04-29 DEFER recommendation, which was made before the duplication was discovered. No further pipeline stages run.
