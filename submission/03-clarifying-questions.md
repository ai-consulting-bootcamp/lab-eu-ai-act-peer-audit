# Phase 3: Clarifying Questions Log

## Question 1 — Bot disclosure on first contact

**What I need to know:** Does the system send any message identifying itself as an automated bot (not Anand's father / shop staff) before or during a school's very first interaction with it?

**Why it matters:** This is the single fact that determines whether Article 50's AI-disclosure obligation is met. The evidence available (README, exported n8n workflow, test report) shows a fallback help message that explains bot capabilities, but only *after* a message has already been sent — there is no visible "you are talking to an automated assistant" message shown at first contact in any of the provided materials.

**Provisional assumption in the absence of an answer:** Assuming disclosure is **not currently present** at first contact, since none of the three source documents show it. This is treated as the single most important open finding in this audit (see Finding 1 in the audit report).

---

## Question 2 — "Dad's checkpoint" discrepancy between README and pitch deck

**What I need to know:** The pitch deck's architecture slide shows a human review step ("Dad's checkpoint — reviews, confirms") and a confidence-check routing step (low-confidence matches → "unmatched queue") before an order is finalized. Neither of these appears in the README's architecture diagram or the exported `school_book_order_bot.json` workflow, both of which show the reply and log happening automatically with no human step. Which one reflects what's actually running in production — is the review step live, planned, or aspirational messaging for the pitch?

**Why it matters:** This materially affects the human-oversight picture. A live human checkpoint before an order is confirmed is a meaningfully stronger practice than a fully automated pipeline, even though this system's risk tier doesn't currently require it. It also affects how confidently this audit can describe the actual architecture.

**Provisional assumption in the absence of an answer:** Assuming the **README and workflow JSON are authoritative** (since they are the technical documentation, not marketing material) and that no human checkpoint currently exists before a reply is sent or an order is logged.

---

## Question 3 — Photo/OCR data handling and retention

**What I need to know:** When a school sends a photo of a handwritten order list (which may include a letterhead with the school's name and address, as seen in the test report's Fig. 6), is that image retained anywhere after parsing, or discarded immediately after the LLM extracts the order text?

**Why it matters:** This doesn't change the AI Act risk tier (the system still isn't evaluating a person), but it's a relevant parallel-legal question — if photos containing identifiable business/institutional letterhead information are stored, that has separate data-retention and GDPR-adjacent implications worth flagging, especially once this becomes a multi-tenant product per the GTM plan (Sprint 1) handling data from many distributors' schools.

**Provisional assumption in the absence of an answer:** Assuming images are processed in-memory and not persisted, since no image-storage step appears in the documented workflow — but this is genuinely unconfirmed, not verified.

---

## Question 4 — Who sees the unmatched-item and consolidated publisher-order data

**What I need to know:** The "generate publisher order" flow consolidates order data across multiple schools into one message. Who can trigger this flow — any school, or only Anand's father / authorized shop staff? Is there any access control on who can request a cross-school consolidated report via Telegram?

**Why it matters:** If any school (or anyone with the bot's Telegram handle) can trigger a report that reveals other schools' order volumes and pending items, that's a business-confidentiality issue between competing institutions, even though it stays outside AI Act scope. Worth checking now, since the GTM plan explicitly describes onboarding multiple distributors — this kind of cross-tenant data leakage risk gets more serious at scale, not less.

**Provisional assumption in the absence of an answer:** Assuming, without evidence either way, that this command is restricted to a known/authorized chat ID — but this is flagged as unconfirmed and worth verifying directly.

---

## Question 5 — Catalogue and tracking sheet access permissions

**What I need to know:** Who has edit access to the Google Sheets catalogue and orders-tracking sheet that the bot reads from and writes to?

**Why it matters:** Since pricing and order data flow directly from this sheet into what schools are told and billed, unrestricted edit access is an operational-integrity risk (accidental or unauthorized price changes propagate directly into live customer-facing replies) — not an AI Act issue, but a parallel operational-risk finding worth including.

**Provisional assumption in the absence of an answer:** Assuming standard Google Workspace access controls are in place (i.e., only Anand and his father have edit access), since this is the default expectation for a small family business's internal sheet, but unconfirmed.
