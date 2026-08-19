# Phase 5 - Debrief Closing Note

## Classification comparison

| | Self-audit tier (builder) | Peer audit tier (auditor) | Match? |
|---|---|---|---|
| RegGuard-Mini | Limited risk, transparency obligations under Article 50 | Minimal risk, with Article 50 logged as a minor finding | No, builder's tier confirmed correct after debrief |

## Where the tiers agreed or disagreed, and why

Both audits agreed the system clears Article 5 prohibited practices and sits outside all eight Annex III areas.

The disagreement was on the Article 50 trigger. The peer audit treated the chat interface as a disclosure gap on an otherwise minimal-risk system. The builder's self-audit placed more weight on the chat being connected to an LLM, which raises the stakes of that interaction beyond a simple disclosure fix, since generated text can be wrong or misleading in ways a static interface can't be, and that risk compounds with how the output gets used downstream. This pushed her to classify the system as limited risk rather than minimal risk with a minor finding attached. After discussion, this reasoning holds. Limited risk is the correct call.

The builder was also right on the Annex I question. She addressed Article 6(1) directly and flagged the tool's position relative to Annex I Section B as the weakest joint in the classification. The peer audit noted the tool sits outside the vehicle but didn't test that conclusion as rigorously.

## Gap list comparison

**Findings the self-audit caught that the peer audit missed:**
- Correct tier: limited risk, driven by the LLM-connected chat interaction, not just a disclosure add-on.
- The Article 6(1) / Annex I safety-component question, addressed directly and correctly identified as the weakest joint in the analysis.
- The marketing-drift scenario: if Onyx Dynamics ever markets the tool as compliance assurance rather than advisory guidance, the regulatory status changes even though the tool's design doesn't. Flagged as the single most important escalation.
- Article 25 exposure if a deployer substantially modifies the system or puts its own name on it, making that deployer a provider in its own right.
- A timing note on which AI Act provisions are actually in force, and a flag that the dates should be reconfirmed before the memo is acted on.
- A cross-check against the European Commission's compliance checker tool.

**Findings the peer audit caught that the self-audit missed:**
- Personal data retention and storage location for session data (questions, geometry references, report recipient details) was not addressed in the self-audit.
- Confirmation of what data reaches the third-party LLM vendor, and whether contractual terms prevent retention or training use, was not addressed.

## Joint closing note

Auditing your own work makes it easy to under-weight risks that are baked into decisions you already made without noticing, like treating an LLM-connected chat as a minor disclosure item instead of a tier-defining feature. The builder held the correct tier because she stayed closer to the system's actual mechanics. The external audit, working only from the brief, caught two things the builder's closeness to the project let slip past her: undefined data retention and unclear LLM vendor handling of confidential geometry. Neither view alone was complete. The best answer only came from combining an insider's grip on the mechanics with an outsider's willingness to question what the brief left unstated.