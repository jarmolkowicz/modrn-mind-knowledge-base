# Self-Critique: Hermann, Puntoni & Morewedge (2025) — GenAI and the Psychology of Work

## Overall: READY

All drafts pass all three lenses with minor revisions, and the AI Failure Checklist is clean. Some small concerns flagged below were addressed during drafting (status set to `emerging` for both NEW entries; `[Inference]` labels applied where synthesis goes beyond the source; theoretical-vs-empirical distinction made explicit in identity-threat-coping limitations).

## AI Failure Checklist

- [x] Hallucinated citations: clean. All cited works (Brynjolfsson 2025, Noy & Zhang 2023, Dell'Acqua 2023, Toner-Rodgers 2024, Otis 2024, Doshi & Hauser 2024, Schmitt et al. 2024, SimanTov-Nachlieli 2025, Bankins et al. 2024, Ryan & Deci 2017, Van den Broeck 2016) match real references in the source.md, with [p.N] locators preserved.
- [x] Methodology fabrication: clean. The source.md draft explicitly characterizes the paper as theoretical synthesis, not new empirical work. The five-strategy taxonomy is described as "imported from self-discrepancy research and applied analogically" — does not falsely attribute empirical demonstrations to Hermann et al. that they don't claim.
- [x] Statistical drift: clean. The single specific number cited (Brynjolfsson et al. 2025: 34% productivity gain for novice customer support workers) matches the table on [p.5] of source.md verbatim. No other numerical claims were extracted.
- [x] Conflated constructs: clean. Paradox-of-expertise explicitly differentiates from novice-vulnerability (mirror), upskilling-deskilling-paradox (within-individual), and automation-bias (different mechanism). Identity-threat-coping explicitly carves out from complementarity-framework, strategic-alternation, and think-first.
- [x] Status overstatement: clean. Both NEW entries set to `emerging` not `solid`. Source distillation set to `solid` (TiCS venue, established authors), but with explicit notes that empirical claims it makes are second-hand and inherit the quality of underlying primary sources.
- [x] Broken wikilinks: deferred to Stage 4.5 mechanical validation; the validate_drafts.py script will catch any. All wikilinks I drafted target slugs I verified exist in the KB (cross-checked against `ls concepts/` + `ls methods/` outputs taken at start of session) or against the new drafts in this workbench.
- [x] False novelty: clean. Paradox-of-expertise: searched KB for "expertise" and "paradox" — no existing entry. Confirmed via grep against existing concepts/sources during drafting. Identity-threat-coping: searched for "coping" + "compensation" + "identity threat" — no existing method covers the five-strategy taxonomy.

## drafts/source.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The synthesis-vs-primary-paper distinction is made explicit. Quotes preserve original wording with page locators. Connection to existing KB clusters (BPNT umbrella, performance-paradox, novice-vulnerability) is well-supported. Minor concern: the Open Questions section asserts that publication-bias adjustment (Bartoš et al. 2026) "may apply to AI-at-work productivity claims" — this is [Inference] from a learning-context finding to a workplace-productivity context. The framing was already labelled hedged ("may"), so acceptable as a flag for future work rather than a load-bearing claim. |
| Practitioner | APPROVE | The "BPNT diagnostic question" framing in Relevance ("which of competence, autonomy, or relatedness is being frustrated here?") gives a practitioner a single concrete handle for what would otherwise be a sprawling cluster. Productivity table is mentioned without re-listing every effect size — appropriate. The 7am-before-client-meeting test passes. |
| Adversarial | APPROVE | Strongest counter-argument: this is just self-determination theory applied to AI, and the KB doesn't really need a peer-reviewed citation to know that frustrating people's basic needs causes problems. Rebuttal: the value isn't the SDT framing per se — it's the integration of SDT with the GenAI-specific work-design literature (Morgeson-Humphrey) and the identity-threat-coping taxonomy, which together provide vocabulary the KB lacks. Also: the paper is in TiCS, which is a citable anchor for a frame the KB has been using informally. Concern noted but not blocking: a future second-source on BPNT-applied-to-GenAI would reduce the reliance on this single piece. |

**Synthesis:** Substantial source distillation appropriate for a review article that anchors multiple existing entries. Integrative framing is the contribution; underlying empirical claims are second-hand and so labelled.
**Suggested action:** integrate

## drafts/concepts/paradox-of-expertise.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The paradox is explicitly named in Hermann et al. [p.5] with the exact phrase "paradox of expertise" — not a fabricated label. The three components (overestimation of expertise, identity-skill misalignment, self-marginalization) each map to passages in the source. Status correctly set to emerging — single-source. The connection to SimanTov-Nachlieli (2025) is appropriate cross-citation; the connection to threat-to-status-and-comparative-advantage research is well-grounded. |
| Practitioner | APPROVE | The mirror-table comparison to novice-vulnerability is operationally useful. The "neither end of the skill spectrum self-calibrates" framing gives an organizational design implication (don't assume self-direction; build scaffolding) that is concrete enough to act on. |
| Adversarial | APPROVE | Strongest counter-argument: this is just garden-variety reactance to new technology, not anything specific to AI or expertise. Rebuttal: Hermann et al. specifically frame the mechanism as "self-perceived deep domain knowledge and high skill level" producing the dismissal — i.e., the *expertise* is the mechanism, not just generic technology resistance. The paradox-of-expertise label captures this specifically. Concern noted: the construct is empirically grounded in only a small number of studies (Schmitt 2024; SimanTov-Nachlieli 2025; Bankins 2024). Status: emerging is appropriate; should not be promoted to solid without independent corroboration. |

**Synthesis:** Genuine new vocabulary, distinct from neighbouring constructs, well-grounded in the source.
**Suggested action:** integrate

## drafts/methods/identity-threat-coping.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE with minor flag | The five strategies are correctly attributed to self-discrepancy research (Stinson et al. and others, cited via Hermann et al.). The mapping to BPNT three needs follows Hermann et al.'s Table 3 [p.7]. The Limitations section explicitly flags that Hermann et al. provide no GenAI-specific empirical demonstrations — this is the load-bearing honesty for an emerging-status method. Concern: the method draft includes a "What To Do" diagnostic procedure that goes beyond what Hermann et al. explicitly prescribe. The procedure is [Inference] — building on the taxonomy's vocabulary to operationalize it. The draft does not currently flag this with `[Inference]` markers. **Suggested fix:** add [Inference] to the diagnostic-procedure section header or to the introductory sentence of "What To Do." |
| Practitioner | APPROVE | The 5-step diagnostic procedure is what a practitioner would actually use. The strategy-by-need mapping table is operationally clear. The "When NOT to use" carve-out (don't classify as a substitute for engaging with the substantive concern) is the kind of guardrail that prevents the method from being wielded reductively. |
| Adversarial | APPROVE with minor flag | Strongest counter-argument: the method risks pathologizing workers — labelling a worker's response to GenAI as "escapism" or "symbolic self-completion" is a power-asymmetric move that may itself be a management failure to address legitimate concerns. The draft's Limitations section explicitly raises this ("Maladaptive strategies may also be diagnoses of organizational failure rather than worker choice — the method risks pathologizing workers who are responding rationally to under-supportive environments"). Concern is acknowledged. Second concern: the five strategies may not be exhaustive — collective bargaining (Hollywood Writers' strike, mentioned in Hermann et al. itself) doesn't fit the individual-frame. Limitations section addresses this. Both concerns are flagged in-draft. |

**Synthesis:** Method is grounded but the "What To Do" prescriptive section extends the source. Add [Inference] flag to that section.
**Suggested action:** revise (add [Inference] flag to "What To Do" section), then integrate

## drafts/updates/professional-identity-threat.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The BPNT framing is correctly attributed and grounded. The "paradox of expertise" cross-link and the "identity-threat-coping" cross-link are both to drafts in this workbench (will resolve when integrated). |
| Practitioner | APPROVE | The new paragraph adds useful framing without bloating the entry. Voice matches existing entry. |
| Adversarial | APPROVE | The existing entry already has Self-Determination Theory mentioned; the update extends it rather than introducing it. No risk of overwriting prior contributions. |

**Synthesis:** Clean, focused single-paragraph addition.
**Suggested action:** integrate

## drafts/updates/agency.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | "Algorithmic cage" is a quote-attributable phrase from Hermann et al. (citing Sand & Solberg 2024 in the original; Hermann et al. use it as a term in their text). Decoupled accountability and surveillance/monitoring claims are page-locatable. |
| Practitioner | APPROVE | The "workplace-deployment lens" framing distinguishes it cleanly from situational-disempowerment's per-interaction lens — useful operational distinction. |
| Adversarial | APPROVE | Strongest counter-argument: agency entry is already long; do these mechanisms warrant addition? Rebuttal: the workplace-deployment lens is genuinely missing from the entry, and surveillance-as-most-serious-autonomy-threat is a specific claim worth carrying. |

**Synthesis:** Targeted addition that fills a real gap (deployment-level autonomy threats).
**Suggested action:** integrate

## drafts/updates/novice-vulnerability.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The Brynjolfsson 34% claim is correctly attributed (via Hermann et al.'s Table 2, which cites Brynjolfsson et al. 2025). The simultaneous-satisfaction-and-frustration framing is accurate to the source. The [Inference] marker on the "both ends vulnerable" claim is appropriate. |
| Practitioner | APPROVE | The "both ends of skill spectrum vulnerable for opposite reasons" framing is a memorable, actionable insight for organizational design. |
| Adversarial | APPROVE | Strongest counter-argument: the U-shape claim is speculative without empirical support. Rebuttal: it's labelled [Inference], not a load-bearing factual claim. Acceptable hedge. |

**Synthesis:** Clean addition that ties novice-vulnerability and paradox-of-expertise together as mirror patterns.
**Suggested action:** integrate

## drafts/updates/ai-self-efficacy-erosion.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | "Comparison threat" and "deskilling-by-offloading" are characterizations of mechanisms Hermann et al. describe; the language is mine but the underlying mechanisms map to passages on [p.4] of the source. |
| Practitioner | APPROVE | Connecting self-efficacy erosion to the performance-paradox and cognitive-debt clusters is useful KB-cohesion work. |
| Adversarial | APPROVE | Strongest counter-argument: "comparison threat" sounds like new vocabulary I'm coining without source attribution. Rebuttal: it's used as descriptive shorthand for a mechanism Hermann et al. articulate; the paragraph attributes the framing to Hermann et al. and characterizes the mechanism in plain language. Not promoted to a separate construct. |

**Synthesis:** Reasonable extension that ties self-efficacy erosion into the wider erosion cluster.
**Suggested action:** integrate

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: All drafts pass all three lenses. One minor revision needed: add [Inference] flag to the "What To Do" section of identity-threat-coping.md to mark that the diagnostic procedure extends Hermann et al.'s framework. After that fix, proceed to Stage 4.5 mechanical validation.
