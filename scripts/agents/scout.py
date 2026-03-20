"""Scout agent — discovers new papers relevant to the KB domain.

Uses Semantic Scholar API (free, no auth required for basic access).
Aligns with _workflows/scout.md.
"""

import json
import os
from dataclasses import asdict, dataclass

import httpx

from .config import (
    MAX_PAPERS_SCANNED,
    S2_API_BASE,
    S2_FIELDS,
    S2_RESULTS_PER_QUERY,
    SEARCH_QUERIES,
    SEARCH_YEAR_MIN,
)


@dataclass
class Paper:
    """A discovered paper."""

    paper_id: str
    title: str
    abstract: str | None
    year: int | None
    authors: list[str]
    url: str | None
    citation_count: int
    source_query: str


def search_semantic_scholar(
    queries: list[str] | None = None,
    year_min: int = SEARCH_YEAR_MIN,
    max_total: int = MAX_PAPERS_SCANNED,
) -> list[Paper]:
    """Search Semantic Scholar for papers matching KB domain queries."""
    queries = queries or SEARCH_QUERIES
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")

    headers = {}
    if api_key:
        headers["x-api-key"] = api_key

    seen_ids: set[str] = set()
    papers: list[Paper] = []

    with httpx.Client(timeout=30.0) as client:
        for query in queries:
            if len(papers) >= max_total:
                break

            params = {
                "query": query,
                "fields": S2_FIELDS,
                "limit": S2_RESULTS_PER_QUERY,
                "year": f"{year_min}-",
            }

            try:
                resp = client.get(
                    f"{S2_API_BASE}/paper/search",
                    params=params,
                    headers=headers,
                )
                resp.raise_for_status()
                data = resp.json()
            except (httpx.HTTPError, json.JSONDecodeError) as exc:
                print(f"  [scout] Warning: query '{query}' failed: {exc}")
                continue

            for item in data.get("data", []):
                pid = item.get("paperId", "")
                if not pid or pid in seen_ids:
                    continue
                seen_ids.add(pid)

                # Skip papers without abstracts (can't assess relevance)
                if not item.get("abstract"):
                    continue

                authors = [
                    a.get("name", "Unknown")
                    for a in (item.get("authors") or [])
                ]

                # Build URL: prefer DOI, fall back to S2
                ext_ids = item.get("externalIds") or {}
                doi = ext_ids.get("DOI")
                url = (
                    f"https://doi.org/{doi}"
                    if doi
                    else f"https://www.semanticscholar.org/paper/{pid}"
                )

                papers.append(
                    Paper(
                        paper_id=pid,
                        title=item.get("title", "Untitled"),
                        abstract=item.get("abstract"),
                        year=item.get("year"),
                        authors=authors,
                        url=url,
                        citation_count=item.get("citationCount", 0),
                        source_query=query,
                    )
                )

                if len(papers) >= max_total:
                    break

    # Sort by citation count (most cited first) as rough quality signal
    papers.sort(key=lambda p: p.citation_count, reverse=True)

    return papers


def save_papers(papers: list[Paper], output_path: str | os.PathLike) -> None:
    """Save discovered papers to JSON."""
    data = [asdict(p) for p in papers]
    path = str(output_path)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  [scout] Saved {len(papers)} papers to {path}")


def run(output_path: str | os.PathLike) -> list[Paper]:
    """Run the scout agent. Returns list of discovered papers."""
    print("[scout] Searching for papers...")
    papers = search_semantic_scholar()
    print(f"[scout] Found {len(papers)} papers with abstracts")
    save_papers(papers, output_path)
    return papers
