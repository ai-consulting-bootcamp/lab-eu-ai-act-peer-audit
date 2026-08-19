# LAB | Audit your teammate's project — EU AI Act

**Auditor:** Louise Plessis  
**Teammate / Builder:** Mudit  
**Project audited:** Board Game Concierge  
**Date:** 19 August 2026

---

# Lesson alignment

This audit applies the EU AI Act risk-tier, role-mapping, transparency, and compliance-gap framework covered in the lesson. It tests whether an independent reviewer reaches the same conclusions as the system builder and identifies differences between self-assessment and external review.

---

# Submission hygiene

This document contains only material relevant to the peer audit of Mudit's **Board Game Concierge** project. The filename identifies the auditor, teammate project, and regulatory lens.

---

# Kick-off

The peer audit was conducted independently on Mudit's Board Game Concierge project before the debrief.

## What you exchange

The initial audit was based on Mudit's system brief and the available technical/architecture documentation for Board Game Concierge.

His risk-tier classification, gap analysis, and compliance conclusions were not used to form my initial assessment. They were compared with my findings only during the debrief.

## Ground rules

I completed the initial classification, role mapping, and gap analysis independently.

Where information was unclear or incomplete, I documented written clarifying questions and stated my provisional assumptions before receiving Mudit's answers. His answers were then used to update the conclusions and complete the debrief.

---

# CFU checkpoints

## 1. Recognize

My first-pass classification is **limited risk / transparency**.

Board Game Concierge does not appear to involve any prohibited practice under Article 5 and does not operate in an Annex III high-risk area. Its intended purpose is recreational board-game assistance.

However, users interact directly with an AI-powered conversational system through Telegram. This makes the Article 50(1) interaction-transparency requirement relevant.

## 2. Probe

The three most important questions before confirming the classification were:

1. **Are users explicitly informed that they are interacting with AI?**  
   Provisional assumption: no disclosure was evidenced in the documentation.

2. **What user data actually pass through the system and third-party services?**  
   Provisional assumption: message content and some routing identifier are processed, but I did not assume additional identifiers or persistent storage without evidence.

3. **Do user messages or identifiers enter Pinecone or external search services?**  
   Provisional assumption: Pinecone contains rulebook chunks only; external search providers may receive user-derived queries.

These questions were sent to Mudit in writing and answered before the final debrief.

## 3. Map roles

**Provider:** Board Game Concierge project owner/operator, if the system is developed and put into service under their name. The provider is responsible for ensuring the final system meets applicable AI Act obligations, including transparency.

**Deployer:** If the same project owner operates the bot for users, they may also act as deployer/operator in that use context. Individual Telegram users using the bot for personal recreational purposes are recipients/users rather than organisational deployers.

**Upstream AI provider:** OpenAI provides the underlying AI/model service. Its obligations are distinct from the final-system provider's responsibility for the Board Game Concierge user experience.

**Other third-party services:** Telegram, n8n, Pinecone, SerpApi, Serper, and Tavily support communication, orchestration, retrieval, and search. Their main relevance to this audit is the parallel GDPR/vendor layer rather than changing the AI Act risk classification.

## 4. Find the gaps

Because the system is classified as limited risk / transparency rather than high-risk, the 11 high-risk provider obligations are not applied as a mandatory checklist.

The key AI Act gap is **Article 50 interaction transparency**. Mudit confirmed that users are currently not explicitly informed that they are interacting with an AI-powered assistant.

Parallel legal issues also arise under **GDPR**, because the system processes Telegram messages, identifiers, usernames/display names when present, preferences, and short-lived conversational context. Consumer-protection risk appears low in the current recreational context but would need reconsideration if the product or claims became commercial or consequential.

## 5. Debrief

The independent audit and Mudit's self-audit reached the same AI Act classification: **limited risk / transparency**.

The debrief confirmed that the main AI Act gap is the missing user-facing AI disclosure. It also surfaced implementation details that were not fully evidenced in the original documentation, particularly around user-data flows and third-party services.

---

# Core

# Phase 1 — Read and annotate

## System summary

Board Game Concierge is a Telegram-based AI assistant designed to help users play and choose board games. Users can ask questions about game rules, ask follow-up questions, receive strategy tips, and request recommendations based on criteria such as player count, playtime, and complexity.

Telegram is the primary user interface. n8n orchestrates the interaction and calls a FastAPI backend. The system uses OpenAI for conversational synthesis, Pinecone to retrieve imported rulebook content, local structured data for recommendations, and external search providers for some strategy queries.

The intended use is recreational board-game assistance. Nothing in the reviewed system description indicates use in employment, education, essential services, law enforcement, migration, biometric identification, justice, or another Annex III high-risk domain.

