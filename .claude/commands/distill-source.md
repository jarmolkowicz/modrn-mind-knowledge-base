---
description: Distill an approved source into KB drafts (concepts, methods, source distillation). Outputs to workspace/processing/ for human review.
---

Invoke the `researcher` sub-agent on the source path provided as the argument.

If no path is provided, list files in `workspace/inbox/` (preferring those marked INCLUDE or PARTIAL by the screener) and ask the user which to distill.

The researcher produces drafts in `workspace/processing/[source-slug]/` following the templates in `tooling/templates/`.

After the researcher completes:
- Show the user the SUMMARY.md
- Walk through each draft entry created
- Recommend running `/verify-draft workspace/processing/[source-slug]` to invoke the 3-lens panel
- Or proceed directly to user review if the user prefers to skip the panel for low-stakes entries
