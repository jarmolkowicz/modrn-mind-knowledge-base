# Contributing

## How to Contribute

### Suggest via Issue

The quickest way to contribute — no git knowledge needed. [Open an issue](https://github.com/jarmolkowicz/modrn-mind-knowledge-base/issues) to:

- Suggest a source or paper
- Flag an error or misinterpretation
- Propose a new concept or method

### Add an Entry Directly

To write and submit a KB entry:

1. **Fork** the repository
2. **Create** your entry using templates in `tooling/templates/`
3. **Submit** a pull request

All contributions require human review before merging.

### AI-Assisted Workflows (for collaborators using Claude Code)

For ingesting sources, use the agents and slash commands in `.claude/`. These are designed for Claude Code — not scripts, not fully automated pipelines.

#### Required Claude Code plugins (one-time setup)

The ingestion agents (especially `screener` and `researcher`) call Anthropic skills to read PDFs, Word documents, and PowerPoints. Install the plugin once:

```
claude
/plugin install anthropic-skills
```

This makes the following skills available:
- `anthropic-skills:pdf` — read, extract text and tables from PDF files (essential for academic papers)
- `anthropic-skills:docx` — read Word documents
- `anthropic-skills:pptx` — read PowerPoint decks

Plugin installation is per-machine, not per-project. Each contributor (you, Julia, anyone using Claude Code in this repo) installs once and the skills become available across all their Claude Code sessions.

If you don't install the plugin, the agents will still work for plain markdown sources and short PDFs (≤10 pages), but will fail or degrade on long PDFs, DOCX, and PPTX inputs.

**Why semi-automated?** AI handles discovery and extraction. Humans make every editorial decision — what gets in, how it's framed, what it connects to.

**5-stage pipeline:**

1. **`/scout-sources`** — Discover new sources relevant to the KB domain. Outputs go to `raw/inbox/`. (Agent: `.claude/agents/scout.md`)
2. **`/screen-source <path>`** — Assess a source for relevance and quality. Recommends INCLUDE, PARTIAL, SKIP, or DEFER. (Agent: `.claude/agents/screener.md`)
3. **`/distill-source <path>`** — Extract concepts, methods, and source distillation from an approved source into `raw/processing/[source-slug]/`. (Agent: `.claude/agents/researcher.md`)
4. **`/verify-draft <path>`** — Run a 3-lens panel (Evidence, Practitioner, Adversarial) over drafts as additional input for review. Optional but recommended for substantive entries. (Agent: `.claude/agents/verifier.md`)
5. **`/integrate-draft <slug>`** — After human review, move drafts into KB folders, rename and move the raw source file into the right `raw/<type>/` subfolder, refresh `index.md` and `log.md`. (Command: `.claude/commands/integrate-draft.md`)

**Guardrail:** All workflow outputs go to `raw/processing/[source-slug]/` — never directly to KB folders (`concepts/`, `methods/`, `sources/`). The user reviews drafts during the session and approves before any entry moves into the KB.

## Templates

Use the appropriate template in `tooling/templates/`:

- `concept.md` — Atomic named phenomena (cognitive offloading, fluency bias)
- `method.md` — Structured guidance: descriptive models, prescriptive practices, or both
- `source.md` — Per-source distillation with citation, key passages, relevance, supports, contradicts/extends, open questions

## Required Metadata

Every entry needs YAML frontmatter:

```yaml
---
status: solid | emerging | speculative
area: [risk, erosion, preservation]
sources:
  - "Citation or reference"
---
```

Source entries also include `type: paper | book | article | video | talk`.

## Quality Standards

- **One concept per entry** — Keep entries focused
- **Plain language** — Accessible to non-academics
- **Source everything** — No unsourced claims
- **Connect entries** — Use `[[wikilinks]]` to relate concepts and methods

## Naming Conventions

**KB entries** (in `concepts/`, `methods/`, `sources/`): lowercase, hyphens.
- Concepts: `cognitive-offloading.md`
- Methods: `think-first.md`
- Sources: `<author(s)>-<keyword>-<year>.md` — e.g., `bjork-desirable-difficulties-2011.md`

**Raw source files** (in `raw/<type>/`): descriptive, human-readable.
- Pattern: `<Author(s)> (<Year>) - <Short Title>.<ext>`
- Examples: `Bjork (2011) - Desirable Difficulties.pdf`, `Lodge et al. (2026) - Cognitive Offloading and Education.pdf`

The raw file and the source entry are paired by content but use different naming conventions for their different purposes (file-system browsing vs. slug-friendly cross-referencing).

## What to Contribute

Good contributions:
- Research papers with clear implications
- Frameworks or methods from domain experts
- Methods (descriptive models or prescriptive practices) with evidence or strong reasoning
- Corrections or clarifications to existing entries

Not a fit:
- Opinion without evidence
- Content outside the "human thinking with AI" domain
- Duplicates of existing concepts (check `index.md` first)
