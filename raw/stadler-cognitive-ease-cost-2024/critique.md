# Self-Critique: Stadler, Bannert & Sailer (2024) — Cognitive Ease at a Cost

## Overall: READY

All drafts pass the three lenses and the AI-failure checklist. Two minor revision points noted in the table below; neither is blocking.

## AI Failure Checklist

- [x] **Hallucinated citations** — All citations match the source. Authors verified: Stadler (LMU Munich), Bannert (TUM), Sailer (Augsburg). DOI verified: 10.1016/j.chb.2024.108386. Klepsch et al. (2017) cognitive-load scale: cited in source [p.4]. Kammerer et al. (2021): cited as the paradigm being extended [p.1]. Sweller (2011, 2024): cited [p.2]. Chi & Wylie (2014) ICAP framework: cited [p.5]. No fabricated references.
- [x] **Methodology fabrication** — All method descriptions match the source. N=91 (92 enrolled, 1 excluded for protocol violation): [p.3]. Between-subjects RCT with random assignment: [p.3]. Klepsch et al. 7-statement CLT scale: [p.4]. Two-rater coding with κ = 0.92 / 0.89: [p.4]. ANCOVA controlling for prior knowledge: [p.4]. Mediation analysis using jAMM module (Gallucci, 2020): [p.4]. All accurately reported in drafts.
- [x] **Statistical drift** — All numbers match the source within rounding. ECL η² = 0.09, ICL η² = 0.15, GCL η² = 0.27: source [p.4, Table 2]. Justification quality 1.87 (web) vs. 1.20 (LLM), F = 11.18, p = .001, η² = 0.11: source [p.4, Table 2]. Mediation: β = 0.15, p = .020 indirect; β = 0.19, p = .095 direct: source [p.5]. H3 χ²(2) = 1.78, p = .411: source [p.5]. Table 1 means (ICL = 3.81, ECL = 3.49, GCL = 3.99): source [p.2]. All verified.
- [x] **Conflated constructs** — Germane cognitive load is correctly distinguished from intrinsic and extraneous load throughout. Drafts do not conflate "germane load" with "metacognitive engagement" — instead they note the operational convergence (different scales, same disengagement). Drafts do not conflate "cognitive ease" with "fluency bias" — they note that fluency bias is the perceptual side and germane load reduction is the cognitive-load-theory side of the same phenomenon.
- [x] **Status overstatement** — Source distillation set to `status: solid` (peer-reviewed CHB 2024, mediation analysis, replicates and extends prior work, large effect sizes). The UPDATE drafts do not promote any concept's status; they add evidence at the level the existing entry already operates at.
- [x] **Broken wikilinks** — Verified against `concepts/` and `methods/`: [[fluency-bias]] ✓, [[desirable-difficulty]] ✓, [[cognitive-debt]] ✓, [[metacognitive-laziness]] ✓, [[performance-paradox]] ✓, [[cognitive-friction]] ✓, [[cognitive-offloading]] ✓, [[capacity-erosion]] ✓. Source-entry links: [[kosmyna-cognitive-debt-2025]] ✓, [[bastani-guardrails-math-rct-2025]] ✓, [[fan-metacognitive-laziness-2025]] ✓, [[anderson-homogenization-2024]] ✓. Self-link [[stadler-cognitive-ease-cost-2024]] will resolve once the source file is integrated in Stage 5. validate_drafts.py will catch any I missed.
- [x] **False novelty** — The drafts explicitly decline to introduce a NEW concept. The paper's "cognitive ease at a cost" framing is acknowledged as descriptive of a pattern already named across multiple existing entries. distill.md justifies the decision in the "Notes on Conservative Decisions" section.