## Risk-relevant annotations

### Elements affecting the risk-tier classification

- Direct interaction between an AI system and natural persons through Telegram.
- Generative AI produces explanations, recommendations, and strategy responses.
- Intended use is recreational and low-consequence.
- No documented use in an Annex III high-risk domain.

### Elements initially unclear

- Whether users were explicitly informed they were interacting with AI.
- Whether the intended purpose could extend beyond recreational use.
- Which parts of the system process user-derived information.
- Whether user-derived information is stored by retrieval or search providers.

### Elements suggesting a specific obligation applies

- Direct conversational interaction triggers the Article 50(1) transparency analysis.
- Processing of user messages and identifiers creates parallel GDPR obligations.

---

# Phase 2 — First-pass classification

| Question | My answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No.** Nothing in the documented intended purpose suggests a prohibited AI practice. |
| Does this system operate in any of the eight Annex III areas? | **No.** The system provides recreational board-game information and recommendations and does not operate in an identified Annex III high-risk domain. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | **N/A.** |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **Yes.** Users directly interact with an AI-powered conversational bot through Telegram. |
| First-pass risk tier | **Limited risk / transparency** |
| One-sentence justification citing the specific Article or Annex entry | Board Game Concierge does not appear to fall under Article 5 or Annex III, but its direct conversational interaction with natural persons triggers the Article 50(1) transparency obligation. |

## Uncertainty at first pass

The risk tier itself was relatively clear. The main uncertainty was whether the Article 50 transparency obligation was already satisfied in the Telegram user journey.

That uncertainty was addressed through the written clarifying questions in Phase 3.

---

# Phase 3 — Clarifying questions log

## Question 1 — AI transparency

**What I needed to know:**  
When users first interact with the Telegram bot, are they explicitly told that responses are generated by or with AI?

**Why it matters:**  
This determines whether the Article 50(1) interaction-transparency requirement is already addressed.

**My provisional assumption:**  
I assumed the disclosure was not yet evidenced because I could not find it documented in the project documentation I reviewed.

**Mudit's answer:**  
No. He had a small subtext suggesting that responses were automatically generated via n8n, but removed it before the demo.

**Updated conclusion:**  
The transparency obligation is a confirmed gap rather than merely an undocumented safeguard.

## Question 2 — Personal-data flow

**What I needed to know:**  
Which Telegram data are sent through n8n to FastAPI and OpenAI — for example message text, username, chat ID, or other metadata — and what is retained?

**Why it matters:**  
This helps identify the system's actual interaction model and flags parallel GDPR obligations.

**My provisional assumption:**  
I assumed user messages must transit the orchestration/backend path to provide the service, but did not assume additional identifiers or persistent storage without evidence.

**Mudit's answer:**  
Message text, follow-up questions, Telegram user ID/chat ID, username/display name if present, user-stated game preferences/constraints, and short-lived conversation context/pending intent are processed.

**Updated conclusion:**  
The system processes more user-derived information than was explicit in the original documentation. This does not change the AI Act tier but creates a substantive parallel GDPR layer.

## Question 3 — Pinecone and external providers

**What I needed to know:**  
Does any user message, identifier, conversation history, or other user-derived information get embedded or stored in Pinecone or sent to external search providers?

**Why it matters:**  
This helps map third-party dependencies and parallel data-protection risks.

**My provisional assumption:**  
I assumed Pinecone stores the documented rulebook chunks only.

**Mudit's answer:**  
Not directly. Messages are reviewed and broken down to identify the core message and extract keywords, which are then sent as query parameters within API requests.

**Updated conclusion:**  
My assumption that Pinecone primarily stores rulebook material was correct. External search services receive transformed user-derived queries rather than full raw conversations.

## Question 4 — Storage

**What I needed to know:**  
Is conversation/session state persisted anywhere beyond the documented in-memory state?

**Why it matters:**  
Persistence affects the parallel GDPR assessment and helps determine whether the documented architecture reflects actual system behaviour.

**My provisional assumption:**  
Application session state is transient/in-memory, while vendor-side logging and retention remain unknown.

**Mudit's answer:**  
Conversation context is in-memory only for the active session.

**Updated conclusion:**  
Application-level conversation persistence appears limited. Vendor-side logging and retention remain a separate GDPR question.

## Question 5 — Intended purpose

**What I needed to know:**  
Is the intended use strictly recreational, or is there a plan to use the assistant in organised competitions or another context where outputs could determine more consequential outcomes?

**Why it matters:**  
A material change in intended purpose could require the AI Act classification to be revisited.

**My provisional assumption:**  
Recreational use only.

