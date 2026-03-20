"""Cross-reference agent — updates wikilinks in new and affected entries.

Uses Haiku for fast pattern matching across the KB.
"""

import json
import re

import anthropic

from .budget import SpendTracker
from .config import KB_DIRS, MODEL_CROSSREF


SYSTEM_PROMPT = """\
You are a cross-reference updater for the Modern Mind Knowledge Base.

Given a new KB entry and a list of all existing entries, identify which \
existing entries should link TO this new entry and which the new entry \
should link FROM.

## Rules
- Only suggest links where there's a genuine conceptual relationship
- Use [[wikilinks]] format
- Each link needs a brief relationship note (e.g., "- [[fluency-bias]] - compounds this effect")
- Don't suggest links that already exist in the entry
- Be conservative — fewer accurate links beat many vague ones

## Existing KB entries
{existing_entries}

## Response format
Return valid JSON only:

{{
  "add_to_new_entry": [
    {{"target": "entry-name", "note": "brief relationship"}}
  ],
  "add_to_existing": [
    {{"entry": "existing-entry-name", "link": "new-entry-name", "note": "brief relationship"}}
  ]
}}
"""


def get_existing_entries_with_related() -> dict[str, list[str]]:
    """Get all entries and their current Related sections."""
    entries: dict[str, list[str]] = {}
    for dir_path in KB_DIRS.values():
        if not dir_path.exists():
            continue
        for f in dir_path.glob("*.md"):
            content = f.read_text()
            # Extract existing wikilinks
            links = re.findall(r"\[\[([^\]]+)\]\]", content)
            entries[f.stem] = links
    return entries


def suggest_crossrefs(
    draft: dict,
    tracker: SpendTracker,
) -> dict:
    """Suggest cross-references for a draft entry."""
    client = anthropic.Anthropic()

    existing = get_existing_entries_with_related()
    existing_summary = "\n".join(
        f"- {name} (links to: {', '.join(links) if links else 'none'})"
        for name, links in sorted(existing.items())
    )

    system = SYSTEM_PROMPT.format(existing_entries=existing_summary)
    content = draft.get("content", "")
    filename = draft.get("filename", "unknown.md").replace(".md", "")

    try:
        response = client.messages.create(
            model=MODEL_CROSSREF,
            max_tokens=1000,
            system=system,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"New entry name: {filename}\n\n"
                        f"New entry content:\n{content}"
                    ),
                }
            ],
        )

        tracker.record(
            agent="crossref",
            model=MODEL_CROSSREF,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )

        raw = response.content[0].text.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1]
            if raw.endswith("```"):
                raw = raw[: raw.rfind("```")]

        return json.loads(raw)

    except (json.JSONDecodeError, anthropic.APIError) as exc:
        print(f"  [crossref] Warning: failed for '{filename}': {exc}")
        return {"add_to_new_entry": [], "add_to_existing": []}


def run(
    drafts: list[dict],
    panel_results: list,
    tracker: SpendTracker,
) -> dict:
    """Run cross-reference suggestions for approved/revise drafts."""
    from .config import STAGING_DIR

    # Only process approved or revise drafts (skip rejected)
    active_drafts = []
    for draft, result in zip(drafts, panel_results):
        if result.consensus != "reject":
            active_drafts.append(draft)

    print(f"[crossref] Suggesting cross-references for {len(active_drafts)} drafts...")

    all_suggestions = {}
    for draft in active_drafts:
        filename = draft.get("filename", "unknown")
        print(f"  [crossref] Processing: {filename}")
        suggestions = suggest_crossrefs(draft, tracker)
        all_suggestions[filename] = suggestions

    # Save suggestions
    output_path = STAGING_DIR / "crossref-suggestions.json"
    with open(str(output_path), "w") as f:
        json.dump(all_suggestions, f, indent=2)

    total_new = sum(
        len(s.get("add_to_new_entry", [])) for s in all_suggestions.values()
    )
    total_existing = sum(
        len(s.get("add_to_existing", [])) for s in all_suggestions.values()
    )
    print(
        f"[crossref] Suggested {total_new} links to new entries, "
        f"{total_existing} links to existing entries"
    )

    return all_suggestions
