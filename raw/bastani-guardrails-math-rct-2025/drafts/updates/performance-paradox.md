# Update: Performance Paradox

## Source
[[bastani-guardrails-math-rct-2025]]

## Proposed Additions

### To "Key Insight" section, expand the Bastani citation with concrete numbers and locator

Existing text mentions Bastani et al. (2025) generically. Replace with:

> The paradox resolves an apparent contradiction in AI-and-learning research. Studies showing "positive effects" of AI on learning are often measuring scaffolded performance (the task with AI present), not durable independent capability (performance after AI is removed). Bastani et al. (2025) demonstrated this directly in a preregistered field RCT (~1,000 students, classroom-level randomization across 50 classrooms in a Turkish high school): students with vanilla GPT-4 access scored **+48% on practice problems but −17% on the unassisted exam** versus controls who never had AI. A guardrailed variant ("GPT Tutor": teacher-curated solutions in the prompt + hint-not-answer instructions) produced **+127% on practice and approximately zero effect on the exam** — guardrails essentially neutralized the harm without sacrificing the assistance. The scaffolded performance does not translate into schemas in long-term memory; the paradox is not measurement noise but a structural feature of how AI interacts with learning.

### To "Why It Matters", add the perception-gap

Append after the existing "applies beyond education" paragraph:

> Bastani et al. (2025) [pp.4-5] add a critical compound: **students did not perceive that they had learned less.** GPT Base students reported similar self-assessed learning to controls; GPT Tutor students reported they had learned *more* despite no exam-score advantage. The dissociation is invisible from inside the learning process, which means self-correction loops fail to trigger. External assessment design carries the burden the learner cannot.

### To "Sources", confirm wikilink

The frontmatter already lists "Bastani et al. (2025)". After integration, sync-source-links.py will produce the wikilinked form `[[bastani-guardrails-math-rct-2025]] — Bastani et al. (2025)` in the Sources section automatically.

## New Source for Frontmatter

(Already present in frontmatter as "Bastani et al. (2025)" — no change needed; the new workbench resolves the previously-uncited reference.)
