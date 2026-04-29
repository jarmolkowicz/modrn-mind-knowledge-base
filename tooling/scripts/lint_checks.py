"""Shared lint check primitives for linter.py and validate_drafts.py.

Both consumers (whole-KB linter and per-draft pre-integrate validator) need the
same broken-wikilink, missing-related, and frontmatter logic. Centralized here
so both stay in sync.

The functions are parameterized: each takes a `text` (or set of wikilinks /
sources) and a `target_pool` / `title_map` produced by the caller. This keeps
them free of any dependence on the kb_search Entry class while letting both
consumers use them with appropriate scope.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass


@dataclass
class Finding:
    check: str
    entry: str
    issue: str
    fix: str = ""


def normalize_for_match(s: str) -> str:
    """Lowercase + strip diacritics for robust substring matching."""
    return "".join(
        c for c in unicodedata.normalize("NFKD", s.lower()) if not unicodedata.combining(c)
    )


# [[target]] or [[target|display]] — captures only the target slug.
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def extract_wikilinks(text: str) -> list[str]:
    """Return target slugs of all [[wikilinks]] in text, in order, with duplicates."""
    return [m.group(1) for m in WIKILINK_RE.finditer(text)]


def extract_alias_links(text: str) -> list[tuple[str, str]]:
    """Return (target, display) pairs for every [[X|Y]] alias-form wikilink.
    Plain `[[X]]` (no alias) is excluded — only matches with the pipe character.
    Used by the alias-form sanity check to catch backwards aliases like
    [[old-slug|new-slug]] where old-slug doesn't exist.
    """
    out: list[tuple[str, str]] = []
    for m in WIKILINK_RE.finditer(text):
        target, display = m.group(1), m.group(2)
        if display is not None:
            out.append((target, display))
    return out


# Source slug shape: lowercase kebab-case ending in a 4-digit year.
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*-(19|20)\d{2}$")


# Citation-shape heuristic for the vague_cite check. Unicode-letter class
# `[^\W\d_]` (not [A-Za-z]) handles accented authors (Gašević, Müller, Józsa).
HAS_AUTHOR_YEAR_RE = re.compile(r"[^\W\d_]{3,}[\s,&.()'\-\w]*(19|20)\d{2}")


# ---------------------------------------------------------------------------
# Generalized check primitives — used by both whole-KB linter and per-draft
# pre-integrate validator.
# ---------------------------------------------------------------------------


def find_broken_wikilinks(
    text: str,
    target_pool: set[str],
    *,
    entry_label: str,
    file_hint: str = "",
) -> list[Finding]:
    """Return findings for any [[wikilink]] in `text` whose target isn't in
    `target_pool`. Deduplicates so each missing target is reported once."""
    findings: list[Finding] = []
    seen: set[str] = set()
    for link in extract_wikilinks(text):
        if link in target_pool or link in seen:
            continue
        seen.add(link)
        fix = f"create '{link}' entry or fix typo"
        if file_hint:
            fix = f"create '{link}' entry or fix typo in {file_hint}"
        findings.append(
            Finding(
                check="broken_wikilinks",
                entry=entry_label,
                issue=f"links to [[{link}]] which does not exist",
                fix=fix,
            )
        )
    return findings


def find_alias_form_mistakes(
    text: str,
    target_pool: set[str],
    *,
    entry_label: str,
) -> list[Finding]:
    """Catch the backwards-alias mistake `[[old-slug|new-slug]]` where the
    target (old-slug) doesn't exist but the display text (new-slug) does — a
    pattern that recurred 3-of-3 in pilot ingests when slugs had been renamed.

    Distinct from broken_wikilinks: only fires on alias-form links AND only
    when the displayed text would itself be a valid slug, suggesting the
    user wrote the pieces in the wrong order.
    """
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    for target, display in extract_alias_links(text):
        if target in target_pool:
            continue
        if (target, display) in seen:
            continue
        seen.add((target, display))
        # Only flag as a likely backwards-alias if the display text is itself
        # a valid slug-shaped string. Plain display text like "Author (2024)"
        # is normal aliasing and not a mistake.
        if SLUG_RE.match(display) and display in target_pool:
            findings.append(
                Finding(
                    check="alias_form",
                    entry=entry_label,
                    issue=(
                        f"alias-form wikilink [[{target}|{display}]] looks backwards: "
                        f"'{target}' is not a slug, but '{display}' is. "
                        f"Did you mean [[{display}]]?"
                    ),
                    fix=f"replace with [[{display}]]",
                )
            )
    return findings


def find_missing_related(
    text: str,
    wikilinks: set[str],
    title_to_stem: dict[str, str],
    *,
    entry_label: str,
    self_stem: str | None = None,
) -> list[Finding]:
    """Return findings where `text` mentions a known KB title (case-insensitive)
    but doesn't include a `[[target_stem]]` wikilink to the corresponding entry.

    `title_to_stem` maps lowercased multi-word titles → target slug.
    `wikilinks` is the set of slugs already wikilinked in the text.
    """
    findings: list[Finding] = []
    body_lc = text.lower()
    for title_lc, target_stem in title_to_stem.items():
        if target_stem == self_stem or target_stem in wikilinks:
            continue
        if title_lc in body_lc:
            findings.append(
                Finding(
                    check="missing_related",
                    entry=entry_label,
                    issue=f"body mentions '{title_lc}' but has no [[{target_stem}]] link",
                    fix=f"add [[{target_stem}]] to Related section",
                )
            )
    return findings


def check_frontmatter_fields(
    *,
    entry_label: str,
    entry_type: str,
    status: str | None,
    area: list[str] | None,
    sources: list[str] | None,
    valid_statuses: set[str],
    valid_areas: set[str],
) -> list[Finding]:
    """Validate frontmatter status/area/sources for a single entry.

    Empty `sources` is allowed only when status=speculative — speculative
    concepts may name a phenomenon practitioners recognize before any
    KB-verifiable source exists.
    """
    findings: list[Finding] = []

    if not status:
        findings.append(
            Finding(
                check="frontmatter",
                entry=entry_label,
                issue="missing status field",
                fix=f"set status to one of {sorted(valid_statuses)}",
            )
        )
    elif status not in valid_statuses:
        findings.append(
            Finding(
                check="frontmatter",
                entry=entry_label,
                issue=f"invalid status: {status!r}",
                fix=f"use one of {sorted(valid_statuses)}",
            )
        )

    if not area:
        findings.append(
            Finding(
                check="frontmatter",
                entry=entry_label,
                issue="missing area field",
                fix=f"add area tag from {sorted(valid_areas)}",
            )
        )
    else:
        for a in area:
            if a not in valid_areas:
                findings.append(
                    Finding(
                        check="frontmatter",
                        entry=entry_label,
                        issue=f"invalid area: {a!r}",
                        fix=f"use one or more of {sorted(valid_areas)}",
                    )
                )

    if entry_type != "source" and not sources and status != "speculative":
        findings.append(
            Finding(
                check="frontmatter",
                entry=entry_label,
                issue="no sources cited in frontmatter (allowed only when status=speculative)",
                fix="add at least one source citation, or demote status to speculative",
            )
        )

    return findings


# ---------------------------------------------------------------------------
# Slug-format check (used by linter only, but lives here so the regex +
# stoplist sit alongside other slug logic).
# ---------------------------------------------------------------------------


# Institution / venue tokens that aren't author surnames. When a source slug
# starts with one of these, the slug_format check raises an advisory finding
# suggesting a rename to <author>-<keyword>-<year>.
INSTITUTION_PREFIXES: frozenset[str] = frozenset({
    # Venues and journals
    "pnas", "sciadv", "bjet", "fpsyg", "npj", "nature", "science",
    "ssrn", "arxiv", "biorxiv", "medrxiv", "psyarxiv", "osf",
    "hbr", "mit", "mit-tr",
    # Big-tech / labs
    "anthropic", "openai", "google", "deepmind", "microsoft",
    "ibm", "meta", "stanford", "harvard", "berkeley", "cmu",
    # Research orgs and consultancies
    "pew", "deloitte", "pwc", "ey", "kpmg", "accenture",
    "mckinsey", "bcg", "bain", "gartner", "forrester",
    "oecd", "wef", "weforum", "imf", "worldbank", "iea",
    # Generic acronyms / aggregators that aren't human authors
    "scispace",
})


def check_slug_against_format(stem: str) -> list[Finding]:
    """Two checks on a single source slug:
    1. Matches `<word>-...-<year>` shape.
    2. Doesn't start with a known institution token (advisory — flags but
       doesn't block; user may want to keep e.g. `pew-` as-is for org reports).
    """
    findings: list[Finding] = []
    if not SLUG_RE.match(stem):
        findings.append(
            Finding(
                check="slug_format",
                entry=stem,
                issue="slug doesn't match <author(s)>-<keyword(s)>-<year> pattern",
                fix="rename to <lead-author>-<keyword>-<4-digit-year>; update wikilinks across KB",
            )
        )
        return findings  # if it's not even kebab-cased-with-year, the prefix check is moot
    first_token = stem.split("-", 1)[0]
    if first_token in INSTITUTION_PREFIXES:
        findings.append(
            Finding(
                check="slug_format",
                entry=stem,
                issue=(
                    f"slug starts with institution/venue prefix '{first_token}' "
                    f"rather than an author surname"
                ),
                fix=(
                    f"consider renaming to <lead-author>-<keyword>-{stem.rsplit('-', 1)[-1]} "
                    f"(advisory — keep as-is if this is genuinely an anonymous/institutional source)"
                ),
            )
        )
    return findings
