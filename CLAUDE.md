# CLAUDE.md — Modrn Mind Knowledge Base

Operating instructions for Claude Code working in this repo.

## What this repo is

The Modrn Mind Knowledge Base — a curated, public reference on the domain "human thinking with AI": cognitive sovereignty, capacity preservation, professional judgment under AI.

This is the **central trunk** of the broader Modrn Mind project. Books (`still-you` and successors), public writing, and workshop materials are downstream artifacts that draw from this KB and contribute back. The KB outlives any single project.

External users download `dist/modern-mind-kb.md` (the bundle) and upload it to Claude Projects, NotebookLM, or similar. Audience: Educators (trainers, professors, content creators) and Practitioners (consultants, leaders, researchers).

## Two modes Claude Code operates in

### Maintenance — *editing* the KB

User asks to ingest a source, refine an entry, run health checks, or restructure content. See **Common asks** and **Workflows** below.

Key rules:
- Drafts always land in `raw/processing/[slug]/`. **Never** write directly to `concepts/`, `methods/`, or `sources/`.
- After any structural change, run the linter.
- After ingesting, refresh the index and append to the log.

### Consumer — *using* the KB as context

This repo is referenced from another project (e.g., `still-you` book chapters), or someone uploaded the bundle to an AI tool.

Key rules:
- Read `index.md` first. It's the entry point — don't bulk-load entries.
- For a topic query: `uv run python tooling/scripts/kb_search.py search "<topic>"`
- Follow `[[wikilinks]]` to navigate; cite entries by stem (`[[cognitive-offloading]]`).

## Common asks → what to run

| User says | Action |
|---|---|
| "Ingest this paper" / "Distill this source" | `/screen-source <path>` (optional) → `/distill-source <path>` → `/integrate-draft <slug>` |
| "Run the linter" / "KB health check" | `uv run python tooling/scripts/linter.py` |
| "Update the index" | `/update-index` (or `uv run python tooling/scripts/build-index.py`) |
| "Refresh source links" | `uv run python tooling/scripts/sync-source-links.py` |
| "What does the KB say about X?" | `uv run python tooling/scripts/kb_search.py search "X"` |
| "Show me entry X" | `uv run python tooling/scripts/kb_search.py get <stem>` |
| "Find broken wikilinks" | `uv run python tooling/scripts/linter.py --check broken_wikilinks --stdout` |
| "Build the bundle" | `bash tooling/scripts/build-bundle.sh` |
| "Log this change" | `/log "<category> | <message>"` |

## Repository structure

```
modrn-mind-knowledge-base/
│
├── concepts/        # Atomic named phenomena (cognitive-offloading.md, fluency-bias.md, ...)
├── methods/        # Structured guidance: descriptive models + prescriptive practices, unified
├── sources/        # Per-source distillations (one entry per cited source)
│
├── raw/             # Source files + ingestion lifecycle (gitignored contents, tracked structure)
│   ├── inbox/        # New arrivals awaiting screening
│   ├── processing/  # In-flight drafts during ingestion (per-slug folders)
│   ├── papers/, articles/, books/, transcripts/, decks/, other/   # Post-ingestion, by type
│
├── private/        # Reviewer feedback only (gitignored — tools NEVER write here)
├── dist/            # Build artifacts: bundle + tool reports (gitignored)
│
├── index.md        # Auto-generated catalog, one row per entry, scannable
├── log.md          # Chronological record of ingests and notable changes
│
├── tooling/
│   ├── scripts/    # kb_search, linter, build-index, sync-source-links, build-bundle
│   └── templates/  # concept.md, method.md, source.md
│
├── .claude/
│   ├── agents/     # scout, screener, researcher, verifier
│   ├── commands/   # 7 slash commands (see Common asks)
│   └── skills/     # Document-handling skills (PDF/DOCX/PPTX) — load automatically
│
└── .github/workflows/build-kb-bundle.yml   # Auto-bundles on push to main
```

## Schema

Every entry has YAML frontmatter:

```yaml
---
status: solid | emerging | speculative   # required
area: [risk, erosion, preservation]      # required, list of one or more
sources: ["Author (Year)", ...]          # required (omitted on sources/ entries — they ARE the source)
type: paper | book | article | video | talk    # sources/ entries only
---
```

| Field | Meaning |
|---|---|
| `status: solid` | Peer-reviewed support; teach with confidence |
| `status: emerging` | Developing or single-source; treat carefully |
| `status: speculative` | Hypothesis; needs more evidence |
| `area: risk` | Capabilities threatened by AI |
| `area: erosion` | How and why capacity degrades |
| `area: preservation` | What to do about it |

