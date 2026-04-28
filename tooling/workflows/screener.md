# Screener Workflow

## Purpose

Assess a source for relevance and quality. Recommend whether to include in KB.

## Input

- Source file (PDF, URL, or pasted text) from `workspace/inbox/`

## Process

### 1. Summarize
- What is this source about? (2-3 paragraphs)
- Who is the author? What's their credibility?
- What type of evidence is this? (empirical, theoretical, practitioner)

### 2. Assess Relevance
Does it address the KB domain?
- **Risk**: What's at stake for human cognition with AI?
- **Erosion**: Why/how does capacity degrade?
- **Preservation**: What to do about it?

Rate relevance: HIGH / MEDIUM / LOW

### 3. Assess Quality
- Is it well-sourced/evidence-based?
- Is it original or derivative?
- Does it add something not already in KB?

Rate quality: HIGH / MEDIUM / LOW

### 4. Identify Key Elements
List what could be extracted, by entry type:
- **Concepts**: New ideas, terms, named phenomena, mechanisms
- **Frameworks**: Coherent systems from a specific author, with components
- **Practices**: Actionable guidance — specific protocols, checklists, behavioral rules with steps
- **Claims**: Testable statements with evidence (feed into concepts)
- **Microlearning candidates**: Teachable moments (feed into practices or concepts)

For each type, note whether candidates exist or the source doesn't contain that type.

### 5. Recommend
- **INCLUDE**: High relevance, adds value
- **PARTIAL**: Include specific sections only
- **SKIP**: Low relevance or low quality
- **DEFER**: Interesting but not priority

## Output Format

Update the inbox file with screening results:

```markdown
# [Source Title]

## Basic Info
[from Scout]

## Screening Results

### Summary
[2-3 paragraphs]

### Relevance Assessment
- Risk: [yes/no - brief note]
- Erosion: [yes/no - brief note]
- Preservation: [yes/no - brief note]
- **Relevance**: HIGH | MEDIUM | LOW

### Quality Assessment
- Evidence basis: [note]
- Originality: [note]
- **Quality**: HIGH | MEDIUM | LOW

### Extractable Elements
- Concepts: [list]
- Frameworks: [list]
- Practices: [list]
- Microlearning: [list]

### Recommendation
**[INCLUDE | PARTIAL | SKIP | DEFER]**

Reason: [1-2 sentences]

## Status
- [x] Screened
- [ ] Awaiting human decision
```

## Handoff

Human reviews screening, makes decision, triggers Processor for approved sources.
