# Self-Critique: Fernandes et al. (2026)

## Overall: READY

All drafts passed all three lenses and the AI failure checklist. Quantitative claims were verified against the paper's source.md (page-locator-anchored). The conservative "no new concept" call held under the Adversarial lens.

## AI Failure Checklist

- [x] **Hallucinated citations**: every cited author/year in the drafts (Fisher & Oppenheimer 2021, Tankelevitch et al. 2024, Koriat 1997, Jansen et al. 2021, Buçinca et al. 2021) appears in the paper's reference list and is used in the same way the paper uses it.
- [x] **Methodology fabrication**: the description of the SNAIL three-subscale instrument, the Bayesian *b/σ* model, the LSAT 20-item task, the AI-group/no-AI-group design (Study 1 quasi-experimental against Jansen et al. 2021; Study 2 randomized with monetary incentive), and the prompt-count quantitative description all match what is reported in the paper.
- [x] **Statistical drift**: all numerical claims spot-checked against source.md page locators:
  - "~3 points performance gain, ~4 points overestimation" → §7 conclusion + §6.4 implications [p.15]
  - σ_AI = 1.01 (95% HDI [0.84, 1.19]); σ_noAI = 1.78 (95% HDI [1.69, 1.88]) → [p.9–10]
  - *r* = .21 (Study 1), *r* = .20 (Study 2) for SNAIL TU × ΔEP → Tables 2 and 5 [p.9, p.12]
  - AUC ≈ .62 (AI), .61 (no-AI), p < .001 vs .70 benchmark → [p.12]
  - 46% one prompt/question; 8% > 3 prompts; M = 1.15 (SD = 0.34) → Table 3 [p.10]
  - 99% of bias posterior samples larger in AI group; 0% σ overlap → [p.10]
  - +£0.50 ≈ 8% bonus → [p.13]
  - All within paper's reported precision.
- [x] **Conflated constructs**: bias (estimate–performance gap) and sensitivity (AUC, trial-level confidence-correctness discrimination) are kept distinct in both the source draft and the metacognition update. The Bayesian decomposition (bias *b_k* vs. noise *σ_k*) is explicit. AI literacy (SNAIL composite vs. TU/CA/PA subscales) is also kept distinct.
- [x] **Status overstatement**: `status: solid` for the source entry is justified — peer-reviewed publication in *Computers in Human Behavior* (Elsevier), two studies (one with randomization), pre-registered analyses (implied by OSF data deposit), Bayesian model with R-hat < 1.1 and ESS > 1000. The UPDATE proposals do not change the parent entry's status.
- [x] **Broken wikilinks**: pre-validated. Initially used `[[overreliance]]` (does not exist) → corrected to `[[automation-bias]]`. Removed `[[dolan-competence-assessment-2025]]` (no entry yet, since dolan was DEFER) — replaced with plain text reference. Stage 4.5 will run validate_drafts.py for full sweep.
- [x] **False novelty**: explicitly *did not* propose a NEW concept entry for "AI literacy paradox", on the grounds that (a) Fernandes does not introduce a labeled construct and (b) the finding is a moderation result that strengthens `[[confidence-competence-gap]]` rather than carving out a new phenomenon. The conservative path was deliberate; see Adversarial lens below.

## drafts/source.md — `fernandes-metacognition-2025`

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Quantitative claims match the paper. The Bayesian computational model is described in plain enough language to be usable without misrepresenting the priors or the *b/σ* logic. The augmentation-hypothesis framing follows the paper's own framing. The claim that "AUC sensitivity is uniformly low" is correctly hedged: both groups fall below .70 — i.e., it is not specific to AI use, although AI use does not improve sensitivity either. |
| Practitioner | APPROVE | The headline numbers (~3-point gain / ~4-point overestimation; DKE flattening; AI-literacy paradox; null effect of incentives) are immediately citeable in workshops and writing. The "explain-back" design recommendation is concrete enough to act on. The 46% one-prompt finding is a vivid descriptive anchor for shallow-engagement claims. Some Bayesian-model terminology may be jargon-y but appears only in the Key Findings section, which a reader can skim. |
| Adversarial | APPROVE with note | Strongest counter-argument: the AI-literacy result rests on *self-reported* SNAIL scores, and self-report is correlated with the better-than-average effect by construction — so the paradox could be partially methodological (people who claim high AI literacy are also people prone to overclaiming generally). The paper acknowledges this (§6.3 limitation 6). Open Questions section already flags this concern, so the entry is not vulnerable to "I read the entry but missed the caveat". The no-NEW-concept call holds: creating an "AI literacy paradox" concept would fragment the KB; the finding is well-housed inside `[[confidence-competence-gap]]`. |

**Synthesis:** The entry is ready. Numbers are accurate, framing is hedged appropriately, and it slots cleanly into the existing concept network without overclaiming.
**Suggested action:** integrate.

## drafts/updates/confidence-competence-gap.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The proposed addition extends the existing entry's empirical base without contradicting any prior claim. The Bayesian decomposition is novel material in the KB. The AI-literacy paradox is a legitimate moderation finding. |
| Practitioner | APPROVE | The DKE-flattening framing ("AI doesn't correct overconfidence; it raises everyone to a uniform high baseline") is the kind of crisp formulation a consultant can use directly. |
| Adversarial | APPROVE | The proposed text does not pre-empt the existing entry's other mechanisms (Shaw & Nave's per-item confidence, Leonardi's organizational artificial certainty, Reich's social comparison). It adds a complementary computational-decomposition story. No de-emphasis of pre-existing material. |

**Synthesis:** Clean update; strengthens an existing solid concept with a primary empirical anchor.
**Suggested action:** integrate.

## drafts/updates/metacognition.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The AUC sensitivity claim ("below .70 in both groups") is faithful to the paper. The framing through Tankelevitch et al. (2024) and Koriat (1997) reproduces the paper's own theoretical framing. |
| Practitioner | APPROVE | The added subsection gives the metacognition entry a clean empirical anchor for the "metacognitive sensitivity is degraded" claim that previously relied on theoretical citations. The "Did I evaluate this AI output, or did it arrive so smoothly that my monitoring never engaged?" question (already in the entry) now has direct empirical support. |
| Adversarial | APPROVE with note | The AUC ≈ .62 finding applies to *both* groups in this study. The framing should not imply that AI uniquely degrades sensitivity — it shows that sensitivity is generally low *and* that AI does not improve it. The draft phrasing handles this correctly: "for both AI and no-AI groups". |

**Synthesis:** Tight, additive update.
**Suggested action:** integrate.

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: All drafts passed all lenses and the AI failure checklist. Quantitative claims are verified against page-locator-anchored extracts. Conservative "no new concept" call held under Adversarial pressure. Stage 4.5 mechanical validation runs next.
