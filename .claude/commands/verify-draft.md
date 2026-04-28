---
description: Run the 3-lens panel (Evidence / Practitioner / Adversarial) over draft KB entries. Produces VERIFICATION.md as additional input for the user's review.
---

Invoke the `verifier` sub-agent on the draft path provided as the argument.

The path is typically `workspace/processing/[source-slug]/` (a directory with multiple drafts) or a single draft file.

The verifier:
1. Runs mechanical checks first (frontmatter, wikilinks, template compliance)
2. Then runs three expert lenses in parallel where possible (Evidence, Practitioner, Adversarial)
3. Writes `VERIFICATION.md` in the draft directory with verdicts and concerns

After the verifier completes:
- Show the user the VERIFICATION.md contents
- Highlight the highest-confidence concerns
- Note that the verifier output is advisory — the user decides what to integrate, revise, or reject
