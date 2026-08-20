# Stretch — consulting work plan for Finding 1 (Article 50(1) disclosure)

Taking the Significant finding that goes to the heart of the classification: the system's only
tier-specific obligation is disclosure, and there is no evidence of it in the product.

**Deliverable that closes the gap.** Not a policy — a product change plus one page of copy:

1. A first-response disclosure line, injected in the bot's onboarding message and repeated in the
   daily digest footer: *"Whizbiz is an AI assistant. It reads your receipts and messages
   automatically — check figures before you file them."* One sentence discharges Article 50(1) and
   opens the Article 4 literacy point at the same time.
2. A short **limitations note** reachable by a `/about` command: what the bot reads, what it sends to
   an AI model, what it can get wrong, and the user's responsibility for the filed figures.
3. A one-paragraph **record of compliance** in the repository stating which obligation the wording
   satisfies and why — because the useful artefact at audit time is not the sentence but the reason
   it exists.

**Who is responsible.** The builder, for items 1 and 2 — both are edits to existing Telegram message
nodes and one new command branch, no architectural change. The provider entity, once decided, owns
item 3; if that is a Whizbiz company rather than an individual, the wording should be reviewed
alongside the subscriber terms.

**Realistic timeline.** Half a day for the copy and node edits, one day to review it against the
subscriber-facing material, so **within one week** and comfortably before any paid launch. This is
not the long pole — the GDPR blockers in the companion audit are.

**Evidence that would verify it is closed.** Three things, in order of strength: a screenshot of a
real conversation showing the disclosure on first contact; the workflow export showing the wording in
the message nodes, so it cannot be a demo-only change; and the `/about` output captured in the
repository. A verifier should test it as a **new** user, since a disclosure that only appears in
onboarding is invisible to anyone already using the bot — which is the most likely way this fix is
implemented and still fails.
