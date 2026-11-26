# Phase 5: Debrief - Model Intake Brief

> **Simulation disclosure.** Sergii was not available for a live debrief today (26 Nov 2026), and his own peer audit of Menohelp was also completed without a live exchange (see his [`simulation-disclosure.md`](https://github.com/s-rostovskyi/lab-eu-ai-act-peer-audit/blob/main/simulation-disclosure.md)).
> - **Real:** his system brief, his repo, and his **written self-audit and memo** ([assessment](https://github.com/s-rostovskyi/lab-eu-ai-act-self-audit/blob/main/deliverables/model-intake-eu-ai-act-assessment.md), [memo](https://github.com/s-rostovskyi/lab-eu-ai-act-self-audit/blob/main/deliverables/model-intake-compliance-memo.md)). I opened them only after `03` was finished.
> - **Builder responses (step 2):** taken from his written self-audit where it addresses the point (quoted or cited). Points it doesn't address are marked *simulated*.
> - **Closing note:** written by me alone. Sergii is unavailable, so there was no joint session. His perspective comes from his written self-audit, as in step 2. He has not reviewed or approved the note.

## 1. Auditor presents

I presented [`03-peer-audit-report-model-intake.md`](./03-peer-audit-report-model-intake.md) as written:
- **Tier:** limited risk, Art 50(2) only.
- **Six findings:** two significant ones (evidence integrity, no sign-off), plus legal-services positioning, which is significant before any paid offer.
- **Recommendation:** proceed with conditions.

## 2. Builder responds

| Point | Builder's context | Source |
|---|---|---|
| Is it even "placed on the market"? | The course demo, public code and a future market placement are distinct events. Art 2(8) excludes pre-market research and development, and public source alone doesn't make it a qualifying open-source release (Art 2(12)). | Self-audit, evidence base |
| Art 50(1) | He applies the first-interaction notice *conservatively*: the "obvious to a well-informed user" exception might apply, but he wouldn't rely on it without counsel. | Self-audit, Gap 1 |
| B2B exception | He considered the Commission's narrow route for controlled business-to-business deployments under the Art 50 guidance, and rejected it. Reports are downloadable and shared onward, and the prototype has no controls that would justify it. | Self-audit, Phase 2 |
| Data to OpenAI | The assessment request sets `store: false`, so OpenAI's own storage is narrower than I assumed. Vendor retention and transfers are still unverified. | Self-audit, Gap 3 |
| Stability | Only **6 of 15** core checks kept the same status over 5 runs, before the latest change. That is stronger evidence for my Finding 2 than I had. | Self-audit, Gap 4 |
| Prompt injection / self-declared sources | *Simulated:* "Quote verification and the approved-domain filter were meant to stop bad evidence, but I treated the source as trusted. A model card is the supplier talking about itself." | Not in self-audit |
| Legal-services positioning | *Simulated:* "I kept it as 'information, not legal advice' and didn't consider member-state rules on legal services." | Not in self-audit |

## 3. Compare classifications

| | Builder self-audit | Auditor (me) | Why they differ |
|---|---|---|---|
| Tier | Limited risk / transparency | Limited risk, at the low end | **Same tier.** |
| Art 50(1) | Apply notice conservatively; obviousness exception unconfirmed | Not triggered (no conversational interaction) | **A real regulatory disagreement**, not a gap in the brief. He reads "interacting" broadly, so a web form plus generated output counts. I read it as dialogue-like interaction. His reading is safer and cheap, and I adopt it. |
| Art 50(2) | Gap; method needs validating for mixed Markdown | Applies to status and gap explanation; *Minor* | **We agree it applies, but rate the severity differently.** He treats it as an open legal duty. I weighted it by harm. Both are defensible, but a legal duty that is unmet shouldn't be rated "minor" just because the harm is low. |
| Scope (Art 2) | Explicitly analysed (Art 2(8), 2(12)) | Not analysed | **The brief didn't communicate it,** and I didn't ask. I should have checked scope before tier. |

## 4. Compare gap lists

| Topic | Self-audit | Peer audit | Who caught it |
|---|---|---|---|
| Art 50(2) marking of generated findings | Gap 2 | Finding 3 | Both |
| Personal data in sources, vendor transfers | Gap 3 | Finding 5 | Both |
| Reviewer literacy + sign-off before reliance | Gap 4 | Finding 2 | Both. He had the stability number; I proposed renaming the status. |
| Art 50(1) first-interaction notice | Gap 1 | Not raised | **Self-audit only** |
| Art 2 scope and open-source question | Evidence base | Not raised | **Self-audit only** |
| Field-level provenance (quote vs interpretation) | Design reflection | Per-field label in Finding 3 | Both, from different angles |
| **Evidence integrity: self-declared sources, prompt injection** | Not raised | Finding 1 | **Peer audit only** |
| **Legal-services regulation, corpus staleness, liability** | Not raised | Finding 4 | **Peer audit only** |

**Pattern:**
- **The builder's strengths:** precise *legal mechanics*, such as scope, exceptions and the exact Art 50 limbs. He knows his system's facts well, for example `store: false`.
- **What the outside view caught:** risks that come from the *purpose and the environment*. Who writes the evidence? What does the label "Evidence found" do to a busy reviewer? What does selling a "compliance" product imply?
- **Shared blind spot:** neither of us started from the question "can the input be hostile?"

## 5. Closing note *(written by the auditor alone; the builder was unavailable)*

> Auditing your own system, you check the rules against what you *intended* it to do. That made the self-audit stronger on legal precision: scope, exceptions, and the facts only the builder knows. Auditing someone else's system, you look at what it *does* in the world: who writes its inputs, and how its outputs will be read and used. That surfaced risks the builder was too close to see. The two audits agreed on the tier and on three gaps. The most useful findings were the ones only one side found, so a real review needs both.

---

## Reinforce

**1. The questions Sergii asked me about Menohelp: which can't I answer?** From his [question log](https://github.com/s-rostovskyi/lab-eu-ai-act-peer-audit/blob/main/menohelp-classification-and-questions.md):
- **Q1** (approved intended purpose and any MDR/IVDR assessment): **can't answer.** There is no written intended purpose and no qualification assessment. My self-audit reached the same conclusion (Gap 1), but his question shows it isn't documented anywhere a reviewer could find it.
- **Q3** (vendor regions, retention, contracts): **only partly.** I know what *my* code sends, not what OpenAI, Supabase or Resend keep, or where.
- **Q5** (rights for coaching material in paid use; owners for incidents, literacy and change approval): **can't answer.** The rights are demo-only, and there are no named owners.
- **What this says about my documentation:** the README describes *how the system works* very well, but nothing about *who is accountable* and *what it is for*. Those are the two things an auditor asks first.

**2. A finding from Sergii's audit I initially disagreed with:**
- **His Finding 3:** "Failed checks do not prevent release". I checked the code (`app/agent/nodes.py`, `route_after_check` and `route_after_guard`). After the first attempt and 2 retries, both the number check and the wording check let the workflow finish anyway. The UI shows "All automatic checks passed" only on a full pass, but a failed report still reaches the reader.
- **My first reaction:** this felt unfair. The number check and guardrail are the most carefully built part of Menohelp, and the README calls the analysis "verified".
- **After the debrief:** I agree. "Verified" is a claim, and if the check can fail and the report still ships, the claim is false in exactly the cases that matter. My self-audit missed this because I knew the checks almost always pass. The fix is small: when checks still fail after the retries, withhold the report (and its download and email) and show a safe fallback instead.
