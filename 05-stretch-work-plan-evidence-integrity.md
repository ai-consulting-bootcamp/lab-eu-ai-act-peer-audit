# Stretch: consulting work plan - Finding 1 (evidence integrity, Significant)

**Problem:** the evidence Model Intake Brief assesses is partly written by the party under review (model cards, provider pages). That text goes into the prompt unguarded, so a supplier could steer statuses through over-claiming or planted instructions.

| | Plan |
|---|---|
| **Deliverables** | 1. **Technical change** in `assessment.py`: sources passed as delimited, quoted data, with an explicit rule that text inside sources is evidence, never instructions. A pre-check flags instruction-like phrases ("ignore", "mark as", "assistant:") and records them in the report. 2. **Source-type label** on every finding: *self-declared* (model card, provider docs) or *independent* (third-party evaluation, regulator, audit). The summary shows "X of 15 findings rest only on self-declared sources". 3. **Adversarial test fixtures:** a model card with a planted instruction, one that over-claims every checklist item, and one with a claim for a different model variant. 4. **Instructions-for-use paragraph:** "Evidence found means the supplier documents it, not that it is true." |
| **Owner** | Builder (Sergii) for 1–3. Client governance lead approves 4 and the acceptance thresholds. |
| **Timeline** | About 1 week: 2 days for the prompt and pre-check, 1 day for labels and the summary, 2 days for fixtures and tests, half a day for docs. Done before the Sprint 2 inventory pilot. |
| **Evidence it's closed** | 1. The new tests pass in CI: the planted instruction changes **no** status and is flagged in the report; the over-claiming card yields findings labelled *self-declared*. 2. A 5-run stability check on an adversarial fixture shows no status drift attributable to the injected text. 3. Two sample reports regenerated with source labels, reviewed by the client's governance lead. 4. The USER_GUIDE diff shows the new paragraph. |