## Naming

| Where | Convention | Example |
|---|---|---|
| KB entries (concepts/, methods/, sources/) | lowercase, hyphens, code-friendly | `cognitive-offloading.md` |
| Source entries | `<author(s)>-<keyword>-<year>.md` | `bjork-desirable-difficulties-2011.md` |
| Raw files (`raw/<type>/`) | `<Author(s)> (<Year>) - <Short Title>.<ext>` | `Bjork (2011) - Desirable Difficulties.pdf` |
| Wikilinks | `[[entry-stem]]` — by stem, no path | `[[cognitive-offloading]]` |

The raw file is browse-friendly; the source entry is slug-friendly. They pair by content: `raw/papers/Bjork (2011) - Desirable Difficulties.pdf` ↔ `sources/bjork-desirable-difficulties-2011.md`.

## Ingestion workflow

```
Drop file in raw/inbox/
  ↓
/screen-source <path>      (optional triage — INCLUDE / PARTIAL / SKIP / DEFER)
  ↓
/distill-source <path>     (researcher writes drafts to raw/processing/[slug]/)
  ↓
/verify-draft <slug>       (optional — 3-lens panel produces VERIFICATION.md)
  ↓
human review               (user reads drafts in session, edits, approves)
  ↓
/integrate-draft <slug>    (drafts → KB folders, raw → raw/<type>/, refresh index, append log)
```

LLM proposes; user edits in real time during the session; entry exists because the user committed it. No separate review queue.

## Content guardrails (non-negotiable)

- **No hype, urgency triggers, fear-mongering, or alarmist framing.** AI is augmentation, not replacement of human thinking.
- **Label uncertainty.** Use `[Inference]` or `[Speculation]` when synthesizing beyond what sources support.
- **No fabricated citations.** If a source isn't in `sources/`, don't invent one. Cite by author + year matching an entry.
- **Plain language.** Specific. Useful at 7am before a client meeting. Avoid AI-tell phrases ("dive into", "delve", "harness", "navigate the landscape", "in today's fast-paced world").

## Setup (one-time per contributor)

### Python tooling: invoke via `uv run`

KB tooling scripts (`tooling/scripts/*.py`) **must be invoked with `uv run python ...`**, never with system Python. `uv` reads `pyproject.toml`, manages `.venv/` automatically, and ensures every contributor runs the same dependency versions.

```bash
uv run python tooling/scripts/linter.py          # ✓ correct
python tooling/scripts/linter.py                 # ✗ wrong — uses system Python
```

If `uv` isn't installed: https://docs.astral.sh/uv/getting-started/installation/

### Document-handling skills

PDF, DOCX, PPTX skills live in `.claude/skills/` and load automatically — no `/plugin install` needed.

System binaries the skills depend on (install on the contributor's machine):
- **pandoc** — DOCX text extraction
- **Python 3** — script runtime
- **LibreOffice** (`soffice`) — DOC↔DOCX, DOCX→PDF
- **poppler** (`pdftoppm`) — PDF→image
- **Node.js** + `npm install -g docx` — only if creating new .docx files

Without the binaries, ingestion still works for plain markdown and short PDFs (≤10 pages); fails or degrades on long PDFs, DOCX, PPTX.

The skill bundles are pinned snapshots — refresh periodically by re-copying from `~/.claude/plugins/cache/anthropic-agent-skills/` when the upstream plugin updates.

## Where things live

| Folder | What goes here | Tools may write? |
|---|---|---|
| `concepts/`, `methods/`, `sources/` | Curated, public KB content | Only via `/integrate-draft` after human review |
| `raw/inbox/` | Incoming source files awaiting triage | Yes (manual drops, scout output) |
| `raw/processing/[slug]/` | In-flight drafts during ingestion | Yes (screener, researcher, verifier) |
| `raw/<type>/` (papers, articles, …) | Source files post-ingestion | Yes (`/integrate-draft` move) |
| `private/` | Reviewer feedback, personal notes | **No — tools must never write here** |
| `dist/` | Bundle + any tool reports | Yes (build-bundle.sh, optional `--out`) |

## Pointers

- `CONTRIBUTING.md` — public-facing contributor guide (forks, PRs, plugin install)
- `.claude/agents/` — sub-agent system prompts (scout, screener, researcher, verifier)
- `.claude/commands/` — slash command definitions
- `tooling/templates/` — entry templates (concept, method, source)
- `tooling/scripts/` — CLI tools listed in **Common asks** above
