---
status: solid
area: [preservation]
sources:
  - "Passalacqua et al. (2024)"
  - "Scispace Literature Synthesis (2025)"
  - "Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic."
---

# Partial Automation Principle

## What It Is

Partial automation preserves skills AND motivation better than full automation. Keeping humans engaged in part of the process—rather than automating everything—produces better long-term outcomes.

## Why It Matters

This is the strongest evidence-based principle for AI collaboration design. With a large effect size (d = 0.9), it provides confident guidance: don't automate completely even when you can.

## Key Insight

From 831-paper literature synthesis:
- Full automation → 23% worse skill acquisition vs. partial automation
- Mechanism: Partial automation maintains autonomy, cognitive engagement, and practice opportunities
- Reduced autonomy → lower motivation → less engagement → skill deficit

## The Chain

```
Full automation
    ↓
Reduced autonomy
    ↓
Lower self-determined motivation
    ↓
Less cognitive engagement
    ↓
Skill deficit over time
```

## Design Implication

When designing AI workflows:
- Keep humans involved in meaningful parts of the process
- Don't optimize purely for efficiency
- Preserve opportunities for practice and judgment
- Human-in-the-loop is not just for safety—it's for capability

## Evidence Quality

This is among the strongest findings in AI-human collaboration research. Multiple studies converge on the same conclusion with large effect sizes.

Handa et al. (2025) provide the first production-scale empirical observation that augmentative use is the dominant emergent pattern, not just the normative recommendation. In ~4M Claude.ai conversations classified into five collaboration patterns, **57% are augmentative** (Task Iteration, Learning, Validation) and **43% are automative** (Directive complete-task delegation, Feedback Loop) [p.3]. The paper's authors note that users may iterate on AI outputs outside the chat window, "suggesting that the true proportion of augmentative conversations may be even higher" [p.9] — meaning 57% is a lower bound on partial-automation behavior at scale.

The pattern is not uniform. **Directive (full-delegation) conversations concentrate in writing and content-generation tasks** (e.g., "Draft and optimize professional business email communications") and schoolwork-style tasks. **Feedback Loop conversations concentrate in coding and debugging**. **Task Iteration concentrates in front-end development and professional communication. Learning concentrates in general education and advice-seeking. Validation (smallest category) is largely confined to language translation** [p.9–10]. This gives the partial-automation principle a sharper deployment heuristic: certain task types pull users toward full delegation by default (single-shot writing requests, geometry homework), and design or workflow scaffolding may be most needed there.

[Inference] The 57/43 split is consistent with Passalacqua et al.'s d ≈ 0.9 effect for partial > full automation: if users were systematically experiencing full automation as worse for skill and motivation, we would expect them to drift toward partial-automation patterns spontaneously, which is what Handa et al. observe. This is correlational, not causal — but it is the first production-scale observation aligned with the principle.

## Related

- [[strategic-alternation]] - how to implement this
- [[cognitive-debt]] - what full automation accumulates
- [[desirable-difficulty]] - why engagement matters
- [[think-first]] - practice that applies this

## Sources

- [[passalacqua-less-ai-2024]] — Passalacqua et al. (2024)
- Scispace Literature Synthesis (2025)
- [[handa-economic-tasks-claude-2025]] — Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic.

