# Phase 5 – Debrief with the builder

**Participants:** Murat Çömez (auditor) · Max (builder) · **Date:** 18 Nov 2026 (written exchange on Slack)

## 1. Auditor presents
Walked through the audit report ([`03_audit_report_career_intelligence_agent.md`](03_audit_report_career_intelligence_agent.md)) without interruption.

## 2. Builder responds (5 min)
Based on the builder's written answers (18 Nov 2026, see [`02_clarifying_questions_log.md`](02_clarifying_questions_log.md)):
- **B2C only:** employer screening, applicant ranking and recruitment decisions are explicitly out of scope; any employer-facing use would trigger a new AI Act assessment.
- **Score is rule-based:** OpenAI never calculates or changes the score; it is used only for optional insights, which are off by default.
- **No sharing feature:** users can download reports and decide themselves whether to share them.
- **Better than the brief suggested:** the UI already describes the system as AI-assisted and explains that the score is not a hiring probability.
- **Confirmed open items:** no retention policy (reports with candidate data saved locally), transfers not verified, no fairness testing, no machine-readable AI marking.

## 3. Compare classifications
| | Tier | Basis |
|---|---|---|
| Builder's self-audit (Max) | _not shared in writing at submission_ | – |
| My audit | Limited risk / transparency (Annex III 4(a) open) | Art. 50(2); B2C purpose outside 4(a); Art. 6(3) profiling rule if B2B |
| Genuine disagreement about the law, or missing information in the brief? | **Missing information in the brief.** Max's written answers confirmed my assumptions (B2C only, rule-based score, no employer sharing). The open points were facts the brief did not state, not a different reading of the law. | |

## 4. Compare gap lists
| | Builder's top findings | My top findings |
|---|---|---|
| 1 | | F1 Business model and classification (Annex III 4(a)) |
| 2 | | F2 Art. 50(2) marking of AI-generated output |
| 3 | | F3 GDPR data flows to OpenAI / Tavily / Pinecone |

- What the builder knew that I could not see: the score is rule-based and AI features are off by default, which narrowed my Art. 50(2) and accuracy findings.
- What the external audit added: the Annex III 4(a) risk if reports reach employers, local storage of reports with candidate data and no retention policy, and no fairness testing. Max confirmed these as open items.

## 5. Joint closing note (written together with Max, 18 Nov 2026)
> Both projects are MVPs, so both audits found gaps, like no AI labels, unclear data transfers and no real human approval step. These are normal at this stage and can be fixed before real users or real data are involved.
>
> The debrief showed a difference: as builders, we judged what we planned to build, so some things felt clear to us. As auditors, we could only judge what was written in the brief, so the same things became open questions. In a self-audit you can add missing points from your own knowledge of the system; when auditing someone else's project, that is almost impossible. What is not written down is not a control. Self-audits know the system better, but external audits find the gaps.

## Reinforce (optional)
- Questions Max asked about my RCSA agent that I could not answer: which OpenAI entity, region, retention setting and transfer mechanism apply; and what accuracy thresholds and version records support the risk ratings. My answer to both was "not verified" / "not yet". This shows my documentation describes what the agent does, but not how it is governed (vendor terms, validation, versioning).
