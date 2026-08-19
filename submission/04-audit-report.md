# Peer Audit Report — School Book Order Bot
**Auditor:** Jay Ramamoorthi
**System audited:** School Book Order Bot (Anand Narasipuram, Project 3)
**Materials reviewed:** README.md, stack_decision.md, gtm_future_sprints.md, exported n8n workflow (school_book_order_bot.json), Telegram testing report, pitch deck

---

## Section 1: System Summary

This is an n8n-based order-intake automation for a school textbook distribution business. Schools send book orders to a Telegram bot as typed text or a photo of a handwritten list. An LLM (GPT-4o-mini) parses the message and classifies it into one of four intents — place an order, check order status, generate a consolidated per-publisher order, or a non-order message. Matched orders are priced against a live Google Sheets catalogue using deterministic keyword-and-class matching, replied to the school automatically, and logged to a tracking sheet. The system also supports a cross-school view that consolidates all pending orders by publisher into a single purchase order. The intended production users are non-technical distributor office staff, with a documented go-to-market plan to onboard additional book distributors as customers.

## Section 2: Risk Classification

| Question | Answer |
|---|---|
| Prohibited category (Article 5)? | No — no manipulation, scoring, or biometric/emotional inference of any person. |
| Annex III area? | No. "Education" under Annex III covers AI that determines access to education or evaluates students (admissions, grading, proctoring). This system evaluates neither — it is a B2B order-processing tool between a distributor and school administrative staff, not a determination about any student. |
| Article 50 disclosure trigger? | **Resolved during debrief — no.** Schools never interact with the bot directly. They send orders to Anand's father via WhatsApp, and he personally re-enters them into Telegram. The only person actually messaging the AI system is the deployer himself, who plainly knows it is automated since he operates it. Article 50 protects the person *interacting with the AI system* from deception about what they're talking to — since that person is the deployer, not the schools, there is no undisclosed-AI-interaction problem. |
| **Final risk tier** | **Minimal risk.** |
| **Justification** | The system does not fall within any Article 5 or Annex III category, and the Article 50 question — initially flagged as a live open finding based on documentation alone — is resolved once the actual interaction structure is confirmed: schools never message the AI system directly, only the deployer does. |

**Resolution note:** this is a case where documentation-only review correctly identified a real ambiguity (Finding 1, originally rated Significant) that could not be resolved without direct confirmation from the builder. The debrief conversation, not the source documents, is what closed it. This is exactly the scenario the lab's Phase 5 process is designed to catch.

## Section 3: Role Map

| Role | Entity | Key AI Act obligations |
|---|---|---|
| **Provider** | Anand, who designed and built the system | If confirmed limited-risk: ensure the Article 50 disclosure is actually implemented. If confirmed minimal-risk: none specific to the Act. |
| **Deployer** | Anand's father / the family bookshop business, who operates the bot day-to-day as part of the business | Same as above — the obligation to disclose (if applicable) falls on whoever operates the live system schools interact with, which is the deployer in this relationship. |
| **Vendor — AI component** | OpenAI (GPT-4o-mini: intent classification, order parsing, and photo/vision parsing) | Carries its own general-purpose AI model obligations, separate from this system's classification. |
| **Vendor — infrastructure (non-AI)** | Google Sheets API (catalogue + tracking), Telegram Bot API (delivery channel) | No AI Act obligations — data storage and message-delivery infrastructure only. |
| **Vendor — deprecated** | Pinecone (originally used for catalogue semantic search, removed from the current version per stack_decision.md) | No current obligations — no longer part of the live system. |

**Note:** unlike the self-audited system, provider and deployer are held by two different people here (Anand builds; his father's business operates it day-to-day) — though Anand also appears operationally involved, so this may be a shared/blended role in practice. Worth confirming directly rather than assuming a clean split.

## Section 4: Compliance Findings

**Finding 1 — Article 50 bot-disclosure at first contact**
**Severity: Resolved (originally Significant)**
**Description:** Initial documentation review found no evidence of bot self-identification at first contact, and flagged this as a live Article 50 concern. **Resolved during the Phase 5 debrief:** schools never message the bot directly — they send orders to the deployer (Anand's father) via WhatsApp, and he manually re-enters them into Telegram. The only person interacting with the AI system is the deployer himself, who is fully aware it is automated. No disclosure gap exists.
**Recommended action:** None required. Recommend updating the README's architecture diagram, which currently depicts schools messaging Telegram directly — this is now confirmed inaccurate, not just incomplete (see Finding 2).
**Escalation needed?** No.

**Finding 2 — Architecture discrepancy between README/workflow and pitch deck (human review step)**
**Severity: Resolved (originally Minor)**
**Description:** The pitch deck's "Dad's checkpoint" step is confirmed accurate: the deployer is the sole point of contact between schools and the bot, manually relaying WhatsApp orders into Telegram. The README and workflow diagram, which show schools messaging the bot directly, are the inaccurate documents.
**Recommended action:** Update the README's architecture section to reflect the actual flow (school → WhatsApp → deployer → Telegram bot → deployer → school), since this is now a documentation-accuracy issue rather than an open compliance question.
**Escalation needed?** No.

**Finding 3 — Photo/OCR data retention unconfirmed**
**Severity: Minor — still open**
**Description:** Unaffected by the debrief resolution above. Photos of handwritten order lists (now confirmed to be forwarded by the deployer, originally received by him via WhatsApp) may contain school letterhead and identifying information. No documentation confirms whether these images are discarded after parsing or retained.
**Recommended action:** Confirm and document the retention behavior; if images are retained, establish a stated retention period and basis, particularly ahead of the Sprint 1 multi-distributor rollout.
**Escalation needed?** No, unless retention is confirmed and found to be indefinite/undocumented — in which case a brief data protection review would be worthwhile before scaling to multiple distributors' data.

**Finding 4 — Cross-school data exposure via "generate publisher order"**
**Severity: Resolved (originally Minor)**
**Description:** Resolved during debrief — since only the deployer can message the bot at all, no school can ever trigger the consolidated publisher-order view themselves. The access-control concern doesn't apply under the confirmed interaction model.
**Recommended action:** None required.
**Escalation needed?** No.

**Finding 5 — Catalogue/tracking sheet edit-access controls unconfirmed**
**Severity: Minor — still open**
**Description:** Unaffected by the debrief resolution. Pricing and order data flow directly from a Google Sheet into customer-facing replies; edit-access controls on that sheet are not documented.
**Recommended action:** Confirm standard access restrictions are in place; document this as part of onboarding procedure for the multi-distributor product described in the GTM plan.
**Escalation needed?** No.

## Section 5: Overall Recommendation

**Clear to proceed, minor issues noted.** The debrief conversation resolved the audit's one Significant finding (Article 50 disclosure) by clarifying the true interaction model: the deployer, not the schools, is the sole party interacting with the AI system, which removes the transparency concern entirely and confirms **minimal risk** as the final tier. Two minor, unrelated findings remain open (photo retention, sheet access controls) — neither blocks current single-business operation, but both are worth closing before the Sprint 1 multi-distributor rollout, where data-handling practices will be exposed to more parties and more scrutiny than in the current single-family-business context.

## Section 6: What This Report Is Not

This report is a first-pass, independent compliance review conducted by a peer without legal training, based solely on the documentation and code provided. It is not a legal opinion, not a formal conformity assessment, and not a certification. Conclusions — particularly the provisional risk tier, which depends on unresolved Clarifying Question 1 — should be verified with qualified legal counsel before relying on them for any EU market placement or client-facing compliance claim.
