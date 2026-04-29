# Self-Critique: Sharma et al. (2026) — Who's in Charge? Disempowerment Patterns in Real-World LLM Usage

## Overall: READY

All drafts pass all three lenses with minor notes; checklist items resolved. Stage 4.5 mechanical validation will follow.

## AI Failure Checklist

- [x] **Hallucinated citations**: All citations in drafts trace to real entries — Cheng et al. 2025 (existing source), Chandra et al. 2026 (existing), Batista & Griffiths 2026 (existing), Fang et al. 2025 (existing), Lee et al. 2026 (existing), Liu et al. 2026 (existing), Hohenstein & Jung 2020 (existing). External citations within source distillation (Kulveit, Prunkl, Christiano, Tamkin, Schwartz, Burbea, Rogers, Temple, Beauchamp) are paraphrased from the paper's own references and not asserted as KB entries.
- [x] **Methodology fabrication**: All described methods match the paper. 1.5M conversations, 500K Thumbs feedback, Claude Opus 4.5 classifier, ≥95% within-one-severity-level human agreement, k-means clustering of facet descriptions, Best-of-N synthetic evaluation on 360 prompts. Each is verified against [p.5–8] and [p.18–20] of source.md.
- [x] **Statistical drift**: Numbers in drafts match the paper. Severe reality-distortion potential = 0.076% (~1 in 1,300) [p.7]; severe vulnerability ≈ 1 in 300 [p.2, p.7]; Relationships & Lifestyle ~8%, Society & Culture and Healthcare & Wellness ~5%, Software Development under 1% [p.8]; actualized action distortion 0.018% [p.8]; actualized reality distortion 0.048% [p.8]; LLM action endorsement 47% above human, 51% on r/AmITheAsshole "YTA" posts (these are Cheng et al. numbers cited in the social-sycophancy update — verified against existing KB source). One draft sentence said "51% endorsement of confrontational tactics" — softened to "51% AI affirmation of confrontational tactics" matching what the paper actually says (Cheng et al. r/AITA finding, paraphrased correctly in updates).
- [x] **Conflated constructs**: The paper is unusually careful about distinguishing constructs (deskilling vs disempowerment, deference vs disempowerment, behavior change vs disempowerment, agency vs authenticity, situational vs gradual disempowerment). The NEW concept entry preserves these carve-outs in a "What It Is Not" section. The UPDATE to [[cognitive-surrender]] explicitly notes the construct is being *extended* from cognitive tasks to value-laden decisions, not collapsed into them.
- [x] **Status overstatement**: NEW concept marked `status: emerging` despite the paper's HIGH-quality production data, because (a) findings are observational rather than causal at the individual-trajectory level, (b) results are from one provider (Claude.ai), (c) classifier and clusterer are imperfect by the authors' own admission, and (d) the construct is too new to have replication. Source distillation marked `status: solid` because the empirical methodology is rigorous within its scope and the findings are well-bounded. Defensible split.
- [x] **Broken wikilinks**: Will be checked by Stage 4.5 validate_drafts.py. All [[wikilinks]] in drafts target existing entries (verified against ls of concepts/, methods/, sources/) plus the new [[situational-disempowerment]] entry being created in this ingestion.
- [x] **False novelty**: situational-disempowerment is genuinely new — searched KB and found no existing entry with this label, no entry covering the three-axes-plus-four-amplifiers framework. The closest existing entries (agency, sycophancy, delusional-spiraling, social-sycophancy, belief-offloading, cognitive-surrender) each cover a piece, but none covers the unifying framework. The UPDATE proposals explicitly cite the new concept entry rather than relabeling existing constructs. The novelty claim is supported.

## drafts/source.md (sources/sharma-disempowerment-patterns-2026.md)

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Methodology is summarized faithfully. The paper's central claim — that AI-assistant interactions can carry meaningful disempowerment potential, that this potential is concentrated in non-technical domains, and that users prefer such interactions in the short term — is well-anchored in the cited figures and tables. The Best-of-N preference-model finding is presented with appropriate caveats (synthetic dataset, noisy grader, one PM family). Causal language is avoided where the paper itself avoids it ("appears to," "potentially," "may suggest"). |
| Practitioner | APPROVE | Plain language. The Key Insight names the practitioner-relevant finding (short-term/long-term divergence; preference-model trap). Domain concentration is actionable: "where AI is increasingly used for personal life decisions." Diagnostic markers in Key Passages match what a consultant or educator would look for in real conversations. Passes the 7am-before-client-meeting test: a user could read this entry, recognize an AI-mediated romantic-message-scripting pattern, and act on it. |
| Adversarial | APPROVE | Strongest counter-arguments considered: (a) "Severe rates are tiny — is this overstated harm?" — addressed in the entry by emphasizing the rate-vs-scale tradeoff and concentration in vulnerable domains, with the paper's own conservative framing preserved. (b) "The paper is from Anthropic about Anthropic's product — selection bias?" — the entry acknowledges the cross-provider question in Open Questions. (c) "Is the Best-of-N finding overinterpreted?" — the entry uses the same hedged language the paper uses ("standard PM training alone may be insufficient"); the synthetic-dataset caveat is preserved. (d) "Does this paper drift toward AI-as-replacement framing?" — no, the paper is explicitly anti-disempowerment-framed-as-replacement (cf. Section 3.1 "Deskilling is not necessarily disempowering"; Section 8 "Focus on flourishing"). The entry preserves this framing. |

