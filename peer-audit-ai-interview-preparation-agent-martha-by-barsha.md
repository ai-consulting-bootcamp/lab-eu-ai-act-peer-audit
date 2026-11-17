# Peer Audit - AI Interview Preparation Agent (Martha's Project 3)

**Auditor:** Barsha Mishra
**Builder / client:** Martha
**System audited:** AI Interview Preparation Agent (n8n workflow, Ironhack Project 3)
**Source used:** Martha's system brief for independent peer audit, received 16 November 2026. I did not see Martha's self-audit before writing this.
**Date:** 16 November 2026

---

## Phase 1 - Read and annotate

Key:
- **[TIER]** = affects the risk tier
- **[UNCLEAR]** = needs clarification
- **[OBLIGATION]** = suggests a specific obligation applies

| # | Element in the brief | Mark | Why it matters |
|---|---|---|---|
| 1 | "helps a job seeker prepare for an interview" / "not an employer's applicant-screening or hiring-decision system" | [TIER] | The stated intended purpose. If the tool were used for recruitment or selection, it would fall under Annex III point 4(a) (employment). Used by the candidate for themselves, it does not. |
| 2 | "outputs are generated text and preparation suggestions, not a numerical hiring score, automated rejection or employment decision" | [TIER] | Supports "no decision about people". |
| 3 | "In a live deployment, the workflow operator would manage the n8n environment" | [UNCLEAR] | Who is the operator: Martha, a career coaching service, a bootcamp, a job centre, or a recruiter? This decides the deployer and could change the tier. |
| 4 | "uploads a CV in PDF format and gives the requested consent" | [OBLIGATION] [UNCLEAR] | Personal data, so GDPR applies. What does the consent cover? German CVs often include photo, birth date, nationality or religion, which can be special-category data (GDPR Art. 9). |
| 5 | Context sent to "OpenAI GPT-4o-mini" | [OBLIGATION] | CV data goes to a US AI provider, which raises GDPR processor and transfer questions. OpenAI is a general-purpose AI (GPAI) model provider. |
| 6 | "The workflow also creates a formatted report in Notion" | [OBLIGATION] [UNCLEAR] | Personal CV-based reports are stored in a third-party workspace. Who can access it, and for how long? |
| 7 | "draft a structured, seven-section interview preparation report" / "suggested STAR-style examples" | [OBLIGATION] | AI-generated text, so Article 50(2) marking may apply. The STAR examples could include experiences the candidate never had. |
| 8 | "There is no documented mandatory expert review of each report" | [OBLIGATION] | No human check before output. This is acceptable at minimal risk, but it creates an accuracy risk. |
| 9 | "Tavily search and NewsAPI", "Pinecone knowledge base ... 2025 annual reports" | [UNCLEAR] | Third-party vendors. Tavily is an AI-powered search API. News results may contain personal data about company staff. |
| 10 | "tested with synthetic candidate information" | [TIER] [UNCLEAR] | It is a prototype. Production use with real CVs is not yet designed. |

---

## Phase 2 - First-pass classification

| Question | Your answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No.** There is no manipulation, exploitation of vulnerabilities, social scoring, biometric categorisation or emotion recognition. It does not assess the candidate in any way that leads to treatment by others. |
| Does this system operate in any of the eight Annex III areas? | **It touches the employment area (Annex III point 4) but, as described, is not covered by it.** Point 4(a) covers AI used *for recruitment or selection*, such as filtering applications or evaluating candidates. Here, the candidate uses the tool to prepare themselves, and no employer receives any output. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | **Not applicable as intended.** It makes no hiring decision and gives no score to an employer. **If** a recruiter or employer used it to assess candidates against a job description, it would likely become high-risk. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **Possibly, under Article 50(2).** The report is AI-generated text, so the provider may need to mark it as AI-generated in a machine-readable way. Article 50(1) (chatbot interaction) is unlikely to apply, because users submit a form rather than chat. |
| First-pass risk tier | **Minimal risk**, with a possible Article 50(2) transparency duty. |
| One-sentence justification citing the specific article or Annex entry | The agent is a self-help tool used by job seekers and not by employers, so it falls outside Annex III point 4(a) recruitment and selection and outside Article 5. Its only AI Act touchpoint is AI-generated text under Article 50(2). |