**Updated conclusion:**  
Nothing in Mudit's clarification contradicts the recreational intended purpose, so the classification remains unchanged.

---

# Phase 4 — Audit report

## Section 1 — System summary

Board Game Concierge is an AI-powered Telegram assistant providing board-game rules explanations, follow-up answers, strategy information, and recommendations. It combines OpenAI-based conversational generation with retrieval from a Pinecone rulebook knowledge base, local recommendation data, and external search APIs. User interactions are orchestrated through n8n and a FastAPI backend. Its intended purpose is recreational assistance rather than consequential decision-making.

## Section 2 — Risk classification

**Final classification: Limited risk / transparency**

There is no evidence of an Article 5 prohibited practice or Annex III high-risk use.

Article 50(1) is relevant because the system is intended to interact directly with natural persons. The principal uncertainty in the first-pass audit was whether the required transparency was already implemented.

Mudit subsequently confirmed that users are currently **not explicitly informed** that responses are AI-generated or AI-assisted. The transparency issue is therefore a confirmed gap.

## Section 3 — Role map

| Actor | Role | Key obligation / implication |
|---|---|---|
| Board Game Concierge project owner/operator | **Provider**, if developed and put into service under their name | Ensure the final system meets applicable AI Act requirements, including Article 50 transparency. |
| Board Game Concierge operator | **Potential deployer/operator** when operating the bot for users | Use the system consistently with its intended purpose and applicable instructions/obligations. |
| Telegram users | Recipients/users | Receive applicable AI-interaction transparency. |
| OpenAI | Upstream AI/model provider | Separate upstream regulatory role; does not remove the final-system provider's obligations. |
| Telegram | Third-party communication platform | Mainly relevant to parallel GDPR/data-flow obligations. |
| n8n | Workflow/orchestration service | Mainly relevant to parallel GDPR/data-flow obligations. |
| Pinecone | Vector database/infrastructure service | Mainly relevant to retrieval and parallel GDPR/data-flow obligations. |
| SerpApi / Serper / Tavily | External search services | Mainly relevant to parallel GDPR/data-flow obligations. |

## Section 4 — Compliance findings

### Finding 1 — Article 50 AI interaction disclosure

**Severity:** Significant

**Description:**  
Board Game Concierge directly interacts with natural persons through Telegram. Mudit confirmed that the current product does not explicitly tell users that they are interacting with an AI-powered system.

**Recommended action:**  
Add a clear AI disclosure in the Telegram `/start` or onboarding flow, visible **before or at the first AI-generated response**. For example:

> I'm an AI-powered Board Game Concierge.

Document the implementation so that the disclosure can be evidenced.

**Escalation needed?**  
No — product/builder can implement this directly.

**Evidence to close:**  
Screenshot or test recording of a new user's first interaction showing the disclosure, plus the corresponding `/start` configuration/code.

### Finding 2 — Transparency evidence and documentation

**Severity:** Minor

**Description:**  
The architecture documents AI use, but there is no current compliance artifact identifying where Article 50 transparency is implemented in the user journey.

**Recommended action:**  
Add a short transparency section to the README or compliance documentation identifying the disclosure text and where it appears.

**Escalation needed?**  
No.

**Evidence to close:**  
README/compliance documentation linked to the implemented user flow.

### Finding 3 — Parallel GDPR governance

**Severity:** Significant

**Description:**  
Mudit confirmed that the system processes Telegram user/chat IDs, usernames/display names when present, message text, preferences, and short-lived conversational state.

These facts do not change the AI Act classification but create parallel GDPR obligations concerning lawful basis, transparency, processors, retention, rights, and potentially international transfers.

**Recommended action:**  
Complete the GDPR data map, vendor-role analysis, retention assessment, privacy notice, and relevant processor/transfer checks.

**Escalation needed?**  
Yes — privacy/legal review before broader deployment.

**Evidence to close:**  
Completed data-flow map/vendor register and documented privacy controls.

### Finding 4 — Intended-purpose boundary

**Severity:** Minor

**Description:**  
The limited-risk classification is based on the current recreational purpose. A material repurposing into a consequential domain could change the regulatory assessment.

**Recommended action:**  
Document the intended purpose as recreational board-game assistance and require a new AI Act classification review before material expansion into consequential use cases.

**Escalation needed?**  
No under the current intended purpose.

**Evidence to close:**  
Documented intended-purpose statement in product/compliance documentation.

## Section 5 — Overall recommendation

### PROCEED WITH CONDITIONS

Board Game Concierge is appropriately classified as **limited risk / transparency**. Both the independent audit and Mudit's self-audit reached the same classification.

