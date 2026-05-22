# Self-Critique: When combinations of humans and AI are useful (Vaccaro et al. 2024)

## Overall: READY

All four drafts passed all three lenses and the AI failure checklist. One minor
adversarial flag (a single sentence in the new concept's Key Insight) is noted below
as a consideration, not a blocker.

## AI Failure Checklist

- [x] **Hallucinated citations**: One source cited — Vaccaro, Almaatouq & Malone (2024), *Nature Human Behaviour* 8:2293–2303, DOI 10.1038/s41562-024-02024-1. Matches the ingested PDF. All `[[wikilinks]]` point to existing KB entries or to the new drafts in this batch.
- [x] **Methodology fabrication**: Draft descriptions (preregistered, PRISMA, three-level random-effects meta-analytic model, 106 experiments from 74 papers, 370 effect sizes, ACM/Web of Science/AIS databases, Jan 2020–Jun 2023, Egger's regression and rank-correlation bias tests, leave-one-out sensitivity) all match the source [p.1–2, p.6–8].
- [x] **Statistical drift**: Every figure verified against the source — synergy g = −0.23 (CI −0.39 to −0.07; t₉₂ = −2.89; P = 0.005) [p.3]; augmentation g = 0.64 (CI 0.53–0.74; t₉₈ = 11.87) [p.3]; decision g = −0.27 (n = 344; P = 0.002) and creation g = 0.19 (n = 34; P = 0.180) [p.4]; task-type F₁,₁₀₄ = 7.84, P = 0.006 [p.4]; relative-performance F₁,₁₀₄ = 81.79 [p.3]; human-stronger g = 0.46, AI-stronger g = −0.54, AI-stronger augmentation g = 0.74 [p.3]; I² = 97.7% / 93.8% [p.3]; 58%/42% and 85%/15% splits [p.2, Fig. 1]; Egger synergy P = 0.438, augmentation P = 0.002 [p.8]. No drift.
- [x] **Conflated constructs**: Augmentation and synergy kept distinct throughout; complementarity correctly equated with synergy; the new concept explicitly separates itself from `performance-paradox` (learning loss) and `human-ai-complementarity` (positive condition).
- [x] **Status overstatement**: Source `solid` — justified (peer-reviewed *Nature Human Behaviour*, preregistered, full bias/sensitivity diagnostics). New concept `emerging` — justified (single meta-analysis, novel framing). `complementarity-framework` status left `speculative`.
- [x] **Broken wikilinks**: All links checked against `concepts/` and `sources/` globs — `human-ai-complementarity`, `complementarity-framework`, `automation-bias`, `performance-paradox`, `jagged-frontier`, `dellacqua-jagged-frontier-2023`, `yu-radiologists-ai-2024`, `handa-economic-tasks-claude-2025` all exist; `augmentation-synergy-gap` and `vaccaro-human-ai-meta-analysis-2024` resolve within this batch. Mechanical re-check in Stage 4.5.
- [x] **False novelty**: `augmentation-synergy-gap` checked against the two nearest entries. It is not a relabel: `human-ai-complementarity` is the positive condition (synergy achieved); `performance-paradox` is durable-competence loss. The gap names a distinct evaluation trap — crediting a system on the augmentation baseline when the synergy baseline is the one that applies. User confirmed standalone.

## source.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Numbers, methods, and CIs faithful to the source. The augmentation result is correctly flagged as subject to publication bias (Egger P = 0.002) and presented as an upper bound — this matches the paper's own caution and avoids overstating the "AI helps humans" finding. |
| Practitioner | APPROVE | The two-baseline framing and the "which baseline applies" question are directly usable. Key Findings section is scannable. Plain language; no jargon left undefined. |
| Adversarial | APPROVE | Balanced — presents the negative synergy result *and* the positive augmentation result, the moderators, and four limitations. No cherry-picking. Frames the null result as a design agenda, not AI-pessimism, consistent with KB voice. |

**Synthesis:** Faithful, well-bounded source distillation of a high-quality meta-analysis.
**Suggested action:** integrate.

## concepts/augmentation-synergy-gap.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The 85%-augment / 42%-synergize split and the g-values are accurate. The concept correctly states augmentation is "necessary but not sufficient" for synergy — true by the paper's definitions (synergy's baseline strictly dominates augmentation's). |
| Practitioner | APPROVE | Genuinely useful: it gives practitioners the question "which baseline are we measuring against?" before declaring an AI deployment a success. The legal/ethical/safety carve-out is retained so the concept does not dismiss augmentation-only systems where automation is barred. |
| Adversarial | APPROVE (with one flag) | The Key Insight sentence "a system that only augments is a system that should probably be left to the AI" could be read as endorsing AI-as-replacement. On balance it is acceptable: it is explicitly conditional ("where automation is genuinely an option"), it is the source's own logic ("otherwise, they would just use the best of the two" [p.2]), and it concerns a narrow performance benchmark, not human judgment or agency wholesale. The surrounding text keeps the human-augmentation case legitimate. No change required; noted for transparency. |

**Synthesis:** A distinct, well-evidenced concept that fills a real KB gap; the lone adversarial flag is a conditional, source-grounded statement that does not violate the replacement guardrail.
**Suggested action:** integrate.

## updates/human-ai-complementarity.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The revision corrects a genuine overstatement. The original sentence ("Meta-analyses show that human-AI teams can outperform either party alone") was uncited and is contradicted by the largest meta-analysis on the question. The replacement is accurate and cited. |
| Practitioner | APPROVE | The added paragraph sharpens the existing "uncertain middle ground" claim into something more actionable: complementarity depends on the human still being the stronger party. |
| Adversarial | APPROVE | The update revises one claim and adds one paragraph plus links — surgical, not a rewrite. It does not over-claim: the paragraph keeps "conditional minority result" framing rather than swinging to AI-pessimism. |

**Synthesis:** A correction the KB needed; well-scoped.
**Suggested action:** integrate (apply by hand in Stage 5, preserving the entry's voice).

## updates/complementarity-framework.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Vaccaro et al. genuinely grounds the task-type and relative-ability factors. The null-result caution on AI explanations/confidence is accurately characterized and correctly framed as a caution, not a refutation, of the framework's interrogation principle. |
| Practitioner | APPROVE | The additions are concrete and attached to the right bullets. The reviewer note about `status` is appropriate — does not silently promote the entry. |
| Adversarial | APPROVE | The update is honest about scope: it explicitly states Vaccaro does not validate the framework as a unified model, so it does not manufacture support the source cannot bear. |

**Synthesis:** Modest, well-bounded grounding for a previously source-less entry.
**Suggested action:** integrate (apply by hand in Stage 5).

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-05-22
- **Reason**: User confirmed; critique verdict READY, flagged line left as-is (conditional and source-grounded).
