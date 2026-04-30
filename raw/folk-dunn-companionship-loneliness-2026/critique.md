# Self-Critique: folk-dunn-companionship-loneliness-2026

## Overall: READY

## AI Failure Checklist

- [x] Hallucinated citations: All cross-source references in drafts ([[fang-ai-loneliness-2025]], [[sharma-disempowerment-patterns-2026]], [[boyd-markowitz-human-connection-2026]], [[mira-model]], [[social-friction]], [[capacity-erosion]], [[ai-loneliness-effect]]) verified to exist in the KB. Folk-Dunn citation matches abstract and DOI. References cited in the Folk-Dunn body (Madison et al., Stein et al., De Freitas et al., Hamaker et al.) match the paper's reference list.
- [x] Methodology fabrication: Sample size (N=2,149), four-wave 4-month-interval design, RI-CLPM with social-stressor covariates, FIML estimation, lavaan in R — all verified against [p.3]–[p.5] of the source. Country composition (UK 50%, US 28%, Canada 14%, Australia 8%) matches [p.3]. Model fit indices (CFI, RMSEA, SRMR) match [p.5] and [p.7].
- [x] Statistical drift: Effect sizes verified — chatbot use → emotional isolation β = .06–.08 (paper reports W1→W2 = .07, W2→W3 = .07, W3→W4 = .08, p = .006); emotional isolation → chatbot use β ≈ .06 (W1→W2 = .06, W2→W3 = .06, W3→W4 = .06, p = .023); social connection → chatbot use β = −.07 to −.09 (W1→W2 = −.09, W2→W3 = −.08, W3→W4 = −.07, p = .004); chatbot use → connection β = −.02 to −.03, p = .369. Robustness: 5/6 significant, 6th marginal (p=.069 emotional isolation; p=.054 connection). Between-person variance: 70–73% emotional isolation, 85–89% social connection. All verified against [p.5]–[p.7] and Table 2.
- [x] Conflated constructs: The two loneliness measures are kept distinct throughout — emotional isolation (single-item Gallup-style) vs. social connection (20-item Lee scale). The umbrella term "loneliness" is used per the paper's own convention [p.2]. Substitution vs. enhancement is correctly attributed to MIRA principle 4 rather than to Folk-Dunn directly.
- [x] Status overstatement: source.md uses `status: emerging` — appropriate. The paper is not preregistered and the authors explicitly label findings exploratory. Effects are small. Cross-lagged identification assumptions only partially satisfied. All caveats reproduced in the draft.
- [x] Broken wikilinks: All `[[wikilinks]]` in drafts/source.md and drafts/updates/ai-loneliness-effect.md verified to exist as either KB entries (concepts/, methods/, sources/) or as the workbench slug being integrated. Will be confirmed by Stage 4.5 validate_drafts.py.
- [x] False novelty: No NEW concepts proposed. Distill.md ledger explicitly records (none) for concepts and methods. The contribution is framed as longitudinal observational *evidence* extending an existing concept, not as a new construct.

## drafts/source.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Effect sizes, model fit, sample composition, and authors' caveats are reproduced faithfully. The two-measures divergence is interpreted in the authors' own language (narrow within-person vs. broad trait-loaded). Causal language is hedged appropriately ("predicted later increases," "consistent with reciprocal exacerbation," "initial evidence"). The Open Questions section flags the right limits: causal direction partially identified, generalizability beyond Western Anglophone samples, modality moderators collapsed. No drift from the paper's claims. |
| Practitioner | APPROVE | Useful at 7am: a consultant reading this entry learns (a) loneliness and chatbot use track each other over months in the wild, (b) the bidirectional finding is small but robust across most analyses, (c) measurement choice matters (single-item picks up within-person change; 20-item trait scale does not). The Key Findings section is scannable and decision-supporting. The Why the Two Measures Diverge section explains the apparent contradiction without statistical jargon. |
| Adversarial | APPROVE | The strongest counter-argument is that the effects are tiny (β ≈ .06–.09) and the study was not preregistered, so the entry might overstate the strength of the evidence. Defended: the draft repeatedly flags small effect sizes, exploratory framing, the authors' own caution about p-values not surviving multiple-comparisons corrections, and partial satisfaction of RI-CLPM identification assumptions. The Key Insight paragraph and Open Questions both repeat these caveats. The framing positions Folk-Dunn as one leg of an evidence triangulation (alongside Fang and Sharma) rather than as standalone proof. No KB-guardrail violations: no hype, no urgency, no AI-as-replacement framing — the paper's own substitution language is used in a discussion of *risk* rather than inevitability. |

**Synthesis:** Faithful representation of an exploratory longitudinal study. Caveats and effect sizes preserved. The triangulation framing earns its keep.
**Suggested action:** integrate.

## drafts/updates/ai-loneliness-effect.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The proposed insertion preserves effect sizes, p-values, and the measure-dependent pattern. The triangulation across Fang (RCT, 4 weeks), Folk-Dunn (longitudinal observational, 12 months), and Sharma (production-scale cross-section) is accurately characterized — three distinct designs converging on a dose-response curve. The "does not establish causation" qualifier appears in the closing sentence. |
| Practitioner | APPROVE | A practitioner reading the updated [[ai-loneliness-effect]] learns the new evidence's role (longitudinal leg, months scale) without having to track down the source. The insertion location (after "Friction-Erosion Companion Pathway" and before "Related") preserves the entry's existing arc. Voice matches the existing entry — measured, cautious, evidence-anchored. |
| Adversarial | APPROVE | The strongest counter-argument: the UPDATE risks restating what the existing entry already implies (that the AI-loneliness-effect dose-response curve has empirical support across designs). Defended: the existing entry currently anchors on Fang (RCT) and Sharma (production data). Folk-Dunn's specific contribution is *temporal precedence in the wild*, which neither prior leg supplies. The triangulation is meaningfully strengthened, not duplicated. |

**Synthesis:** The UPDATE adds genuine evidence-base coverage (longitudinal observational leg) without bloat. Voice and structure match existing entry.
**Suggested action:** integrate.

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: AUTO mode. Overall READY: all checklist items pass; both drafts approved on all three lenses. No FLAGS, no BLOCKED. Proceed to Stage 4.5 validation.