**Uncertainty:** the tier depends on **who operates the tool and for whom**. Martha's answers (Phase 3) confirm it is a self-service tool for job applicants that she currently operates, and that it is not designed for recruitment screening. So the tier stays **minimal risk**. The remaining uncertainty is misuse: anyone can upload someone else's CV (see Finding 3).

---

## Phase 3 - Clarifying questions log

*Information requested from client (Martha) on 16 November 2026, in writing. Written answers received on 17 November 2026.*

| # | What I need to know | Why it matters | Provisional assumption | Martha's answer (17 Nov 2026) | Effect on audit |
|---|---|---|---|---|---|
| 1 | Who is the "workflow operator" in production? | It decides the deployer. Employer or recruiter use would bring Annex III 4(a) and **high-risk**. | A career-support provider for job seekers only. | Martha operates and maintains the workflow herself. It is a **self-service tool for job applicants**. Career coaches or training organisations might use it in future. It is **not designed or validated for recruitment screening or hiring decisions**. | Tier stays **minimal risk**. Martha is currently **provider and deployer**. Future coaches or training organisations would be deployers. |
| 2 | Can someone upload another person's CV? | Shows whether the intended purpose is protected against recruiter misuse. | Nothing prevents it. | **Confirmed:** there is no identity check, so someone else's CV could be uploaded. Martha sees this as an area for improvement. | **Finding 3 confirmed.** It also creates a GDPR issue: a third person's CV can be processed without their knowledge (Finding 1). |
| 3 | Consent text, storage, retention, Notion access? | GDPR: lawful basis, transparency, retention, access. | Single checkbox, no deletion period. | A **mandatory privacy acknowledgement** exists. n8n is **set not to save production executions**, which is good, but older saved executions and data held by external services (OpenAI, Notion, etc.) are not deleted. Consent wording, Notion permissions, provider retention and end-to-end deletion are **not yet verified**. There is no complete retention policy. | **Finding 1 partly mitigated**, but still Significant. |
| 4 | Is the report labelled as AI-generated? Is there machine-readable marking? | Article 50(2). | No notice, no marking. | The tool is called an "AI" agent, but it is **not verified that every report has a clear AI disclosure**, and there is **no machine-readable marking**. | **Finding 4 confirmed.** A saved or printed PDF loses the tool's name, so the report itself needs the label. |
| 5 | Can STAR examples include experiences not in the CV? | Accuracy and misleading claims. | Yes. | **Risk confirmed in testing:** the model invented achievements and numbers. The prompt now requires CV-grounded examples, forbids invented achievements, employers and metrics, and separates suggestions from documented experience. No full grounding audit has been done yet. | **Finding 2 partly mitigated**, but still Significant until it is tested. |

---|---|---|---|
| 1 | Who is the "workflow operator" in production: you as a service, a career coach or bootcamp, a job centre, or a recruiter or employer? | It decides who the deployer is. If employers or recruiters use it on candidates, Annex III 4(a) applies and the system becomes **high-risk**. | It is operated by a career-support provider for job seekers only, and employers have no access. |
| 2 | Could the tool be used to assess someone else's CV, for example by a recruiter uploading candidates' CVs? Is this prevented technically or by the terms of use? | Shows whether the intended purpose is protected against misuse, which would turn it into a recruitment tool. | Nothing prevents it, so I assume the risk exists (see Finding 3). |
| 3 | What does the consent text say? Where are CVs and reports stored (n8n logs, Notion), for how long, and who can access them? | GDPR: lawful basis, transparency, retention, access control, possible special-category data. | Consent is a single checkbox. Data stays in n8n logs and Notion with no deletion period. |
| 4 | Does the report tell the user it was written by AI, and does it carry any machine-readable marking? | Article 50(2) transparency. | No AI notice or marking. |
| 5 | Can the STAR examples include experiences that are not in the CV? | Accuracy. Invented examples could mislead the candidate and, through them, an employer. | Yes, the model can invent or embellish examples. |

