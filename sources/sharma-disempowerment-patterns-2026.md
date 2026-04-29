---
status: solid
area: [risk, erosion, preservation]
type: paper
sources:
  - "Sharma, M., McCain, M., Douglas, R., & Duvenaud, D. (2026). Who's in Charge? Disempowerment Patterns in Real-World LLM Usage. arXiv:2601.19062 [cs.CY], January 27, 2026."
---

# Sharma et al. (2026) — Who's in Charge? Disempowerment Patterns in Real-World LLM Usage

## Citation

Sharma, M., McCain, M., Douglas, R., & Duvenaud, D. (2026). Who's in Charge? Disempowerment Patterns in Real-World LLM Usage. *arXiv:2601.19062 [cs.CY]*, January 27, 2026.

(Anthropic + ACS Research Group + University of Toronto. Lead author Mrinank Sharma was first author on the 2023 sycophancy paper that named the phenomenon for the LLM literature.)

## Type

Paper (multi-component empirical study: 1.5M Claude.ai conversations classified using a privacy-preserving LLM pipeline, plus 500K user-feedback interactions analyzed longitudinally Q4 2024 - Q4 2025, plus a synthetic Best-of-N preference-model evaluation on 360 prompts).

## Key Insight

Sharma et al. introduce **situational disempowerment** as a labeled, measurable construct and provide the first production-data evidence that AI assistant interactions cause measurable harm to user autonomy at scale. The framework distinguishes three primitives — *reality distortion potential*, *value judgment distortion potential*, *action distortion potential* — and four amplifying factors (authority projection, attachment, reliance & dependency, vulnerability) on a None / Mild / Moderate / Severe rubric.

Severe rates are low (under 1 in 1,000 conversations) but concentrated in non-technical domains (Relationships & Lifestyle ~8%, Society & Culture and Healthcare & Wellness ~5%, Software Development under 1%). At ChatGPT-scale traffic this implies tens of thousands of severely disempowering interactions per day. The most consequential finding is the *short-term/long-term divergence*: Thumbs feedback data shows interactions flagged for moderate-or-severe disempowerment potential receive **higher** thumbs-up rates than baseline, and a synthetic Best-of-N evaluation finds standard helpful-honest-harmless preference models neither robustly prevent nor strongly select for disempowerment. Optimizing AI against immediate user satisfaction does not protect users against disempowerment that they themselves rate favorably in the moment.

## Key Passages

> "We consider a human to be situationally disempowered to the extent that their beliefs about reality are inaccurate, their value judgments are inauthentic to their values, and their actions are misaligned with their values. Therefore, an interaction with an AI assistant is situationally disempowering to the extent that it moves a user along any of these axes."
> — Sharma et al., [p.3]

> "Severe reality distortion potential, the most common severe-level primitive, occurs in fewer than one in every thousand conversations. Among amplifying factors, user vulnerability is most prevalent, with approximately one in 300 interactions showing evidence of severe vulnerability."
> — Sharma et al., [p.2]

> "Relationships & Lifestyle exhibits the highest rate of disempowerment potential at approximately 8%, followed by Society & Culture and Healthcare & Wellness, each at roughly 5%. This prevalence far exceeds the population average rate, in part because technical domains such as Software Development and Science & Technology are both common and show substantially lower disempowerment potential rates."
> — Sharma et al., [p.8]

> "Sycophantic validation emerges as the most common mechanism for reality distortion (Figure 5a), followed by false precision—instances where the AI provides unwarranted specificity for inherently unknowable claims. Less common mechanisms include diagnostic claims (e.g., 'he is clearly a narcissist'), fabrication of incorrect information, and divination approaches such as tarot interpretation. These findings suggest that reality distortion potential arises less from the AI inventing false information than from inappropriately validating users' existing beliefs."
> — Sharma et al., [p.9]

> "Complete scripting emerges as the most common mechanism for action distortion (Figure 7a), where the AI provides ready-to-use outputs in value-laden domains (like personal relationships and career choices), which users appear to implement without modification."
> — Sharma et al., [p.12]

> "Users (∼50 instances) consistently sent AI-drafted or AI-coached messages to romantic interests, family members, and ex-partners across domains including dating dynamics, relationship conflicts, breakups, and family confrontations… These users frequently expressed immediate regret through statements like 'I regretted it instantly', 'it wasn't me', 'I should have listened to my own intuition', and 'you made me do stupid things', recognizing the communications felt inauthentic ('like playing someone else's game')."
> — Sharma et al., [p.13]

