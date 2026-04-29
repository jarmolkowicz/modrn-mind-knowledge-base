# CLAUDE.md — Modrn Mind Knowledge Base

Operating instructions for Claude Code in this repo.

## What this is

Public, curated reference on how AI reshapes human thinking, identity, and agency. Atomic entries in `concepts/`, `methods/`, `sources/`. Status-tagged (`solid` / `emerging` / `speculative`).

The KB is the central trunk of the broader Modrn Mind project — downstream artifacts (books, writing, workshops) draw from it and contribute back.

## How to operate

This repo gets used two ways. Notice which mode you're in.

**Editing the KB** — user asks to ingest a source, refine an entry, restructure content.

- For new sources: `/ingest <path>` (HITL) or `/ingest <path> --auto` (autonomous). The librarian agent (`.claude/agents/librarian.md`) drives the full 5-stage pipeline (catalog → triage → distill → critique → integrate) out of `raw/<slug>/`.
- Drafts always land in `raw/<slug>/drafts/`. **Never** write to `concepts/`, `methods/`, or `sources/` directly — only Stage 5 of the librarian does, after Decision is recorded.
- Per-source directory `raw/<slug>/` is the durable audit trail (binary + extracted text + every stage's artifact + log.md). Never delete it.
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

For PDF extraction (`extract.py`), the optional dependency `opendataloader-pdf` requires Java 11+ on `PATH`. Without it, extraction falls back to `pypdf`/`pdfplumber` (text-only, weaker on multi-column or scanned PDFs). To enable: install OpenJDK 21+ and ensure `java` is on `PATH`, then `uv sync --extra pdf-pro`. The extractor used is recorded per source in `raw/<slug>/source.json: extractor`.

## Where things live

| For | Look at |
|---|---|
| Slash commands | `.claude/commands/` |
| Sub-agent system prompts | `.claude/agents/` |
| Entry schema and templates | `tooling/templates/` |
| Tooling scripts (each has a docstring) | `tooling/scripts/` |
| External-contributor onboarding | `CONTRIBUTING.md` |
