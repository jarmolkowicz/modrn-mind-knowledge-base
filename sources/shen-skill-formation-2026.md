---
status: emerging
area: [erosion, risk]
type: paper
sources:
  - "Shen, J.H. & Tamkin, A. (2026). How AI Impacts Skill Formation. arXiv:2601.20245v2."
---
# How AI Impacts Skill Formation

## Citation
Shen, J.H. & Tamkin, A. (2026). How AI Impacts Skill Formation. arXiv:2601.20245v2. Anthropic Fellows Program.

## Type
Paper

## Key Insight
In an RCT with 52 developers learning a new Python library, AI assistance impaired conceptual understanding, code reading, and debugging abilities (Cohen's d = 0.738, p = 0.010) — a 17% score reduction or two grade points — without delivering significant efficiency gains on average. Six distinct AI interaction patterns emerged; three that preserved cognitive engagement also preserved learning outcomes.

## Relevance
First rigorous experimental demonstration that AI-assisted task completion impairs skill formation in a professional coding context. Moves the evidence base beyond surveys and observational studies. The six interaction patterns provide actionable guidance for practitioners and educators designing AI-assisted learning.

## Key Findings

**Skill formation deficit**: AI group scored 17% lower on library-specific comprehension quiz (conceptual understanding, code reading, debugging). Effect held across all experience levels (1-3, 4-6, 7+ years of coding experience). Debugging questions showed the largest score gap.

**No significant productivity gain**: Contrary to prior studies, AI assistance did not significantly accelerate task completion. Time saved on coding was consumed by time spent composing queries and interacting with the AI assistant (some participants spent up to 11 minutes on AI interaction during a 35-minute task).

**Six AI interaction patterns**:

Low-scoring (avg quiz <40%):
1. **AI Delegation** — Wholly relied on AI to write code. Fastest completion, poorest learning.
2. **Progressive AI Reliance** — Started with questions, gradually delegated everything to AI.
3. **Iterative AI Debugging** — Used AI to debug/verify code repeatedly (5-15 queries) without building understanding.

High-scoring (avg quiz >65%):
4. **Generation-Then-Comprehension** — Had AI generate code, then asked follow-up questions to understand it.
5. **Hybrid Code-Explanation** — Asked for code generation combined with explanations.
6. **Conceptual Inquiry** — Asked only conceptual questions; resolved errors independently. Fastest among high-scoring patterns.

**Error encounters drive learning**: Control group encountered more errors during the task and independently resolved them, which improved their skill formation. The process of encountering and resolving errors is a key learning mechanism that AI bypasses.

## Supports
- [[novice-vulnerability]] - RCT evidence that AI impairs skill development across experience levels, with particular implications for those still building competence
- [[capacity-erosion]] - demonstrates that skill formation deficit occurs during AI-assisted task completion, not just through long-term disuse
- [[cognitive-offloading]] - six interaction patterns map a spectrum from full offloading (AI Delegation) to strategic engagement (Conceptual Inquiry)
- [[desirable-difficulty]] - error encounters and independent resolution are the productive struggle AI removes
- [[six-pattern-diagnostic]] - practice built on the six AI interaction patterns
- [[think-first]] - "Embrace the Error" variant grounded in the error-encounter finding
