---
status: solid
area: [erosion]
sources:
  - "Parasuraman & Riley (1997)"
  - "Goddard et al. (2012)"
  - "Jarmołkowicz (2025)"
  - "Gonzalez et al. (2026)"
  - "Shaw & Nave (2026)"
reviewed_by:
reviewed_date:
---
	
# Automation Bias

## What It Is

The tendency to over-trust automated systems and AI relative to your own judgment, leading to uncritical acceptance of machine-generated outputs even when they contain errors.

Shaw & Nave (2026) position automation bias as a related but narrower mechanism than [[cognitive-surrender]]. Automation bias focuses on specific errors of omission or commission in response to automated tools — failing to notice an AI error or accepting a specific wrong output. Cognitive surrender describes a broader disposition: the user doesn't just make an error of trust on one item — they stop deliberative thinking altogether and accept AI as the default cognitive locus. Automation bias can be a symptom of cognitive surrender, but surrender is the deeper structural shift.

## Why It Matters

Automation bias directly undermines quality evaluation—the core capacity needed to use AI effectively. If you systematically trust AI over your own judgment, you lose the ability to catch AI errors. And AI errors in areas beyond your competence may never surface.

Gonzalez et al. (2026) provide team-level evidence for automation bias as the primary barrier to human-AI complementarity. Their meta-analytic synthesis shows that poorly designed human-AI interaction — driven by overreliance on AI advice — can produce outcomes worse than either humans or AI working independently. This means automation bias doesn't just degrade individual performance; it can make the entire human-AI team worse than no collaboration at all.

## Key Insight

Creates a dangerous feedback loop:
1. Trust AI → don't verify → miss errors
2. Missing errors feels like AI was right
3. Trust increases → verify less
4. Capability to verify erodes

Appropriate reliance is learnable but not the default.

Shaw & Nave (2026) show that the feedback loop described here operates at scale: across 9,593 trials, participants who engaged AI followed its advice on ~80% of faulty trials (Study 1). The loop is not just about individual errors — it reflects a systemic reallocation of cognitive control to an external system. Their data also show that incentives + item-level feedback can partially break the loop (override rates doubled), suggesting the bias is malleable but persistent.

The complementarity framework identifies a structural mechanism: AI systems can "fail silently with high confidence when encountering unfamiliar conditions," while human vigilance degrades under fatigue and cognitive load. This creates a compounding failure mode where both parties miss errors simultaneously — the human trusts the confident AI, and the AI is confidently wrong.

Teams perform best when humans actively interrogate AI recommendations rather than passively accepting them (Vaccaro et al., 2024). Designing interfaces that surface uncertainty and rationales — rather than presenting clean recommendations — helps counter automation bias at the interaction level.

## Related

- [[fluency-bias]] - amplifies automation bias
- [[cognitive-offloading]] - automation bias makes offloading feel safe
- [[calibration]] - the skill that counters automation bias
- [[capacity-erosion]] - where automation bias leads
- [[human-ai-complementarity]] - automation bias is the primary barrier to achieving complementarity
- [[complementarity-framework]] - addresses automation bias through attention orchestration and interrogation protocols
- [[cognitive-surrender]] - broader phenomenon that automation bias sits within
- [[tri-system-theory]] - framework that contextualizes automation bias as one dynamic among several
