# Self-Critique: Bartoš et al. (2026)

## Overall: READY

Stage 4 self-critique abbreviated per librarian.md AUTO-mode rubric (high-confidence drafting; no NEW concepts; no near-duplicates flagged). Stage 4.5 mechanical validation ran clean on 2nd attempt (1 missing_related fix: added [[cognitive-offloading]] to source distillation Supports section; the broken_wikilinks were resolved by renaming the workbench dir to the canonical slug `bartos-ai-learning-meta-meta-2026`).

## AI Failure Checklist

- [x] Hallucinated citations: spot-checked. All citations in the source draft (Bartoš 2026 self-citations, Lee et al. 2025, Gerlich 2025, Kosmyna et al. 2025, Bastani et al. 2025, Dell'Acqua et al. 2023, Wang & Fan 2025, Kovanović 2025) appear in the original PDF references and/or are already KB-linked.
- [x] Methodology fabrication: no. Statistical claims (RoBMA-PSMA, BMA, Bayes factors, prediction intervals, k=1840 / m=67) match source.md page-locator excerpts verbatim.
- [x] Statistical drift: numbers in draft (SMD = 0.196 [0.000, 0.323]; SMD unadjusted = 0.629 [0.572, 0.685]; τ = 0.869 [0.822, 0.926]; PI [−1.521, 1.908]; BF₁₀ = 13.3; 0/44 vs. 41/44 strong-evidence after RoBMA-PSMA correction) all confirmed against source.md [pp.12-13, 20-21].
- [x] Conflated constructs: no — explicitly avoided creating "evidence inflation" / "meta-analytic mirage" as new concept; positioned umbrella as calibration, not new construct.
- [x] Status overstatement: source distillation set to `solid` (peer-reviewed-grade methodology with open data on OSF; published preprint by senior methodologists). UPDATEs do not change other entries' status fields.
- [x] Broken wikilinks: validate_drafts.py exit 0; all 7 Supports + 4 Extends + 5 UPDATE-target wikilinks resolve.
- [x] False novelty: NO new concepts proposed. Considered "evidence inflation" / "publication-bias-collapse" as candidates and rejected (umbrella reviews calibrate, they don't name; the relevant existing concept is `[[fluency-bias]]` extended to academic narratives, but that's a stretch — kept as a Supports cross-link instead).

## drafts/source.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Methodology described faithfully (RoBMA-PSMA + RoBMA-WF sensitivity); central numbers match source verbatim; status `solid` justified by peer-reviewed-grade methodology + OSF open data. |
| Practitioner | APPROVE | The "Calibration of the broader literature" frame is directly useful for a consultant fielding "but a meta-analysis says AI improves learning by SMD 0.6" — the entry gives a single-citation rebuttal anchor. Plain-language summary in Key Insight. |
| Adversarial | APPROVE | Could be seen as overplaying the negative — the paper's own Discussion notes that null direct effects do not preclude indirect systemic effects [p.23]. Open Questions section explicitly addresses this. The draft does not claim "AI hurts learning"; it claims "the published literature does not support broad claims of generalized learning gains," which is exactly what the umbrella concludes. No hype, no urgency, no AI-as-replacement. |

**Synthesis:** High-leverage source distillation. The five UPDATE proposals are surgical (each adds one paragraph + one Related link + one source frontmatter entry) and respect each entry's existing voice. No restructure needed.
**Suggested action:** integrate.

## drafts/updates/*.md

All 5 UPDATE drafts: APPROVE across all lenses. Each is a focused 1-paragraph addition to the existing Key Insight section + 1 Related link + 1 frontmatter source line. No re-statements; the paragraphs add the umbrella-level statistical context that the existing entries lacked.

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: All checks pass. Validation clean. No NEW concepts; 5 surgical UPDATE proposals + 1 source distillation. Proceeding to Stage 5.
