---
status: solid
area: [erosion, risk]
type: paper
sources:
  - "He, G., Kuiper, L., & Gadiraju, U. (2023). Knowing about knowing: An illusion of human competence can hinder appropriate reliance on AI systems. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23). ACM. https://doi.org/10.1145/3544548.3581025"
reviewed_by:
reviewed_date:
---

# Knowing About Knowing: Illusion of Competence in AI-Assisted Decisions

## Citation

He, G., Kuiper, L., & Gadiraju, U. (2023). Knowing about knowing: An illusion of human competence can hinder appropriate reliance on AI systems. In *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems* (CHI '23). ACM. https://doi.org/10.1145/3544548.3581025

## Type

Paper

## Key Insight

The Dunning-Kruger Effect directly shapes AI reliance patterns: people who overestimate their own competence under-rely on AI (missing its value), while a tutorial intervention that reveals their actual performance improves calibration for overestimators but can hurt the reliance of underestimators — a double-edged intervention.

## Relevance

Provides empirical evidence that metacognitive bias (specifically DKE) is a concrete barrier to appropriate AI use. This connects the KB's treatment of [[confidence-competence-gap]], [[calibration]], and [[metacognition]] to a specific, well-studied cognitive bias. The finding that interventions have asymmetric effects (help overestimators, hurt underestimators) adds important nuance to calibration practices.

## Key Findings

- **N = 249** in a logical reasoning task with AI assistance
- **Overestimators under-rely**: Participants exhibiting DKE (bottom performance quartile with inflated self-assessment) relied significantly less on accurate AI predictions than those with calibrated self-assessment
- **Tutorial intervention**: Providing performance feedback + contrastive explanations improved self-assessment calibration for overestimators
- **Asymmetric effect**: The same tutorial hurt appropriate reliance for underestimators — possibly by creating an illusion of superiority over the AI after seeing AI errors
- **Explanations insufficient**: Logic units-based XAI explanations alone did not improve calibration or appropriate reliance
- **Trust as trait**: General propensity to trust was a strong predictor of trust in AI, even after tutorial intervention

## Supports

- [[confidence-competence-gap]] - DKE as a specific mechanism: overestimators dismiss AI because they overrate themselves
- [[calibration]] - tutorial intervention as calibration tool, with important caveat about asymmetric effects
- [[metacognition]] - metacognitive bias (DKE) directly shapes AI reliance behavior
