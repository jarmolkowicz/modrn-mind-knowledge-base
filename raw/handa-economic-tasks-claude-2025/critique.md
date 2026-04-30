# Self-Critique: Handa et al. (2025) — Which Economic Tasks are Performed with AI?

## Overall: READY

All drafts pass all three lenses with focused revision suggestions captured in this critique. No blockers. No AI-failure-checklist findings of concern. Statistical figures in drafts match the source within rounding.

## AI Failure Checklist

- [x] Hallucinated citations: every citation in the drafts (Handa et al. 2025; Sharma 2026; Bastani 2025; Hai 2025; Eloundou 2023; Webb 2019; Passalacqua 2024) matches a real source — Handa is the source under ingestion; all others map to existing KB entries (verified by Glob against `sources/`).
- [x] Methodology fabrication: descriptions of Clio classification, O*NET mapping, ≥15 conversations across ≥5 unique-account privacy threshold, and Free/Pro-only sample match the source's own description.
- [x] Statistical drift: all numbers in drafts match source within rounding — 4M conversations [p.1], 57/43 augment/automate split [p.1, p.3], ~36% of occupations with ≥25% tasks [p.2, p.7], ~4% with ≥75% [p.2, p.7], ~11% with ≥50% [p.7], 37.2% Computer & Mathematical [p.6], 10.3% Arts/Design/Entertainment/Sports/Media [p.6], ~57% of occupations using AI for ≥10% of tasks vs Eloundou prediction [p.13].
- [x] Conflated constructs: the five-pattern collaboration taxonomy (Directive, Feedback Loop, Task Iteration, Learning, Validation) is described as the paper describes it; not blended with [[partial-automation-principle]]'s d ≈ 0.9 finding (the source.md "Inference" tag flags the consistency claim explicitly as inference, not causal).
- [x] Status overstatement: source.md status is `solid` — justified by ~4M-conversation sample, validated Clio pipeline (Tamkin et al. 2024), human validation in Appendix C, conservative privacy thresholds, public dataset on Hugging Face, well-established Anthropic team. The paper is observational, not causal — but its descriptive findings are quantitatively robust at the population level. `solid` matches the convention used for Sharma et al. (2026) in the existing KB.
- [x] Broken wikilinks: every `[[link]]` in the drafts resolves. Verified targets: `partial-automation-principle`, `human-ai-complementarity`, `execution-commoditization`, `novice-vulnerability`, `professional-identity-threat`, `situational-disempowerment`, `performance-paradox`, `jagged-frontier`, `sharma-disempowerment-patterns-2026`, `handa-economic-tasks-claude-2025` (self-reference, will resolve at Stage 5).
- [x] False novelty: no NEW concepts created. The collaboration-pattern taxonomy was considered for NEW but rejected because it is operationally adjacent to existing constructs and the paper does not develop it as a load-bearing theoretical construct (it is a measurement scheme).

## drafts/source.md (Handa source distillation)

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The source distillation is faithful to the paper. Every Key Passage is verbatim with page locator. Key Findings section accurately reports task/occupation/skill/wage/Job-Zone/augment-automate distributions. The "Inference" tags on the Webb/Eloundou comparisons and the partial-automation correlational claim are appropriately flagged. The "Open Questions" section accurately reflects the paper's own limitations section. No drift from the source. |
| Practitioner | APPROVE | Useful at 7am before a client meeting: the Key Insight gives three concrete numbers (57/43 split, 36% breadth, 4% depth) that a consultant can use immediately. The Key Findings tabulation is dense but scannable. Plain language throughout. The "Supports" section gives the practitioner a map of which existing KB entries this anchors empirically, which is the right call for a descriptive baseline paper. Suggestion: the long Open Questions section may read as over-hedged for some practitioner audiences, but the alternative (under-hedging) is worse for a single-platform observational study. |
| Adversarial | APPROVE with note | The strongest counter-argument is that the paper is a single-provider snapshot (Claude.ai Free/Pro, two months) and that source.md should be more cautious about generalizing to "AI usage in the economy" broadly. The draft addresses this in the Open Questions section explicitly ("Cross-provider generalization is unknown") and in the Type field ("over four million Claude.ai conversations"). The "counter-anchor for hype and over-pessimism" framing in the Relevance section is the most advocacy-flavored sentence in the draft; adversarial concern is whether this drifts into normative endorsement. **Concession-threshold rebuttal**: rated 4/5. The draft frames this as a *quantitative corrective* tied to specific findings (the 4% depth number), not a values claim, so it stays within descriptive bounds. Keep as-is, but no further normative additions. |