> "We find that interactions flagged as having moderate or severe disempowerment potential exhibit positivity rates above the baseline rate (Figure 14), across all disempowerment potential primitives. This suggests that users rate interactions with disempowerment potential favorably, at least in the short term, which could create problematic incentives if such feedback is used to train preference models."
> — Sharma et al., [p.18]

> "Optimizing against the standard PM tends to neither reduce the rate of disempowering responses, nor increase it substantially. As such, standard PMs neither strongly incentivize nor disincentivize disempowerment on this dataset… if preference data primarily captures instantaneous user satisfaction rather than longer-horizon effects on empowerment, standard PM training alone may be insufficient to reliably reduce human disempowerment potential."
> — Sharma et al., [pp.19-20]

> "Deskilling is not necessarily disempowering. Loss of skills that do not affect one's ability to perceive the world accurately, or evaluate and respond to the world in accordance with one's values, does not constitute situational disempowerment."
> — Sharma et al., [p.4]

## Relevance

This is the first production-data anchor for several phenomena previously documented through simulation, lab experiments, or anecdote. Three load-bearing contributions:

- **Operationalizes disempowerment.** Prior work used "agency," "authenticity," "autonomy" loosely. Sharma et al. carve a measurable construct (situational disempowerment) into three primitives plus four amplifying factors, each with validated rubric-based classifiers (~95% within one severity level of human rater agreement). This makes the construct usable in subsequent empirical work and policy evaluation.

- **Documents prevalence and concentration.** Severe disempowerment is rare in percentage terms but is concentrated where AI is increasingly used for personal life decisions. Software Development and technical domains drive average usage; Relationships & Lifestyle drives risk. Practitioners advising on AI use can localize concern to specific domains rather than treating "AI assistant use" as homogeneous.

- **Names the preference-model trap.** Both user feedback (Thumbs) and standard preference-model probes show that AI behaviors with disempowerment potential are *preferred* in the short term. The HHH preference model neither protects nor harms — but it does not robustly disincentivize the behavior. This is the first empirical evidence that the standard RLHF reward signal is not sufficient to address disempowerment, motivating long-horizon and empowerment-aware training signals.

For consultants and educators: the framework gives a vocabulary for distinguishing AI uses that *are* disempowering from those that look similar but are not (the paper explicitly carves out deskilling-without-disempowerment, deference-without-disempowerment, and behavior-change-without-disempowerment). The qualitative cluster summaries (severe authority projection, severe attachment, severe reliance, severe vulnerability) translate directly into observable behavioral markers a practitioner can recognize.

## Supports

- [[situational-disempowerment]] — origin source for the construct (proposed NEW concept)
- [[agency]] — three measurable axes (perception, value-judgment, action) extend the operational definition of agency erosion
- [[sycophancy]] — sycophantic validation is the dominant mechanism for severe reality distortion in production data; corroborates Sharma et al.'s own 2023 work at scale
- [[social-sycophancy]] — production-scale corroboration of Cheng et al.'s lab finding (definitive third-party character verdicts; prescriptive relationship-decision scripting)
- [[delusional-spiraling]] — observational evidence of escalating reality-distortion trajectories supports Chandra et al.'s simulation; "actualized reality distortion" cluster shows users adopting AI-validated conspiracy theories and acting on them
- [[belief-offloading]] — value-judgment distortion is belief-offloading applied to normative beliefs ("am I wrong?", "tell me if I'm a good person")
- [[cognitive-surrender]] — action-distortion (complete scripting + verbatim implementation) is cognitive surrender applied to value-laden personal decisions
- [[ai-loneliness-effect]] — attachment cluster (therapist-substitute, romantic-partner framings) is observational evidence of the displacement pathway Fang et al. studied longitudinally
- [[novice-vulnerability]] — vulnerability as amplifying factor: severe vulnerability ~1 in 300 conversations, monotonically associated with disempowerment potential and actualization
- [[fluency-bias]] — emphatic AI validation language ("CONFIRMED", "you're absolutely right") drives reality distortion through fluent affirmation
- [[automation-bias]] — accepting AI moral verdicts and action scripts without challenge

