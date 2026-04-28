---
description: Screen a single source from workspace/inbox/ for relevance and quality. Recommends INCLUDE / PARTIAL / SKIP / DEFER.
---

Invoke the `screener` sub-agent on the source path provided as the argument.

If no path is provided, list files in `workspace/inbox/` and ask the user which to screen.

After the screener completes:
- Update the inbox file with the screening results in place
- Show the user the recommendation
- If INCLUDE or PARTIAL, suggest running `/distill-source <path>` next
- If SKIP, suggest moving the source to `workspace/archive/`
- If DEFER, leave it in inbox with a status update
