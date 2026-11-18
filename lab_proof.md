# Lab Proof: Audit your teammate's project

**Auditor:** Elif Yurdakul · **Teammate:** Pieter · **Project audited:** Pieter's Project 3, *Vendor Due Diligence Agent* (pre-screening companies before onboarding, for compliance officers at Dutch regulated firms)

## File map
| File | Contents |
|---|---|
| `lab_proof.md` | Entry point: annotations, classification, clarifying questions, debrief, closing note, stretch |
| [`peer_audit_report_pieter_vendor_screening.md`](peer_audit_report_pieter_vendor_screening.md) | Phase 4: the two-page audit report |
| `Pieter_Phase1_system_brief.pdf` | The input: Pieter's system brief (the only material I received) |

**Input:** Pieter's Phase 1 system brief. **Output:** the audit report. I did not see his classification, gap analysis or memo before the debrief.

---

## Phase 1: Annotations

| Element in the brief | Mark | Why |
|---|---|---|
| "pre-screens one company before it becomes a vendor" | 🔵 Affects tier | Subject is a company, not a person: keeps it out of credit scoring (Annex III 5(b)) and employment (Annex III 4) |
| "Code then screens… against sanctions and PEP data" | 🔵 Affects tier · 🟢 Obligation | Objective list matching, not profiling (relevant to Art. 5(1)(d)); PEP data is personal data |
| "people named in news… in connection with alleged crimes. They don't know they're being screened" | 🟢 Obligation | Criminal-offence data (GDPR Art. 10), information duty, DPIA |
| "The AI proposes a risk rating… code sets a minimum rating the AI can raise but never lower" | 🔵 Affects tier | Strong control; AI output is advisory |
| "It does not approve or reject the vendor" / "A compliance officer reads every report and makes the decision" | 🔵 Affects tier | Human decision, preparatory role |
| "In the MVP, no one checks the report before the officer sees it" | 🟠 Unclear | What does the officer have to check? Are overrides logged? |
| "Vendors, who may be delayed or turned down" | 🟠 Unclear | Are vendors only companies, or also sole traders and freelancers (natural persons)? |
| "LangSmith (tracing)" | 🟢 Obligation | Stores full run data, including personal data, with a US provider |
| "OpenSanctions sanctions and PEP data" | 🟢 Obligation | Licence terms for commercial use |
| "Compliance officers at Dutch regulated firms (law firms, notaries, payment companies)" | 🟠 Unclear · 🟢 Obligation | Wwft obliged entities, but Wwft covers clients, not vendors: legal basis for vendor screening? Will it ever be used for client due diligence? |
| "KvK (in the MVP its test environment, with fictitious data)" | 🔵 Affects tier | MVP uses no real KvK data; production will |

🔵 = affects the risk tier · 🟠 = unclear, needs clarification · 🟢 = suggests a specific obligation

---

## Phase 2: First-pass classification

| Question | My answer |
|---|---|
| Does this system fall under any prohibited category (Art. 5)? | **No.** Closest is Art. 5(1)(d) (predicting criminal risk of a person based solely on profiling). It assesses companies, uses objective, verifiable data (official lists) and supports a human assessment. |
| Does it operate in any of the eight Annex III areas? | **No.** Not credit scoring of natural persons (5(b)), not employment (4), not law enforcement (6, the user is a private firm), not essential public services. |
| If Annex III: significant influence or narrow/preparatory? | Not applicable. If it were, the officer's decision and the advisory rating would point toward preparatory. |
| Does it interact with end users or generate content requiring disclosure (Art. 50)? | **No.** It does not interact with the public and does not publish AI-generated text; the user is a professional. Voluntary labelling of AI-written parts is still recommended. |
| First-pass risk tier | **Minimal risk** (AI Act), with significant obligations under **GDPR, sanctions and AML rules** |
| One-sentence justification | The system screens companies against official lists and proposes an advisory rating for a human decision, so it falls outside Art. 5 and Annex III; the main legal weight lies in GDPR Art. 10 data about people named in the sources. |

**Uncertainty:** the tier could change if vendors include natural persons (sole traders) or the tool is extended to client due diligence. Questions 1 and 2 below resolve this.

---

## Phase 3: Clarifying questions log
*Information requested from client (Pieter) in writing on [date].*