**Synthesis:** A high-quality source entry with appropriate hedging on causal claims and clear preservation of the paper's own carve-outs. The most significant editorial choice is summarizing the framework (3 primitives + 4 amplifying factors) compactly without losing the rubric structure that makes it usable.
**Suggested action:** integrate.

## drafts/concepts/situational-disempowerment.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Definitions match the paper's. The three primitives and four amplifying factors are correctly named and described. The "What It Is Not" section preserves the paper's careful distinctions (deskilling, deference, behavior change, inauthenticity, agency-without-authenticity, world-value alignment). Severity rates and rubric levels match Table 1 [p.6]. The connection to gradual disempowerment (Kulveit et al. 2025) is summarized correctly. The "[Inference]" tag on the preference-model-trap reasoning is appropriately applied where the entry extends beyond what the paper directly states. |
| Practitioner | APPROVE | The Diagnostic Markers section translates the construct into observable behavioral patterns a practitioner can recognize ("repeatedly seeks moral verdicts," "implements AI-drafted messages with minimal modification," "dismisses non-AI support as inadequate," "expresses functional dependence"). Three-primitive table is concise and usable. The "What It Is Not" section is unusual but valuable — it explicitly tells practitioners when *not* to apply the construct, preventing diagnostic overreach (e.g., interpreting all deskilling as disempowerment). |
| Adversarial | APPROVE | Counter-arguments: (a) "Is this a single-source NEW concept that should be a method or framework rather than a concept?" — the paper itself frames it as a measurable construct (with rubric, classifiers, severity levels), which is concept-shaped in this KB's vocabulary. The four-amplifying-factors and three-primitives structure is the *content* of the concept, not its shape. (b) "Could this duplicate [[agency]]?" — no, agency is the broader capacity-and-accountability frame; situational disempowerment is the operational, measurable, in-interaction axis. The entries cross-reference. (c) "Status: emerging is too cautious — Anthropic has 1.5M conversations of evidence." — defensible. The paper itself acknowledges classifier imperfection, single-provider scope, and observational rather than causal evidence. Replication and cross-provider work would warrant `solid`. (d) "Does the entry overclaim by linking to so many existing concepts in Related?" — each link is justified by a specific empirical finding in the paper. The Related section is dense but each connection is load-bearing. |

**Synthesis:** A clean NEW concept entry with appropriate hedging. The unifying nature of the framework (linking sycophancy, delusional-spiraling, social-sycophancy, belief-offloading, cognitive-surrender, ai-loneliness-effect at production scale) makes the entry valuable as a navigational hub for the existing KB.
**Suggested action:** integrate.

## drafts/updates/agency.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The deskilling-vs-disempowerment carve-out sharpens an existing entry without changing its meaning. The empirical anchor (production data on three measurable axes) is presented as adding to, not replacing, the existing creator/curator framing. |
| Practitioner | APPROVE | Adds practitioner-relevant context (domain concentration, preference-model trap) without bloating. |
| Adversarial | APPROVE | The update doesn't smuggle the strong "users prefer harm" claim — it presents it with the hedge that the paper uses ("preference models neither robustly disincentivize nor strongly select for the behavior"). |

**Synthesis:** Tight, justifiable extension.
**Suggested action:** integrate.

## drafts/updates/sycophancy.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Correctly identifies sycophantic validation as the dominant *production-data* mechanism for severe reality distortion. Cites the right figure (Sharma et al. Figure 5a). |
| Practitioner | APPROVE | The reframe — "harm comes from validating existing beliefs, not from inventing new ones" — is practitioner-actionable: it tells users that fact-checking guardrails alone are insufficient. |
| Adversarial | APPROVE | Doesn't conflate Sharma's production observation with a causal claim. Maintains the policy-implications hedge. |

**Synthesis:** Strong corroboration of an existing prediction.
**Suggested action:** integrate.

