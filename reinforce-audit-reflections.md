# Reinforce — reflections on the peer audit

## 1. The clarifying questions my teammate asked about my system

Received: five questions on AI Pre-Scan. I predicted, before seeing them, that I would struggle on
**retention and deletion** and on **who the provider would be**. Half right — and the miss is the
interesting part.

| His question | Can my documentation answer it? |
|---|---|
| Q1 — market placement, or builder-only? | **Yes.** The proposal and README describe a named buyer and GTM sprints; his provisional assumption (provider frame applies) is right |
| Q2 — do findings ever assess an identifiable person? | **Yes**, and precisely: the report spec restricts the subject to organisations, and `LESSONS.md` records that quotes may name someone incidentally |
| Q3 — what editorial step does the adviser apply before handing a report to a client? | **No. Nothing in my documentation answers this**, and I had never asked it |
| Q4 — transfer mechanism for OpenAI and Pinecone? | **Yes** — my own docs say it is absent and required before real client use. He credited the project for stating it rather than treating it as his discovery |
| Q5 — who holds provider responsibility, individual or entity? | **No.** Predicted, and confirmed |

**What the one unpredicted gap says.** I expected to fail on questions about *documents I have not
written*. Q3 is different: it asks about a **step in someone else's workflow** — what the adviser
does between receiving a report and handing it to a client. My documentation describes my system
exhaustively and stops precisely at its boundary, and the entire Article 50 question turns on what
happens one inch past that boundary. Writing for engineers produces documentation that is complete
about the artefact and silent about the workflow it sits inside; a compliance reader needs the
second more than the first.

## 2. A finding I initially disagreed with

**His Finding 1 — Article 50(2) synthetic-content marking on the generated report.**

**Why I disagreed at first.** My instinct was that AI Pre-Scan does not *generate* content in the
sense Article 50(2) targets. Its outputs are extractions: a quoted passage lifted verbatim from a
source page, a vendor name, a date, a confidence value. The whole architecture exists to stop the
model producing anything that is not anchored to retrieved text, and Article 50(2) carries an
exemption where a system performs an assistive function for standard editing or does not
substantially alter the input data or its semantics. Marking a table of quotes as "AI-generated"
felt like it would mislabel the artefact and, worse, dilute the disclosure for cases that really are
synthetic.

**Why I now think he is more right than I was.** Three reasons, and the first is the one that moved
me. The report is not only quotes: the **discussion list is genuinely generated prose** — questions
phrased for a client by a model, present in every report, including the ones where no evidence was
found and the discussion list is the entire deliverable. The exemption cannot cover that. Second, my
counter-argument is an argument, and Article 50 questions get decided on what the recipient could
reasonably believe, not on how the builder characterises his own pipeline — a client receiving a
polished document from their adviser has no way to tell extraction from generation. Third, and this
is the part I would have been slowest to concede: my own report spec fixes a standing legal notice
that is *"not editable by any generation step"*, which I had always thought of as a safeguard.
Vittal read the same rule as evidence **against** the human-editorial exemption — if the notice
cannot be edited, the document is not one the adviser has taken editorial responsibility for. Same
sentence, opposite inference, and his reading is the one a regulator would more plausibly take.

**Where I still hold ground.** He classes it Significant and escalates it as "launch-blocking". I
would keep it Significant but note that the fix is a line of text plus a documented review step, and
that the exemption question is genuinely open rather than settled against me. The disagreement is now
about severity and confidence, not about whether there is a finding — which is a much better place to
be than where I started, which was "this does not apply to us".

## 3. What auditing someone else's system taught me

Written before the debrief, and left unedited afterwards so the prediction can be checked against
what actually happened.

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


## 4. Checked afterwards — did section 3 hold up?

It half held. "External review is faster and shallower in the same places" was right: I found the
third-party customer data in minutes and could not tell whether it had ever touched a real customer.
But I claimed the peer audit's blind spot is *fact*, and the debrief showed something sharper — the
facts I could not see were not incidental details, they were the ones that **changed a finding's
shape**. `Kunde` and `Addresse` are mandatory content of a German invoice, which I could not have
known, and that single answer turned a vague necessity complaint into a precise notice gap.

The symmetrical thing happened to me: Vittal could not see, from my repository, what happens between
a report being printed and a client reading it — because nothing I have ever written describes it.
Each of us was blind in exactly the place the other's answer lived, which is a better argument for
peer audit than "fresh eyes".
