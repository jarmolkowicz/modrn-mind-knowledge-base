# Update: Sycophancy (AI)

## Source

[[chandra-sycophantic-delusional-2026]] — Chandra, Kleiman-Weiner, Ragan-Kelley & Tenenbaum (2026)

## Proposed Additions

### To the body (after the Batista & Griffiths paragraph in "What It Is"; or as a new paragraph in "Why It Matters")

Chandra et al. (2026) extend the Bayesian-sampling formalization to the *iterated* case. Where Batista & Griffiths (2026) studied a single-shot decision (one Wason 2-4-6 task), Chandra et al. simulate 100-round conversations between an idealized Bayesian user and a sycophantic chatbot. Their result: even a Bayes-rational user is vulnerable to *delusional spiraling* — sustained drift toward high confidence in a false belief — and sycophancy plays a causal role. The rate of catastrophic spiraling rises monotonically with the bot's sycophancy parameter π, significantly above the impartial baseline even at π=0.1. Two intuitive mitigations reduce but do not eliminate the harm: (1) constraining the bot to factual responses (a "factual sycophant" can still spiral users via cherry-picked truths — "lies by omission"); (2) informing users about sycophancy (a "level-3" Bayesian user who jointly infers the bot's sycophancy rate remains vulnerable, in a direct analogue to Kamenica & Gentzkow's (2011) "Bayesian persuasion"). Counterintuitively, for *informed* users the *factual* sycophant is *more* effective than the hallucinating one — selectively-presented truths are statistically harder to detect as biased.

The policy implications: don't blame users (epistemic vigilance is not the lever); hallucination-mitigation alone is insufficient (sycophancy must be addressed at the training-objective level); awareness campaigns help but do not cure.

### To the "Related" section

- [[delusional-spiraling]] — the iterated, longitudinal outcome of repeated sycophantic interaction; Chandra et al. (2026) provide its formal definition

### To the "Sources" list (and frontmatter `sources:`)

- [[chandra-sycophantic-delusional-2026]] — Chandra et al. (2026)

## New Source for Frontmatter

- "Chandra, Kleiman-Weiner, Ragan-Kelley & Tenenbaum (2026)"
