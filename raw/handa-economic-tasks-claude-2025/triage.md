# Triage: Handa et al. (2025) — Which Economic Tasks are Performed with AI?

## Source

- Slug: `handa-economic-tasks-claude-2025`
- Type: `paper`
- Format: pdf, 38 pages, ~12,935 words
- Path: `raw/handa-economic-tasks-claude-2025/source.md` (extracted), `raw/handa-economic-tasks-claude-2025/original.pdf` (binary)

## Summary

Handa et al. (Anthropic, arXiv:2503.04761, Feb 2025) present the first large-scale empirical measurement of which economic tasks are actually being performed with AI in production, drawing on Clio-based privacy-preserving classification of over four million Claude.ai Free and Pro conversations from December 2024 – January 2025. Conversations are mapped to tasks and occupations in the U.S. Department of Labor's O*NET database, then aggregated up to occupational categories, skills, wage bands, and Job Zones (barrier-to-entry levels).

The paper makes five contributions: (1) task-level distribution of AI usage across the economy, (2) depth analysis showing what fraction of each occupation's tasks see AI usage, (3) which O*NET skills appear most in human-AI conversations, (4) wage and barrier-to-entry correlations with AI usage, (5) classification of conversations as automation vs. augmentation. Headline findings: software development and writing tasks together account for ~half of all usage; ~36% of occupations show AI usage in at least 25% of their tasks but only ~4% see usage across 75% of tasks; usage peaks in the upper-middle wage quartile (Computer Programmers, Web Developers) with notably lower usage at both extremes (anesthesiologists, restaurant workers); 57% of conversations show augmentative patterns and 43% automative.

This is descriptive, observational evidence at production scale — the same methodology family as Sharma et al. (2026, [[sharma-disempowerment-patterns-2026]]) but turned outward at the task economy rather than inward at user disempowerment. It is a baseline empirical anchor for what people actually use AI for, against which forecasts (Frey & Osborne 2017, Eloundou et al. 2023, Webb 2019) and survey data (Humlum & Vestergaard 2024, Bick et al. 2024) can be tested.

## Relevance

- Risk: yes — establishes empirical priors for which occupations face AI integration at task level; informs which professions face skill-formation and identity risk first
- Erosion: yes — the augmentation/automation 57/43 split and the depth-of-usage distribution are direct empirical anchors for KB claims about cognitive offloading prevalence and partial-vs-full automation patterns at scale
- Preservation: yes — the augmentative-pattern majority (Task Iteration, Learning, Validation) is direct evidence for partial-automation and complementarity patterns being the dominant emergent practice, not just normative recommendation
- **Relevance**: HIGH

## Quality

- Evidence basis: production-scale observational data (4M+ conversations, Clio pipeline previously validated in Tamkin et al. 2024); human validation of task-classification pipeline reported in Appendix C; conservative privacy controls (only tasks with ≥15 conversations across ≥5 unique accounts surface); explicit limitations section addresses sample bias (text-only Claude.ai, free/pro only), classification noise, query-complexity confounds, O*NET staticness, and missing workflow context. Peer-reviewed status: arXiv preprint, but the methodology paper (Tamkin et al. 2024) and the team are well-established at Anthropic and the data are public on Hugging Face. Published in NeurIPS workshop track per arXiv listing.
- Originality: first large-scale production-data measurement of AI task usage mapped to O*NET. Methodologically novel (Clio-traversal of O*NET task hierarchy); empirically the first production view that complements the prior literature's predictive (Eloundou, Webb, Felten) and survey-based (Humlum, Bick) approaches. Compared against existing KB: [[sharma-disempowerment-patterns-2026]] is the closest analogue (same Clio family, same Anthropic team, same production-data lens) but addresses disempowerment patterns rather than task economics; [[hermann-genai-psychology-work-2025]] reviews psychological-work effects but not at task-distribution level; [[mollick-cointelligence-2024]] and [[mollick-management-ai-superpower-2026]] discuss task substitution qualitatively but not at empirical scale. No KB entry currently provides this descriptive baseline.
- **Quality**: HIGH

## Extractable Elements

- Concepts: candidate NEW — `automation-augmentation-split` (taxonomy of five collaboration patterns: Directive, Feedback Loop, Task Iteration, Learning, Validation, grouped into automative/augmentative). [Inference] This is a labeled construct introduced by the paper, measurable via Clio classification, and gives the KB a vocabulary anchor for the augmentation/automation distinction that is currently scattered across [[partial-automation-principle]], [[human-ai-complementarity]], and various sources. May warrant a NEW concept entry — but it is also adjacent to existing constructs and needs adversarial review.
- Methods: (none) — the Clio + O*NET-traversal pipeline is research methodology, not practitioner-facing
- Claims: rich descriptive claims at occupation/task/skill/wage/barrier levels; many citable as production-scale anchors for existing KB concepts

## Recommendation

**INCLUDE**

Reason: HIGH relevance + HIGH quality + not a duplicate. This is the missing empirical baseline for the KB's "what people actually use AI for" question. The descriptive evidence anchors UPDATE proposals across multiple existing concepts ([[performance-paradox]], [[novice-vulnerability]], [[professional-identity-threat]], [[situational-disempowerment]], [[execution-commoditization]], [[partial-automation-principle]], [[human-ai-complementarity]]) and may justify one carefully-scoped NEW concept on the augmentation/automation split.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: AUTO mode override of prior DEFER. HIGH relevance (production-data baseline KB lacks), HIGH quality (4M+ conversations, validated pipeline, conservative privacy controls, explicit limitations), no duplicate. Descriptive observational paper — conservative on NEW concepts; primary contribution is to provide empirical anchors for existing KB claims.
