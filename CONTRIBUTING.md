# Contributing

## How to Contribute

### Suggest via Issue

The quickest way to contribute — no git knowledge needed. [Open an issue](https://github.com/jarmolkowicz/modern-mind-knowledge-base/issues) to:

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

**Why semi-automated?** AI handles discovery and extraction. Humans make every editorial decision — what gets in, how it's framed, what it connects to.

**4-stage pipeline:**

1. **`/scout-sources`** — Discover new sources relevant to the KB domain. Outputs go to `workspace/inbox/`. (Agent: `.claude/agents/scout.md`)
2. **`/screen-source <path>`** — Assess a source for relevance and quality. Recommends INCLUDE, PARTIAL, SKIP, or DEFER. (Agent: `.claude/agents/screener.md`)
3. **`/distill-source <path>`** — Extract concepts, methods, and source distillation from an approved source into `workspace/processing/[source-slug]/`. (Agent: `.claude/agents/researcher.md`)
4. **`/verify-draft <path>`** — Run a 3-lens panel (Evidence, Practitioner, Adversarial) over drafts as additional input for review. Optional but recommended for substantive entries. (Agent: `.claude/agents/verifier.md`)

After integration, run **`/update-index`** to regenerate `index.md`, and **`/log "ingest | <source name>"`** to record the change in `log.md`.

**Guardrail:** All workflow outputs go to `workspace/` — never directly to KB folders (`concepts/`, `methods/`, `sources/`). The user reviews drafts during the session and approves before any entry moves into the KB.

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
