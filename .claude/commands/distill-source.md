---
description: Distill an approved source from raw/inbox/ into KB drafts (concepts, methods, source distillation). Outputs to raw/processing/ for human review.
---

Invoke the `researcher` sub-agent on the source path provided as the argument.

If no path is provided, list files in `raw/inbox/` (preferring ones with a SCREENING.md showing INCLUDE/PARTIAL) and ask the user which to distill.

The researcher produces drafts in `raw/processing/[source-slug]/` following the templates in `tooling/templates/`.

After the researcher completes:
- Show the user the SUMMARY.md
- Walk through each draft entry created
- Recommend running `/verify-draft raw/processing/[source-slug]` to invoke the 3-lens panel
- Or proceed directly to user review if the user prefers to skip the panel for low-stakes entries

After the user approves the drafts, run `/integrate-draft <slug>` to move drafts into KB folders, rename and relocate the raw source under `raw/<type>/`, refresh `index.md`, and append to `log.md`.