**Synthesis:** Source distillation is faithful, well-located, and appropriately hedged. No revisions required.
**Suggested action:** integrate.

## drafts/updates/partial-automation-principle.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The 57% augmentative / 43% automative split is exactly as the source reports [p.1, p.3]. The "lower bound" framing (because users may iterate outside chat) is the paper's own caveat [p.9]. The per-task-type concentrations (Directive in writing/schoolwork; Feedback Loop in coding; Task Iteration in front-end/professional communication; Learning in education; Validation in translation) are taken directly from [p.9–10]. The [Inference] tag on the Passalacqua-consistency claim is appropriately flagged — the data alone does not prove the principle, but they are consistent with it. |
| Practitioner | APPROVE | Sharper deployment heuristic ("certain task types pull users toward full delegation by default") is directly actionable. A consultant designing AI workflows can use this to prioritize where partial-automation scaffolding matters most (single-shot writing tasks, schoolwork, business email). |
| Adversarial | APPROVE | Strongest counter: "57% augmentative" could be misread as "AI is 57% safe" or "users have figured this out." The draft pre-empts this by labeling the inference explicitly as correlational and not causal. The note that Validation is the smallest category and concentrated in translation prevents over-reading the augmentative number as evenly distributed. No concession-threshold pushback needed. |

**Synthesis:** Solid update. No revisions required.
**Suggested action:** integrate.

## drafts/updates/human-ai-complementarity.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Skill-distribution claim (Critical Thinking, Reading Comprehension, Programming, Writing high; Installation, Equipment Maintenance, Repairing, Negotiation low) is directly from [p.7–8]. The wage/barrier-to-entry observations match [p.3, p.8–9, p.12]. The Active Listening caveat (reflects Claude's default conversational behaviors, not user intent) was acknowledged in source.md but not carried into the update — minor omission, not drift. |
| Practitioner | APPROVE | The "complementarity sweet spot is a function of human-side factors as much as task structure" framing is exactly the kind of nuance a workshop facilitator needs. It directs attention to organizational readiness and regulatory environment as adoption levers, not just technical feasibility. |
| Adversarial | APPROVE with note | Strongest counter: the entry is currently `speculative` status and uses the [Inference] frame heavily. Adding production-data anchors might tempt status promotion to `emerging` later; the update should not implicitly advocate for status change. The draft does not propose status change — good. **Concession-threshold rebuttal**: rated 5/5. The current draft only adds evidence, does not propose status promotion. |

**Synthesis:** Solid update. Optional minor improvement: include the Active-Listening caveat for fidelity. Not a blocker.
**Suggested action:** integrate.

