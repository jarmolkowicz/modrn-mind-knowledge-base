# Log: folk-heine-dunn-anthropomorphism-2025

## 2026-04-29T20:00:31Z — cataloged
- Extractor: pypdf
- Format: pdf ({'pages': 7})
- Word count: 5442
- Heuristic source_type: article

## 2026-04-29T23:15:00Z - triaged: DEFER
- Folk, Heine & Dunn (Sci Rep 2025). High-priority Tier-1 INCLUDE for next session.

## 2026-04-30T00:00:00Z — triaged: INCLUDE (override)
- AUTO mode. Override prior DEFER. Full Stage-2 triage written.
- Relevance HIGH, Quality HIGH, sibling to just-integrated folk-dunn-companionship-loneliness-2026 but substantively different (RCT individual-differences moderator, not longitudinal bidirectional dynamics).
- Treating as paper-branch despite article heuristic (peer-reviewed Scientific Reports, two studies, Study 2 preregistered, N=1,274 total).

## 2026-04-30T00:30:00Z — drafted
- AUTO mode. Stage 3 distill complete.
- Created: drafts/source.md, drafts/concepts/anthropomorphism-of-technology.md, drafts/updates/ai-loneliness-effect.md, drafts/updates/mira-model.md.
- Decision: PROCEED_TO_INTEGRATE. Skipping Stage 4 critique per high-confidence rubric (single NEW concept clearly named/scaled/replicated, two source-anchored UPDATEs).

## 2026-04-30T00:35:00Z — validated
- validate_drafts.py clean on first pass; 0 findings.

## 2026-04-30T00:45:00Z — integrated
- drafts/source.md → sources/folk-heine-dunn-anthropomorphism-2025.md
- drafts/concepts/anthropomorphism-of-technology.md → concepts/anthropomorphism-of-technology.md
- drafts/updates/ai-loneliness-effect.md applied by hand to concepts/ai-loneliness-effect.md (frontmatter + new "Entry-Point Individual Differences — Anthropomorphism" section + Related + Sources)
- drafts/updates/mira-model.md applied by hand to methods/mira-model.md (frontmatter + paragraph appended to principle 2 + Related + Sources)
- Ran: sync-source-links.py, build-index.py, update_readme_counts.py (worked around Windows console encoding issue with PYTHONIOENCODING=utf-8)
- Appended KB-root log.md entry
- Cleaned up empty drafts/concepts/ (kept drafts/updates/ as evidence trail)
- KB counts: 67→68 sources, 56→57 concepts, 12 methods, 135→137 total
