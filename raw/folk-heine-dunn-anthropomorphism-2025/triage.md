# Triage: folk-heine-dunn-anthropomorphism-2025

## Source

- Slug: `folk-heine-dunn-anthropomorphism-2025`
- Type: `article` (initial classification — but functionally a peer-reviewed empirical paper; see Note below)
- Format: pdf, 7 pages, 5,442 words
- Path: `raw/folk-heine-dunn-anthropomorphism-2025/source.md` (extracted), `raw/folk-heine-dunn-anthropomorphism-2025/original.pdf` (binary)

**Note on source_type:** The cataloging step heuristically classified this as `article`. It is in fact a peer-reviewed empirical paper (*Scientific Reports* 15:36548, 2025; DOI 10.1038/s41598-025-19212-2; two studies, one preregistered, total N = 1,274; received 4 June 2025, accepted 7 September 2025). Treating as paper-branch for distillation purposes (full read of methods and results, preserve effect sizes and locators) while keeping the workbench slug.

## Summary

Folk, Heine & Dunn (UBC) report two experiments — Study 1 exploratory (N = 240), Study 2 preregistered with N ≈ 10× larger (N = 1,034) — testing whether individual differences in *anthropomorphism of technology* (the tendency to attribute human-like qualities to AI) explain divergent emotional reactions to AI chatbot interaction. American and Canadian Prolific participants completed an 8-item anthropomorphism-of-technology measure (Folk et al., 2025), then were randomly assigned either to text with a ChatGPT-3.5-backed chatbot prompted to be warm and conversational for 6 minutes ("chatbot condition") or to journal about the past month for 6 minutes ("journal condition"); afterwards they reported a single-item state social-connection measure.

Across both studies, a Condition × Anthropomorphism interaction was significant (Study 1 B = 0.218, p = .013; Study 2 B = 0.100, p = .013), and the chatbot condition produced higher mean social connection than journaling (Study 1 d = 0.32; Study 2 d = 0.15). Johnson-Neyman spotlight analyses identified anthropomorphism thresholds (3.13/6 in Study 1; 2.87/6 in Study 2) above which the chatbot condition outperformed journaling — 58% (Study 1) and 72% (Study 2) of the sample exceeded that threshold. Exploratory text analysis (ChatGPT-4o-mini rated participants' messages on warmth and self-disclosure) found participants disclosed and wrote more warmly when *journaling* than when texting the chatbot (Cohen's d = 0.60 for self-disclosure), but warmth and disclosure did not mediate the anthropomorphism effect — the authors hypothesize the mechanism is interpretive (anthropomorphizers feel more genuinely understood by the chatbot's responses) rather than behavioral.

The paper is empirical, peer-reviewed (Scientific Reports), preregistered for Study 2, with open data and code on OSF. Authors explicitly cite the sibling paper [[folk-dunn-companionship-loneliness-2026]] as a longitudinal counterpoint warning that immediate connection benefits may erode over time and ask whether anthropomorphism buffers or amplifies long-term costs — an open question.

## Relevance

- **Risk**: yes — provides the individual-difference moderator (anthropomorphism of technology) for who is most susceptible to immediate AI-companion engagement; foreshadows the long-term substitution risk articulated by sibling Folk & Dunn (2026) and Fang et al. (2025).
- **Erosion**: yes — empirical leg for the [[ai-loneliness-effect]] dose-response curve at the *entry point* (who reaps short-term connection rewards from chatbots and is therefore most likely to escalate use).
- **Preservation**: indirect — by naming individual variation, it argues against one-size-fits-all framings of AI companionship and supports practitioner attention to user-level moderators.
- **Relevance**: HIGH

## Quality

- **Evidence basis**: Two RCT-style experiments, total N = 1,274; Study 2 preregistered (with addendum to expand sample); peer-reviewed in Scientific Reports (Nature Portfolio); open data + R code on OSF. Effect sizes reported; spotlight analyses; controlled for age/gender/prior chatbot use; six robustness sensitivity. Effect sizes are small (chatbot vs. journal d = 0.15 in the larger Study 2) and the authors flag the Study 1 d = 0.32 as likely upward-biased by sampling variation.
- **Originality**: Fills a specific gap — the *individual-difference moderator* for who connects with AI. KB has [[ai-loneliness-effect]] (population-average dose-response, Fang) and [[folk-dunn-companionship-loneliness-2026]] (longitudinal between-person dynamics) but no entry on *who* is most susceptible to the immediate-connection effect at the entry point. Folk-Heine-Dunn provides exactly that: an empirical anchor for the anthropomorphism construct in the AI-companion context, plus an intriguing exploratory finding (anthropomorphism predicts richer mental imagery during journaling too — pointing to imagination as a possible cross-condition mechanism). Sibling to [[folk-dunn-companionship-loneliness-2026]] but a *different* study (the latter is observational longitudinal; this is two RCT-style experiments at a single timepoint with anthropomorphism as the moderator).
- **Quality**: HIGH

## Extractable Elements

- **Concepts**:
  - NEW candidate: `anthropomorphism-of-technology` — labeled construct for the trait-level individual difference in attributing human-like qualities to AI/technology, distinct from general anthropomorphism (r ≈ .40); measured by an 8-item validated scale (Folk et al., 2025); empirically linked to social-connection benefits from chatbots and (less directly) cultural attitudes toward AI. **Justification:** the construct is named, measured, and shown to be load-bearing across two studies; it sits cleanly alongside existing concepts ([[ai-loneliness-effect]] describes the outcome; this names a key moderator on the *who connects* side). One concept, atomic. Without it, the KB will keep referring to "tendency to anthropomorphize" without a stem.
- **Methods**: none — the anthropomorphism scale and Johnson-Neyman spotlight analysis are research instruments, not practitioner-facing methods.
- **Claims**: anthropomorphism-of-technology moderates the immediate social-connection benefit of chatbot interaction; chatbot interaction yields a small but reliable connection benefit over journaling on average; warmth and self-disclosure do not mediate the anthropomorphism effect; anthropomorphism is also weakly associated with social connection during journaling, possibly via mental-imagery vividness.

## Recommendation

**INCLUDE**

Reason: Peer-reviewed, preregistered (Study 2), high-powered (N ≈ 1,274 total) experimental evidence on a moderator that the KB's loneliness/companion cluster has been pointing at without naming. Sibling to a just-integrated source ([[folk-dunn-companionship-loneliness-2026]]) but a substantively different contribution (entry-point individual differences vs. months-scale bidirectional dynamics).

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: Overrides prior session's DEFER (queued as Tier-1 for the next session). High-relevance, high-quality empirical anchor for the previously un-housed `anthropomorphism-of-technology` construct; complements the just-integrated sibling Folk & Dunn (2026) longitudinal paper without duplicating its contribution.
