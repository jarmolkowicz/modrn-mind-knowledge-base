# Modern Mind KB — Agent Update System

## Overview

Automated pipeline that scouts for new research, drafts KB entries, runs a multi-agent review panel, and creates GitHub PRs for human curator review. Runs weekly on GitHub Actions.

## Design Principles

- **GitHub-native**: no infrastructure beyond GitHub Actions
- **No framework**: each agent is a Python function with a system prompt
- **Human in the loop**: agents propose, human approves via PR review
- **Budget-controlled**: model tiering (Haiku for classification, Sonnet for reasoning), hard spend limits, max entries per run
- **KB practices what it preaches**: strategic alternation — agents handle throughput, human retains editorial judgment

## Pipeline

```
Weekly cron (GitHub Actions, Monday 8am UTC)
│
├─ 1. SCOUT (Haiku)
│    Search Semantic Scholar + arxiv for papers matching KB taxonomy
│    Output: papers.json (title, abstract, URL, relevance guess)
│    Budget: ~50 papers scanned, top 10-15 flagged
│
├─ 2. ASSESSOR (Haiku)
│    Score each paper against KB taxonomy
│    Output: assessed.json (relevant/not, entries touched, action type)
│    Actions: new_entry / update / contradiction / skip
│
├─ 3. DRAFTER (Sonnet)
│    Draft new entries or edits in exact KB format
│    Output: draft .md files in staging directory
│    Budget: max 5 drafts per run
│
├─ 4. PANEL (Sonnet, 4 agents per draft)
│    Agents: evidence, practitioner, coherence, adversary
│    Output: review.json per draft (approve/revise/reject + notes)
│
├─ 5. CROSS-REF (Haiku)
│    Update [[wikilinks]] and ## Related in new and affected entries
│
└─ 6. PR CREATOR (no LLM)
     Create GitHub PR with changes, panel notes, confidence scores
```

## Agent Roles

| Agent | Model | Task | Est. Cost/Call |
|-------|-------|------|---------------|
| Scout | Haiku | Search APIs, flag relevant papers | ~$0.005 |
| Assessor | Haiku | Score relevance against KB taxonomy | ~$0.01 |
| Drafter | Sonnet | Write entries in KB schema | ~$0.05 |
| Panel: Evidence | Sonnet | Evaluate source quality | ~$0.03 |
| Panel: Practitioner | Sonnet | Evaluate actionability | ~$0.03 |
| Panel: Coherence | Sonnet | Check fit with existing KB | ~$0.03 |
| Panel: Adversary | Sonnet | Argue against inclusion | ~$0.03 |
| Cross-ref | Haiku | Update wikilinks | ~$0.005 |

## Cost Estimate

- Weekly: ~$1.00-$2.00
- Monthly: ~$4-8
- Hard limit: $5.00/week (configurable)

## File Structure

```
scripts/agents/
├── SPEC.md              # this file
├── config.py            # model choices, budget limits, search queries
├── scout.py             # search Semantic Scholar + arxiv
├── assessor.py          # relevance scoring
├── drafter.py           # write entries in KB format
├── panel.py             # multi-agent review
├── crossref.py          # update wikilinks
├── pr.py                # create GitHub PR
├── budget.py            # token tracking and spend limits
├── run_weekly.py        # orchestrator
└── spend-log.json       # auto-generated cost ledger
```

## Dependencies

```
anthropic
httpx
pyyaml
pygithub
```

## GitHub Actions

Trigger: weekly cron (Monday 8am UTC) + manual dispatch
Runner: ubuntu-latest
Secrets: ANTHROPIC_API_KEY, GITHUB_TOKEN
Free tier: 2,000 min/month (pipeline uses ~15 min/run)

## Human Curator Role

- Reviews weekly PR (15 min)
- Sets editorial direction (what areas to expand)
- Final call on contradictions and ontology changes
- Periodic unassisted entry creation (strategic alternation safeguard)

## Trust Tiers

- **Auto-merge after panel approval**: minor evidence additions to existing entries
- **Requires human review**: new entries, significant rewrites
- **Always flags for human**: contradictions with existing entries, ontology changes

## Safeguards

- All agent-drafted entries get `status: emerging` (never `solid` or `foundational`)
- `reviewed_by` stays empty until human reviews
- Panel discussion stored as PR comments (provenance)
- Budget tracker halts pipeline if weekly limit exceeded
- Max 5 new entries per run
- Max 15 papers assessed per run