---

## Phase 4 - Audit report

### Section 1 - System summary

The AI Interview Preparation Agent is an n8n workflow that helps a job seeker prepare for an interview at a specific company. The user enters the company name and job description, uploads a CV (PDF) and gives consent. The workflow researches the company using Tavily, NewsAPI and, for Microsoft and SAP, annual reports stored in Pinecone. GPT-4o-mini then writes a seven-section preparation report with tailored STAR examples. The report is shown as printable HTML and saved in Notion. No one reviews it before the candidate sees it, and the candidate decides how to use it.

### Section 2 - Risk classification

**Minimal risk**, with a possible **Article 50(2)** duty to mark AI-generated text.

The system matches no Article 5 practice. It is not covered by **Annex III point 4(a)**, because it supports the candidate's own preparation and does not select or evaluate candidates for an employer.

**Uncertainty:** if the operator were an employer or recruiter, or the tool were used on other people's CVs, it would likely become **high-risk**. This is the most important point to confirm (clarifying questions 1 and 2).

### Section 3 - Role map

| Role | Entity | Key obligations |
|---|---|---|
| **Provider** | **Martha**, who built the workflow and offers it | Article 50(2) marking of AI-generated output (if it applies); Article 4 AI literacy; a clearly documented intended purpose. |
| **Deployer** | **Today: Martha** operates the workflow herself (confirmed 17 Nov), so she is provider *and* deployer. **In future:** career coaches or training organisations that run it for job seekers. | Article 4 AI literacy for staff; use the tool within its intended purpose; as GDPR controller, all data protection duties. |
| **End users** | **Job seekers**, who use it privately | Not deployers under the AI Act, because their use is personal and non-professional. They are data subjects under GDPR. |
| **Vendor - AI model** | **OpenAI (GPT-4o-mini)** | GPAI model provider obligations under Article 53: technical documentation, information to downstream providers, copyright policy, training-data summary. |
| **Vendors - other** | **Tavily** (AI-powered search API), **NewsAPI**, **Pinecone**, **Notion**, **n8n** hosting | No direct AI Act duties for this use. They are GDPR processors (data processing agreements, transfers outside the EU). Tavily's own AI features are its responsibility as a provider. |

### Section 4 - Compliance findings

**Finding 1 - GDPR: CV data protection, consent and storage**
**Severity: Significant**
- **Description:** CVs contain personal data, and German CVs often contain special-category data (photo, religion, health, nationality). Martha confirmed a mandatory privacy acknowledgement, and n8n is set not to save production executions, which is good. Still missing or unverified: what the consent covers, a privacy notice, how long CVs and reports are kept in n8n logs and **Notion**, who can access the Notion workspace, or the agreements with US processors (OpenAI, Tavily, Notion, Pinecone). There is also no check that the uploader owns the CV, so a third person's data can be processed without their knowledge. The prototype used synthetic data only, so the risk applies as soon as real CVs are processed.
- **Recommended action:** before using real CVs:
  1. Write a clear privacy notice and consent text.
  2. Tell users not to upload special-category data, or strip it out.
  3. Set retention and deletion rules (e.g. delete the CV after the report is generated, and delete the report after 30 days).
  4. Restrict Notion access.
  5. Sign data processing agreements and record the legal basis for transfers.
- **Escalation needed?** **Yes, to a data protection officer or privacy lawyer.**

