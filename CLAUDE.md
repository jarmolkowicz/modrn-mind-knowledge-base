# CLAUDE.md — Modrn Mind Knowledge Base

Operating instructions for Claude Code working in this repo.

## What this repo is

The Modrn Mind Knowledge Base — a curated, public-facing reference for the domain "human thinking with AI." Maintaining cognitive sovereignty while using AI productively.

This is the **central trunk** for the broader Modrn Mind project. Books (still-you and future works), LinkedIn writing, and workshop materials are downstream artifacts that draw from and contribute back to this KB. The KB outlives any single project.

**Audience:**
- **Educators** — Corporate trainers, L&D professionals, professors, content creators
- **Practitioners** — Consultants, strategists, leaders navigating AI in professional work
- **Researchers** — Collaborators (not audience), who review entries and contribute sources

## Repository structure

```
Modrn Mind - Knowledge Base/
│
├── concepts/           # Atomic named phenomena (cognitive offloading, fluency bias, ...)
├── methods/            # Structured guidance: descriptive models AND prescriptive practices
├── sources/            # Per-source distillations with key passages, relevance, open questions
│
├── raw/                # Source PDFs/articles (gitignored — local only, copyright)
├── workspace/          # Working area (gitignored — inbox, processing, archive, feedback)
│
├── index.md            # Auto-generated catalog: one row per entry, scannable
├── log.md              # Chronological record of ingests and changes
│
├── tooling/            # Plumbing
│   ├── scripts/        # kb_search, linter, contradiction_scan, build-index, build-bundle
│   └── templates/      # Entry templates: concept, method, source
│
├── .claude/            # Claude Code agents and slash commands
│   ├── agents/         # scout, screener, researcher, verifier
│   └── commands/       # /scout-sources, /screen-source, /distill-source, /verify-draft, /update-index, /log
│
├── dist/               # Bundle output (auto-built on push to main)
└── .github/workflows/  # build-kb-bundle.yml
```

## Two modes Claude Code operates in here

### Maintenance mode (you are *editing* the KB)

When the user asks to ingest a source, refine an entry, run health checks, or restructure content:

- Use the slash commands (`/scout-sources`, `/screen-source`, `/distill-source`, `/verify-draft`, `/update-index`, `/log`) and the sub-agents in `.claude/agents/`
- Drafts always land in `workspace/processing/[source-slug]/`, never directly in `concepts/`, `methods/`, or `sources/`
- After ingestion, update `index.md` (`/update-index`) and append to `log.md` (`/log`)
- Run `python tooling/scripts/linter.py` after structural changes to catch broken wikilinks, orphans, frontmatter drift

### Consumer mode (you are *using* the KB as context)

When this repo is referenced from another project (e.g., still-you book chapters need to draw on Modrn Mind concepts), or when a user uploads the bundle to Claude Projects:

- `index.md` is the entry point. Read it first to find relevant entries — don't bulk-load every file
- Use `[[wikilinks]]` to follow connections; entry stems match filenames
- For a topic-focused query, run `python tooling/scripts/kb_search.py search "<topic>"` to find ranked relevant entries
- Cite entries by stem (`[[cognitive-offloading]]`) when synthesizing — don't restate the whole entry

## Content guardrails (non-negotiable)

- **No hype, no urgency triggers, no fear-mongering**
- **No alarmist framing.** AI is augmentation, not replacement
- **No AI-as-replacement language.** Frame AI as augmenting thinking, intuition, judgment, and responsibility
- **Label uncertainty.** Use `[Inference]` or `[Speculation]` when synthesizing beyond what sources support
- **No client material.** Never surface content from `Brain/Areas/Clients/` or `Brain/Projects/Active/Client - *` folders
- **No fabricated citations.** If a citation isn't in `sources/`, don't invent one
- **Match the audience.** Plain language. Specific. Useful at 7am before a client meeting

## Metadata schema

Every entry requires YAML frontmatter:

```yaml
---
status: solid | emerging | speculative
area: [risk, erosion, preservation]
sources:
  - "Citation"
---
```

Source entries also have `type: paper | book | article | video | talk`.

### Status levels
- **solid** — Peer-reviewed support, teach with confidence
- **emerging** — Supported but developing, or from thought leaders
- **speculative** — Hypothesis, needs more evidence

### Area tags
- **risk** — Capabilities threatened
- **erosion** — How and why capacity degrades
- **preservation** — What to do about it

## Naming conventions

- Files: lowercase with hyphens (`cognitive-offloading.md`)
- Sources: `author-keyword-year.md` (`bjork-desirable-difficulties-2011.md`)
- Use `[[wikilinks]]` for internal references — by stem, no path prefix

## Ingestion workflow

```
Source → /scout-sources → /screen-source → /distill-source → (optional) /verify-draft → human review → integrate → /update-index → /log
```

The user reviews drafts during the session. There's no separate review queue — the LLM proposes, the user edits, and the entry exists because the user committed it.

## Templates

In `tooling/templates/`:
- `concept.md` — atomic phenomena
- `method.md` — structured guidance (frameworks and practices, merged)
- `source.md` — per-source distillation

## Tools

On-demand CLI tools in `tooling/scripts/`:
- `kb_search.py` — search / list / get / similar / stats over the KB
- `linter.py` — pure-Python health checks (broken wikilinks, orphans, uncited sources, missing-related, frontmatter drift) → writes `workspace/lint-report.md`
- `contradiction_scan.py` — LLM coherence pass over wikilinked entry pairs → writes `workspace/contradiction-report.md` (costs ~$0.50/run, requires `ANTHROPIC_API_KEY` in `.env`)
- `build-index.py` — regenerates `index.md` from current entries (mechanical, fast)
- `build-bundle.sh` — concatenates KB content into `dist/modern-mind-kb.md`

## Contributing

See `CONTRIBUTING.md` for the contributor-facing version of this guide (humans who want to suggest sources or write entries via PR).
