---
description: Screen a source from raw/inbox/ for relevance and quality. Recommends INCLUDE / PARTIAL / SKIP / DEFER.
---

Invoke the `screener` sub-agent on the source path provided as the argument.

If no path is provided, list files in `raw/inbox/` and ask the user which to screen.

The screener writes its results to `workspace/processing/[source-slug]/SCREENING.md` (creating the directory if needed; the researcher uses the same directory for drafts later).

After the screener completes:
- Show the user the SCREENING.md contents and the recommendation
- If INCLUDE or PARTIAL, suggest running `/distill-source raw/inbox/<filename>` next
- If SKIP, suggest moving the source to `raw/other/`
- If DEFER, leave it in `raw/inbox/` with a note in SCREENING.md
