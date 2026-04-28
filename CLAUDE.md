# CLAUDE.md — Modrn Mind Knowledge Base

Operating instructions for Claude Code working in this repo.

## What this repo is

The Modrn Mind Knowledge Base — a curated, public-facing reference for the domain "human thinking with AI." Maintaining cognitive sovereignty while using AI productively.

This is the **central trunk** for the broader Modrn Mind project. Books, public writing, and workshop materials are downstream artifacts that draw from and contribute back to this KB. The KB outlives any single project.

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
├── raw/                # Source files + ingestion lifecycle (gitignored contents, tracked structure)
│   ├── inbox/          # New arrivals, awaiting screening + distillation
│   ├── processing/     # In-flight drafts (per-source folder during ingestion)
│   ├── papers/         # Academic papers (post-ingestion)
│   ├── articles/       # Web articles, blog posts
│   ├── books/          # Books and book chapters
│   ├── transcripts/    # Video / podcast / talk transcripts
│   ├── decks/          # Slide decks
│   └── other/          # Anything that doesn't fit
│
├── private/          # Reviewer feedback and personal notes (gitignored — tools must NOT write here)
├── dist/              # Build artifacts: bundle + tool reports (gitignored)
│
├── index.md            # Auto-generated catalog: one row per entry, scannable
├── log.md              # Chronological record of ingests and changes
│
├── tooling/            # Plumbing
│   ├── scripts/        # kb_search, linter, build-index, sync-source-links, build-bundle
│   └── templates/      # Entry templates: concept, method, source
│
├── .claude/            # Claude Code agents and slash commands
│   ├── agents/         # scout, screener, researcher, verifier
│   └── commands/       # /scout-sources, /screen-source, /distill-source, /verify-draft, /integrate-draft, /update-index, /log
│
└── .github/workflows/  # build-kb-bundle.yml
```

## Required setup (one-time per contributor)

Document-handling skills for PDF, DOCX, and PPTX are committed in `.claude/skills/` and load automatically when this repo opens — no `/plugin install` needed.

The skills depend on system binaries you'll need installed on your machine:

- **pandoc** — text extraction from .docx (https://pandoc.org/installing.html)
- **Python 3** — runs validation/conversion scripts
- **LibreOffice** (`soffice`) — DOC↔DOCX conversion, DOCX→PDF rendering
- **poppler** (`pdftoppm`) — PDF→image rendering
- **Node.js** + `npm install -g docx` — only if creating new .docx files

For the typical research-ingestion flow (papers as PDF, articles as web text → markdown distillations), pandoc + Python + LibreOffice + poppler is the practical minimum.

Without these binaries, ingestion agents still handle plain markdown and short PDFs (≤10 pages) via the built-in Read tool, but will fail or degrade on longer PDFs, .docx, and .pptx inputs.

The skill bundles are pinned snapshots — refresh them periodically by re-copying from your local `~/.claude/plugins/cache/anthropic-agent-skills/` cache when the upstream plugin updates.

## Two modes Claude Code operates in here

### Maintenance mode (you are *editing* the KB)

When the user asks to ingest a source, refine an entry, run health checks, or restructure content:

- Use the slash commands (`/scout-sources`, `/screen-source`, `/distill-source`, `/verify-draft`, `/integrate-draft`, `/update-index`, `/log`) and the sub-agents in `.claude/agents/`
- Drafts always land in `raw/processing/[source-slug]/`, never directly in `concepts/`, `methods/`, or `sources/`
- After ingestion, update `index.md` (`/update-index`) and append to `log.md` (`/log`)
- Run `python tooling/scripts/linter.py` after structural changes to catch broken wikilinks, orphans, frontmatter drift

### Consumer mode (you are *using* the KB as context)

When this repo is referenced from another project (e.g., a downstream writing project drawing on Modrn Mind concepts), or when a user uploads the bundle to Claude Projects:

- `index.md` is the entry point. Read it first to find relevant entries — don't bulk-load every file
- Use `[[wikilinks]]` to follow connections; entry stems match filenames
- For a topic-focused query, run `python tooling/scripts/kb_search.py search "<topic>"` to find ranked relevant entries
- Cite entries by stem (`[[cognitive-offloading]]`) when synthesizing — don't restate the whole entry

## Content guardrails (non-negotiable)

- **No hype, no urgency triggers, no fear-mongering**
- **No alarmist framing.** AI is augmentation, not replacement
- **No AI-as-replacement language.** Frame AI as augmenting thinking, intuition, judgment, and responsibility
- **Label uncertainty.** Use `[Inference]` or `[Speculation]` when synthesizing beyond what sources support
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

**KB entries** (`concepts/`, `methods/`, `sources/`): lowercase, hyphens, code-friendly.
- Concepts: `cognitive-offloading.md`
- Methods: `think-first.md`
- Sources: `<author(s)>-<keyword>-<year>.md` — e.g., `bjork-desirable-difficulties-2011.md`

**Raw files** (`raw/<type>/`): descriptive, human-readable, for browsing.
- Pattern: `<Author(s)> (<Year>) - <Short Title>.<ext>`
- Single author: `Bjork (2011) - Desirable Difficulties.pdf`
- Two authors: `Risko & Gilbert (2016) - Cognitive Offloading.pdf`
- Three+ authors: `Lodge et al. (2026) - Cognitive Offloading and Education.pdf`

The raw file (browse-friendly) and the source entry (code-friendly slug) both reference the same source. Pairing example: `raw/papers/Bjork (2011) - Desirable Difficulties.pdf` ↔ `sources/bjork-desirable-difficulties-2011.md`.

**Wikilinks**: `[[wikilinks]]` for internal references — by entry stem, no path prefix. Sources are wikilinked via the slug (`[[bjork-desirable-difficulties-2011]]`), not by raw filename.

## Ingestion workflow

```
Drop source in raw/inbox/
  ↓
/screen-source       (optional triage — INCLUDE / SKIP / DEFER)
  ↓
/distill-source      (researcher writes drafts to raw/processing/[slug]/)
  ↓
/verify-draft        (optional — 3-lens panel produces VERIFICATION.md)
  ↓
human review
  ↓
/integrate-draft     (move drafts → KB folders, rename raw file → raw/<type>/,
                      run sync-source-links + build-index, append to log)
```

The user reviews drafts during the session. There's no separate review queue — the LLM proposes, the user edits, and the entry exists because the user committed it.

Source files and the entire ingestion lifecycle (incoming, in-flight drafts, processed) live in `raw/`. New arrivals go to `raw/inbox/`, distillation work happens in `raw/processing/[slug]/`, and after ingestion sources move to `raw/<type>/` based on their `type:` frontmatter. Tool-generated reports (linter, contradiction scan) write to `dist/`. Reviewer feedback and personal notes live in `private/` — tools must not write there.

## Templates

In `tooling/templates/`:
- `concept.md` — atomic phenomena
- `method.md` — structured guidance (frameworks and practices, merged)
- `source.md` — per-source distillation

## Tools

On-demand CLI tools in `tooling/scripts/`:
- `kb_search.py` — search / list / get / similar / stats over the KB
- `linter.py` — pure-Python health checks (broken wikilinks, orphans, uncited sources, missing-related, frontmatter drift)
- `build-index.py` — regenerates `index.md` from current entries (mechanical, fast)
- `build-bundle.sh` — concatenates KB content into `dist/modern-mind-kb.md`

## Contributing

See `CONTRIBUTING.md` for the contributor-facing version of this guide (humans who want to suggest sources or write entries via PR).
