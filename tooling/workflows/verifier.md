# Verifier Workflow

## Purpose

Verify processed KB entries for accuracy, fit, and integrity before human review. Runs a 7-expert panel that catches errors, misinterpretations, and structural issues so human review focuses on editorial decisions — not error detection.

## Position in Pipeline

```
Source → Screener → Processor → **Verifier** → Human Review → KB
```

## Input

- All outputs from `workspace/processing/[source-slug]/` (new entries, updates, SUMMARY.md)
- Current KB state (all entries in `concepts/`, `frameworks/`, `practices/`, `sources/`)
- The original source material (PDF, URL, or text)

## Process

### 1. Load Context

Read thoroughly:
- Every file in `workspace/processing/[source-slug]/`
- The original source (from `workspace/inbox/` or provided directly)
- All existing KB entries referenced by the processed outputs (wikilinked or mentioned)
- Adjacent KB entries that cover related concepts

### 2. Run Expert Panel

Run each expert lens **sequentially** — later experts benefit from earlier flags. For each entry (new or update), every expert produces exactly one verdict:

- **PASS** — No issues found within this expert's domain
- **FLAG** — Specific concern identified, with a suggested fix. Entry can proceed with adjustment.
- **BLOCK** — Serious problem. Entry should not enter KB without resolution. (Misattribution, unsupported claim, duplicate, factual error.)

---

#### Expert 1: Cognitive Scientist

**Focus**: Construct validity and definitional accuracy.

Check:
- Is the concept correctly defined according to established literature?
- Is it properly distinguished from adjacent/overlapping concepts in the KB?
- Are cognitive mechanisms described accurately?
- Are causal claims supported, or is correlation presented as causation?
- Does the `status` level match the actual evidence strength?
  - `solid` — peer-reviewed, replicated or strongly supported
  - `emerging` — supported but developing, or single high-quality source
  - `speculative` — hypothesis, needs evidence

**Common flags**: Overstatement of evidence, conflation of distinct constructs, status level too high for evidence base.

---

#### Expert 2: Behavioral Scientist

**Focus**: Behavioral mechanisms, intervention validity, and evidence rigor.

Check:
- Are behavioral mechanisms described accurately?
- Are intervention claims (nudges, practices) supported by evidence?
- Are effect sizes or replication status mentioned where relevant?
- Does the entry distinguish between demonstrated effects and theoretical predictions?
- Are behavioral science constructs (motivation, habit, bias) used correctly?
- Is the evidence base current? Have key findings been challenged or replicated since publication?

**Common flags**: Overgeneralized behavioral claims, interventions presented without evidence qualification, outdated findings presented as current.

---

#### Expert 3: Human-AI Interaction Researcher

**Focus**: Accuracy of human-AI interaction dynamics.

Check:
- Does the entry accurately describe how humans and AI actually interact?
- Are interaction dynamics oversimplified (e.g., treating AI as a static tool rather than a dynamic collaborator)?
- Does it account for bidirectional effects — AI's influence on human behavior AND human behavior's influence on AI outputs?
- Are claims about AI capabilities current and accurate?
- Does the entry avoid the twin traps: AI-as-replacement framing AND naive AI-as-pure-tool framing?
- Are user adaptation patterns (workarounds, over-reliance, strategic use) acknowledged?

**Common flags**: Oversimplified interaction model, outdated AI capability claims, missing bidirectional effects, deterministic framing of outcomes that depend on usage patterns.

---

#### Expert 4: AI Adoption & Organizational Change Specialist

**Focus**: Organizational reality and practical applicability.

Check:
- Do organizational claims hold at scale, or only in controlled settings?
- Are adoption barriers and incentive structures accounted for?
- Is the workplace implication practical or purely theoretical?
- Does the entry distinguish between top-down mandated adoption and bottom-up organic adoption?
- Are organizational power dynamics acknowledged where relevant?
- Would a practitioner (consultant, L&D professional, manager) find this actionable?

**Common flags**: Lab findings presented as organizational reality, missing incentive analysis, impractical recommendations, ignoring adoption context.

---

#### Expert 5: Learning Scientist

**Focus**: Pedagogical soundness and teachability.

Check:
- Will this entry teach the concept correctly to the target audience (educators, practitioners)?
- Is the language accessible without sacrificing accuracy?
- Does the `status` label accurately set expectations for how confidently this can be taught?
- Are learning implications correctly derived from the evidence?
- Would an educator build a workshop exercise around this without risk of teaching something wrong?

**Common flags**: Status too high for teaching confidence, jargon without explanation, learning implications overstated, missing caveats an educator would need.

---

#### Expert 6: KB Editor

**Focus**: Structural integrity and consistency with existing KB.

Check:
- **Duplicates**: Does a substantially similar entry already exist? (Check by name, aliases, and description similarity)
- **Naming**: Does the filename follow conventions? (`lowercase-with-hyphens.md`, sources: `author-keyword-year.md`)
- **Frontmatter**: All required fields present? (`status`, `area`, `sources`, `reviewed_by`, `reviewed_date`)
- **Wikilinks**: Do `[[linked-entries]]` actually exist in the KB? Flag broken links.
- **Template compliance**: Does the entry follow the correct template structure from `tooling/templates/`?
- **Consistency**: Does the entry's framing align with how related concepts are framed in existing entries?
- **Update merges**: For updates — does the proposed addition fit naturally into the existing entry's structure and tone?
- **Extraction balance**: Does SUMMARY.md include an Extraction Ledger with all four entry types assessed (concepts, frameworks, practices, source)? If any type shows NONE, is the rationale documented?

