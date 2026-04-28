# CLAUDE.md — Modrn Mind Knowledge Base

Operating instructions for Claude Code working in this repo.

## What this is

Public, curated reference on "human thinking with AI" — cognitive sovereignty, capacity preservation, professional judgment under AI. Content lives in `concepts/`, `methods/`, `sources/`.

This is the **central trunk** of the broader Modrn Mind project. Books (`still-you` and successors), public writing, and workshop materials are downstream artifacts that draw from this KB and contribute back. The KB outlives any single project.

External users download `dist/modern-mind-kb.md` (the bundle) and upload it to Claude Projects, NotebookLM, or similar.

## Two modes Claude Code operates in

### Editing the KB

User asks to ingest a source, refine an entry, run health checks, or restructure content.

- Use slash commands in `.claude/commands/`. Each command's frontmatter describes what it does and when to invoke it.
- Sub-agents in `.claude/agents/` are invoked by commands; don't run them directly unless asked.
- Drafts always land in `raw/processing/[slug]/`. **Never** write to `concepts/`, `methods/`, or `sources/` directly — only `/integrate-draft` does, after human review.
- After structural changes, run the linter.

### Using the KB as context

User in another project (e.g., `still-you`) references this KB, or someone uploaded the bundle to an AI tool.

- Read `index.md` first — it's the entry point. Don't bulk-load entries.
- For topic search: `uv run python tooling/scripts/kb_search.py search "<topic>"`
- Cite by stem: `[[cognitive-offloading]]`. Don't restate full entries.

## Always invoke Python via uv

`uv run python tooling/scripts/<script>.py` — never bare `python`. uv reads `pyproject.toml` and manages `.venv/` automatically, ensuring contributors run identical dependency versions.

## Universal guardrails

- No hype, urgency triggers, fear-mongering, or alarmist framing. AI is augmentation, never replacement.
- Label uncertainty as `[Inference]` or `[Speculation]` when synthesizing beyond what sources support.
- No fabricated citations — match author + year to a real `sources/` entry.
- Plain language. Useful at 7am before a client meeting.
- Tools NEVER write to `private/` (reviewer feedback, gitignored).

## Where specifics live

| For | Look at |
|---|---|
| Slash commands and what each does | `.claude/commands/` |
| Sub-agent system prompts | `.claude/agents/` |
| Entry schema (status, area, sources) and templates | `tooling/templates/` |
| Naming conventions, raw-file naming | `CONTRIBUTING.md` |
| Tooling scripts (each has its own docstring) | `tooling/scripts/` |
| Setup, binaries, plugins, contributor onboarding | `CONTRIBUTING.md` |
