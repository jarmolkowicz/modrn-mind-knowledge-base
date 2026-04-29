---
description: Ingest a source from raw/inbox/ through the full 5-stage pipeline (catalog → triage → distill → critique → integrate). Default is human-in-the-loop; pass --auto to run autonomously.
---

Invoke the `librarian` sub-agent (`.claude/agents/librarian.md`) to ingest the source.

## Argument

`$ARGUMENTS` — typically a path to a file in `raw/inbox/`. May also be a slug of an in-progress source in `raw/<slug>/` (the librarian resumes from `source.json: status`). Optionally followed by `--auto` for autonomous mode.

If no argument is provided, list files in `raw/inbox/` and ask the user which to ingest.

If `--auto` is present:
- Strip the flag from the path.
- Run the librarian as a background sub-agent (autonomous mode). The librarian applies its own judgment at decision points, escalates only when genuinely ambiguous, and writes Decision sections in every stage's artifact for retroactive audit.

If `--auto` is absent:
- Run the librarian inline in the main session. The librarian pauses at decision points (after triage, after distill, after critique) to present findings and ask the user for the Decision.

## What the librarian does

Five stages, all working out of `raw/<slug>/`:

1. **Catalog** — runs `tooling/scripts/extract.py` to extract text + metadata into `raw/<slug>/{original.ext, source.md, source.json, log.md}`.
2. **Triage** — type-aware cheap read; writes `triage.md` with INCLUDE / PARTIAL / SKIP / DEFER recommendation + Decision section.
3. **Distill** (if proceed) — type-specialized full read; produces drafts in `raw/<slug>/drafts/` + extraction ledger in `distill.md`.
4. **Self-critique** (if drafted) — 3-lens panel (Evidence / Practitioner / Adversarial) + AI failure checklist; writes `critique.md`.
5. **Integrate** — moves drafts to `concepts/`/`methods/`/`sources/`, updates `index.md`, KB-wide `log.md`, and the source's own `source.json: status=integrated`.

The librarian's full instructions are in `.claude/agents/librarian.md` — including the type playbooks (paper / book / article / report / transcript), the resumption table, and the universal guardrails.

## After completion

- Show the user the final state: which stage was reached, what entries (if any) landed in the KB, what (if any) is queued for human review.
- If the librarian escalated, surface the escalation note from the relevant artifact's Decision section.
