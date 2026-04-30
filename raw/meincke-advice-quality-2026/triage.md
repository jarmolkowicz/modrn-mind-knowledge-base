# Triage: Meincke, Nave & Terwiesch (2026) — Advice Quality and Source Disclosure

## Source
- Slug: `meincke-advice-quality-2026` (canonical; workbench dir renamed at Stage 3 from `meincke-et-al-2026-advice-quality` to match)
- Type: `article` (per source.json source_type; in practice a peer-reviewed Registered Report in *Scientific Reports* — empirical paper)
- Format: pdf, 11 pages, ~9.4K words
- Path: `raw/meincke-advice-quality-2026/source.md` (extracted), `raw/meincke-advice-quality-2026/original.pdf` (binary)

## Summary

Meincke, Nave & Terwiesch (Wharton, *Scientific Reports* 2026, 16:11868) use a Registered Report design to address two questions about AI-generated ethical advice: (1) is its quality competitive with that of a human expert, and (2) will humans accept it? The empirical anchor is a comparison between GPT-4 advice and the advice of NYT Ethicist columnist Kwame Anthony Appiah on 20 ethical dilemmas published *after* the model's training cutoff (avoiding contamination — a methodological improvement over prior work).

A pilot study (N=187: 17 ethics experts including academics + clergy, 69 Wharton MBA students, 100 Prolific laypeople) found no usefulness difference between AI-generated and human-expert advice in an absolute-rating condition (B=0.11, n.s.) and a 57% preference for AI advice in the relative-choice condition (OR=1.34, p<.035). The result generalizes prior findings (Howe et al. 2023; Aharoni et al. 2024; Dillion et al.) to populations with greater ethical-decision expertise.

The pre-registered main study (N=642 Prolific participants, three conditions) is the contribution: Condition A — choice between AI and human advice *before* seeing it (a-priori) — revealed strong algorithm aversion: only 27.4% chose AI. Condition B — same choice *after* seeing both pieces of advice with sources disclosed — preference for AI rose to 46.8% (B=0.96, OR=2.62, p<.001). Condition C — same advice with sources hidden — AI preference rose further to 53.7% (B=0.32, OR=1.38, p=.005). Two clean findings: (1) algorithm aversion in the ethical domain shrinks substantially once advice quality is observed; (2) source disclosure imposes a residual penalty even when quality is held constant — a domain-specific instance of the disclosure penalty.

This is empirical, peer-reviewed, registered, and methodologically tight (Registered Report; pre-registered analyses; mixed logistic regressions with random intercepts for participants and dilemmas; >95% power; protocol deviations transparently reported).

## Relevance

- Risk: **yes** — algorithm aversion reduction once quality is "demonstrated" maps to over-reliance pathways the KB tracks; non-disclosure preference creates incentive structures relevant to KB's [[disclosure-penalty]] / [[transparency-paradox]] entries.
- Erosion: **yes** — once people accept AI ethical advice without source awareness, the substitution dynamics the KB tracks under [[cognitive-surrender]], [[automation-bias]], and [[social-sycophancy]] intensify, particularly in normatively loaded domains.
- Preservation: **partial** — the paper does not directly inform preservation strategies, but its findings (humans cannot reliably distinguish AI from expert ethical advice, and discount it only for source) sharpen the question of what kind of human judgment we want to preserve and why.
- **Relevance**: HIGH

## Quality

- **Evidence basis**: Registered Report in *Scientific Reports* (Stage 1 protocol accepted 13/09/24, OSF DOI registered, OSF data archive at osf.io/pz2sf/). N=187 pilot + N=642 main study. Two preregistered hypothesis tests, mixed logistic regression with random intercepts. >95% statistical power simulated. Protocol deviations (sample size 658 vs 618 target; preference question wording change; technical loss of post-dilemma attention checks) transparently reported.
- **Originality**: Builds on Howe et al. (2023), Aharoni et al. (2024), and Dillion et al. (a-priori vs ex-post comparison + source-disclosure manipulation are the new contributions). Compared against KB entries: complements [[reimann-schilke-disclosure-2025]] (general disclosure penalty) and [[raj-disclosure-penalty-2026]] (creative-writing disclosure penalty) by extending the disclosure-penalty pattern into the ethical-advice domain. Complements [[batista-sycophantic-ai-2026]], [[cheng-sycophantic-prosocial-2025]], [[chandra-sycophantic-delusional-2026]] — those papers describe what's wrong with AI moral advice; Meincke et al. show people may prefer it anyway once exposed to it. Connects to [[ai-moralization]] / [[demello-moralization-2026]] (people see AI use as morally suspect — yet here, blinded users prefer AI).
- **Quality**: HIGH

