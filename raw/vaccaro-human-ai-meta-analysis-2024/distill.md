# Distillation: When combinations of humans and AI are useful (Vaccaro et al. 2024)

## Extraction Ledger

### Concepts
- NEW: `augmentation-synergy-gap` — the distinction between a human-AI system beating
  the human alone (augmentation) vs. beating both parties (synergy), and the fact that
  the two routinely come apart (85% augment, 42% synergize in the meta-analysis). The
  paper's two-baseline framing is genuinely novel to the KB and not a relabel of an
  existing entry: `human-ai-complementarity` covers synergy-achieved (the positive
  condition); `performance-paradox` covers durable-learning loss. Neither names the
  evaluation trap of crediting a system on the augmentation baseline when the synergy
  baseline is the one that applies.
- DUPLICATE: "human-AI synergy" as a standalone concept — synergy *is* the existing
  `human-ai-complementarity`. Not created separately; handled via the UPDATE below.

### Methods
- (none) — the paper reports findings; it does not introduce a protocol or model.
  Its findings update the existing `complementarity-framework` method.

### Updates
- UPDATE: `human-ai-complementarity` — the paper is the meta-analytic anchor this
  concept lacked. Includes a *revision* (the "Why It Matters" section currently states
  meta-analyses show teams outperform either party — the reverse of what Vaccaro et al.
  found) plus additions.
- UPDATE: `complementarity-framework` — empirical grounding for the task-type and
  relative-ability factors; null-result caution on AI explanations/confidence; first
  real source for an entry whose `sources:` list is currently empty.

### Source Entry
- drafts/source.md — always.

## Files Created
- drafts/source.md
- drafts/concepts/augmentation-synergy-gap.md
- drafts/updates/human-ai-complementarity.md
- drafts/updates/complementarity-framework.md

## Editorial notes for reviewer
1. **New concept call.** `augmentation-synergy-gap` is the main editorial decision.
   It is defensible as separate from `human-ai-complementarity` (positive condition)
   and `performance-paradox` (learning loss). If the reviewer prefers a leaner KB,
   the alternative is to fold the distinction into the `human-ai-complementarity`
   update and not create a standalone entry.
2. **Source status = `solid`.** Justified: peer-reviewed *Nature Human Behaviour*,
   preregistered, full bias/sensitivity diagnostics. The new concept is `emerging`
   (single meta-analysis, novel framing — cautious default).
3. **`complementarity-framework` status unchanged** (`speculative`). One grounding
   source does not validate the framework as a unified model. Flagged, not changed.

## Decision

- **Outcome**: PROCEED_TO_CRITIQUE
- **Date**: 2026-05-22
- **Reason**: User confirmed proceed to critique and confirmed `augmentation-synergy-gap` as a standalone new concept.
