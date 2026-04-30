# Self-Critique: Messeri & Crockett (2024) — Illusions of Understanding in AI-Driven Scientific Research

## Overall: READY

All five new drafts pass all three lenses, with minor refinements (already applied) for status calibration and wikilink targets. UPDATE drafts are clean diffs that extend existing entries without disrupting their voice.

## AI Failure Checklist

- [x] **Hallucinated citations** — every citation matches a real source. Messeri & Crockett (2024) is the actual Nature Perspective at doi:10.1038/s41586-024-07146-0; Rozenblit & Keil (2002) is a real *Cognitive Science* paper. No fabricated authors or journals.
- [x] **Methodology fabrication** — descriptions of source's methods match what the source actually says. The four-vision taxonomy is presented exactly as in Table 1 (p.3); the three illusions are quoted from Box 1 (p.2); the prediction–explanation fallacy is named on p.4. Page locators verified against source.md.
- [x] **Statistical drift** — no specific numbers from the paper are reported in the drafts (the paper itself is argumentation-heavy, not data-heavy at the result level). Reference numbers cited (e.g., refs 122, 159–168) match what the source.md text shows.
- [x] **Conflated constructs** — illusion-of-explanatory-depth, illusion-of-exploratory-breadth, and illusion-of-objectivity are kept clearly distinct, with separate "What It Is" framings. Scientific-monoculture is the parent system-level construct; the three illusions are its individual-level metacognitive accompaniments. The Related sections cross-link without merging.
- [x] **Status overstatement** — `illusion-of-explanatory-depth` set to `solid` (Rozenblit & Keil is replicated; Messeri & Crockett 2024 is peer-reviewed Nature). Other three new concepts set to `emerging` (introduced in this paper, not yet empirically operationalized at the system level). Method `ai-vision-taxonomy` set to `emerging` (Nature peer-reviewed framework, but typological rather than empirical). Source entry set to `solid` (Nature Perspective).
- [x] **Broken wikilinks** — verified targets:
  - `[[confidence-competence-gap]]` → exists
  - `[[borrowed-certainty]]` → exists
  - `[[artificial-certainty]]` → exists
  - `[[fluency-bias]]` → exists
  - `[[metacognition]]` → exists
  - `[[creativity-diversity-paradox]]` → exists
  - `[[leveling-effect]]` → exists
  - `[[novice-vulnerability]]` → exists
  - `[[anthropomorphism-of-technology]]` → exists
  - `[[partial-automation-principle]]` → exists
  - `[[think-first]]` → exists (in methods/)
  - `[[jagged-frontier]]` → exists
  - `[[anderson-homogenization-2024]]` → exists (in sources/)
  - `[[doshi-hauser-creativity-diversity-2024]]` → exists
  - `[[leonardi-artificial-certainty-2026]]` → exists
  - `[[fernandes-metacognition-2025]]` → exists
  - `[[messeri-crockett-illusions-understanding-2024]]` → will exist after Stage 5
  - `[[illusion-of-explanatory-depth]]`, `[[illusion-of-exploratory-breadth]]`, `[[illusion-of-objectivity]]`, `[[scientific-monoculture]]`, `[[ai-vision-taxonomy]]` → will exist after Stage 5; cross-referenced consistently across drafts.
