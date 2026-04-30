# Distillation: Yu et al. (2024) — Heterogeneity and Predictors of AI Assistance on Radiologists

## Extraction Ledger

### Concepts
- (none) — Article-type playbook default. The paper applies established statistical constructs (treatment effect, calibration vs. discrimination, empirical Bayes shrinkage, split sampling) without introducing new named phenomena. The paper's headline phrase "heterogeneous treatment effects" is a generic statistical-methodology term, not a candidate KB concept. Conservative call: 0 NEW per article-type playbook.

### Methods
- (none) — The paper's methodological recommendation ("measure individual treatment effects under realistic deployment conditions before deciding who receives AI") is a research-practice recommendation for AI-deployment teams, not a transferable practitioner method appropriate for the methods/ folder. Better captured as a Supports link from [[calibration]].

### Source Entry
- drafts/source.md — always

### Updates
- UPDATE: automation-bias — specialist-context dose-response: AI absolute error >80 yields treatment effect of −16.845 in 140 board-certified radiologists; experience-based and skill-based predictors of automation-bias susceptibility all fail. Direction-of-error finding (underestimation > overestimation) adds nuance to the failure-mode picture.
- UPDATE: human-ai-complementarity — direct empirical demonstration that complementarity is heterogeneous at the individual-expert level: same AI, same expert pool, same tasks, treatment effects span both improvement and degradation. Adds AI-error-profile dimension to the entry's existing task-structure framing.
- UPDATE: novice-vulnerability — counter-evidence sharpening boundary conditions: lower-performing radiologists within an expert cohort did not consistently benefit more from AI. The "AI as leveler" framing is about developmental skill formation across novices→experts, not within-expert skill variation. Sharpens — does not contradict — the entry's core claim.
- UPDATE: paradox-of-expertise — Yu's failure-of-experience-predictors finding sharpens the paradox: even when experts do use AI (Yu's experimental design ruled out under-adoption), experience does not predict productive integration. Implies the paradox is more about the adoption decision than the post-adoption outcome.

## Files Created

- drafts/source.md
- drafts/updates/automation-bias.md
- drafts/updates/human-ai-complementarity.md
- drafts/updates/novice-vulnerability.md
- drafts/updates/paradox-of-expertise.md

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: AUTO mode, HIGH confidence on all NEW classifications (zero NEW concepts; all UPDATEs target existing entries with clear, well-attested KB stems). Per Stage 3 AUTO rule, skip Stage 4 self-critique and proceed directly to Stage 4.5 mechanical validation.