**Finding 2 - Accuracy: STAR examples may be invented**
**Severity: Significant**
- **Description:** GPT-4o-mini writes "tailored" STAR examples, and no one reviews them. Martha's testing confirmed the model **did invent achievements and numbers**. The prompt has since been tightened (CV-grounded examples only, no invented metrics), which is a good mitigation, but no grounding audit has been done yet. If the model still embellishes, the candidate could repeat untrue claims in an interview. That harms the candidate and misleads the employer. If the tool is sold to consumers, misleading output can also raise consumer protection issues.
- **Recommended action:**
  1. Instruct the model to use only facts from the CV, and to mark any suggested example as "to adapt with your own experience".
  2. Add a visible warning at the top of the report: "Check every example against your real experience."
  3. Run a grounding test: about 20 test CVs with deliberate gaps, checking every STAR example against the CV, and record the invention rate before going live.
- **Escalation needed?** **No.**

**Finding 3 - Intended purpose not protected against recruiter use**
**Severity: Significant**
- **Description:** the low risk tier depends entirely on the tool being used *by the candidate*. Martha confirmed there is no check that the uploader owns the CV. So a recruiter could upload a candidate's CV and job description and use the report to judge the candidate. That would move the use into **Annex III point 4(a)** and bring high-risk obligations, which the system is not designed to meet.
- **Recommended action:**
  1. Document the intended purpose in the instructions and terms of use, and explicitly exclude employer or recruiter use.
  2. Add a form confirmation: "I am uploading my own CV".
  3. Recheck the classification if the business model ever targets employers.
- **Escalation needed?** **Yes, to a lawyer**, to confirm the classification and the terms of use wording.

**Finding 4 - No AI-generated label on the report**
**Severity: Minor**
- **Description:** the report is AI-generated text. Martha confirmed that a clear AI disclosure in every report is not verified, and that there is no machine-readable marking, which **Article 50(2)** may require. The tool's name says "AI", but a saved or printed PDF of the report loses that context.
- **Recommended action:** add "This report was generated by AI (OpenAI GPT-4o-mini)" to the HTML report and the Notion page, and add machine-readable metadata (e.g. an HTML meta tag).
- **Escalation needed?** **Yes, to a lawyer**, to confirm whether Article 50(2) applies and which marking standard to use.

### Section 5 - Overall recommendation

**Proceed with conditions.** There are no blocking findings. The system is minimal risk as intended and makes no decisions about people. However, three significant findings must be closed **before real candidates' CVs are processed**:
1. GDPR safeguards for CV data (Finding 1).
2. Controls against invented STAR examples (Finding 2).
3. A documented and enforced candidate-only intended purpose (Finding 3).

The AI label (Finding 4) should be added at the same time.

### Section 6 - What this report is not

This report is a first-pass peer review based only on the builder's system brief. It is **not a legal opinion, not a conformity assessment and not a certification**. Conclusions should be verified with legal counsel, and data protection points with a data protection officer, before any placement on the EU market.

---

## Phase 5 - Debrief (with Martha, 17 November 2026, held in writing)

**1. Auditor presents:** I shared this audit report with Martha: tier, four findings and recommendation.

**2. Builder's response:** Martha added context that the brief did not contain:
- n8n is now set not to save production executions.
- In testing, the model **did** invent achievements and metrics, and she has since tightened the prompt.
- There is no check that the uploader owns the CV.
- The tool is currently operated by her as a self-service tool for job applicants, not for recruiters.

**3. Compare classifications**

| | Tier |
|---|---|
| Martha's self-audit | **Limited risk / transparency** (provisional): Article 50(1), because users interact with an AI-based service |
| My peer audit | **Minimal risk**, with a possible **Article 50(2)** duty to mark AI-generated text |
| Same / different, and why | **We agree on the important point: not high-risk**, because the tool does not evaluate, rank or reject candidates for employers (outside Annex III 4(a)). We differ only on *which* transparency rule applies. Martha reads the form-based service as "interacting directly" with users (Art. 50(1)). I read Art. 50(1) as aimed at conversational systems such as chatbots, and saw the AI-written report as the trigger (Art. 50(2)). This is a **genuine interpretation question about the regulation**, not something the brief failed to communicate. The practical result is the same: **label the tool and the report as AI-generated**. Which article applies should be confirmed by a lawyer. |

