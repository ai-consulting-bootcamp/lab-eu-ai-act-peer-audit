# Debrief Notes: Peer Audit of DrugDev-AI

**Auditor:** Zahra Moghaddasi · **Builder:** Nevena · **Status:** Held

Debrief held 2026-08-18, following Phase 5 of `instructions.md`.

---

## 1. Auditor presents
Walked through `peer-audit-drugdev-ai.md` with Nevena, start to finish, without interruption. Nothing in the report was disputed at this stage, she agreed with the classification, the role map, and all five findings as presented.

## 2. Builder responds
Nevena agreed with the audit as presented, no corrections, missing context, or pushback on any of the findings.

## 3. Compare classifications
- Nevena's self-audit tier: Limited risk, transparency obligations. Her own justification: "DrugDev-AI is a general-purpose AI application that generates content for end users but does not fall under Article 5 prohibited practices or Annex III high-risk systems, therefore, Article 50 transparency obligations are the primary AI Act requirement."
- Auditor's (this) tier: Limited risk, transparency obligations, with the Annex III education question mostly resolved by her brief but still flagged for direct confirmation (see Finding 3)
- Where they differ and why (a genuine regulatory disagreement, or a communication gap in the brief): We landed on the same tier. Worth discussing in the debrief: whether she considered the Annex III(3)(b) education angle for Learn mode at all, or ruled it out for a different reason than the one in my report.

## 4. Compare gap lists

Prepared from Nevena's self-audit gap analysis (`DrugDevAI_audit.md`, same PR) against my findings in `peer-audit-drugdev-ai.md`. Both land on the same three core areas: missing AI-interaction/transparency notice, missing verification or reliance guidance, and a GDPR privacy-documentation gap. Details below to confirm together in the live debrief.

- Findings the self-audit caught that this external audit missed:
  - Nothing structurally new, her three gaps line up with my Findings 1, 2, and 4.
  - She went further on one point: she drafted the actual ready-to-use Transparency Notice text, instead of just recommending one in the abstract like I did.
  - She named the escalation contact specifically (Data Protection Officer or privacy specialist) for the privacy gap, where I said "confirm data-processing agreements" more generally without naming a role.

- Findings this external audit caught that the self-audit missed:
  - A more specific version of the third-party data-flow gap: I called out data residency and model-training opt-out for OpenAI, Pinecone, and Cohere by name, her Gap 3 covers privacy documentation more broadly without naming those specifics.
  - I raised a skepticism point her self-audit could not really raise about itself: her own brief claims "all outputs are reviewed by the user before any action is taken," but nothing in the visible UI code (`src/app.py`) enforces or reminds the user to do that. Her self-audit's Gap 2 recommends verification guidance too, but does not connect it back to that specific claim in her own brief.
  - A different escalation call on the verification/reliance gap: she marked her equivalent Gap 2 as "Escalation Needed: No," I marked mine as "Yes, legal or compliance review before commercial launch." Worth discussing whether that is a real disagreement or just a different read of how urgent it is.
  - Note: she did explicitly rule out Annex III education (she names "employment, education, law enforcement, migration, essential public services" in her first-pass reasoning), so my earlier open question on that front was not something she missed, just something I reasoned through in more detail before landing in the same place.

## 5. Joint closing note

Auditing your own work is both easy and difficult at the same time: you know the system well enough to design real fixes fast, but that same closeness makes you stop questioning assumptions you have already internalized as true. Auditing someone else's work has the opposite trade-off: an outside auditor has no such blind spot, but also no shortcut to the fix, only the gap. Neither view alone is complete, the debrief is where the two get reconciled.
