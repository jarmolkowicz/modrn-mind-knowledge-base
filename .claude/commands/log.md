---
description: Append a chronological entry to log.md with today's date. Args become the log message.
---

Append a new line to `log.md` at the repo root using the format:

```
## [YYYY-MM-DD] <category> | <message>
```

Where YYYY-MM-DD is today's date (use the system date), and `<category>` is a short tag like `ingest`, `cleanup`, `tooling`, `restructure`, etc.

Parse the user's argument as the message. If a category prefix is present (e.g., "ingest | Lodge & Loble paper"), use it. Otherwise infer the category from context or default to `note`.

If `log.md` doesn't exist, create it with this header:

```
# Modrn Mind KB — Log

Chronological record of ingests, restructures, and notable changes.
Each entry: `## [YYYY-MM-DD] <category> | <message>`.

Parseable: `grep "^## \[" log.md | tail -20` shows recent activity.

---
```

Append the new entry at the end of the file (newest at the bottom — chronological).

After appending, confirm to the user with the line that was added.
