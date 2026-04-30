# Distillation: Latikka et al. (2026) — Six-Country Social Chatbot Study

## Extraction Ledger

### Concepts
- (none NEW) — Cross-country observational studies typically test, rather than introduce, constructs. Latikka et al. (2026) deploy existing measures (R-UCLA-3 loneliness, MHI-5 distress, single-item self-esteem) and existing theoretical framings (CASA, MASA, Media Evocation, need to belong, strong/weak ties). The empirical contribution is generalizability evidence, not a new construct.
- UPDATE: `ai-loneliness-effect` — adds cross-cultural breadth; six EU countries replicate the higher-distress association universally and the loneliness association in 4/6 samples; refines substitution framing toward subjective rather than objective contact register.
- UPDATE: `anthropomorphism-of-technology` — adds preliminary cross-cultural data on chatbot uptake and psychosocial correlates, complementing the open generalizability question Folk-Heine-Dunn (2025) flagged. Latikka et al. do not measure anthropomorphism directly.

### Methods
- (none NEW) — Standard logistic + robust linear regression (Stata 17, mm-estimator robreg). MASA/CASA/Media Evocation are theoretical lenses, not protocols. Binary chatbot-use measure is too coarse to enter `methods/` as a contribution.

### Source Entry
- drafts/source.md — always

## Files Created
- drafts/source.md
- drafts/updates/ai-loneliness-effect.md
- drafts/updates/anthropomorphism-of-technology.md

## Confidence

HIGH on every classification:
- No NEW concept candidates emerged on full read of methods/results/discussion. The paper is explicit that its contribution is cross-national replication of associations the literature already names.
- UPDATE classifications are obvious: the paper's most cited prior work in this KB cluster is the loneliness/companion-chatbot literature, and its most generalizable findings (age + distress + loneliness associations across six countries) directly extend [[ai-loneliness-effect]]. Anthropomorphism-of-technology gets a smaller UPDATE because the cross-cultural angle complements the open question Folk-Heine-Dunn flagged, even though Latikka et al. don't measure anthropomorphism.
- No suspected near-duplicates. Searched `latikka`, `six.country`, `cross.cultural`, `chatbot` against `sources/` and KB search; no match.

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: AUTO mode. HIGH confidence on all NEW/UPDATE classifications; no near-duplicates flagged; cross-cultural observational paper extending the existing loneliness cluster with explicit generalizability evidence. Skip Stage 4 editorial critique; proceed directly to Stage 4.5 mechanical validation.
