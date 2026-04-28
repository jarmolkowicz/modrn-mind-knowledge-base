# CLAUDE.md — Modrn Mind Knowledge Base

Operating instructions for Claude Code in this repo.

## What this is

Public, curated reference on how AI reshapes human thinking, identity, and agency. Atomic entries in `concepts/`, `methods/`, `sources/`. Status-tagged (`solid` / `emerging` / `speculative`).

The KB is the central trunk of the broader Modrn Mind project — downstream artifacts (books, writing, workshops) draw from it and contribute back.

## How to operate

This repo gets used two ways. Notice which mode you're in.

**Editing the KB** — user asks to ingest a source, refine an entry, restructure content.

- Use slash commands in `.claude/commands/`. Frontmatter says when each fires.
- Drafts always land in `raw/processing/[slug]/`. **Never** write to `concepts/`, `methods/`, or `sources/` directly — only `/integrate-draft` does, after human review.
- Tools never write to `private/` (gitignored).

**Using the KB as context** — downstream project references it, or the bundle was loaded into an AI tool.

- Read `index.md` first. Don't bulk-load entries.
- For topic search: `uv run python tooling/scripts/kb_search.py search "<topic>"`
- Cite by stem: `[[cognitive-offloading]]`. Don't restate entries.

## Voice

The repo is about this — embody it.

- No hype, urgency triggers, fear-mongering. AI as augmentation, never replacement.
- Label uncertainty as `[Inference]` or `[Speculation]` when synthesizing beyond what sources support.
- No fabricated citations — match author + year to a real `sources/` entry.
- Plain language. Useful at 7am before a client meeting.

## Python tooling

`uv run python tooling/scripts/<script>.py` — never bare `python`. uv reads `pyproject.toml` and manages `.venv/` automatically.

## Where things live

| For | Look at |
|---|---|
| Slash commands | `.claude/commands/` |
| Sub-agent system prompts | `.claude/agents/` |
| Entry schema and templates | `tooling/templates/` |
| Tooling scripts (each has a docstring) | `tooling/scripts/` |
| External-contributor onboarding | `CONTRIBUTING.md` |