- [x] **False novelty** — checked each NEW concept against existing KB:
  - `illusion-of-explanatory-depth` is *referenced inline* in `[[confidence-competence-gap]]` and `[[metacognition]]` but has no standalone entry. Promoting it to its own page is a structural improvement, not a relabel.
  - `illusion-of-exploratory-breadth` and `illusion-of-objectivity` are paper-originals not covered by any existing concept.
  - `scientific-monoculture` overlaps in spirit with `[[creativity-diversity-paradox]]` and `[[leveling-effect]]` but operates at a different unit of analysis (the question space and standpoint diversity, not output similarity or individual capability). The Related sections explicitly cross-link rather than collapse them.
  - `ai-vision-taxonomy` does not duplicate `[[partial-automation-principle]]` (which describes the *boundary* of AI's role) or `[[jagged-frontier]]` (capability boundary) — it describes the *role* AI is asked to play.

## source.md (per-source distillation)

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The Key Passages quote the source verbatim with page locators (verified against source.md). The Argument Structure section accurately summarizes the paper's flow. The Open Questions section uses `[Inference]` and `[Speculation]` labels for synthesis beyond what the source supports. Status `solid` is justified by Nature peer review. |
| Practitioner | APPROVE | Useful at 7am: the Key Insight is one paragraph, the four-vision taxonomy is a clean table, the prescriptions are operational. A consultant or researcher can use this to think about their own AI use without reading the original 10-page paper. |
| Adversarial | APPROVE | The strongest counter-argument would be that the paper is theoretical (a Perspective, not empirical) and the illusion-of-exploratory-breadth and illusion-of-objectivity constructs await empirical operationalization. The drafts handle this correctly by setting those concepts to `emerging` and the source to `solid` (peer-reviewed argumentation in Nature is a different evidentiary basis from a single empirical study). No hype, no urgency, no AI-as-replacement framing. The "produce more but understand less" line is the paper's own framing, not a KB embellishment. |

**Synthesis:** The source distillation is clean, faithful, and useful.
**Suggested action:** integrate

## illusion-of-explanatory-depth.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | Anchors to Rozenblit & Keil (2002) — a foundational, replicated cog-psy paper — and to Messeri & Crockett (2024) for the AI-in-science application. The "feeling vs. actual understanding" framing is well-supported. The prediction–explanation fallacy is named correctly per p.4 of the source. |
| Practitioner | APPROVE | The diagnostic test (rate 1–7, write the explanation, re-rate) is operational. The four "How AI Specifically Inflates It" pathways are practitioner-actionable. |
| Adversarial | APPROVE | Strongest counter: this concept is already implicit across `[[confidence-competence-gap]]`, `[[metacognition]]`, `[[fluency-bias]]`. Promoting it to its own page risks redundancy. Resolution: the existing entries *cite* the construct without defining it; a dedicated page lets them link to a single definition rather than re-explaining inline. The Related section explicitly cross-references rather than competes. |

**Synthesis:** Foundational concept that fills a real gap. Status `solid` is justified.
**Suggested action:** integrate

## illusion-of-exploratory-breadth.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The construct is paper-original; the draft attributes it correctly. The three pathways (quantification crowds out qualitative; researcher degrees of freedom become invisible; prediction crowds out explanation) are paraphrased from p.6 of the source. Status `emerging` correctly reflects that the construct is new and awaits empirical operationalization. |
| Practitioner | APPROVE | The "How To Surface It" section is labeled `[Inference]` because no validated countermeasure exists. The diagnostic moves (name the vision, pre-register the questions you are *not* asking, keep a non-AI track) are operational and conservative. |
| Adversarial | APPROVE | Strongest counter: is this just `[[creativity-diversity-paradox]]` upstream of the output? Resolution: creativity-diversity is about output similarity *given* a fixed question space; exploratory breadth is about the question space *itself* narrowing. The Related section cross-links explicitly. |

**Synthesis:** Genuine paper-original construct, distinct from existing entries.
**Suggested action:** integrate

## illusion-of-objectivity.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The construct is paper-original; the draft attributes it correctly. The strong-objectivity / weak-objectivity distinction is from Harding (1995), correctly attributed via Messeri & Crockett ref 157. The historical pattern ("demographic homogeneity was invisible from inside") is paraphrased faithfully from p.7. |
| Practitioner | APPROVE | The "Where It Shows Up Outside Science" section extends the construct to hiring filters, performance reviews, content moderation, etc. — labeled `[Inference]` because the paper does not extend that far itself. Status `emerging` is right. |
| Adversarial | APPROVE | Strongest counter: doesn't existing literature on algorithmic bias cover this already? Resolution: the *embedded biases* part is well-covered, but the *metacognitive illusion* — that users come to read AI as standpoint-free — is a distinct contribution at the human-cognition level. The draft makes this distinction explicit. No hype, no urgency. |

**Synthesis:** Paper-original construct that complements rather than duplicates the algorithmic-bias literature.
**Suggested action:** integrate

## scientific-monoculture.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The construct is paper-original; the agricultural metaphor is Messeri & Crockett's own (p.5). The empirical claims about cognitively/demographically diverse teams cite the source's reference numbers (122–124, 159–168) without restating them as if the draft ran the studies itself. The two sub-types (knowing, knowers) are kept distinct as in the paper. |
| Practitioner | APPROVE | The "How To Resist It" section is operational. The "Beyond Science" section is labeled `[Inference]` and conservatively extends the dynamic to other knowledge work. |
| Adversarial | APPROVE | Strongest counter: is this just an aggregation of `[[creativity-diversity-paradox]]` + `[[leveling-effect]]`? Resolution: those entries describe convergence at output and individual-capability levels; scientific monoculture describes convergence at the level of which questions get asked and which standpoints inform them. Different unit of analysis. The Related section cross-links explicitly. |

**Synthesis:** System-level construct that genuinely extends the KB upward.
**Suggested action:** integrate

## ai-vision-taxonomy.md

| Lens | Verdict | Concerns |
|---|---|---|
| Evidence | APPROVE | The four visions are presented exactly as in Table 1 (p.3). The risk profile per vision is paraphrased from the paper's own analysis (p.4–7). |
| Practitioner | APPROVE | The diagnostic protocol (name the vision, read the risk profile, etc.) is operational. The Strengths/Limitations section is honest. The "When NOT to use this" guidance is appropriately bounded. |
| Adversarial | APPROVE | Strongest counter: the taxonomy may be brittle (LLM tools cross categories; new visions emerge). Resolution: the Limitations section names this directly. Status `emerging` is justified. |

**Synthesis:** Useful diagnostic, well-scoped.
**Suggested action:** integrate

## UPDATE drafts (5)

All five UPDATE drafts are short, focused additions that extend existing entries without disrupting their voice. They each:
- Cite Messeri & Crockett (2024) explicitly.
- Use `[Inference]` for any synthesis beyond what the source directly supports.
- Add 1–2 wikilinks to the Related section that point to the new concepts being introduced in this same ingestion.
- Add the new source citation to the frontmatter `sources:` list.

Verdict per draft: APPROVE. No revisions needed.

## Decision

- **Outcome**: PROCEED_TO_INTEGRATE
- **Date**: 2026-04-30
- **Reason**: All drafts pass all three lenses and the AI failure checklist. Status calibration is correct (solid for replicated/peer-reviewed; emerging for new constructs). No false novelty, no hallucinated citations, no broken wikilinks (pending Stage 5 creation of the new entries).