## Extractable Elements

- **Concepts**: Mostly UPDATE candidates rather than NEW.
  - UPDATE [[disclosure-penalty]] — domain-specific evidence in ethical-advice domain (28% → 47% → 54% as conditions strip source info).
  - UPDATE [[transparency-paradox]] — converging instance: people punish disclosed AI even when quality is identical.
  - UPDATE [[automation-bias]] — borderline; this is more about *acceptance under quality demonstration*, which is mechanistically the *opposite* of the canonical automation-bias dynamic. Will note carefully.
  - UPDATE [[fluency-bias]] — Meincke et al. note one explanation for AI preference: LLMs articulate reasoning in natural language, which appears more transparent and human-like. Their no-disclosure finding (54% AI preference, AI rated equal to or better than expert when source is hidden) is a fluency-bias instance worth recording.
  - UPDATE [[sycophancy]] / [[social-sycophancy]] — note tension: Meincke et al. find users prefer AI ethical advice, but [[cheng-sycophantic-prosocial-2025]] shows AI ethical advice degrades prosocial behavior. The two are not contradictory but the combination tightens the worry: people prefer the advice that may be worst for them, in a domain where they cannot easily verify.
  - UPDATE [[ai-moralization]] / [[demello-moralization-2026]] — Meincke et al. provide a complement: moralized opposition pre-exposure, but reduced opposition post-exposure when quality is evident. Suggests moralization is not fixed.
  - **Possible NEW**: "exposure-mediated aversion reduction" or "demonstrated-quality acceptance" — but this risks relabeling existing literature on advice utilization (Soll et al. 2022) and algorithm aversion (Dietvorst et al. 2015). Decision: do not create. Cover in source distillation only.
- **Methods**: none (no novel prescriptive method introduced; the experimental paradigm is well-formed but is a research design, not a KB-shaped practitioner method).
- **Claims**: 
  - GPT-4 ethical advice rated as useful as expert advice across laypeople, MBA students, and ethics experts (no significant difference).
  - 57% preference for AI advice in pilot's relative condition.
  - A-priori algorithm aversion in ethical domain: 72.6% prefer human advice (only 27.4% prefer AI) before seeing advice.
  - Algorithm aversion drops to 53.2% (46.8% prefer AI) after seeing both pieces with sources disclosed.
  - Algorithm aversion drops further to 46.3% (53.7% prefer AI) when sources are hidden.
  - When source is hidden, AI advice is rated equal to or slightly better than expert advice in absolute usefulness terms.

## Recommendation

**INCLUDE**

Reason: A peer-reviewed Registered Report with strong methods, novel design (a-priori vs ex-post vs no-disclosure), clean findings, and direct relevance to multiple existing KB concepts. Best treated per the article playbook: one source distillation + UPDATEs to several existing concepts ([[disclosure-penalty]], [[transparency-paradox]], [[fluency-bias]], [[sycophancy]] / [[social-sycophancy]], [[ai-moralization]], possibly [[automation-bias]]). No new concepts warranted — every candidate phenomenon has an existing entry that this paper extends rather than supplants.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: Re-triage in AUTO mode overrides prior DEFER. Relevance HIGH (algorithm aversion reduction + residual disclosure penalty in ethical domain is directly load-bearing for KB entries on disclosure, transparency, and AI moral advice). Quality HIGH (peer-reviewed Registered Report, pre-registered analyses, well-powered, transparent protocol deviations). Not a duplicate.