## drafts/updates/execution-commoditization.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The ~half-of-all-usage figure for software+writing [p.1], the 37.2% Computer and Mathematical share [p.5–6], and the Directive-in-writing concentration [p.9] are accurately stated. The "implementation costs and regulatory barriers temper adoption" is a direct paraphrase of [p.12]. |
| Practitioner | APPROVE | The "current map" framing (text/code at bachelor's-degree barrier inside the commoditization zone today; physical-manipulation and high-regulatory-barrier roles outside it) is directly actionable for career advice and organizational planning. |
| Adversarial | APPROVE | Strongest counter: usage data does not equal commoditization — a high volume of AI use in writing tasks does not by itself prove that human writing labor is being commoditized in the economy. The draft addresses this implicitly by sticking to "commoditization frontier in observed usage" rather than "commoditization in labor markets." Could be sharpened with one explicit hedge that observed usage ≠ economic substitution; not a blocker. |

**Synthesis:** Solid update.
**Suggested action:** integrate.

## drafts/updates/novice-vulnerability.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The Job Zone 4 peak [p.8–9], the 37.2% Computer & Mathematical share [p.5–6], and the Directive-mode concentration in writing/schoolwork [p.9] are accurately stated. The Bastani et al. (2025) connection is the strongest claim and is appropriately flagged as [Inference] — Handa data alone do not establish skill-formation harm. |
| Practitioner | APPROVE | The convergence with Bastani's classroom finding is consultant-actionable: the same task types where the field RCT showed −17% on unassisted exam are the dominant Directive-mode use cases at population scale. This supports the "Career Stage Recommendations" already in the entry. |
| Adversarial | APPROVE with note | Strongest counter: the convergence claim could be read as "Handa proves novice vulnerability at scale" when the data only show usage patterns, not learning outcomes. The [Inference] tag and the explicit "do not establish that this usage is harmful to skill formation — it is descriptive observation, not outcome measurement" sentence handle this. **Concession-threshold rebuttal**: rated 5/5. The draft is properly hedged. |

**Synthesis:** Solid update with strong hedging on the inferential leap.
**Suggested action:** integrate.

## drafts/updates/professional-identity-threat.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The 36% / 11% / 4% depth distribution is directly from [p.7]. The "Rather than completely automating entire job roles" quote is verbatim from [p.7]. The Hai et al. within-person daily-fluctuation cross-reference is consistent with the existing entry's framing. |
| Practitioner | APPROVE | The "task-shaped at scale, not role-shaped" framing is genuinely useful for clients who fear AI is wholesale replacing their occupation. It allows nuanced advice: identify the specific tasks under pressure, anchor identity in the rest. |
| Adversarial | APPROVE | Strongest counter: depth distribution does not directly measure identity-threat — high task-share usage might or might not produce identity threat depending on which tasks are AI-mediated. The draft handles this with the [Inference] tag and the "more manageable when localized to specific tasks" qualifier. The data are anchor, not proof. |

**Synthesis:** Solid update.
**Suggested action:** integrate.

## drafts/updates/situational-disempowerment.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Methodological alignment claim (same Clio pipeline, same Anthropic team) is accurate — Sharma et al.'s methods explicitly extend Tamkin et al. 2024 / Clio, the same pipeline Handa et al. use. The 37.2% Computer & Mathematical, 10.3% ADESM, 57/43 augmentation/automation numbers are accurate. |
| Practitioner | APPROVE | The "Handa describes the *what*, Sharma describes the *how it can go wrong*" pairing is the cleanest framing of the production-data layer of the KB and useful for orientation. |
| Adversarial | APPROVE with note | Strongest counter: the inference that severe-disempowerment cases concentrate in Directive-and-Learning patterns is plausible but not directly tested — the two papers were not jointly analyzed. The draft hedges this with [Inference]. **Concession-threshold rebuttal**: rated 4/5. Acceptable hedging; could be slightly tighter ("The data do not directly establish this pairing; it is an inference from the augmentation/automation taxonomy meeting Sharma's domain-concentration findings"). Not a blocker. |

**Synthesis:** Solid update.
**Suggested action:** integrate.

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: All seven drafts (1 source + 6 UPDATEs) pass all three lenses. No AI failure-checklist findings. Optional non-blocking improvements noted (Active-Listening caveat in human-ai-complementarity update; tighter inference language in situational-disempowerment update) but not required for integration. Status `solid` on the source entry justified by sample size, methodological validation, public dataset, and team track record. Proceeding to Stage 4.5 mechanical validation.
