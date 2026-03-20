"""Orchestrator — runs the full agent pipeline in sequence.

Usage:
    uv run python -m scripts.agents.run_weekly
    uv run python -m scripts.agents.run_weekly --dry-run
"""

import argparse
import shutil
import sys
import time
from pathlib import Path

from .budget import BudgetExceeded, SpendTracker
from .config import STAGING_DIR


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Modern Mind KB agent update pipeline"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run scout and assessor only, skip drafting/panel/PR",
    )
    parser.add_argument(
        "--skip-scout",
        action="store_true",
        help="Skip scout, use existing papers.json",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("Modern Mind KB — Agent Update Pipeline")
    print("=" * 60)
    start = time.time()

    # Clean staging directory
    if STAGING_DIR.exists():
        shutil.rmtree(STAGING_DIR)
    STAGING_DIR.mkdir(parents=True, exist_ok=True)

    papers_path = STAGING_DIR / "papers.json"
    assessed_path = STAGING_DIR / "assessed.json"

    tracker = SpendTracker()

    try:
        # ----- Stage 1: Scout -----
        if args.skip_scout and papers_path.exists():
            print("\n[1/6] SCOUT — skipped (using existing papers.json)")
        else:
            print("\n[1/6] SCOUT — searching for papers...")
            from . import scout

            scout.run(papers_path)

        # ----- Stage 2: Assessor -----
        print("\n[2/6] ASSESSOR — scoring relevance...")
        from . import assessor

        assessments = assessor.run(papers_path, assessed_path, tracker)

        if not assessments:
            print("\nNo relevant papers found. Pipeline complete.")
            tracker.save()
            print(f"\n{tracker.summary()}")
            return

        if args.dry_run:
            print("\n[dry-run] Stopping after assessment.")
            tracker.save()
            print(f"\n{tracker.summary()}")
            return

        # ----- Stage 3: Drafter -----
        print("\n[3/6] DRAFTER — creating entries...")
        from . import drafter

        drafts = drafter.run(papers_path, assessed_path, tracker)

        if not drafts:
            print("\nNo entries drafted. Pipeline complete.")
            tracker.save()
            print(f"\n{tracker.summary()}")
            return

        # ----- Stage 4: Panel -----
        print("\n[4/6] PANEL — multi-agent review...")
        from . import panel

        panel_results = panel.run(drafts, tracker)

        # ----- Stage 5: Cross-references -----
        print("\n[5/6] CROSSREF — suggesting links...")
        from . import crossref

        crossref_suggestions = crossref.run(drafts, panel_results, tracker)

        # ----- Stage 6: PR -----
        print("\n[6/6] PR — preparing pull request...")
        from . import pr

        pr_url = pr.run(
            drafts, panel_results, crossref_suggestions, tracker.summary()
        )

        # ----- Done -----
        tracker.save()

        elapsed = time.time() - start
        print("\n" + "=" * 60)
        print("Pipeline complete!")
        print(f"Duration: {elapsed:.1f}s")
        print(f"\n{tracker.summary()}")

        if pr_url:
            print(f"\nPR: {pr_url}")
        else:
            print(f"\nLocal output: {STAGING_DIR}")

        # Summary of actionable items
        approved = sum(
            1 for r in panel_results if r.consensus == "approve"
        )
        revise = sum(
            1 for r in panel_results if r.consensus == "revise"
        )
        rejected = sum(
            1 for r in panel_results if r.consensus == "reject"
        )

        print(f"\nEntries: {approved} approved, {revise} need revision, {rejected} rejected")
        print("Review the PR or staging directory before merging.")
        print("=" * 60)

    except BudgetExceeded as exc:
        print(f"\n[BUDGET] {exc}")
        print("Pipeline stopped to prevent overspend.")
        tracker.save()
        print(f"\n{tracker.summary()}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nPipeline interrupted by user.")
        tracker.save()
        print(f"\n{tracker.summary()}")
        sys.exit(130)


if __name__ == "__main__":
    main()
