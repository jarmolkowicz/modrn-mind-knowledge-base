"""Panel agent — multi-perspective review of drafted entries.

Runs 4 review agents (evidence, practitioner, coherence, adversary) on each
draft. Produces structured review with approve/revise/reject recommendations.
"""

import json
import os
from dataclasses import dataclass
from pathlib import Path

import anthropic

from .budget import SpendTracker
from .config import MODEL_PANEL, PANEL_ROLES, STAGING_DIR


@dataclass
class Review:
    """A single reviewer's assessment."""

    role: str
    verdict: str  # approve / revise / reject
    concerns: list[str]
    suggestions: list[str]


@dataclass
class PanelResult:
    """Combined panel review for a draft."""

    draft_path: str
    draft_filename: str
    reviews: list[Review]
    consensus: str  # approve / revise / reject
    summary: str


REVIEW_INSTRUCTION = """\
Review this KB draft entry. Respond with valid JSON only:

{{
  "verdict": "approve" | "revise" | "reject",
  "concerns": ["list of specific concerns, if any"],
  "suggestions": ["list of specific improvements, if any"]
}}

If the entry is solid, say so — don't invent concerns. But if there are real \
issues, be direct.
"""


def _read_existing_context(entries_touched: list[str]) -> str:
    """Read existing entries that this draft relates to."""
    from .config import KB_DIRS

    context_parts = []
    for name in entries_touched:
        for dir_path in KB_DIRS.values():
            path = dir_path / f"{name}.md"
            if path.exists():
                context_parts.append(f"## Existing: {name}\n{path.read_text()}")
                break
    return "\n\n".join(context_parts) if context_parts else "No related existing entries."


def review_draft(
    draft: dict,
    tracker: SpendTracker,
) -> PanelResult:
    """Run all panel agents on a single draft."""
    client = anthropic.Anthropic()

    content = draft.get("content", "")
    draft_path = draft.get("_path", "unknown")
    filename = draft.get("filename", "unknown.md")

    reviews: list[Review] = []

    for role, system_prompt in PANEL_ROLES.items():
        full_system = f"{system_prompt}\n\n{REVIEW_INSTRUCTION}"

        try:
            response = client.messages.create(
                model=MODEL_PANEL,
                max_tokens=800,
                system=full_system,
                messages=[
                    {
                        "role": "user",
                        "content": f"Draft entry to review:\n\n{content}",
                    }
                ],
            )

            tracker.record(
                agent=f"panel-{role}",
                model=MODEL_PANEL,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
            )

            raw = response.content[0].text.strip()
            if raw.startswith("```"):
                raw = raw.split("\n", 1)[1]
                if raw.endswith("```"):
                    raw = raw[: raw.rfind("```")]

            data = json.loads(raw)
            reviews.append(
                Review(
                    role=role,
                    verdict=data.get("verdict", "revise"),
                    concerns=data.get("concerns", []),
                    suggestions=data.get("suggestions", []),
                )
            )

        except (json.JSONDecodeError, anthropic.APIError) as exc:
            print(f"  [panel-{role}] Warning: review failed: {exc}")
            reviews.append(
                Review(
                    role=role,
                    verdict="revise",
                    concerns=[f"Review failed: {exc}"],
                    suggestions=[],
                )
            )

    # Determine consensus
    verdicts = [r.verdict for r in reviews]
    if all(v == "approve" for v in verdicts):
        consensus = "approve"
    elif any(v == "reject" for v in verdicts):
        consensus = "reject"
    else:
        consensus = "revise"

    # Build summary
    summary_parts = [f"**Consensus: {consensus.upper()}**\n"]
    for review in reviews:
        summary_parts.append(f"### {review.role.title()} — {review.verdict}")
        if review.concerns:
            for c in review.concerns:
                summary_parts.append(f"- Concern: {c}")
        if review.suggestions:
            for s in review.suggestions:
                summary_parts.append(f"- Suggestion: {s}")
        summary_parts.append("")

    return PanelResult(
        draft_path=draft_path,
        draft_filename=filename,
        reviews=reviews,
        consensus=consensus,
        summary="\n".join(summary_parts),
    )


def run(
    drafts: list[dict],
    tracker: SpendTracker,
) -> list[PanelResult]:
    """Run the panel on all drafts. Returns list of panel results."""
    print(f"[panel] Reviewing {len(drafts)} drafts with 4-agent panel...")

    results: list[PanelResult] = []

    for draft in drafts:
        filename = draft.get("filename", "unknown")
        print(f"  [panel] Reviewing: {filename}")

        result = review_draft(draft, tracker)
        results.append(result)
        print(f"    → {result.consensus.upper()}")

    # Save panel results
    reviews_path = STAGING_DIR / "panel-reviews.json"
    reviews_data = []
    for r in results:
        reviews_data.append(
            {
                "draft_path": r.draft_path,
                "draft_filename": r.draft_filename,
                "consensus": r.consensus,
                "reviews": [
                    {
                        "role": rev.role,
                        "verdict": rev.verdict,
                        "concerns": rev.concerns,
                        "suggestions": rev.suggestions,
                    }
                    for rev in r.reviews
                ],
            }
        )
    with open(str(reviews_path), "w") as f:
        json.dump(reviews_data, f, indent=2)

    # Save human-readable summary
    summary_path = STAGING_DIR / "panel-summary.md"
    summary_parts = ["# Panel Review Summary\n"]
    for r in results:
        summary_parts.append(f"## {r.draft_filename}\n")
        summary_parts.append(r.summary)
        summary_parts.append("---\n")
    summary_path.write_text("\n".join(summary_parts))

    approved = sum(1 for r in results if r.consensus == "approve")
    revise = sum(1 for r in results if r.consensus == "revise")
    rejected = sum(1 for r in results if r.consensus == "reject")
    print(
        f"[panel] Results: {approved} approved, {revise} revise, {rejected} rejected"
    )

    return results
