# Scout Workflow

## Purpose

Find new sources relevant to the Modern Mind KB domain: human thinking with AI.

## When to Run

- Periodically (weekly/monthly) to discover new research
- When exploring a specific topic gap in the KB
- When a new author or framework is mentioned

## Search Domains

### Academic
- Google Scholar: "cognitive offloading AI", "human-AI collaboration cognition"
- arXiv: cs.HC (Human-Computer Interaction), cs.AI
- SSRN: behavioral economics + AI

### Books
- New releases on AI and work
- Authors: Ethan Mollick, Cal Newport, related thinkers

### Articles & Essays
- Substack writers on AI and cognition
- Harvard Business Review, MIT Sloan on AI adoption
- One Useful Thing (Mollick's newsletter)

### Videos & Talks
- Conference talks (CHI, NeurIPS workshops on human-AI)
- YouTube: expert interviews on AI and thinking

## Output Format

For each promising source, create `workspace/inbox/[source-slug].md`:

```markdown
# [Source Title]

## Basic Info
- **Type**: paper | book | article | video
- **Author(s)**:
- **Date**:
- **URL/Location**:

## Why Flagged
[1-2 sentences on why this seems relevant]

## Quick Summary
[If easily available, brief summary of content]

## Status
- [ ] Awaiting screening
```

## Handoff

After Scout completes, human reviews inbox and triggers Screener for promising items.