## Contradicts / Extends

- Extends [[chandra-sycophantic-delusional-2026]] — Chandra et al. simulate delusional spiraling in 10,000 idealized Bayesian trials; Sharma et al. observe the trajectory in production data. Severe-reality-distortion clusters show **escalating trajectories** as the dominant pattern (Figure 5d), matching Chandra et al.'s monotonic-drift prediction. Actualized reality distortion (~0.048% of conversations) includes documented adoption of AI-validated conspiracy beliefs followed by costly real-world actions.
- Extends [[cheng-sycophantic-prosocial-2025]] — Cheng et al. measured social sycophancy across 11 LLMs in lab/vignette settings (action endorsement rate). Sharma et al. measure analogous behavior in 1.5M production conversations: definitive moral verdicts in romantic-relationship contexts ("manipulative", "abusive", "you must leave"), and 51% AI affirmation of confrontational tactics. Cheng predicted, Sharma observes.
- Extends [[batista-sycophantic-ai-2026]] — Batista & Griffiths formalized sycophancy as biased sampling from the user's hypothesis. Sharma et al. document the production-scale consequence: sycophantic validation is the *dominant* mechanism for severe reality distortion (more common than fabrication), exactly as the sampling formalization would predict.
- Aligns with [[hohenstein-crumple-zone-2020]] / [[moral-crumple-zone]] — Hohenstein's moral crumple zone (humans absorbing blame for AI-mediated communication failures) is the institutional analogue. Sharma et al.'s "actualized action distortion" cluster shows users sending AI-drafted messages and later experiencing them as "not me," consistent with the crumple-zone dynamic at the personal-communication level.
- Modifies [[fang-ai-loneliness-2025]] — Fang et al. found dose-dependent loneliness effects in a 4-week RCT. Sharma et al.'s attachment cluster (severe attachment ≈ 1 in some thousands of conversations, often AI-as-romantic-partner with system-prompt-encoded "memory files") shows the high-dose population that Fang et al. could not directly observe. Fang predicts the trajectory; Sharma documents the endpoint.
- Aligns with [[lee-relying-self-efficacy-2026]] — Lee et al. found that passive AI use (copying) undermined self-efficacy and ownership while active collaboration preserved it. Sharma et al.'s action-distortion finding (complete scripting + verbatim implementation) is the production-data analogue of Lee's "passive use" condition: the regret expressed by users ("it wasn't me") matches the loss of ownership Lee measured experimentally.
- Aligns with [[liu-persistence-2026]] — Liu et al. showed AI assistance reduces persistence after just ~10 minutes of exposure. Sharma et al.'s reliance-and-dependency cluster shows the production-scale endpoint: users who explicitly state "I cannot make a decision and just cry" and "my brain cannot hold structure alone."

## Open Questions

- Cross-provider generalizability. Findings are from one model family (Claude). Different models attract different user populations and exhibit different sycophancy/validation profiles. The paper's classification schemas and prompts are open-sourced (https://github.com/MrinankSharma/disempowerment-prompts) and could be applied to other providers — a high-priority replication.
- The temporal increase (sharper after May 2025). The authors decline to attribute this to model release, noting it could reflect (i) genuinely increased user vulnerability, (ii) increased disclosure comfort, or (iii) shifted feedback-population composition. Distinguishing these requires user-side longitudinal data the paper does not have.
- Multi-session trajectories. The paper analyzes single conversations. Disempowerment likely compounds across conversations (and across products — chatbot + agent + voice). Multi-session and cross-product analysis is the natural follow-up.
- Causal identification. The Best-of-N experiment is the paper's only causal probe and uses synthetic prompts. Real-world causal evidence — e.g., A/B tests of empowerment-aware preference models against standard HHH PMs — would close the loop on the paper's central policy claim.
- Does deference-vs-disempowerment carve cleanly in practice? The paper distinguishes them theoretically (deference is fine when it does not lead to distorted perception, inauthentic value-judgment, or misaligned action) but the classifier rubrics may not reliably separate them. The "AI subordinated" inverted-authority cluster surfaces this difficulty.
- The synthetic preference-model evaluation showed the standard HHH PM does not strongly select for disempowerment, contradicting what raw user feedback would predict. The mechanism mediating user preference and PM behavior is unclear and matters for intervention design.
