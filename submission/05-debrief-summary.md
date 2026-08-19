# Phase 5 — Debrief Summary

**Participants:** Jay Ramamoorthi (auditor) and Anand Narasipuram (builder)
**System:** School Book Order Bot

## Comparing Classifications

Auditor's first-pass tier (pre-debrief): **Limited risk / transparency (Article 50)**, provisional — explicitly flagged as uncertain pending confirmation of who actually interacts with the bot.

Post-debrief tier (both agreed): **Minimal risk.**

The disagreement was not a genuine dispute about how the regulation works — both parties agreed on what Article 50 requires once the facts were established. It was a gap in what the documentation communicated: the README's architecture diagram depicts schools messaging the bot directly, which is not what actually happens. The deployer (Anand's father) is the sole point of contact — schools reach him via WhatsApp, and he manually relays orders into Telegram himself. Once that was confirmed, the transparency question resolved cleanly, since Article 50 protects the person interacting with the AI system, and that person is the deployer, who plainly knows it's automated.

## Comparing Gap Lists

Three of the five findings from the external audit (Article 50 disclosure, the README/pitch-deck architecture discrepancy, and cross-school data exposure via the publisher-consolidation command) all resolved via the same single fact revealed in debrief — that the deployer is the sole intermediary. This shows how one piece of operational context, invisible from documentation alone, can cascade through multiple findings that looked independent on paper.

Two findings (photo/OCR retention, sheet edit-access controls) were unaffected by this resolution and remain open — worth noting that not every finding an external audit raises depends on the same underlying fact, so resolving one doesn't automatically clear the rest.

## Joint Closing Note

This debrief showed that auditing someone else's work surfaces a different class of gap than auditing your own: documentation review correctly flagged a real transparency question that turned out to be moot, but only because the actual operational reality (who really talks to the bot) wasn't visible in any of the artifacts reviewed. As the builder, this was obvious enough that it never occurred to Anand to write it down explicitly — a classic case of information a builder holds implicitly but never states, because it feels self-evident from the inside. The value of an external audit here wasn't correcting a wrong conclusion, but forcing a genuine ambiguity into the open and requiring it to be resolved with a direct answer rather than an assumption — which is exactly what a real client engagement would need before anyone could sign off on a compliance memo.