**Common flags**: Broken wikilinks, missing frontmatter fields, naming violations, duplicate concept under different name, update that contradicts existing entry's framing, missing Extraction Ledger, entry type skipped without rationale.

---

#### Expert 7: Adversarial Reviewer

**Focus**: Intellectual honesty and robustness.

Check:
- What would a rigorous skeptic say about this entry?
- Is the strongest counter-argument acknowledged or at least not contradicted?
- Is the entry cherry-picking evidence while ignoring contradictory findings?
- Does the framing smuggle in assumptions that should be stated explicitly?
- Is there a selection bias in which sources are cited?
- Does the entry fall into any KB content guardrails violations?
  - Alarmist framing
  - Naively positive framing
  - AI-as-replacement framing
  - Hype language or urgency triggers
  - Unverified outcome claims

**Common flags**: Missing counter-evidence, unstated assumptions, one-sided framing, guardrail violations.

---

### 3. Compile Verification Report

After all experts have reviewed all entries, create `workspace/processing/[source-slug]/VERIFICATION.md`:

```markdown
# Verification Report: [Source Title]

## Overall Status: [READY | FLAGS | BLOCKED]

READY = all entries passed all experts
FLAGS = some entries have flags but no blocks
BLOCKED = at least one entry has a block

---

## New Entries

### [entry-name.md] — [PASS | FLAGS | BLOCKED]

| Expert | Verdict | Note |
|--------|---------|------|
| Cognitive Scientist | PASS | — |
| Behavioral Scientist | PASS | — |
| HCI Researcher | FLAG | [concise issue] |
| AI Adoption Specialist | PASS | — |
| Learning Scientist | PASS | — |
| KB Editor | PASS | — |
| Adversarial Reviewer | PASS | — |

**Flags:**
> **HCI Researcher**: [Detailed description of the issue and suggested fix]

**Suggested fix applied**: [yes/no — if yes, describe the change made to the entry]

---

[Repeat for each new entry]

## Updates to Existing Entries

### Update: [existing-entry.md] from [source] — [PASS | FLAGS | BLOCKED]

[Same table format]

---

## Integration Checklist

- [ ] All BLOCKs resolved
- [ ] All FLAGs reviewed (approved, fixed, or overridden)
- [ ] New entries ready to move to KB folders
- [ ] Updates ready to merge into existing entries
- [ ] Source archived to `workspace/archive/`
```

### 4. Apply Non-Controversial Fixes

When a FLAG has a clear, mechanical fix (e.g., broken wikilink, wrong filename, missing frontmatter field, typo in citation), apply the fix directly to the processed file and note it in the report as "Suggested fix applied: yes."

Do **not** auto-fix:
- Content framing or tone
- Status level changes
- Removal or addition of claims
- Changes to how concepts relate to each other

These require human judgment.

## Output Structure

```
workspace/processing/[source-slug]/
├── SUMMARY.md          (from Processor)
├── VERIFICATION.md     (from Verifier — NEW)
├── [entry files]       (potentially updated with mechanical fixes)
```

## Handoff to Human Review

Present VERIFICATION.md to human. Human makes decisions:
1. **All PASS** → approve integration
2. **FLAGS** → for each: approve suggested fix / override with own direction / request rework
3. **BLOCKS** → resolve before entry can proceed

Human response format — any of:
- "Approve all" — integrate everything as-is
- "Approve with flags accepted" — integrate with all suggested fixes applied
- "Override [entry]: [instruction]" — apply human's direction instead of suggested fix
- "Block [entry]" — do not integrate, needs rework
- "Approve all except [entry]" — integrate everything else, hold one back

---

## Integration (Post-Approval)

After human approval, the AI agent executes integration. This is mechanical — no editorial decisions.

### 1. Integrate New Entries

For each approved new entry:

1. **Move** the file from `workspace/processing/[source-slug]/` to the correct KB folder:
   - Concepts → `concepts/`
   - Frameworks → `frameworks/`
   - Practices → `practices/`
   - Sources → `sources/`
2. **Verify** the filename follows naming conventions
3. **Confirm** all `[[wikilinks]]` in the entry point to entries that exist (or are being created in the same batch)

### 2. Merge Updates into Existing Entries

For each approved update:

1. **Read** the current version of the existing KB entry
2. **Apply** the proposed additions to the correct sections — match the existing entry's voice and structure
3. **Add** the new source to the entry's `sources:` frontmatter list
4. **Preserve** everything else in the entry unchanged

Rules:
- Never overwrite existing content — only add
- Insert new content in a natural position within the section (not just appended at the end)
- If the update adds a `## Related` link, add it to the existing Related section
- If the existing entry's structure differs from what the update assumes, adapt the update to fit the actual structure

### 3. Archive Source

1. **Move** the original source file from `workspace/inbox/` to `workspace/archive/`
2. **Remove** the `workspace/processing/[source-slug]/` directory (all files have been integrated or rejected)

### 4. Integration Report

After integration, output a brief confirmation:

```markdown
## Integration Complete: [Source Title]

### Added to KB
- `concepts/judgment.md` — NEW
- `concepts/execution-commoditization.md` — NEW
- `sources/duncan-judgment-ai-era-2026.md` — NEW

### Updated
- `concepts/capacity-erosion.md` — added organizational dimension (Duncan 2026)
- `concepts/novice-vulnerability.md` — added workplace context (Duncan 2026)

### Archived
- `workspace/inbox/duncan-judgment-ai-era-2026.md` → `workspace/archive/`
- `workspace/processing/duncan-judgment-ai-era-2026/` → removed

### Not Integrated
- [any rejected entries and reason]
```

Human reviews the integration in Obsidian or via git diff to confirm everything looks right.
