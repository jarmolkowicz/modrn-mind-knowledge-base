"""Assessor agent — scores papers for relevance against KB taxonomy.

Maps to _workflows/screener.md. Uses Haiku for fast classification.
"""

import json
import os
from dataclasses import dataclass

import anthropic

from .budget import SpendTracker
from .config import KB_DIRS, MAX_PAPERS_ASSESSED, MODEL_ASSESSOR


@dataclass
class Assessment:
    """Assessment result for a single paper."""

    paper_id: str
    title: str
    relevance: str  # HIGH / MEDIUM / LOW
    action: str  # new_entry / update / contradiction / skip
    entries_touched: list[str]  # existing KB entries this relates to
    rationale: str
    extractable: list[str]  # concept / framework / practice / source


SYSTEM_PROMPT = """\
You are a relevance assessor for the Modern Mind Knowledge Base — a curated \
collection of concepts, frameworks, practices, and sources on how AI affects \
human thinking and how to preserve professional judgment.

Your job: given a paper's title and abstract, assess whether it belongs in \
this KB.

The KB covers three areas:
- **risk**: What capabilities are threatened by AI use
- **erosion**: Why and how human cognitive capacity degrades with AI
- **preservation**: What to do about it (practices, calibration, metacognition)

## Existing KB concepts (for matching)
{existing_entries}

## Instructions

Respond with valid JSON only. No markdown, no explanation outside the JSON.

{{
  "relevance": "HIGH" | "MEDIUM" | "LOW",
  "action": "new_entry" | "update" | "contradiction" | "skip",
  "entries_touched": ["concept-name", ...],
  "rationale": "1-2 sentences explaining your assessment",
  "extractable": ["concept", "source", ...]
}}

- **new_entry**: Introduces a concept/finding not yet in the KB
- **update**: Adds evidence or nuance to an existing entry
- **contradiction**: Challenges or contradicts an existing entry (always flag)
- **skip**: Not relevant enough, or already fully covered
"""


def get_existing_entries() -> list[str]:
    """List all existing KB entry filenames (without .md extension)."""
    entries = []
    for dir_path in KB_DIRS.values():
        if dir_path.exists():
            entries.extend(
                f.stem for f in dir_path.glob("*.md") if f.is_file()
            )
    return sorted(entries)


def assess_paper(
    paper: dict,
    existing_entries: list[str],
    tracker: SpendTracker,
) -> Assessment | None:
    """Assess a single paper for KB relevance."""
    client = anthropic.Anthropic()

    system = SYSTEM_PROMPT.format(
        existing_entries=", ".join(existing_entries)
    )

    user_msg = (
        f"Title: {paper['title']}\n\n"
        f"Abstract: {paper.get('abstract', 'No abstract available')}\n\n"
        f"Year: {paper.get('year', 'Unknown')}\n"
        f"Citations: {paper.get('citation_count', 0)}"
    )

    try:
        response = client.messages.create(
            model=MODEL_ASSESSOR,
            max_tokens=500,
            system=system,
            messages=[{"role": "user", "content": user_msg}],
        )

        tracker.record(
            agent="assessor",
            model=MODEL_ASSESSOR,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )

        raw = response.content[0].text.strip()
        # Strip markdown code fences if model adds them
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1]
            if raw.endswith("```"):
                raw = raw[: raw.rfind("```")]

        data = json.loads(raw)

        return Assessment(
            paper_id=paper["paper_id"],
            title=paper["title"],
            relevance=data.get("relevance", "LOW"),
            action=data.get("action", "skip"),
            entries_touched=data.get("entries_touched", []),
            rationale=data.get("rationale", ""),
            extractable=data.get("extractable", []),
        )

    except (json.JSONDecodeError, anthropic.APIError, KeyError) as exc:
        print(f"  [assessor] Warning: failed to assess '{paper['title']}': {exc}")
        return None


def run(
    papers_path: str | os.PathLike,
    output_path: str | os.PathLike,
    tracker: SpendTracker,
) -> list[Assessment]:
    """Run the assessor on discovered papers. Returns relevant assessments."""
    with open(str(papers_path)) as f:
        papers = json.load(f)

    existing_entries = get_existing_entries()
    print(f"[assessor] KB has {len(existing_entries)} existing entries")
    print(f"[assessor] Assessing up to {MAX_PAPERS_ASSESSED} papers...")

    assessments: list[Assessment] = []
    assessed_count = 0

    for paper in papers:
        if assessed_count >= MAX_PAPERS_ASSESSED:
            break

        result = assess_paper(paper, existing_entries, tracker)
        assessed_count += 1

        if result is None:
            continue

        if result.relevance in ("HIGH", "MEDIUM") and result.action != "skip":
            assessments.append(result)
            print(
                f"  [assessor] {result.relevance}: {result.title[:60]}... "
                f"→ {result.action}"
            )

    # Save all assessments (including skipped, for audit)
    with open(str(output_path), "w") as f:
        json.dump(
            [
                {
                    "paper_id": a.paper_id,
                    "title": a.title,
                    "relevance": a.relevance,
                    "action": a.action,
                    "entries_touched": a.entries_touched,
                    "rationale": a.rationale,
                    "extractable": a.extractable,
                }
                for a in assessments
            ],
            f,
            indent=2,
        )

    print(f"[assessor] {len(assessments)} papers passed assessment")
    return assessments
