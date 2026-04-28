# CLAUDE.md - Modrn Mind Knowledge Base

## Project Overview

**What**: Curated knowledge base for the "human thinking with AI" domain—maintaining cognitive sovereignty while using AI productively.

**Purpose**: Research, practice, and professional insight translated into concepts you can teach from, apply, and verify. For anyone teaching about or navigating AI use.

**Audience — two personas:**
- **Educator** — Corporate trainers, L&D professionals, workshop facilitators, professors, and content creators who build learning experiences about AI and human thinking.
- **Practitioner** — Professionals who use AI daily — consultants, strategists, designers, developers, leaders, and anyone navigating AI in their work — who want to preserve their thinking, judgment, and expertise.

**Researcher = Collaborator, not audience.** Academics and scientists who review entries, validate claims, and contribute sources. We translate their work for practitioners. They don't need us to explain their own field.

## Repository Structure

```
Modrn Mind - Knowledge Base/
│
├── concepts/          # Ideas, phenomena, terms
├── frameworks/        # Coherent systems from authors
├── practices/         # Actionable guidance
├── sources/           # Evidence base (papers, books, articles)
│
├── workspace/         # Working area (gitignored, not curated content)
│   ├── inbox/         # New sources awaiting screening
│   ├── processing/    # Drafts in flight
│   ├── archive/       # Processed sources
│   └── feedback/      # Reviewer notes by month
│
├── tooling/           # Plumbing — visible but separate from content
│   ├── scripts/       # CLI tools (kb_search, linter, contradiction_scan, build-bundle)
│   ├── workflows/     # Ready prompts: scout, screener, processor, verifier
│   └── templates/     # Entry templates: concept, framework, practice, source
│
├── dist/              # Bundle output (built by tooling/scripts/build-bundle.sh)
│
├── README.md
├── CLAUDE.md          # This file
├── CONTRIBUTING.md    # How to contribute
│
└── .github/workflows/
    └── build-kb-bundle.yml  # Auto-bundles on push to main
```

## Knowledge Pack

A single concatenated markdown file containing the full KB, auto-generated via GitHub Actions on every push to `main` that changes content files. Published as a GitHub Release at `releases/latest`. Users download this file and upload it to Claude Projects, NotebookLM, Custom GPTs, or any AI assistant to use the KB as context.

## Metadata Schema

Every entry requires YAML frontmatter:

```yaml
---
status: solid | emerging | speculative
area: [risk, erosion, preservation]
sources:
  - "Citation"
reviewed_by:
reviewed_date:
---
```

### Status Levels
- **solid** — Peer-reviewed support, teach with confidence
- **emerging** — Supported but developing, or from thought leaders
- **speculative** — Hypothesis, needs evidence

### Area Tags
- **risk** — What capabilities are threatened
- **erosion** — Why and how capacity degrades
- **preservation** — What to do about it

## Naming Conventions

- Files: lowercase with hyphens (`cognitive-offloading.md`)
- Sources: `author-keyword-year.md` (`bjork-desirable-difficulties-2011.md`)
- Use `[[wikilinks]]` for internal references

## Workflow

All content goes through human review:

```
Source → Screener → Processor → Verifier → Human Review → AI Integration → KB
```

### Guardrails

- **Never** write directly to `concepts/`, `frameworks/`, `practices/`, `sources/`
- **Always** output to `workspace/processing/[source-slug]/` for review
- **Leave** `reviewed_by` and `reviewed_date` empty—reviewer fills these

## Templates

Use templates in `tooling/templates/` for new entries:
- `concept.md`
- `framework.md`
- `practice.md`
- `source.md`

## Tools

On-demand CLI tools in `tooling/scripts/`:
- `kb_search.py` — search/list/get/similar/stats over the KB
- `linter.py` — pure-Python health check (broken wikilinks, orphans, stale reviews, frontmatter drift, etc.) → writes `workspace/lint-report.md`
- `contradiction_scan.py` — LLM coherence pass over wikilinked entry pairs → writes `workspace/contradiction-report.md` (costs ~$0.50/run, requires `ANTHROPIC_API_KEY` in `.env`)
- `build-bundle.sh` — concatenates KB content into `dist/modern-mind-kb.md`

## Contributing

See `CONTRIBUTING.md` for full guidelines.
