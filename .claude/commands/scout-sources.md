---
description: Discover new sources relevant to the KB domain. Optionally specify a topic or area focus.
---

Invoke the `scout` sub-agent to find new sources relevant to the Modrn Mind KB domain (human thinking with AI).

If the user provided arguments, treat them as topic guidance (e.g., "metacognition", "organizational AI adoption", "fill the gap on team-level AI dynamics"). Pass that focus to the agent.

If no arguments, do a periodic scan across the standard search domains.

After the scout completes, summarize what was added to `workspace/inbox/` and recommend next steps (typically: review the inbox, then `/screen-source` on promising items).
