# Triage: lee-critical-thinking-survey-2025

## Source
- Slug: `lee-critical-thinking-survey-2025`
- Type: `report` (survey study, CHI '25 archival paper — quantitative+qualitative knowledge-worker survey, treated as a report for distillation purposes given its findings-heavy character)
- Format: pdf, 23 pages, 22,719 words
- Path: `raw/lee-critical-thinking-survey-2025/source.md`, `raw/lee-critical-thinking-survey-2025/original.pdf`

## Summary

Lee, Sarkar, Tankelevitch, Drosos, Rintel, Banks, and Wilson (CMU + Microsoft Research, CHI '25) survey 319 knowledge workers who use GenAI tools at work at least once per week (Prolific platform, English-speaking, broad occupational mix), eliciting 936 first-hand examples of GenAI use across three task categories (creation, information, advice). Participants reported when and how they enacted critical thinking, and rated effort changes for each of Bloom's six cognitive activities (knowledge, comprehension, application, analysis, synthesis, evaluation) on a 5-point scale. Quantitative analysis used random-intercepts logistic and linear regressions with Benjamini–Hochberg correction (corrected p-threshold 0.007). Qualitative analysis open-coded free-text responses on motivators, inhibitors, and effort-shift rationales.

The study's empirical anchor is the confidence pair: **higher confidence in GenAI is associated with less critical thinking** (β = −0.69, p < 0.001 for perceived enaction), while **higher self-confidence is associated with more critical thinking** (β = +0.26, p = 0.026 for enaction; positive coefficients on Application and Evaluation effort). Higher overall trust in GenAI predicted lower perceived effort across four of the six cognitive activities. Knowledge workers self-reported enacting critical thinking on ~60% of examples (555/936), and perceived reduced effort for all six Bloom-level activities when using GenAI (e.g., 79% reported "less" or "much less" effort for Comprehension; 72% for Knowledge and Analysis; 55% for Evaluation).

The qualitative contribution is the framing of three effort shifts: (1) Knowledge & Comprehension shift from **information gathering to information verification** (because of hallucination + reliability issues); (2) Application shifts from **problem-solving to AI response integration** (selecting which parts to keep, modifying style/tone); (3) Analysis, Synthesis, and Evaluation shift from **task execution to task stewardship** (steering, articulating intentions, accountability without material production). The "stewardship" framing is the paper's signature contribution: in human-AI interaction the worker retains accountability while delegating production, making "stewardship" a more apt metaphor than "collaborator" or "supervisor." Three motivators (work quality, avoiding negative outcomes, skill development) and three inhibitor classes (awareness, motivation, ability barriers) structure the qualitative findings.

Evidence type: empirical, mixed-methods survey. Not an RCT — observational/correlational and self-report-based. The paper acknowledges this: confidence-thinking association is not causal, self-reports may conflate "less general effort" with "less critical thinking effort," and the sample skews younger and more tech-skilled. Key strength: scale (319 workers, 936 examples) across diverse occupations, complementing controlled-lab studies cited in the KB (Fan, Bastani, Stadler, Kosmyna).

## Relevance
- Risk: yes — the trust-in-AI → less-critical-thinking finding is the survey-level analogue of the cognitive-surrender/automation-bias mechanism documented in lab settings.
- Erosion: yes — empirical evidence that real-world knowledge workers report under-engaging when they trust the tool, explicitly framed by the authors via Bainbridge's *Ironies of Automation* (cited in paper [p.10]).
- Preservation: yes — three identified motivators (work quality, avoiding negative outcomes, skill development) and three inhibitor classes (awareness, motivation, ability) provide a design vocabulary for interventions; the "stewardship" framing is a useful target state.
- **Relevance**: HIGH

## Quality
- Evidence basis: peer-reviewed CHI '25 archival paper, large self-report sample (N=319, 936 examples), mixed quant + qual, Benjamini–Hochberg correction, validated reflective-thinking and trust-in-tech instruments. Limitations clearly acknowledged (correlational, self-report, English-only, age skew). For a survey-design study this is a strong execution.
- Originality: the **task stewardship** framing and the three effort-shift mappings (gathering → verification, problem-solving → integration, execution → stewardship) are the paper's signature contributions. The KB already cites "task stewardship (Lee et al. 2025)" in `[[metacognitive-laziness]]` and `[[performance-paradox]]` (via Bartoš et al. 2026 referencing this paper) — but lacks the workbench-level grounding. This source provides that grounding directly. Compared against `[[fan-metacognitive-laziness-2025]]` (lab RCT), `[[lee-relying-self-efficacy-2026]]` (different Lee, experiment + survey on self-efficacy/ownership/meaning), `[[handa-economic-tasks-claude-2025]]` (telemetry of which tasks AI is used for), `[[shaw-cognitive-surrender-2026]]` (lab quantification of surrender) — Lee et al. CHI '25 is complementary, not duplicative: it adds **survey-level prevalence** and **the stewardship effort-shift framing** to lab-grounded mechanisms.
- **Quality**: HIGH

## Extractable Elements
- Concepts: candidates checked — `task-stewardship` (the paper's signature framing) is a NEW concept candidate. However, per the report-type playbook, reports rarely warrant new concept entries; the stewardship idea is largely covered by existing concepts (`[[metacognitive-laziness]]`, `[[cognitive-offloading]]`, `[[performance-paradox]]`, `[[capacity-erosion]]`) plus the `[[professional-identity-threat]]` editor-not-creator framing. Best treated as a Supports anchor in the source distillation, with one or two focused UPDATEs. The confidence pair (confidence-in-AI vs. confidence-in-self) maps cleanly onto `[[confidence-competence-gap]]` and `[[fluency-bias]]`. The three effort-shift mappings are descriptive findings, not new concepts.
- Methods: none. The study itself is a survey instrument; its findings don't propose new prescriptive practices.
- Claims: (a) higher confidence in GenAI predicts less critical thinking; (b) higher self-confidence predicts more critical thinking; (c) ~60% of GenAI uses involve self-reported critical thinking; (d) participants perceive reduced effort across all 6 Bloom activities under GenAI; (e) effort shifts: gathering→verification, problem-solving→integration, execution→stewardship.

## Recommendation
**INCLUDE**

Reason: HIGH relevance + HIGH quality + cited (but not yet workbench-grounded) by two existing KB concepts. Per report-type playbook, default output is one source distillation with strong "Supports" links; one or two narrow UPDATE drafts where the survey-prevalence numbers genuinely empirically anchor an existing concept (specifically: `[[metacognitive-laziness]]` for the task-stewardship framing it already cites, and possibly `[[confidence-competence-gap]]` for the confidence-pair finding).

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: Re-triage overrides prior 2026-04-29 DEFER. Lee et al. (CHI '25) is HIGH relevance (knowledge-worker survey on critical thinking under GenAI) + HIGH quality (peer-reviewed, N=319, mixed-methods). Already cited indirectly by KB concepts via Bartoš et al. (2026) but not yet ingested as a primary source. Decision matches recommendation.
