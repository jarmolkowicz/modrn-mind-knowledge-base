# Triage: folk-dunn-companionship-loneliness-2026

## Source
- Slug: `folk-dunn-companionship-loneliness-2026`
- Type: `paper`
- Format: pdf, 11 pages, 8,098 words
- Path: `raw/folk-dunn-companionship-loneliness-2026/source.md` (extracted), `raw/folk-dunn-companionship-loneliness-2026/original.pdf` (binary)
- Citation: Folk, D., & Dunn, E. (2026). How Does Turning to AI for Companionship Predict Loneliness and Vice Versa? *Psychological Science*, 37(4), 276–286. https://doi.org/10.1177/09567976261427747

## Summary

Folk & Dunn report a 12-month, four-wave longitudinal panel study (N = 2,149 adults from UK / US / Canada / Australia recruited via Prolific) on the bidirectional relationship between social chatbot use and loneliness. Loneliness was measured two ways — a single-item *emotional isolation* item (Gallup) and a 20-item *social connection* scale (Lee et al., 2001) — explicitly treated as related but distinct constructs under the loneliness umbrella. Cross-lagged paths were estimated with random-intercept cross-lagged panel models (RI-CLPMs) controlling for breakups, relocations, new relationships, and becoming a parent.

Two findings dominate. (1) With the *emotional isolation* measure, increases in chatbot use predicted increases in loneliness 4 months later (β ≈ .07, p = .006), and increases in loneliness predicted subsequent chatbot use (β ≈ .06, p = .023) — a bidirectional pattern consistent with reciprocal exacerbation. (2) With the *social connection* measure, lower connection predicted later chatbot use (β ≈ −.08, p = .004), but chatbot use did not significantly predict subsequent decreases in connection (p = .369). Both effects survived six robustness checks, becoming marginal only in subsamples that lost statistical power. The authors flag the study as exploratory (no preregistration) and explicitly caution against strong causal conclusions, noting the standard RI-CLPM assumptions (positivity, exchangeability, consistency) are only partially satisfied.

This is empirical, longitudinal, observational evidence — not an RCT. Folk and Dunn (UBC, Department of Psychology) frame the work against an existing experimental literature that has documented short-term mood/loneliness benefits from chatbot interaction (De Freitas et al., 2024; Drouin et al., 2022; Folk et al., 2024; Ho et al., 2018), arguing that those short-term benefits may belie long-term costs. The theoretical anchor is parasocial-relationship compensation: chatbots may serve a similar compensatory function to parasocial bonds, providing rewarding-in-the-moment interaction that does not mitigate loneliness as effectively as real-world friendships.

## Relevance
- Risk: yes — provides longitudinal observational evidence that chatbot companionship may exacerbate loneliness over months, complementing the [[fang-ai-loneliness-2025]] short-window RCT.
- Erosion: yes — substitution-displacement mechanism (chatbots replacing rather than supplementing human interaction) directly relevant to relational [[capacity-erosion]].
- Preservation: indirect — the substitution-vs-enhancement question (also central to [[mira-model]]) is sharpened by these data.
- **Relevance**: HIGH

## Quality
- Evidence basis: Large multinational longitudinal sample (N = 2,149, four waves, 12-month span, four countries) with appropriate within-person panel modeling (RI-CLPM), public preregistration of materials and data on OSF, computational reproducibility independently confirmed by the journal's STAR team. Effects are small (β ≈ .06–.09) and acknowledged as such by the authors. The single-item emotional-isolation measure is a known limitation; the 20-item connection scale is well-validated but heavily trait-loaded (85–89% between-person variance), which limits its sensitivity to short-term change.
- Originality: Distinct from existing entries.
  - [[fang-ai-loneliness-2025]] — 4-week RCT with engineered chatbot conditions (voice/text × topic × engagement) and 981 participants. Folk-Dunn is observational, longer (12 months), larger (2,149), real-world chatbot use rather than randomized exposure. The Fang RCT establishes dose-dependent within-experiment effects; Folk-Dunn establishes between-wave temporal precedence over months in the wild.
  - [[ai-loneliness-effect]] — concept already exists, currently anchored on Fang + Sharma + Perry. Folk-Dunn adds a third leg (longitudinal observational) to the empirical triangulation.
  - [[boyd-markowitz-human-connection-2026]] — already cites "Folk-Dunn" as part of the empirical loneliness literature MIRA frames; this paper is the empirical anchor for MIRA principle 4 (relational substitution vs. enhancement).
  - Not a duplicate of any existing source.
- **Quality**: HIGH

## Extractable Elements
- Concepts: none NEW — this paper extends two existing concepts ([[ai-loneliness-effect]], [[social-friction]]) and supports the substitution arm of [[mira-model]] principle 4. No new named phenomenon is introduced; "parasocial compensation" is borrowed from prior literature (Madison et al., 2016; Stein et al., 2024).
- Methods: none NEW — RI-CLPM is the analytic vehicle but is a generic statistical method (Hamaker et al., 2015), not a candidate for the methods/ folder.
- Claims: bidirectional loneliness ↔ chatbot-use cycle (with caveats); short-term benefits may belie long-term costs; emotional-isolation vs. social-connection measures yield different patterns (the narrower measure is more sensitive to within-person change).

## Recommendation
**INCLUDE**

Reason: HIGH-relevance, HIGH-quality longitudinal study that closes a gap in the loneliness cluster (between Fang's short RCT and Sharma's production-data cluster). Distinct contribution; not a duplicate. Conservative on NEW concepts — value lies in UPDATEs to existing entries.

## Decision

- **Outcome**: INCLUDE
- **Date**: 2026-04-30
- **Reason**: AUTO mode — Relevance HIGH, Quality HIGH, no duplication. Overrides prior DEFER. Adds a longitudinal observational leg (12 months, 4 countries, N=2,149) to the [[ai-loneliness-effect]] evidence base; sharpens [[mira-model]] principle 4 (substitution); strengthens the friction-erosion pathway in [[social-friction]]. Conservative extraction: source distillation + UPDATEs to existing entries; no NEW concepts.
