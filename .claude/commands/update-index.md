---
description: Regenerate index.md from current KB entries. Mechanical and fast.
---

Run `uv run python tooling/scripts/build-index.py` to regenerate the KB index.

After the script completes:
- Confirm `index.md` was written
- Optionally summarize what changed since the previous version (run `git diff index.md` to see)
- Mention the entry count from the script output

This command is mechanical and deterministic. Run it after any ingestion or restructure that adds, removes, or renames entries.