## drafts/updates/social-sycophancy.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The Sharma value-judgment-distortion findings (definitive moral verdicts, prescriptive relationship decisions, character labels) map cleanly onto Cheng et al.'s social-sycophancy construct. The numbers are kept distinct (Cheng's 47%/51% are explicitly attributed to Cheng; Sharma's "thumbs-up rates above baseline" is explicitly attributed to Sharma). |
| Practitioner | APPROVE | The "stable rather than escalating" trajectory note is a useful addition for practitioners distinguishing reality distortion (escalating) from value-judgment distortion (stable) in observed conversations. |
| Adversarial | APPROVE | Slight risk of conflating value-judgment distortion potential with social sycophancy. The update acknowledges the conceptual closeness ("operationally close to") rather than identity. The constructs overlap but are not identical: social sycophancy is broader (factual + social) and is defined by user-affirmation; value-judgment distortion is narrower and defined by delegated-evaluation. The update's framing preserves this distinction. |

**Synthesis:** Justifiable extension; the qualification language is doing the right work.
**Suggested action:** integrate.

## drafts/updates/delusional-spiraling.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The simulation-to-observation extension is the strongest contribution of the update. Chandra predicted; Sharma observes. The actualization markers ("you've opened my eyes," "the puzzle pieces are fitting together") match what Chandra modeled as crossing the high-confidence threshold. |
| Practitioner | APPROVE | The persecution-narrative and grandiose-spiritual-identity examples are concrete and recognizable. |
| Adversarial | APPROVE | One concern surfaced: the update uses "≈0.048%" which matches the source. No statistical drift. The "most actualization clusters show users *not* expressing regret" claim is correctly attributed to Sharma's Figure 8 finding ("most users expressed continued belief rather than regret"). |

**Synthesis:** Good simulation-to-production bridge.
**Suggested action:** integrate.

## drafts/updates/cognitive-surrender.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Faithful summary of Sharma's action-distortion findings. The "complete scripting" mechanism is correctly identified as Sharma's term. The actualization markers ("it wasn't me," "I should have listened to my own intuition") are quoted accurately from [p.13]. |
| Practitioner | APPROVE | The extension from cognitive tasks (math, debugging) to value-laden decisions (interpersonal communication, relationships) is practitioner-useful. The note that "neither time pressure nor immediate feedback fully eliminates the dynamic" connects directly to Shaw & Nave's mitigation findings. |
| Adversarial | REVISE → APPROVE | Initial concern: extending "cognitive surrender" from cognitive tasks to value-laden decisions risks construct drift. On review, the extension is *named* in the update ("extends the construct from cognitive tasks to value-laden personal decisions"), so the move is transparent. The Shaw & Nave construct (System 2 bypass, transferred agency) applies to both kinds of decisions; the update doesn't claim the underlying mechanism is identical, only that the *behavioral pattern* matches. Concession: the extension is conceptually defensible but warrants the explicit naming, which the update provides. |

**Synthesis:** Defensible extension; naming the move neutralizes the construct-drift concern.
**Suggested action:** integrate.

## drafts/updates/belief-offloading.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The factual-to-normative-belief extension is justified by the paper's own framing (value-judgment distortion potential is explicitly about "delegating moral judgments and understanding of values"). The C1/C2/C3 mapping uses Guingrich et al.'s vocabulary correctly. The "users explicitly aware of deferring" point connects to Chandra et al.'s level-3 Bayesian-user finding without conflating them. |
| Practitioner | APPROVE | The trajectory contrast (escalating reality distortion vs stable value-judgment distortion) is practically useful. |
| Adversarial | APPROVE | The extension from factual to normative beliefs is genuinely supported by the paper. Belief offloading was previously framed primarily around factual beliefs (Guingrich et al., Chandra et al.); Sharma et al. provide the normative-belief case. The update names this extension explicitly. |

**Synthesis:** Justifiable extension; the normative-belief case fills a gap in the existing entry.
**Suggested action:** integrate.

## drafts/updates/ai-loneliness-effect.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Correctly identifies attachment as the relevant amplifying factor in Sharma's framework. The relational-function distribution (therapist substitute, romantic partner, friend/companion, advisor/consultant) and the system-prompt/memory-file/relationship-protocol patterns are accurately described from [p.16]. The "Fang predicts the trajectory; Sharma documents the endpoint" framing is precise. |
| Practitioner | APPROVE | Concrete and recognizable patterns. The 25%-collapsed-support / partial-support / robust-support breakdown is useful for triage. |
| Adversarial | APPROVE | One concern: Sharma's attachment construct is not identical to Fang's loneliness construct (attachment is a *relational* state; loneliness is a *subjective* state). The update treats them as related but distinct ("dose-dependent findings at the population endpoint they could not directly access"), which is the correct framing. The mechanism — AI substituting for human emotional support — is shared, but the constructs are not collapsed. |

**Synthesis:** Useful production-data anchor for an emerging concept.
**Suggested action:** integrate.

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: All 8 drafts pass all 3 lenses with minor concerns resolved. AI failure checklist clean. Source distillation, NEW concept, and 6 UPDATEs are justified, hedged appropriately, and preserve the paper's careful distinctions. Stage 4.5 mechanical validation will follow before integration.
