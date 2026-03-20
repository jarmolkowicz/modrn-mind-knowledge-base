"""Configuration for the KB agent pipeline."""

from pathlib import Path

# ---------------------------------------------------------------------------
# Paths (relative to repo root)
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]

KB_DIRS = {
    "concepts": REPO_ROOT / "concepts",
    "frameworks": REPO_ROOT / "frameworks",
    "practices": REPO_ROOT / "practices",
    "sources": REPO_ROOT / "sources",
}

TEMPLATES_DIR = REPO_ROOT / "_guide" / "templates"
WORKSPACE_DIR = REPO_ROOT / "_workspace"
INBOX_DIR = WORKSPACE_DIR / "inbox"
PROCESSING_DIR = WORKSPACE_DIR / "processing"
STAGING_DIR = WORKSPACE_DIR / "staging"  # agent pipeline output

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

MODEL_SCOUT = "claude-haiku-4-5-20251001"
MODEL_ASSESSOR = "claude-haiku-4-5-20251001"
MODEL_DRAFTER = "claude-sonnet-4-5-20250929"
MODEL_PANEL = "claude-sonnet-4-5-20250929"
MODEL_CROSSREF = "claude-haiku-4-5-20251001"

# ---------------------------------------------------------------------------
# Budget limits
# ---------------------------------------------------------------------------

WEEKLY_BUDGET_USD = 5.00
MAX_PAPERS_SCANNED = 50
MAX_PAPERS_ASSESSED = 15
MAX_DRAFTS_PER_RUN = 5

# ---------------------------------------------------------------------------
# Search queries for scout
# ---------------------------------------------------------------------------

SEARCH_QUERIES = [
    "cognitive offloading AI",
    "AI overreliance human judgment",
    "human-AI collaboration cognition",
    "AI automation bias decision making",
    "AI deskilling professionals",
    "metacognition artificial intelligence",
    "AI fluency bias trust calibration",
    "generative AI knowledge work productivity",
    "AI cognitive effects workplace",
    "retrieval augmented generation knowledge management",
]

# Year filter: only papers from recent years
SEARCH_YEAR_MIN = 2023

# ---------------------------------------------------------------------------
# Semantic Scholar API
# ---------------------------------------------------------------------------

S2_API_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,abstract,year,authors,url,citationCount,externalIds"
S2_RESULTS_PER_QUERY = 10

# ---------------------------------------------------------------------------
# Panel agent roles
# ---------------------------------------------------------------------------

PANEL_ROLES = {
    "evidence": (
        "You are an evidence quality reviewer for a knowledge base on human "
        "thinking with AI. Evaluate this draft entry strictly on source quality. "
        "Is the cited research peer-reviewed? Is the claim supported by the "
        "evidence, or overstated? Is the status field (emerging/solid/speculative) "
        "appropriate? Flag any unsourced claims. Be rigorous."
    ),
    "practitioner": (
        "You are a practitioner reviewer. You work with enterprise clients on "
        "AI adoption. Evaluate this draft entry on actionability. Would a "
        "consultant, trainer, or team lead find this useful? Is the language "
        "accessible or too academic? Does it pass the '7am before a client "
        "meeting' test — would someone read this and know what to do with it? "
        "Flag anything abstract or impractical."
    ),
    "coherence": (
        "You are a coherence reviewer for a structured knowledge base. Evaluate "
        "this draft entry on fit with the existing KB. Does it overlap with or "
        "contradict existing entries? Are the cross-references ([[wikilinks]]) "
        "accurate? Does it belong in the right category (concept vs framework "
        "vs practice)? Does it use consistent terminology? Flag redundancy."
    ),
    "adversary": (
        "You are an adversarial reviewer. Your job is to argue against including "
        "this entry. What is wrong with it? Where is the evidence weakest? What "
        "would a critic say? Is this genuinely useful or just interesting? Could "
        "this entry mislead someone? Be constructive but unsparing. If you cannot "
        "find a strong objection, say so — but try hard."
    ),
}
