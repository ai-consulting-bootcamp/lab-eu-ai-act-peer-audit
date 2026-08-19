# Phase 1 — Read and Annotate

*First read: the README, stack_decision.md, and gtm_future_sprints.md were read once through without notes, to get the overall shape of the system before analyzing it. Second-pass annotations below.*

## Elements That Affect Risk Tier Classification (underlined)

- **"Schools send their book orders via Telegram"** — establishes this as a live, message-based system with an end user on the other end, not a one-shot report tool. This is the detail that put Article 50 in play at all.
- **"non-technical office staff, not a developer"** as the intended end user — relevant to who is actually meant to operate the system, which matters for the deployer question.
- **The four-way intent classification (order / status / publisher_order / other)** — confirms the LLM's role is narrowly scoped (classification and parsing), not open-ended reasoning or a decision made about a person.
- **No student, applicant, or individual is ever scored or evaluated anywhere in the described flow** — the system's subject throughout is book orders and catalogue matching, which is what ultimately ruled out Annex III's "education" category.
- **The GTM plan's Sprint 1 (multi-distributor onboarding)** — relevant not to the current tier, but to how the system's data-handling practices will need to scale beyond one family business.

## Elements That Were Unclear (circled)

- **The README's architecture diagram shows "Telegram message (text or photo)" flowing directly from an unlabeled source** — it never explicitly states *who* sends that first message. This ambiguity is exactly what later became Clarifying Question 1 and the audit's central finding.
- **The pitch deck's "Dad's checkpoint — reviews, confirms" step**, which appears nowhere in the README or the exported workflow JSON. Two source documents describing the same system inconsistently, with no way to tell from the documents alone which one is current.
- **Photo/OCR handling** — the README describes photo intake as a supported input type but never states what happens to the image after parsing (discarded vs. retained).
- **Access control on the Telegram bot itself** — nothing in the README or workflow specifies who can message the bot, which left open whether schools could directly trigger flows like the cross-school publisher consolidation.
- **Google Sheets edit permissions** — referenced as the data store for catalogue and orders, but access-control setup is never described.

## Elements That Suggest a Specific Obligation Applies (marked)

- **The live, repeated message-exchange structure** — this is what suggested Article 50 might apply at all, as distinct from a one-shot input/output pipeline (like the should-cost benchmarking system audited separately), which has no comparable disclosure question.
- **The "This message was sent automatically with n8n" footer visible in Telegram screenshots** in the test report — noted as a *candidate* disclosure mechanism, but flagged as likely insufficient on its own, since it's a platform-level branding footer rather than a deliberate, user-facing statement that the sender is an AI system.
- **The fallback "hi" response** explaining the bot's capabilities — noted as informative but happening *after* first contact, not as an upfront disclosure.

These annotations directly informed the Phase 2 classification table and became the basis for the five clarifying questions logged in Phase 3.