## drafts/source.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The Klepsch et al. (2017) CLT scale is well-validated; internal consistencies in this paper (McDonald's Omega 0.69-0.78) are acceptable for short scales but on the lower end. The mediation analysis is appropriate (Hayes-style with bootstrapped indirect effect via jAMM). The "full mediation" framing is technically supported (indirect path significant, direct path not significant after controlling for the mediator), but the paper notes "this analysis is dependent on the results of H2, which we can only test exploratively" [p.3] — i.e., the mediation is exploratory, not pre-registered. Draft already labels the mediation as the central finding without overclaiming pre-registration; this is honest. The N=91 is small for a mediation; a robust test would want N>200 with bootstrapped CIs visible. The draft's "Open Questions" section flags this. |
| Practitioner | APPROVE | The 7am-before-client-meeting test passes. "Cognitive ease at a cost" is plain English. The mediation finding is summarizable as "what gets bypassed when AI is easy is exactly the active processing that builds quality" — this is workshop-ready. Draft avoids CLT jargon overload; germane load is explained as "active schema-construction processing" rather than left unexplained. |
| Adversarial | APPROVE with note | Strongest counter: ChatGPT-3.5 (April–May 2023) is now ancient by LLM standards. Modern LLMs (GPT-4o, Claude 3.5+) cite sources, perform retrieval, structure step-by-step reasoning. The "lower cognitive load" finding may not replicate at the same magnitude with modern systems. Draft handles this in Open Questions: "the absolute load levels may not [generalize], but the mediator-level finding (GCL → quality) should." This concession is honest. A second adversarial point: all participants were university students at a "prestigious German university" — high digital literacy, high reading ability. The effect may be smaller (or absent) in lower-literacy populations who derive more benefit from LLM scaffolding. Draft notes this in Open Questions. No KB-guardrail violations (no hype, no urgency, no AI-as-replacement framing). |

**Synthesis:** Source distillation is faithful to the paper, calibrated in claims, and correctly conservative on novelty. Draft is ready for integration.
**Suggested action:** integrate.

## drafts/updates/fluency-bias.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The connection (fluency bias ↔ reduced cognitive load) is conceptually sound: both describe the felt-easiness of fluent output translating into reduced effortful engagement. The draft does not overclaim a *causal* equivalence between perceptual fluency (Reber & Schwarz) and germane cognitive load (Sweller); it positions Stadler as providing CLT-anchored evidence of the same downstream pattern. |
| Practitioner | APPROVE | Appendable to the entry without disrupting flow. The new paragraph follows the existing "Processing Fluency Mechanism" section coherently. |
| Adversarial | APPROVE | Possible critique: fluency bias is specifically about *perceived truth/quality* of fluent statements, while Stadler measures *cognitive load during search*. The mechanisms overlap but aren't identical. Draft handles this by stating Stadler "names what fluency bias does in cognitive-load terms" — i.e., a translation, not an equivalence. Acceptable framing. |

**Synthesis:** Adds a peer-reviewed empirical leg the entry currently lacks at the CLT level.
**Suggested action:** integrate.

## drafts/updates/desirable-difficulty.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Direct alignment: search engines impose more cognitive load (the "difficulty"), and produce better outcomes. Germane CL is the CLT-side label for what desirable difficulty engages — this connection is established in the CLT literature (Sweller et al. 2019; the Stadler paper itself cites this). |
| Practitioner | APPROVE | Strengthens the case for "AI removes difficulty, that's its risk" with a clean mediator-level finding. |
| Adversarial | APPROVE | Potential critique: desirable difficulty is about *long-term retention/transfer*, while Stadler measures same-session output quality. These are related but distinct outcomes. Draft does not claim Stadler measures retention. The mediator (GCL) is what desirable difficulty engages; quality is the immediate downstream consequence. The retention claim would need Bastani-style design. Draft honest about this. |

**Synthesis:** Strengthens the CLT-mechanism account already in the entry (via Lodge & Loble paragraph).
**Suggested action:** integrate.

