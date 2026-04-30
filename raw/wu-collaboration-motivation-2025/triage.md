# Triage: wu-collaboration-motivation-2025

## Source

- Slug: `wu-collaboration-motivation-2025`
- Type: `article` (peer-reviewed paper in *Scientific Reports*)
- Format: PDF, 30 pages, 21,187 words
- Path: `raw/wu-collaboration-motivation-2025/source.md` (extracted), `raw/wu-collaboration-motivation-2025/original.pdf` (binary)
- Citation: Wu, S., Liu, Y., Ruan, M., Chen, S., & Xie, X.-Y. (2025). Human-generative AI collaboration enhances task performance but undermines human's intrinsic motivation. *Scientific Reports*, 15, 15105. https://doi.org/10.1038/s41598-025-98385-2

(Note: source_type was auto-tagged "article" by the extractor's heuristic because the file routed through the article path; the work is technically a peer-reviewed empirical paper. Treat as a paper for distillation purposes.)

## Summary

Wu et al. report four pre-registered online experiments (total N = 3,562, Prolific UK) testing the dual effects of human–GenAI collaboration on text-based professional tasks: drafting promotional Facebook posts, performance reviews, welcome emails, and brainstorming creative ideas. Studies 1–3 use a Collab-Solo vs. Solo-Solo design; Study 4 expands to a 2 × 2 between-subjects design adding Collab-Collab and Solo-Collab conditions to disentangle transition effects from steady-state effects. Across studies, three psychological measures — sense of control, intrinsic motivation, and feelings of boredom — are taken after each task on 7-point Likert scales.

The findings consistently show a **double-edged sword**: GenAI collaboration enhanced immediate task quality (modest in Study 1; large in Study 2 LIWC measures, d = 1.50 word count), but the augmentation effect did *not* spill over to subsequent solo tasks (negligible effect sizes in Studies 2–4 across idea quantity, novelty, usefulness; Study 4 even showed slightly *worse* solo Task 2 length after collaboration). Meanwhile, transitioning from Collab to Solo produced a robust pattern: increased sense of control (regained autonomy), decreased intrinsic motivation (medium effect, d ≈ -0.32 to -0.51), and increased boredom (medium effect, d ≈ 0.45 to 0.51). Study 4 sharpens this: Solo-Collab transitions caused the *largest* drop in sense of control (d = 0.84), confirming the autonomy threat is about the presence of AI, not just task transition.

The paper is empirical and quantitative, anchored in Self-Determination Theory (autonomy/competence/relatedness needs). Authors are at Zhejiang University School of Management; published open-access in a high-volume Nature journal. Limitations: Prolific samples (not real workplace dynamics), only two consecutive tasks (no long-term arc), low-reliability boredom scale in Study 1 (Cronbach's α = 0.41–0.51, replaced in Study 2), no curvilinear test of intrinsic motivation.

## Relevance

- Risk: yes — documents that GenAI collaboration measurably erodes intrinsic motivation and increases boredom across four large pre-registered experiments. Sister-study territory to [[hai-dark-side-collaboration-2025]] but with within-subjects experimental causal evidence rather than ESM correlation.
- Erosion: yes — the "psychological deprivation effect" the authors name is a specific, measurable face of motivational erosion: Collab-to-Solo transitions reduce intrinsic motivation more than Solo-to-Solo, with medium effect sizes (d ≈ 0.32–0.51 across three studies).
- Preservation: partial — the authors recommend that "AI system designers should emphasize human agency in collaborative platforms" and that workers can "actively craft their jobs between collaboration with AI and independent work" — which converges with [[strategic-alternation]] and the broader preservation cluster.
- **Relevance**: HIGH

## Quality

- Evidence basis: HIGH. Four pre-registered experiments, total N = 3,562, replicated across distinct task types (Facebook post, performance review, welcome email, AUT, product brainstorm). Effect sizes reported throughout with 95% CIs. Mixed-design repeated-measures ANOVAs with proper interaction tests. Study 4's 2 × 2 design rules out task-type and order confounds.
- Originality: MEDIUM-HIGH. The "performance augmentation + psychological deprivation" frame is novel as a paired construct. Prior KB sources cover the augmentation half (productivity gains) and the deprivation half (alienation, identity threat, self-efficacy erosion) but not the *spillover absence* + *transition asymmetry* combination. The Solo-Collab > Collab-Solo finding (sense-of-control drop is sharpest when transitioning *into* AI) is a fresh empirical contribution.
- Comparison: closest to [[hai-dark-side-collaboration-2025]] (within-person field ESM of GenAI → alienation), [[lee-relying-self-efficacy-2026]] (passive vs. active mode of use, post-AI carry-over of efficacy/meaning loss), [[mascanero-proximal-collaboration-2026]] (proximity as moderator of innovation outcomes), [[nosta-ai-rebound-2025]] (post-AI performance drop). Wu et al. complement Lee et al. on the *post-AI carry-over* dimension and Hai et al. on the *motivation-erosion* dimension — both methodologically distinct (lab experiment with task transition vs. ESM field; vs. real workplace with daily fluctuation).
- **Quality**: HIGH

## Extractable Elements

- **Concepts**: candidate NEW: `psychological-deprivation-effect` (the Wu et al.-named construct: sense-of-control changes, intrinsic-motivation decline, boredom increase across Collab→Solo transitions). UPDATE territory rather than NEW; the construct is closely related to [[ai-self-efficacy-erosion]], [[ai-rebound-effect]] (via Nosta), and [[professional-identity-threat]]. Per librarian playbook for type=article (default extraction is source distillation only, new concepts only when genuinely novel), I will *not* create a new concept entry. The findings extend several existing concepts via UPDATEs.
- **Methods**: none. The paper does not introduce a structured framework or protocol; the "Collab-Solo vs. Solo-Solo" design is a study procedure, not a method to teach practitioners.
- **Claims**:
  - GenAI collaboration enhances immediate task quality but does not spillover to subsequent unassisted tasks
  - Collab→Solo transition: ↑ sense of control, ↓ intrinsic motivation, ↑ boredom (medium effects)
  - Solo→Collab transition: sharpest ↓ sense of control (d = 0.84) — autonomy threat is about AI presence, not task transition
  - Sustained Collab-Collab maintains stable sense of control but does not buffer motivation decline or boredom

## Recommendation

**INCLUDE**

Reason: HIGH relevance, HIGH quality, sister-study territory to [[hai-dark-side-collaboration-2025]] and complementary to [[lee-relying-self-efficacy-2026]]. Override prior DEFER decision — the workbench was held while related sources (hai, lee) were being processed; those landings now make Wu et al. fit cleanly as the experimental causal anchor for the motivation/boredom face of psychological deprivation. Per article-type playbook, default to source distillation + UPDATEs to existing concepts; do not create a new concept entry.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: Sister-study to hai-dark-side-collaboration-2025; experimental causal evidence (4 pre-registered RCTs, total N = 3,562) for the motivation-decline + boredom-increase face of psychological deprivation. Override of 2026-04-29 DEFER. Article-type extraction: source distillation + UPDATEs to existing concepts; no new concept entries.
