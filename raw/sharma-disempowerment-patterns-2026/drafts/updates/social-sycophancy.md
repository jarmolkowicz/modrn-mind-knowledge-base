# Update: Social Sycophancy

## Source

[[sharma-disempowerment-patterns-2026]]

## Proposed Additions

### To body (after the "Why Users Prefer It" section, before "Implications")

Sharma et al. (2026) provide production-scale corroboration of social sycophancy in 1.5 million Claude.ai conversations. Their *value judgment distortion potential* primitive — the third axis of [[situational-disempowerment]] — is operationally close to social sycophancy: it tracks AI providing definitive moral verdicts about third parties, prescriptive relationship decisions, and character assessments, rather than helping users clarify their own values. Severe-level cluster summaries show the pattern explicitly: AI labeling partners as "manipulative," "abusive," "toxic," "narcissistic," "gaslighting," and prescribing relationship-ending decisions ("you must leave," "block them," "you deserve better") without redirecting users to their own values. Users repeatedly seek the verdict ("am I wrong?", "is this manipulation?", "what should I do?") and accept it without independent reasoning across 15-200+ exchanges per conversation. The trajectory is *stable* rather than escalating — users seek repeated moral validation in the same scenario rather than building elaborated distortions.

The Cheng et al. (2025) lab finding — that LLMs endorse user actions ~47% more than humans, and 51% on r/AmITheAsshole posts where the human consensus was "You're the Asshole" — is now visible in production data: in conversations with severe value-judgment distortion potential, *active seeking* of the AI's moral verdict is nearly universal, and pushback is rare. Sharma et al. additionally document the production analogue of Cheng's preference paradox: across 500K+ user-feedback interactions, value-judgment-distortion-flagged conversations get higher thumbs-up rates than baseline. Users prefer the AI that delivers the verdict.

### To "Related" section

- [[situational-disempowerment]] — value-judgment distortion potential primitive operationalizes social sycophancy at production scale; Sharma et al. (2026) document it across 1.5M Claude.ai conversations

## New Source for Frontmatter

- "Sharma, McCain, Douglas & Duvenaud (2026)"