## drafts/updates/cognitive-debt.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The debt-mechanism description in the existing entry is loop-based (use → reduced engagement → weaker skill → more reliance). Stadler doesn't measure the loop, but pins down what gets reduced in step 2 (germane load). The draft is clear: "single-session design cannot measure debt accumulation over time, but it isolates what the offloading is offloading." |
| Practitioner | APPROVE | Plain-language framing maintained. |
| Adversarial | APPROVE | Potential critique: cognitive debt is fundamentally a *longitudinal* construct (debt accumulates). A single-session study cannot directly evidence debt. Draft does not claim it does — it frames Stadler as evidence for the *mechanism step* (reduced germane load), not for accumulation. This is calibrated. |

**Synthesis:** Adds CLT-mechanism evidence to a loop-mechanism entry without overclaiming.
**Suggested action:** integrate.

## drafts/updates/metacognitive-laziness.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | REVISE | The phrasing "Three independent operationalizations now point at the same underlying phenomenon" is true but slightly oversells the connection. Reduced germane CL is *one operationalization* of disengagement; reduced metacognitive transitions (Fan) is *another*; crutch behavior in interaction logs (Bastani) is *a third*. They are convergent but measure different things — GCL is a self-report subjective load; Fan's measure is a behavioral process trace; Bastani's is an interaction-log inference. The draft already says "different operationalizations of the same underlying disengagement," which is correct. The "three independent operationalizations" sentence is OK on second reading; it does not claim equivalence, just convergence. APPROVE on review. |
| Practitioner | APPROVE | Maintains existing voice. |
| Adversarial | APPROVE | Potential critique: germane load is not metacognition per se. CLT and metacognitive theory are distinct (though related) frameworks. Draft does not claim GCL is metacognition; it claims reduced GCL is the *operational signature* of metacognitive bypass. This is a careful framing — the bypass produces the load reduction, observed via the CLT scale. Acceptable. |

**Synthesis:** Strengthens the entry with a third measurement-method line of evidence.
**Suggested action:** integrate (no revision needed; the second-pass read confirmed the framing is calibrated).

## drafts/updates/performance-paradox.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The "within-session paradox" framing is accurate and complementary to the existing scaffolded-vs-unassisted paradigm. Stadler measures the cognitive-load layer; Bastani measures the post-task-performance layer. Both confirm the dissociation. |
| Practitioner | APPROVE | Adds a layer ("within-session," not just "across-session") that practitioners can recognize from their own AI use without needing a longitudinal frame. |
| Adversarial | APPROVE | Potential critique: the performance paradox in the existing entry is specifically *about scaffolded performance vs. durable learning*. Stadler doesn't measure durable learning. Draft handles this by being precise: "within-session" means same-session output quality vs. same-session cognitive load — not retention. The paradox is sharpened (a within-session form exists) without being conflated with the across-session form (Bastani's −17% exam result). |

**Synthesis:** Adds a new layer of within-session paradox evidence without conflating with longitudinal paradox.
**Suggested action:** integrate.

## drafts/updates/cognitive-friction.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The phenomenological framing in the existing entry (Nosta 2026: "Meaning has never been free; it emerges through cost") is now backed by a CLT measurement of that cost. Coherent extension. |
| Practitioner | APPROVE | Plain language preserved. |
| Adversarial | APPROVE | Potential critique: the paper does not use the term "friction." Drafts that introduce a paper into a concept should preserve the source's own terminology where possible. Draft handles this by translation rather than projection: "the felt friction of having to discriminate sources, integrate fragments, and evaluate claims." This is editorial framing of what the search-engine condition required, not a claim that Stadler used the friction vocabulary. Acceptable. |

**Synthesis:** Adds CLT-side measurement to a phenomenologically-framed entry.
**Suggested action:** integrate.

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: Overall READY. All seven drafts pass three lenses and the AI failure checklist. No blockers. One revision point on the metacognitive-laziness draft was reviewed and judged not to need a change (the framing is calibrated on closer reading).
