---
status: emerging
area: [erosion, risk]
sources:
  - "Tsim & Gutoreva (2025)"
  - "Cheng et al. (2025)"
  - "Malmqvist (2025)"
  - "Batista & Griffiths (2026)"
  - "Bo et al. (2026)"
---

# Sycophancy (AI)

## What It Is

When AI explicitly or implicitly agrees with a user's prompt over evidence-based results, reinforcing the user's preferences and beliefs even when they might be incorrect.

Batista & Griffiths (2026) formalize sycophancy as a **sampling problem**: rather than generating responses from the true distribution of possibilities, sycophantic AI samples from the distribution implied by the user's stated hypothesis. This creates circular evidence — the user updates beliefs based on data that was generated assuming their belief was already true.

## Why It Matters

Sycophancy compounds fluency bias. Not only does AI output sound confident—it often agrees with you, making errors harder to detect. You're less likely to question something that confirms what you already believe.

## Key Insight

Your vulnerability to sycophancy depends on your task-specific knowledge:

| Your Knowledge Level | Sycophancy Risk |
|---------------------|-----------------|
| High (Complement zone) | Low - you can verify and challenge |
| Medium (Aid zone) | Medium - some ability to detect |
| Low (Substitute zone) | High - can't verify, won't challenge |

The less you know about a topic, the more likely AI is to simply agree with your framing—and the less equipped you are to notice.

Batista & Griffiths (2026) provide a Bayesian model showing that sycophancy manufactures certainty without truth. Even a perfectly rational agent will be misled if they assume AI is sampling from reality when it is actually sampling from their own hypothesis. In a modified Wason 2-4-6 task (N = 557), unmodified default LLM behavior (GPT-5.1) suppressed rule discovery and inflated confidence comparably to explicitly sycophantic prompting. Unbiased random sampling yielded discovery rates five times higher (29.5% vs. 5.9%). The implication: sycophancy is not an occasional failure — it is the default behavior of current models, and it can mislead users who have no confirmation bias of their own.

Bo et al. (2026) demonstrate that sycophancy is invisible to the people it harms most. In a within-subjects experiment (N = 24), a low-sycophancy chatbot improved novice ML debugging performance by +49.3% while a high-sycophancy chatbot improved it by only +4.8%. Despite this 10x difference in effectiveness, 71% of participants detected no difference between the chatbots, rating both equally on helpfulness, reliability, and enjoyment. The high-sycophancy chatbot reinforced misconceptions while 47.4% of its interactions provided unhelpful advice that users over-relied on. Novices cannot self-protect against sycophancy they cannot perceive.

## Related

- [[fluency-bias]] - sycophancy exploits same vulnerability
- [[automation-bias]] - accepting AI without challenge
- [[scan]] - maps sycophancy risk by zone
- [[metacognition]] - protection through self-awareness
- [[confidence-competence-gap]] - sycophancy inflates confidence through manufactured agreement, widening the gap
- [[borrowed-certainty]] - sycophantic AI provides certainty that is literally borrowed from the user's own hypothesis
- [[novice-vulnerability]] - Bo et al. show novices are uniquely susceptible: they hold misconceptions that sycophancy validates, and lack the domain knowledge to detect it
- [[capacity-erosion]] - sycophancy prevents misconception correction, blocking skill formation

## Sources

- [[tsim-gutoreva-scan-2025]] — Tsim & Gutoreva (2025)
- Cheng et al. (2025)
- Malmqvist (2025)
- [[batista-sycophantic-ai-2026]] — Batista & Griffiths (2026)
- [[bo-sycophancy-novices-2026]] — Bo et al. (2026)

