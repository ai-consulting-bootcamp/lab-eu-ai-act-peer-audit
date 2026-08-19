# Reinforce — reflections on the peer audit

## 1. The clarifying questions my teammate asked about my system

_Pending — to be completed once Vittal sends his questions about AI Pre-Scan. The exercise asks
whether any of them cannot be answered, and what that says about my documentation._

Recorded in advance so the answer is honest rather than retrofitted: the questions I expect to
struggle with are about **retention and deletion**, because until this week AI Pre-Scan had no
deletion path at all, and about **who the provider would be**, because it has never been placed on a
market. Both are gaps my own self-audit found, which suggests documentation written for engineers
answers "how does it work" fluently and "who is accountable for it" not at all.

## 2. A finding I initially disagreed with

_Pending the debrief — this asks about a finding in the report Vittal wrote on **my** system._

## 3. What auditing someone else's system taught me, before the debrief

Written now, so it is not contaminated by what the debrief reveals.

**External review is faster, and shallower, in the same places.** Reading Whizbiz's workflow, I found
the third-party customer data in about four minutes — it is a column heading, `Kunde`, and once seen
it cannot be unseen. Nobody who built the system would notice it, because the column is *obviously*
necessary for an invoice; the necessity hides the data subject. But I also could not tell whether any
of it had ever been used with a real customer, whether a DPA exists in a drawer, or where it runs in
production. A builder knows all three without asking.

**The self-audit's blind spot is intent; the peer audit's blind spot is fact.** In my own system I
discounted the evidence store because I knew it was "written, not yet read" — my knowledge of intent
told me it was inert, and that was exactly wrong for data protection. In Vittal's system I have no
intent to be misled by, but I had to assume five separate facts and log them, and any one of them
could invalidate a finding.

**The most useful thing I did was refuse to stop at one regime.** The AI Act audit of this system
lands on *proceed with conditions*; the GDPR audit lands on *do not proceed*. An auditor who ran only
the first would have handed a clean-ish report to a client about to process third-party data across
three borders with no contracts.