| # | What I need to know | Why it matters | Provisional assumption |
|---|---|---|---|
| 1 | Do vendors include sole traders or freelancers (natural persons), or only companies? | If it screens individuals, it evaluates natural persons: Art. 5(1)(d) and profiling need a second look, and GDPR duties grow. | Mostly companies; some sole traders possible, so treat it as a risk to manage. |
| 2 | Will the tool only be used for vendor checks, or also for client due diligence under the Wwft? | Client checks of natural persons are much closer to Annex III and have a different legal basis. | Vendor checks only. |
| 3 | What personal data goes to OpenAI, Tavily and LangSmith, and how long is it kept? | Data transfers to the US, a second copy of sensitive data in tracing logs, retention. | Names, news snippets and red flags go to all three; LangSmith keeps full traces with default retention. |
| 4 | Does any output trigger an automatic action (e.g. auto-reject on "Do not onboard")? | An automated decision with significant effect would bring in GDPR Art. 22 and weaken the "preparatory" argument. | No: the officer always decides. |
| 5 | Will it be offered to other firms commercially, or used in-house? | Determines whether Pieter is a provider placing it on the market, and whether OpenSanctions' commercial licence is needed. | Offered commercially to Dutch firms. |

---

## Phase 4: Audit report
See [peer_audit_report_pieter_vendor_screening.md](peer_audit_report_pieter_vendor_screening.md).

**Summary of findings:**
| # | Finding | Severity |
|---|---|---|
| 1 | Legal basis for PEP and adverse-media screening of vendors; criminal-offence data (GDPR Art. 10) | Significant (Blocking if no basis) |
| 2 | No DPIA | Significant |
| 3 | Personal data to US services, incl. LangSmith tracing | Significant |
| 4 | False matches can harm people and vendors | Significant |
| 5 | OpenSanctions licence for commercial use | Significant (production) |
| 6 | Human oversight and automation bias | Minor |

**Recommendation:** Proceed with conditions.

---

## Phase 5: Debrief with Pieter
*[Fill in after the conversation.]*

| | Pieter (self-audit) | Elif (peer audit) | Agree? |
|---|---|---|---|
| Risk tier | [ ] | Minimal risk (AI Act); main weight in GDPR | [ ] |
| Top findings | [ ] | Legal basis / Art. 10 data · DPIA · US tracing · false matches · data licence | [ ] |



**Joint closing note (required):**
[Write together with Pieter, 2–3 sentences. Possible starting point: *Auditing someone else's system made the gaps between what the brief says and what the system does visible; the builder knew the context, the auditor saw the assumptions. Both of us found the legal weight outside the AI Act (in GDPR for Pieter, in consumer protection and profiling for Elif), which the builder had treated as background.*]

---

## Reinforce
- **Questions Pieter asked about my system that I couldn't answer:** Nothing is asked I can't answer. The biggset issue is sending personal data to llm or not and I do not send user's personal data to llm only code reads the data. 
- **A finding from Pieter's audit of my project I first disagreed with:** Nothing

---

## Stretch: work plan for Findings 1 + 2 (legal basis and DPIA)

| | |
|---|---|
| **Deliverable** | (1) A short legal-basis memo per screening type (sanctions, PEP, adverse media) for vendor checks. (2) A DPIA template customers complete before use, plus a technical change: store only the hits and the data needed for the decision, with a retention limit. |
| **Responsible** | Pieter (data flows, technical change, DPIA draft) · external privacy lawyer (legal basis, Art. 10) · the customer's data protection officer (final DPIA) |
| **Timeline** | Weeks 1–2: data flow map and DPIA draft · weeks 2–3: legal review · week 4: technical changes (minimisation, retention, tracing off) · week 5: customer DPO sign-off |
| **Evidence it is closed** | Signed legal memo; completed DPIA with residual risks accepted by the DPO; configuration showing tracing disabled and retention set; a test run showing only necessary personal data stored |

---

## Failure or limitation of this audit
I only had a one-page brief. I could not see the code, the actual data flows or what LangSmith stores, so Findings 3 and 4 rest on assumptions that are logged above. My legal points on the Wwft and OpenSanctions licensing are first-pass and need confirmation by a lawyer.