---
status: solid
area: [erosion, risk, preservation]
type: paper
sources:
  - "Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Marimane, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences, 122(26), e2422633122."
---

# Bastani et al. (2025) — GenAI Without Guardrails Can Harm Learning

## Citation

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Marimane, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences*, 122(26), e2422633122.

**DOI:** [10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122)

**Preregistered:** [aspredicted.org/4DL_Q3J](https://aspredicted.org/4DL_Q3J)

## Type

Paper (preregistered field RCT; ~1,000 students across 50 classrooms in a large Turkish high school, Fall 2023-24; classroom-level randomization across three arms, four sessions covering ~15% of math curriculum)

## Key Insight

Bastani et al. provide the strongest field-experimental evidence to date that **unfettered AI access can harm learning**, and that **prompt-level guardrails substantially mitigate the harm**. The core experiment compares three arms while students study math:

| Arm | Practice (assisted) vs. control | Exam (unassisted) vs. control |
|---|---|---|
| **GPT Base** (vanilla ChatGPT-style) | **+48%** (p<0.01) | **−17%** (p<0.05) |
| **GPT Tutor** (teacher-curated prompts) | **+127%** (p<0.01) | **−0.4%** (n.s., effectively zero) |

The structure of this result is the central finding: GPT Base produced large performance gains *while access was available* and a statistically significant performance *deficit* once it was removed. Students who had no AI at any point outperformed students who had AI during practice but not during the exam. The 17% deficit is the magnitude of the AI-induced learning harm under default deployment conditions.

The paper's mechanism analysis distinguishes two pathways:
1. **Hallucinations mislead learners.** GPT Base makes math errors at non-trivial rates (Fig. 2 documents per-problem error rates from repeated queries). Wrong answers from the tutor could degrade subsequent unassisted performance.
2. **Crutch behavior.** Students treat AI as a way to bypass the learning, asking "What is the answer?" and copying solutions, missing the cognitive work that builds skills.

Two analyses (per-problem error-rate × subsequent performance correlation, plus message-classification of student↔AI exchanges) jointly support **crutch behavior as the dominant mechanism**. The hallucination pathway is real but secondary.

GPT Tutor's design implements two specific guardrails:
- **Solutions in the prompt** — eliminates hallucination-on-answer (the AI knows the right answer)
- **Hint-not-answer behavior** — instructed to provide step-by-step guidance and refuse direct solutions; embedded with common student-mistake patterns and corresponding hint sequences

Both are necessary: solutions-only would leave the crutch pathway open; hint-only without verified solutions would leave hallucination open. The field result shows these in combination essentially eliminate the learning deficit (point estimate −0.4%, statistically equivalent to control).

The most striking secondary finding: **students did not perceive that they had learned less.** GPT Base students reported similar self-assessed learning to controls, and GPT Tutor students reported they had learned *more* — despite no exam-score advantage. Performance/learning dissociation is invisible to the learner. This adds an [[confidence-competence-gap]] dimension that compounds the structural harm: even if students wanted to self-correct, they have no internal signal that something is wrong.

For human thinking with AI: this is the cleanest field-experimental case-study of the [[performance-paradox]] in the KB, with concrete effect sizes (-17%) and a clean intervention contrast (guardrails as a structural counter-measure). It also operationalizes the [[metacognitive-laziness]] mechanism Fan et al. (2025) demonstrated in lab conditions — the same pattern reproduces at field scale across nearly 1,000 students.

## Key Passages

> "Without guardrails, students attempt to use GPT-4 as a 'crutch' during practice problem sessions, and subsequently perform worse on their own. Thus, decision-makers must be cautious about design choices underlying generative AI deployments to preserve skill learning and long-term productivity."
> — Bastani et al., [p.1, abstract]

> "On the exam, students in the GPT Base arm perform statistically significantly worse than students in the control arm by 17%; this negative effect is essentially eradicated in the GPT Tutor arm, though we still do not observe a positive effect."
> — Bastani et al., [p.2]

> "An analysis of student interactions shows that students often use GPT Base as a 'crutch' by asking for and copying solutions, but they use GPT Tutor in more substantive ways like asking for help or independently attempting answers. Finally, we find evidence that students do not perceive any reduction in their learning or subsequent performance as a consequence of copying solutions, suggesting they are not aware of how generative AI can impede their learning."
> — Bastani et al., [p.2]

> "These results demonstrate an inherent tradeoff in access to generative AI tools: While these tools can substantially improve human performance when access is available, they can also degrade human learning (particularly when appropriate safeguards are absent), which may have a long-term impact on human performance."
> — Bastani et al., [p.4]

> "Both GPT Base and GPT Tutor reduced grade dispersion in the assisted practice sessions, matching prior findings that generative AI assistance reduces the 'skill gap' by providing the largest benefits for the weakest students. However, we find no significant effect on HHI for the unassisted exam — i.e., the reduction in the skill gap does not persist when access to AI is removed."
> — Bastani et al., [p.4]

> "Our findings suggest that the second explanation (i.e., students using GPT Base as a crutch) is the main mechanism by which GPT Base impedes student learning."
> — Bastani et al., [p.5]

## Relevance

The cleanest field-experimental case in the KB. Three load-bearing contributions:

- **Quantifies the performance/learning dissociation.** +48% practice → −17% exam is a sharp effect-size contrast within a single experiment. Most prior evidence for the [[performance-paradox]] is either lab-scale (Fan et al. 2025) or qualitative; Bastani delivers the first large-scale field measurement of magnitude.
- **Operationalizes guardrail design.** GPT Tutor's two-component design (curated solutions + hint-only prompting) is a concrete, replicable intervention pattern. This is what KB methods like [[think-first]] and [[scan]] aim at — Bastani provides field evidence that prompt-level structural design can eliminate the harm without sacrificing all of the AI's helpfulness.
- **Documents the perception gap.** Students cannot tell they're learning less. This means [[strategic-alternation]] practices that rely on self-assessment ("am I understanding this?") will fail in this population. External assessment-design counter-measures matter more than learner-side metacognitive nudges when the learners are early in skill formation.

## Supports

- [[performance-paradox]] — the strongest empirical case in the KB
- [[metacognitive-laziness]] — Bastani's field analogue of Fan et al.'s lab demonstration
- [[novice-vulnerability]] — high-school math students are canonically novice; the harm distribution is broadly uniform, not concentrated in any subgroup
- [[cognitive-offloading]] — "crutch behavior" is the operational signature
- [[confidence-competence-gap]] — perception/performance mismatch on self-assessed learning
- [[capacity-erosion]] — durable skill loss from a single semester's deployment
- [[desirable-difficulty]] — Bjorks' framework explains why bypassing struggle in practice degrades exam performance
- [[fluency-bias]] — AI's coherent answers feel like understanding
- [[automation-bias]] — paper explicitly invokes the autopilot analogue (FAA recommended limiting autopilot use precisely to preserve pilot skill)

## Contradicts / Extends

- Aligns with [[fan-metacognitive-laziness-2025]] — Fan demonstrated metacognitive laziness in a 117-student lab task; Bastani replicates the pattern at ~1,000-student field scale across an entire curriculum unit.
- Aligns with [[kosmyna-cognitive-debt-2025]] — Kosmyna et al. measured neural correlates (lower brain connectivity in LLM users); Bastani measures behavioural and performance correlates of the same phenomenon.
- Anticipated by [[bjork-desirable-difficulties-2011]] — the Bjorks predicted that performance and learning dissociate when difficulty is removed; Bastani is a direct field test of that prediction in an AI context.
- Aligns with [[parasuraman-riley-automation-1997]] — Bastani explicitly cites the autopilot literature: the FAA's recommendation to minimize autopilot use to preserve pilot skill is the classical analogue. Same vicious-circle logic, different substrate.
- Modifies [[strategic-alternation]] — alternation alone may not work for novices because they cannot self-detect the dissociation. Structural counter-measures (guardrails, assessment design) become primary; alternation is supplementary.
- The skill-gap-reduction-doesn't-persist finding extends [[dellacqua-jagged-frontier-2023]] and refines [[leveling-effect]] — Dell'Acqua found AI helps lower performers most while AI is present; Bastani shows the leveling effect evaporates when AI is removed.

## Open Questions

- The 17% deficit is measured after a single semester. Is the harm cumulative across years, or does it stabilize? Longitudinal follow-up would distinguish "temporary scaffolding cost" from "durable skill atrophy."
- The GPT Tutor guardrails neutralized harm but did not produce learning *gains* over control. What design adds positive learning effects beyond harm-mitigation? The paper hints at "students with AI could check their answers" as a partial benefit; explicit pedagogy-aware prompt design (Socratic, error-anticipation, self-explanation) is the obvious next direction.
- The field setting is high school math with teacher-curated prompts. The crutch mechanism likely operates in adult professional contexts (e.g., coding, writing, analysis) but with different perception structures — adults may have better calibration of what they don't know. Replication in professional contexts is needed.
- The "students don't perceive they learned less" finding is striking but the perception measurement was self-report. What behavioral measure of perception would corroborate it (e.g., choice between AI access vs. no-AI access for upcoming exam-like tasks)?
- Guardrail design is labor-intensive (problem-specific prompts curated by teachers). Can the design pattern be generalized — e.g., LLM-assisted curation of teacher prompts? The scaling question is operationally critical.