**4. Compare gap lists**

| Martha's top findings (self-audit) | My top findings (peer audit) | Caught by only one of us |
|---|---|---|
| 1. GDPR: retention and deletion across Notion and vendors<br>2. AI transparency notice and privacy information<br>3. Accuracy of STAR examples<br>4. Access and retention controls (Notion permissions, old execution logs) | 1. GDPR: CV data, retention, Notion access, third-party CVs<br>2. Invented STAR examples<br>3. Recruiter misuse could make it high-risk<br>4. No AI-generated label | **Only the external audit (me):** recruiter misuse and the missing CV-ownership check. The builder's self-audit treated the intended purpose as settled. An outside reviewer asked "what if someone else uses it?", and that is the risk that could move the tool into high-risk.<br>**Only the self-audit (Martha):** that the model actually invented metrics in testing, and that n8n execution saving was already switched off. That is inside knowledge that a brief alone could not show me. |

**5. Joint closing note (written together):**
Auditing our own systems, we both knew the details best. Martha knew her model had invented metrics in testing, and Barsha knew exactly how her fact-checker worked. But we also both took our intended use for granted. The external audits found what we had missed: Barsha spotted that anyone could upload someone else's CV, and Martha spotted that Barsha's agent still sends unchecked reports when the fact-checker fails. Self-audits are strong on facts, peer audits are strong on assumptions, and a good compliance review needs both.

---

## Reinforce

**Martha's audit of my AI Search Visibility Agent - what it taught me**
- **We agreed:** minimal risk, proceed with conditions, GDPR and retention gaps, and no AI label on the report.
- **Martha caught something I missed:** when the fact-checker is unavailable, my workflow still sends the **unchecked report** (it is only marked as unchecked). I listed this as a robustness feature in my self-audit, not as a risk. In hindsight it should be a gap, and the fix is to hold the report for human review instead of sending it automatically.
- **Martha also pointed out** that my fact-checker only checks the report against the collected data, so it cannot catch errors in the source data, such as brand-name matching. I listed this as a limitation, but she framed it more clearly as a reliability risk.
- **A finding I initially disagreed with:** Martha said Article 50 disclosure is "not automatically triggered" because my reports are for internal use. That logic fits Article 50(4) (text published to inform the public), but in my view Article 50(2) machine-readable marking applies whether or not a report is published. After the debrief I still think the AI label is needed, but we agree it is a question for legal review, not a settled obligation.
- **What I caught that Martha did not:** the risk of misleading comparative claims about competitor brands (unfair competition law) if clients reuse the findings publicly.
- **Questions I could not fully answer:** Martha's question about where reports and execution data are stored and for how long showed that my documentation does not describe retention or access at all. My README should get a short "Data handling" section.

---

## Stretch - Work plan for Finding 1 (GDPR: CV data)

- **Deliverable:** a "Real CV readiness" package with four parts:
  1. A privacy notice and consent text on the form.
  2. A data retention setting: CV deleted after generation, Notion report auto-deleted after 30 days, n8n execution logs pruned.
  3. Signed data processing agreements and a transfer record for OpenAI, Tavily, Pinecone and Notion.
  4. A short data protection impact assessment screening note.
- **Responsible:** Martha (technical changes in n8n and Notion). The operator's data protection officer reviews the notice and the DPIA screening. A privacy lawyer checks the consent wording.
- **Timeline:** about 2 weeks. Week 1: notice, consent text and retention settings. Week 2: data processing agreements, DPIA screening and the lawyer review.
- **Evidence it is closed:**
  - a screenshot of the form with the notice and consent
  - a test run showing the CV is deleted and the Notion page expires
  - the stored data processing agreements
  - the DPO's sign-off note