Deployment can proceed on the current recreational use case provided that the following conditions are addressed:

1. Implement an explicit AI disclosure in the Telegram `/start` or first-interaction flow.
2. Document and retain evidence of that transparency implementation.
3. Complete the parallel GDPR remediation identified in the GDPR audit before broader deployment involving personal data.
4. Reassess the AI Act classification if the intended purpose materially changes.

No prohibited or Annex III high-risk use has been identified, so no fundamental redesign is required.

## Section 6 — What this report is not

This report is not a legal opinion, not a conformity assessment, and not a certification. Conclusions should be verified with qualified legal counsel before being relied upon for EU market placement.

---

# Phase 5 — Debrief conversation

## 1. Auditor presents

I presented my independent audit classification of **limited risk / transparency**.

My reasoning was that Board Game Concierge does not fall within Article 5 or an Annex III high-risk area, but users directly interact with an AI-powered conversational system, making Article 50(1) transparency relevant.

My main AI Act finding was that the available documentation did not demonstrate an AI-interaction disclosure. I also flagged parallel GDPR issues because the system processes user-derived data and uses several third-party services.

## 2. Builder responds

Mudit confirmed that there is currently no AI disclosure. A small subtext had previously suggested that responses were automatically generated through n8n, but it was removed before the demo.

He also clarified that the system processes Telegram message text, user/chat IDs, usernames/display names when present, preferences, and short-lived conversational context.

He confirmed that conversation context is in-memory only for the active session and that raw user messages are not directly stored in Pinecone or sent as-is to external search providers.

## 3. Compare classifications

**Auditor:** Limited risk / transparency.

**Builder:** Limited risk / transparency obligation under Article 50.

**Result:** Full agreement.

Both audits concluded that the system falls outside Article 5 and Annex III while triggering Article 50 transparency because of its direct conversational interaction with users.

## 4. Compare gap lists

### Builder's self-audit identified
- No AI disclosure.
- No privacy notice.
- No retention schedule.
- No RoPA.
- No DPA evidence.
- No documented deletion workflow.
- No data-subject-rights workflow.
- No incident-response process.

### External audit emphasis
My external AI Act audit focused especially on:
- whether Article 50 disclosure could actually be evidenced in the user journey;
- the distinction between the AI Act classification and parallel GDPR obligations;
- unclear third-party data flows;
- the need to document the intended-purpose boundary.

### What the self-audit caught that the external audit did not initially foreground
Mudit's self-audit identified several formal GDPR governance artifacts — particularly the RoPA, incident-response process, and deletion workflow — that were not central to my first-pass AI Act audit.

### What the external audit surfaced
The external review highlighted that implementation intent is not enough: an auditor needs evidence that the disclosure is actually present. It also surfaced uncertainties around exact vendor payloads, n8n execution-history retention, possible vendor reuse of prompts/queries, and FastAPI data handling that were not fully documented.

## 5. Joint closing note

The debrief showed that auditing your own system gives you stronger implementation context, while an external audit is more likely to challenge what is actually evidenced in the documentation. In this case we reached the same AI Act classification, but the independent review made the missing Article 50 disclosure especially visible because it could not rely on the builder's knowledge of how the interface was intended to work.

---

# Reinforce

The peer audit showed that technical intent and compliance evidence are not the same thing.

A builder may know that a system is recreational and low-consequence, but an external reviewer can only rely on what is documented and visible in the product. The missing AI disclosure is a good example: the product previously contained a hint that responses were automatically generated, but because that disclosure was removed, an external auditor correctly treats transparency as a current gap.

The review also showed a documentation gap around third-party processing. Mudit could answer questions about the intended architecture, but exact vendor payloads, n8n execution retention, vendor reuse, and some FastAPI processing were not fully evidenced in the project documentation.

---

# Stretch — Consulting work plan

## Significant finding selected — Missing Article 50 AI transparency

**Deliverable:**  
Implement and document an AI-interaction disclosure in the Telegram onboarding flow.

**Responsible owner:**  
Product/builder.

**Timeline:**  
One working day for implementation, testing, and documentation.

**Implementation:**  
Add a clear statement in `/start` or equivalent onboarding so that a new user sees it before or at the first AI-generated response.

Example:

> I'm an AI-powered Board Game Concierge. I can help explain rules, answer questions, suggest strategies, and recommend games.

**Evidence required to verify closure:**
- Screenshot or recording of a fresh user's first interaction.
- `/start` configuration/code containing the disclosure.
- README or compliance documentation identifying the disclosure requirement and implementation point.
- Simple test confirming the disclosure appears for a new user before or with the first AI response.

Once those artifacts exist, the Article 50 transparency finding can be considered remediated.
