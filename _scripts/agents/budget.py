"""Token tracking and spend limits for the agent pipeline."""

import json
import time
from dataclasses import dataclass, field
from pathlib import Path

from .config import REPO_ROOT, WEEKLY_BUDGET_USD

SPEND_LOG = REPO_ROOT / "scripts" / "agents" / "spend-log.json"

# Approximate costs per 1M tokens (USD) — update when pricing changes
MODEL_PRICING: dict[str, dict[str, float]] = {
    "claude-haiku-4-5-20251001": {"input": 0.80, "output": 4.00},
    "claude-sonnet-4-5-20250929": {"input": 3.00, "output": 15.00},
}


class BudgetExceeded(Exception):
    """Raised when weekly spend limit is reached."""


@dataclass
class SpendTracker:
    """Tracks API spend across a pipeline run."""

    budget_usd: float = WEEKLY_BUDGET_USD
    entries: list[dict] = field(default_factory=list)
    total_usd: float = 0.0

    def record(
        self,
        agent: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
    ) -> float:
        """Record a single API call. Returns cost in USD. Raises if over budget."""
        pricing = MODEL_PRICING.get(model)
        if pricing is None:
            # Unknown model — estimate conservatively
            pricing = {"input": 3.00, "output": 15.00}

        cost = (
            input_tokens / 1_000_000 * pricing["input"]
            + output_tokens / 1_000_000 * pricing["output"]
        )

        self.total_usd += cost
        self.entries.append(
            {
                "agent": agent,
                "model": model,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "cost_usd": round(cost, 6),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
        )

        if self.total_usd > self.budget_usd:
            self.save()
            raise BudgetExceeded(
                f"Weekly budget ${self.budget_usd:.2f} exceeded "
                f"(spent ${self.total_usd:.4f})"
            )

        return cost

    def save(self) -> None:
        """Persist spend log to disk."""
        data = {
            "budget_usd": self.budget_usd,
            "total_usd": round(self.total_usd, 4),
            "calls": len(self.entries),
            "entries": self.entries,
        }
        SPEND_LOG.write_text(json.dumps(data, indent=2) + "\n")

    def summary(self) -> str:
        """Return a human-readable spend summary."""
        lines = [
            f"Total spend: ${self.total_usd:.4f} / ${self.budget_usd:.2f}",
            f"API calls: {len(self.entries)}",
        ]
        by_agent: dict[str, float] = {}
        for entry in self.entries:
            by_agent[entry["agent"]] = (
                by_agent.get(entry["agent"], 0) + entry["cost_usd"]
            )
        for agent, cost in sorted(by_agent.items()):
            lines.append(f"  {agent}: ${cost:.4f}")
        return "\n".join(lines)
