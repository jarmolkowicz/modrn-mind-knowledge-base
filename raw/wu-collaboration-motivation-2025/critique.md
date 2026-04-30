# Self-Critique: Wu et al. (2025) — GenAI Collaboration Augments Performance, Undermines Intrinsic Motivation

## Overall: READY

All drafts pass the three lenses and the AI failure checklist. One revision applied during critique (removed dead `[[ai-rebound-effect]]` wikilink; replaced with `[[nosta-ai-rebound-2025]]`).

## AI Failure Checklist

- [x] **Hallucinated citations**: All citations in drafts trace to either (a) Wu et al. 2025 itself (verified against `source.md` page locators) or (b) existing KB sources (verified via Glob in concepts/methods/sources). No fabricated authors, no fabricated DOIs.
- [x] **Methodology fabrication**: Cross-checked draft methodology section against source.md [p.15–24]. Sample sizes (Study 1 N=352, Study 2 N=793, Study 3 N=793, Study 4 N=1,624; total 3,562) match the source. Pre-registration noted by authors. ChatGPT 3.5 via Qualtrics Web Service confirmed [p.24]. Cronbach's α values for the boredom scale (0.41–0.51 in Study 1, ≥0.87 in Studies 2–4) match the source's own reliability disclosure [p.24, p.26]. LIWC2015 dictionary use confirmed [p.26].
- [x] **Statistical drift**: Verified all effect sizes against source tables — Study 1 Task 1 d = 0.23 [p.4], Study 2 word count d = 1.50 [p.7], Study 3 word count d = 1.26 [p.11], Study 4 word count d = 1.10 [p.16]. Intrinsic motivation effects: Study 1 Collab-Solo d = -0.51 [p.5], Study 2 d = -0.32 [p.8], Study 3 d = -0.44 [p.13], Study 4 Collab-Solo d = 0.29 / Solo-Collab d = 0.42 (per [p.20] — note the directionality: paper reports decrease as positive d in Study 4 paired t-test table because of how the t-test was framed; the *direction* is decline in all conditions, magnitudes match). Sense of control Study 4 Solo-Collab d = 0.84 [p.20]. Δ values cited in Study 4 narrative (Δ = -1.01 for Solo-Collab; Δ = 0.42 for Collab-Solo; Δ = -0.15 for Solo-Solo; Δ = -0.05 for Collab-Collab) match [p.18–19]. No drift.
- [x] **Conflated constructs**: Sense of control, intrinsic motivation, and boredom kept distinct throughout drafts. The agency UPDATE focuses on sense of control (the paper's measured operationalization of perceived autonomy); the professional-identity-threat UPDATE focuses on intrinsic motivation + boredom (the paper's operationalization of meaning/engagement); the ai-self-efficacy-erosion UPDATE focuses on the within-collaboration sense-of-control suppression (the authors' framing as "perceived autonomy may diminish if they feel that AI-driven contributions override their own decision-making" [p.2]). No conflation of self-efficacy with sense of control: the paper does not measure self-efficacy directly; the UPDATE frames Wu's findings as adjacent evidence in the same SDT-autonomy cluster, not as a self-efficacy measurement.
- [x] **Status overstatement**: Source draft status is `solid` — justified by pre-registration, replication across four studies with N=3,562, and publication in *Scientific Reports* (peer-reviewed Nature journal). The paper is single-team but the within-paper replication across four studies and four task types is strong internal replication. Comparable to other `solid` source entries in the KB. No overstatement.
- [x] **Broken wikilinks**: All wikilinks in source.md and the five UPDATE drafts verified via Glob (concepts/, methods/, sources/). One initial dead link `[[ai-rebound-effect]]` was caught and replaced with the source entry `[[nosta-ai-rebound-2025]]`. All others resolve.
- [x] **False novelty**: The "no new concept" decision is conservative and correct for an article-type extraction. The paper's "performance augmentation + psychological deprivation" pairing is a useful framing but does not introduce a construct distinct from the existing KB cluster (motivation/meaning erosion already covered by professional-identity-threat, ai-self-efficacy-erosion, and the alienation-via-Hai construct). The transition asymmetry (Solo→Collab > Collab→Solo) is novel as a finding but is not itself a new *concept* — it is empirical evidence for the existing autonomy-frustration construct.

## drafts/source.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The paper is methodologically strong (pre-registered, N=3,562, replication across four task types, proper interaction tests with effect sizes and CIs throughout). The boredom scale reliability issue in Study 1 (α = 0.41–0.51) is flagged in the draft's methodology section, matching the authors' own disclosure. SDT framing is faithfully represented. The draft does not overclaim mechanism — it reports the findings and lets the reader infer mechanism within the SDT/BPNT frame already established in the KB. One minor caution: the draft's framing of Solo→Collab as "the autonomy threat is about AI presence, not just task transition" is the author's own interpretation [p.19] and is reasonable but not a settled causal claim. The phrasing in the draft preserves this nuance. |
| Practitioner | APPROVE | The findings are directly actionable for consultants and trainers: "transitioning into AI is the most autonomy-disruptive direction" and "sustained collaboration does not buffer motivation decline" are concrete, useful framings for workshop content. The Cohen's d ranges (0.32–0.51 for motivation decline; 0.84 for Solo→Collab control drop) are interpretable as "medium" and "large" effects without statistical jargon. The draft passes the 7am-before-a-client-meeting test. The Open Questions section honestly flags the Prolific-vs-real-workplace gap, which is exactly the question a practitioner would ask. |
| Adversarial | APPROVE | The strongest counter-argument is sample/setting limitations: Prolific UK respondents doing 5-minute Qualtrics tasks for £2.25 are not the same population as professionals using ChatGPT in their actual work. The motivational-decline finding may reflect "I just did a task with help, now I have to do another one without help" rather than a stable feature of GenAI collaboration. The draft addresses this explicitly in Open Questions and does not over-generalize. A second concern: the spillover-absence finding could be framed as "AI doesn't make you better long-term" but Wu et al. only test transfer to immediately following tasks, not days/weeks later. The draft is careful to say "subsequent unassisted tasks" rather than implying long-term skill transfer. No KB guardrail violations: no hype ("undermines" is the authors' own framing), no urgency ("the deprivation effect is robust" is a methodological claim with effect-size evidence), no AI-as-replacement framing. |

**Synthesis:** The source distillation is methodologically sound, faithful to the source, and adds clear value to the KB by anchoring the motivation-and-autonomy-erosion thesis with experimental causal evidence. Status `solid` is appropriate.
**Suggested action:** integrate

## drafts/updates/agency.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The Solo→Collab d = 0.84 finding is the load-bearing effect; verified against [p.20]. The "Δ = -1.01" framing is the authors' own [p.18]. The recommendation quote is verbatim from [p.23]. |
| Practitioner | APPROVE | Adds a concrete deployment-design implication (the authors' "ensure users retain a sense of control" recommendation is workshop-ready). |
| Adversarial | APPROVE | The UPDATE does not overclaim — it positions Wu et al. as experimental complement to Hai et al.'s field correlation, which is the correct epistemic move. No conflation of sense-of-control with the broader agency construct (the UPDATE explicitly says sense of control is "the autonomy core of agency"). |

**Synthesis:** Clean UPDATE that adds experimental evidence in a third design family.
**Suggested action:** integrate

## drafts/updates/professional-identity-threat.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Effect sizes verified ([p.5, p.8, p.13, p.20]). The SDT/BPNT framing is faithful to both Wu et al. and the existing entry's Hermann-anchored SDT structure. |
| Practitioner | APPROVE | The "third-design-family" framing is useful for explaining why this paper matters distinctly from Hai et al. and Lee et al. |
| Adversarial | APPROVE | One concern surfaced: identity threat is a richer construct than what Wu et al. measure (the paper measures intrinsic motivation and boredom; identity threat in the KB entry includes ownership, craftsmanship, intellectual self-concept). The UPDATE should not claim Wu measures identity threat directly. The draft phrases it as "experimental causal anchor for the motivation-and-boredom face of identity threat" — this preserves the distinction. APPROVE. |

**Synthesis:** Faithful UPDATE that respects construct boundaries.
**Suggested action:** integrate

## drafts/updates/ai-self-efficacy-erosion.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The within-collaboration sense-of-control suppression is supported [p.18–19]. The "sense of control is suppressed during collaboration" claim derives from the Solo-Collab Δ = -1.01 evidence — when participants moved into Collab, their control dropped; this *is* evidence of within-collaboration suppression. The draft is careful to position this as "adjacent evidence in the autonomy cluster" rather than a direct self-efficacy measurement. |
| Practitioner | APPROVE | Useful sharpening of the Hermann "comparison threat" mechanism with timing evidence. |
| Adversarial | APPROVE | The strongest concern: Wu et al. do not measure self-efficacy. The UPDATE should not imply they do. The draft's framing — "sense-of-control suppression operates not only after AI evaluation (Alessandro et al.) or in heavy use over time (Hermann et al.), but immediately within the worker's first session of collaborative use" — keeps the distinction clear: Wu et al. extend the autonomy/control evidence base, not the self-efficacy evidence base directly. The connection to self-efficacy is via the SDT-shared autonomy mechanism, which is what the existing entry already discusses. APPROVE. |

**Synthesis:** Tightly-scoped UPDATE that respects the construct boundary.
**Suggested action:** integrate

## drafts/updates/strategic-alternation.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The four-condition Study 4 evidence is the load-bearing piece; effect sizes verified [p.18–22]. The "alternation requires deliberate design" framing is supported by the Solo→Collab d = 0.84 finding (transitions in *both* directions carry costs). |
| Practitioner | APPROVE | Directly actionable: practitioners can use this UPDATE to refine alternation guidance from "switch modes occasionally" to "minimize transition frequency; design solo blocks for capacity-building, not random switching." Passes the 7am test. |
| Adversarial | APPROVE | The [Inference] tag is correctly applied to the design recommendation that goes beyond what Wu et al. directly tested (they did not vary transition frequency or solo-block intentionality). The draft is honest about this. The strongest counter-argument — "Wu et al.'s 5-minute Qualtrics tasks don't generalize to weeks-long work projects" — is preserved in the source distillation's Open Questions and does not need re-stating in this UPDATE. APPROVE. |

**Synthesis:** Honest UPDATE that flags inference where it operates.
**Suggested action:** integrate

## drafts/updates/performance-paradox.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | All effect sizes verified ([p.4, p.7, p.11, p.16] for Task 1 augmentation; [p.4, p.8, p.13, p.18] for spillover absence). The "three of four studies found no spillover" framing is precise — Study 1 did find positive spillover on idea quality (d = 0.29), and the UPDATE acknowledges this explicitly. |
| Practitioner | APPROVE | The contrast with Bastani's during-AI gap (+48% practice, −17% exam) is a useful complementary frame: Wu et al. show the gap *after* AI use; Bastani shows it *during* AI use. Together they describe a fuller paradox. |
| Adversarial | APPROVE | The strongest concern: the spillover-absence framing could be over-generalized as "AI doesn't help you learn." The draft is careful to scope: Wu et al. only test immediate-subsequent tasks, not delayed transfer. The framing is "the paradox extends to the post-AI dimension" — accurate and bounded. No KB guardrail violations. APPROVE. |

**Synthesis:** Clean UPDATE that complements Bastani et al.'s during-AI evidence with post-AI evidence.
**Suggested action:** integrate

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: All drafts passed all three lenses and the AI failure checklist. One dead wikilink caught and fixed during critique. No methodological, factual, or framing concerns remain. Proceed to Stage 4.5 mechanical validation.
