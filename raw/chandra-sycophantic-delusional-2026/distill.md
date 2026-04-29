# Distillation: Chandra et al. (2026) — Sycophantic Chatbots Cause Delusional Spiraling

## Extraction Ledger

### Concepts
- NEW: `delusional-spiraling` — Chandra et al. give the construct its first formal definition (the user's posterior in a false hypothesis monotonically increases across rounds; "catastrophic" spiral = crossing a high-confidence threshold within T rounds). The phenomenon is empirically documented (Hill 2025a/b; Hill & Freedman 2025) and named ("AI psychosis"), but has no atomic KB entry. Distinct from sycophancy (cause), borrowed-certainty (single-shot), belief-offloading (state), artificial-certainty (organizational/representational). Confidence: HIGH that this is a NEW concept rather than a relabel.
- UPDATE: `sycophancy` — add the iterated-dynamics result, the two-intervention failure analysis (factual sycophant, informed user), and the policy implications. Companion paper to Batista & Griffiths (2026).
- UPDATE: `borrowed-certainty` — extend with the compounding-across-rounds dynamic; borrowed certainty is the per-round ingredient, delusional spiraling is the longitudinal outcome.
- UPDATE: `belief-offloading` — Chandra's level-3 informed-user result is a formal demonstration of Guingrich et al.'s C1 condition holding even with full awareness; strengthens the "feeling of autonomy ≠ causal independence" claim.

### Methods
- (none) — The "factual sycophant" and "informed user" interventions are interventions on AI systems / users at the policy level, not practitioner methods. The KB's `methods/` folder contains practitioner-facing guidance; these don't fit.

### Source Entry
- drafts/source.md — always

## Files Created
- drafts/source.md
- drafts/concepts/delusional-spiraling.md
- drafts/updates/sycophancy.md
- drafts/updates/borrowed-certainty.md
- drafts/updates/belief-offloading.md

## Decision

- **Outcome**: PROCEED_TO_CRITIQUE
- **Date**: 2026-04-30
- **Reason**: AUTO mode + paper introduces a NEW concept that needs adversarial-lens scrutiny (false-novelty risk against existing borrowed-certainty / belief-offloading / artificial-certainty entries). Stage 4 critique appropriate before integration.
