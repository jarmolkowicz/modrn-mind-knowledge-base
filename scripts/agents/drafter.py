"""Drafter agent — creates KB entries from assessed papers.

Maps to _workflows/processor.md. Uses Sonnet for quality writing.
Outputs to _workspace/staging/ (never directly to KB folders).
"""

import json
import os
from pathlib import Path

import anthropic

from .budget import SpendTracker
from .config import (
    KB_DIRS,
    MAX_DRAFTS_PER_RUN,
    MODEL_DRAFTER,
    STAGING_DIR,
    TEMPLATES_DIR,
)


def _read_template(entry_type: str) -> str:
    """Read a KB entry template."""
    path = TEMPLATES_DIR / f"{entry_type}.md"
    if path.exists():
        return path.read_text()
    return ""


def _read_existing_entries() -> dict[str, str]:
    """Read all existing KB entries as {name: content} dict."""
    entries = {}
    for dir_path in KB_DIRS.values():
        if dir_path.exists():
            for f in dir_path.glob("*.md"):
                entries[f.stem] = f.read_text()
    return entries


SYSTEM_PROMPT = """\
You are a knowledge base entry drafter for the Modern Mind KB — a curated \
collection on how AI affects human thinking and how to preserve professional \
judgment while using AI productively.

## Your task
Given a paper's title, abstract, and assessment metadata, draft one or more \
KB entries following the exact templates below.

## Rules
- Write for practitioners (consultants, trainers, team leads), not academics
- Every claim must cite the source paper
- Use [[wikilinks]] for cross-references to existing KB entries
- Set status to "emerging" for all new entries
- Set area tags from: risk, erosion, preservation
- Keep language plain and direct
- One concept per entry — if the paper introduces multiple concepts, create \
  separate entries
- Leave reviewed_by and reviewed_date empty

## Existing KB entries you can cross-reference
{existing_entries}

## Templates

### Concept entry
```
{concept_template}
```

### Source entry
```
{source_template}
```

## Output format
Return a JSON array of entries. Each entry:
{{
  "type": "concept" | "source" | "practice" | "framework",
  "filename": "lowercase-with-hyphens.md",
  "content": "full markdown content including YAML frontmatter"
}}

Always include at least one source entry for the paper itself.
Return valid JSON only. No markdown wrapping.
"""


def draft_entries(
    paper: dict,
    assessment: dict,
    tracker: SpendTracker,
) -> list[dict]:
    """Draft KB entries for a single assessed paper."""
    client = anthropic.Anthropic()

    existing = _read_existing_entries()
    existing_names = sorted(existing.keys())

    system = SYSTEM_PROMPT.format(
        existing_entries=", ".join(existing_names),
        concept_template=_read_template("concept"),
        source_template=_read_template("source"),
    )

    user_msg = (
        f"## Paper\n"
        f"Title: {paper['title']}\n"
        f"Authors: {', '.join(paper.get('authors', ['Unknown']))}\n"
        f"Year: {paper.get('year', 'Unknown')}\n"
        f"URL: {paper.get('url', 'N/A')}\n\n"
        f"Abstract: {paper.get('abstract', 'No abstract')}\n\n"
        f"## Assessment\n"
        f"Action: {assessment['action']}\n"
        f"Relevance: {assessment['relevance']}\n"
        f"Related existing entries: {', '.join(assessment.get('entries_touched', []))}\n"
        f"Extractable elements: {', '.join(assessment.get('extractable', []))}\n"
        f"Rationale: {assessment.get('rationale', '')}\n"
    )

    # If this is an update, include the existing entry content
    if assessment["action"] == "update":
        for entry_name in assessment.get("entries_touched", []):
            if entry_name in existing:
                user_msg += (
                    f"\n## Existing entry: {entry_name}\n"
                    f"```\n{existing[entry_name]}\n```\n"
                )

    try:
        response = client.messages.create(
            model=MODEL_DRAFTER,
            max_tokens=4000,
            system=system,
            messages=[{"role": "user", "content": user_msg}],
        )

        tracker.record(
            agent="drafter",
            model=MODEL_DRAFTER,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )

        raw = response.content[0].text.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1]
            if raw.endswith("```"):
                raw = raw[: raw.rfind("```")]

        entries = json.loads(raw)
        return entries if isinstance(entries, list) else [entries]

    except (json.JSONDecodeError, anthropic.APIError) as exc:
        print(f"  [drafter] Warning: failed to draft for '{paper['title']}': {exc}")
        return []


def save_drafts(
    drafts: list[dict],
    paper_id: str,
) -> list[Path]:
    """Save drafted entries to staging directory. Returns paths."""
    paper_dir = STAGING_DIR / paper_id
    paper_dir.mkdir(parents=True, exist_ok=True)

    paths = []
    for draft in drafts:
        filename = draft.get("filename", "untitled.md")
        entry_type = draft.get("type", "concept")
        content = draft.get("content", "")

        # Organize by type
        type_dir = paper_dir / entry_type
        type_dir.mkdir(exist_ok=True)
        path = type_dir / filename
        path.write_text(content)
        paths.append(path)

    return paths


def run(
    papers_path: str | os.PathLike,
    assessed_path: str | os.PathLike,
    tracker: SpendTracker,
) -> list[dict]:
    """Run the drafter on assessed papers. Returns list of all drafts."""
    with open(str(papers_path)) as f:
        papers_list = json.load(f)
    with open(str(assessed_path)) as f:
        assessments = json.load(f)

    # Index papers by ID for lookup
    papers_by_id = {p["paper_id"]: p for p in papers_list}

    all_drafts = []
    draft_count = 0

    print(f"[drafter] Drafting entries for {len(assessments)} papers...")

    for assessment in assessments:
        if draft_count >= MAX_DRAFTS_PER_RUN:
            print(f"  [drafter] Reached max drafts per run ({MAX_DRAFTS_PER_RUN})")
            break

        paper = papers_by_id.get(assessment["paper_id"])
        if not paper:
            continue

        print(f"  [drafter] Drafting for: {paper['title'][:60]}...")
        drafts = draft_entries(paper, assessment, tracker)

        if drafts:
            paths = save_drafts(drafts, assessment["paper_id"])
            for draft, path in zip(drafts, paths):
                draft["_path"] = str(path)
                draft["_paper_id"] = assessment["paper_id"]
                draft["_paper_title"] = paper["title"]
            all_drafts.extend(drafts)
            draft_count += 1
            print(f"    → {len(drafts)} entries drafted")

    # Save draft index
    index_path = STAGING_DIR / "drafts-index.json"
    with open(str(index_path), "w") as f:
        json.dump(
            [
                {
                    "type": d.get("type"),
                    "filename": d.get("filename"),
                    "path": d.get("_path"),
                    "paper_id": d.get("_paper_id"),
                    "paper_title": d.get("_paper_title"),
                }
                for d in all_drafts
            ],
            f,
            indent=2,
        )

    print(f"[drafter] {len(all_drafts)} total entries drafted")
    return all_drafts
