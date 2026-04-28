---
description: Integrate approved drafts into the KB. Moves drafts to KB folders, renames the raw source, refreshes index, appends log.
---

Given a source slug as the argument (or, if no argument, list directories under `raw/processing/` and ask the user which to integrate), walk through the integration steps below.

This command is mechanical, but each step needs the user's confirmation before it acts. The user has already reviewed the drafts (in their session) — this command is the post-review file-moving + bookkeeping.

## Steps

### 1. Locate and load

- Find `raw/processing/[slug]/`
- Read `SUMMARY.md` (from the researcher) — lists what was extracted
- Read `VERIFICATION.md` if present — surfaces any concerns from the panel
- Read each draft file under `new/` and `updates/`

If the slug doesn't exist, list available slugs and ask the user which one.

### 2. Pre-integration sanity check

Before any moves:

- For each new draft, verify required frontmatter is present and valid (`status`, `area`, `sources`)
- For each `[[wikilink]]` in the new drafts, verify the target exists in the KB (or is being added in this same batch)
- If any issues, surface them and ask the user how to handle (fix, skip the entry, abort)

### 3. Confirm with the user

Show a one-line preview of each draft and update:

```
New entries:
  concepts/<name>.md          [status: emerging, area: ...]
  methods/<name>.md           [status: emerging, area: ...]
  sources/<slug>.md           [status: solid, type: paper]

Updates to existing entries:
  concepts/<existing>.md      (proposed addition to "Why It Matters" + new wikilink)

Raw source rename:
  raw/inbox/<original>.pdf  →  raw/papers/<Author> (<Year>) - <Short Title>.pdf
```

Ask: "Integrate all? Or pick specific entries to integrate / skip?"

### 4. Move new drafts into KB folders

For each confirmed new entry:
- `raw/processing/[slug]/new/<name>.md` (concept) → `concepts/<name>.md`
- `raw/processing/[slug]/new/<name>.md` (method) → `methods/<name>.md`
- `raw/processing/[slug]/new/source.md` → `sources/<slug>.md`

(The researcher's drafts are already in the right form — just move into place.)

### 5. Apply update drafts

For each update draft in `raw/processing/[slug]/updates/`:
- Read the existing target entry and the proposed update
- Show both to the user side by side
- Ask the user how to merge (approve / refine / skip)
- Apply the merge by editing the existing entry — preserve its voice and structure
- Add the new source citation to the existing entry's frontmatter `sources:` list

Don't auto-merge update drafts — they need editorial judgment.

### 6. Move and rename the raw source file

Determine the destination subfolder from the source entry's `type:` frontmatter:
- `paper` → `raw/papers/`
- `book` → `raw/books/`
- `article` → `raw/articles/`
- `video` or `talk` → `raw/transcripts/`
- (other) → `raw/other/`

Construct the descriptive filename in the form `<Authors> (<Year>) - <Short Title>.<ext>`:
- Single author: `Bjork (2011) - Desirable Difficulties.pdf`
- Two authors: `Risko & Gilbert (2016) - Cognitive Offloading.pdf`
- Three+ authors: `Lodge et al. (2026) - Cognitive Offloading and Education.pdf`

Move `raw/inbox/<original>.<ext>` → `raw/<type>/<descriptive>.<ext>`.

If the original isn't in `raw/inbox/` (already moved manually, or never there), warn and skip this step.

### 7. Refresh derivative files

Run two scripts in sequence:

```bash
python tooling/scripts/sync-source-links.py
python tooling/scripts/build-index.py
```

`sync-source-links.py` updates the Sources section in entries that cite this source via wikilinks. `build-index.py` regenerates `index.md` to include the new entries.

### 8. Append to log

Ask the user for a one-line log message (default: `ingest | <source title>`). Append to `log.md`:

```
## [YYYY-MM-DD] ingest | <message>
```

Use today's date.

### 9. Clean up

Remove the now-empty `raw/processing/[slug]/` directory.

### 10. Report

Summarize what was done:
- Entries added: list of paths
- Entries updated: list of paths with one-line description of what was added
- Raw file: where it ended up
- Index entries: now N total
- Log: appended

Note any issues encountered (skipped entries, validation warnings, sanity-check overrides).

## Guardrails

- Never write to `concepts/`, `methods/`, or `sources/` without explicit user confirmation in step 3
- Never auto-merge update drafts (step 5) — ask per draft
- If sanity check (step 2) finds problems, default to "stop and ask" rather than "fix and proceed"
- If the user aborts mid-flow, leave the state as-is (don't roll back partial moves) and report what was done so they can inspect or resume later
