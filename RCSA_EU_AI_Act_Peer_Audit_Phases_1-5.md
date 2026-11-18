# EU AI Act Peer Audit — RCSA Evidence & Challenge Agent

**Review date:** 17 November 2026  
**Review basis:** Two-page system brief describing a functional MVP using synthetic data. No source code, deployment environment, contractual documents or independent test results were reviewed.  
**Assessment status:** Independent, provisional first-pass audit.

## Phase 1 — Read and Annotate

The source brief was reviewed to identify facts relevant to risk classification, unresolved questions and potential compliance obligations. The annotations below document the evidence base.

| System brief evidence | Annotation | Audit implication |
|---|---|---|
| The AI suggests operational risks for each step described by a process owner. | **Underline — classification** | Intended use is internal banking process-risk assessment, not consumer credit scoring. |
| Process owners must respond to each suggested risk and justify their answers. | **Circle — clarification** | Owner-linked responses might be reused to monitor individual worker performance. |
| The agent challenges answers against loss events and key risk indicators (KRIs). | **Underline — classification** | Its outputs may influence material operational-risk discussions. |
| The system estimates inherent risk, control effectiveness and residual risk. | **Underline — classification** | Outputs are substantive recommendations, not just text formatting. |
| It does not independently approve controls, accept risks or change official risk ratings. | **Underline — classification** | Humans retain stated decision authority, although human review does not automatically rule out high-risk status. |
| OpenAI models are accessed through an API, orchestrated with LangGraph. | **Mark — obligation** | Review vendor roles, data transfers, confidentiality, security and output provenance. |
| The MVP uses synthetic data; production loss records may identify employees or customers. | **Circle / mark — clarification and obligation** | GDPR exposure depends on the actual production data flows. |
| Outputs may feed management, capital or supervisory processes after human sign-off. | **Circle — clarification** | Confirm downstream decisions, permitted reliance and auditability. |
| Second-line approval is intended but is not an enforced or logged workflow in the MVP. | **Mark — obligation** | A production-readiness weakness in human control and traceability. |
| The solution could be built in-house or supplied by a software provider or consultancy. | **Circle — clarification** | Final provider and deployer roles depend on the deployment model. |

## Phase 2 — First-Pass Classification

| Classification question | Independent first-pass answer |
|---|---|
| **Does the system fall under any prohibited category (Article 5)?** | **No evidence of a prohibited practice.** It neither conducts prohibited emotion inference nor any other prohibited activity described in the brief. |
| **Does it operate in any of the eight Annex III areas?** | **Not for its documented intended purpose.** Internal operational-risk assessment is different from evaluating the creditworthiness of natural persons (Annex III, point 5(b)). However, individual employee performance monitoring or evaluation could bring an expanded use within Annex III, point 4(b). |
| **If Annex III applies, does it significantly influence decisions, or is it narrow/preparatory?** | **Not applicable to the currently documented purpose.** If the system is used to evaluate employees, the purpose and influence of owner-linked flags must be assessed under Article 6(3). Human sign-off alone would not establish an exemption. |
| **Does it interact with end users or generate content requiring disclosure (Article 50)?** | **Potentially yes.** Article 50(1) may require an AI-interaction notice if the AI directly interacts with users; Article 50(2) may require machine-readable marking of AI-generated report text, subject to applicable exceptions. Internal reports do not normally engage the Article 50(4) disclosure obligation for public-interest publications. |
| **First-pass risk tier** | **Non-high-risk AI with potentially applicable transparency obligations** (*“Limited Risk”* in the LAB terminology). |
| **One-sentence justification with legal reference** | The agent supports internal bank operational-risk assessment rather than the creditworthiness or employee-performance use cases in Annex III, points 5(b) and 4(b), respectively, so it is provisionally non-high-risk under Article 6(2), while its user interaction and generated reports require an Article 50 assessment. |

**Classification uncertainty:** This conclusion assumes that challenges are used only to review risks and controls, not to score or rank staff, and that outputs are not independently adopted as official decisions. A material change in intended purpose requires reassessment.

## Phase 3 — Clarifying Questions Log

**Prepared:** 17 November 2026. **Status:** Questions not yet sent; responses pending. All assumptions below are provisional.

| # | Clarifying question / information needed | Why it matters | Provisional assumption |
|---|---|---|---|
| 1 | Are challenge flags, rejected risks or owner-linked reports ever used in appraisals, productivity monitoring, disciplinary measures or HR decisions? | Could trigger Annex III, point 4(b), on employee monitoring or performance evaluation. | Use is limited to process and control governance; no individual staff evaluation. |
| 2 | Is second-line sign-off mandatory before reports or ratings enter official systems, and are approvals, overrides and rejections recorded? | Determines whether the human review is real, enforceable and auditable. | The final approval step is planned but not technically enforced. |
| 3 | Which personal or confidential bank data would be sent to the OpenAI API, and under what processing terms, access controls, retention settings and transfer safeguards? | Relevant to GDPR, banking confidentiality and ICT third-party risk. | Current testing uses synthetic data only; production arrangements are unverified. |
| 4 | Are users told that they interact with AI, and is AI-generated report text technically marked where Article 50 requires it? | Determines the applicable interaction and output-transparency measures. | Neither mechanism is evidenced in the brief. |
| 5 | What tests, performance thresholds, evidence links and version records support the accuracy of suggested risks, challenge flags and risk ratings? | Errors could undermine official risk reporting and supervisory reliance. | Formal validation and monitoring evidence has not been supplied. |

**Audit trail requirement:** Record the date each question is sent, the reply, supporting documents and any resulting change to the classification or findings.

## Phase 4 — Audit Report

### Section 1 — System Summary

The RCSA Evidence & Challenge Agent assists banks with Risk and Control Self-Assessments. Process owners describe activities, and the AI proposes operational risks, checks their answers against loss events and KRIs, and drafts challenge flags, indicative ratings and a written report. The AI does not directly approve controls or modify official bank ratings. The current MVP uses synthetic data, while future production inputs could include personal and confidential information. Final second-line approval is intended but not yet enforced or logged in the prototype.

### Section 2 — Risk Classification

**Provisional classification: non-high-risk / limited risk with potentially applicable Article 50 obligations.** No Article 5 prohibited practice is apparent. The stated purpose is not natural-person credit scoring under Annex III 5(b). However, if owner-linked flags are intended for employee monitoring or performance evaluation, Annex III 4(b) could require a high-risk reassessment. Article 50(1) may apply to direct AI interaction, and Article 50(2) may apply to generated text, subject to statutory exceptions. The available brief does not establish whether the relevant notices or technical measures exist. Human approval does not automatically change the risk tier.

### Section 3 — Role Map

| Role | Responsible party in a production scenario | Key obligations / responsibilities |
|---|---|---|
| **AI system provider** | Vendor/consultancy offering the solution under its name, or the bank if developed and put into service under its own name. | Classify the intended use; meet applicable AI Act provider and transparency duties; implement the necessary technical controls. If high-risk, reassess the full provider obligations. |
| **Deployer** | Bank operating the system. | Govern the actual use, define decision rights, address personal data and ICT risks, provide relevant staff training and maintain appropriate controls. The bank might also be the provider. |
| **Third-party model/API supplier** | OpenAI. | Supplies the underlying model/API. Specific GDPR processing roles, contractual terms and technical safeguards must be verified. |
| **Framework / potential infrastructure providers** | LangGraph as orchestration software; hosting providers not specified. | LangGraph alone does not establish a separate personal-data recipient. Any actual hosting/sub-processor arrangements must be mapped. |

### Section 4 — Compliance Findings

**Finding 1 — Potential employee-performance monitoring**  
**Severity:** Significant.  
**Description:** Owner-linked challenge flags may expose individual work behaviour, and downstream HR use has not been excluded. Such a use could engage Annex III 4(b).  
**Recommended action:** Document and enforce a process-risk-only intended purpose; prohibit HR reuse unless a fresh legal and risk classification is completed.  
**Escalation needed?** Yes — Legal/Compliance and HR.

**Finding 2 — AI transparency and report provenance**  
**Severity:** Significant.  
**Description:** The brief does not establish whether an AI interaction notice or applicable technical marking of generated text is implemented. Article 50 obligations and exceptions require verification.  
**Recommended action:** Determine which Article 50 provisions apply; implement clear interaction notices and output-marking measures where required.  
**Escalation needed?** Yes — Product owner and Legal/Compliance.

**Finding 3 — Human approval and audit logging**  
**Severity:** Significant.  
**Description:** The source expressly states that second-line validation is not an enforced, logged step in the MVP. This could allow draft results to be confused with approved RCSA conclusions.  
**Recommended action:** Require documented risk-manager approval before official publication/export; log approvals, rejections, overrides, evidence and versions.  
**Escalation needed?** Yes — Head of Operational Risk and Product owner.

**Finding 4 — GDPR and confidential bank data**  
**Severity:** Significant.  
**Description:** Real loss events and owner-linked answers may contain personal data; lawful bases, access, retention, processing contracts and international transfers are not established. Synthetic-data testing alone is not evidence of a GDPR breach.  
**Recommended action:** Map data flows; establish controller/processor roles, lawful basis, minimisation, retention, security, vendor terms and DPIA screening before live-data use.  
**Escalation needed?** Yes — Data Protection Officer and Procurement.

**Finding 5 — Financial-sector ICT and third-party risk**  
**Severity:** Significant.  
**Description:** Reliance on an external AI API raises operational resilience, confidentiality and vendor-management questions. The brief provides no production DORA or information-security assessment.  
**Recommended action:** Complete an ICT/security and third-party risk review addressing contractual controls, access, incident response, resilience and criticality.  
**Escalation needed?** Yes — CISO, ICT Risk and Compliance.

**Finding 6 — Accuracy, explainability and evidence validation**  
**Severity:** Significant.  
**Description:** Risk suggestions and ratings could materially affect internal assessments, but no independent evaluation results, error thresholds or model-version audit records are supplied. This is an evidence gap, not proof that testing did not occur.  
**Recommended action:** Evaluate expert-reviewed cases, measure false flags and missed risks, retain source-level evidence references and version prompts/models.  
**Escalation needed?** Yes — Model Risk and Operational Risk.

**Finding 7 — AI literacy and user guidance**  
**Severity:** Minor.  
**Description:** The brief does not document operator guidance or AI-literacy measures relevant to Article 4.  
**Recommended action:** Provide intended-use instructions and proportionate training on uncertainty, human review and appropriate reliance.  
**Escalation needed?** No — Product/Risk owner can manage remediation.

### Section 5 — Overall Recommendation

**Proceed with conditions.** The synthetic-data prototype can continue to be developed and tested. Before processing live bank data or feeding official RCSA and supervisory reporting, the implementing organisation should confirm the intended-use boundary, address applicable AI transparency requirements, enforce and record human approval, complete GDPR and ICT/vendor assessments, and validate output quality. If the system will be used to evaluate employees, the risk classification must be reopened before deployment. These are conditions for production readiness, not a finding that the existing MVP is unlawful.

### Section 6 — What This Report Is Not

This report is **not a legal opinion, conformity assessment or certification**. It is a provisional review based on the available brief; conclusions should be confirmed with qualified legal counsel before EU market placement or operational deployment.

## Phase 5 — Debrief Conversation

In refered project 3 all bootcamp members did only work on a MVP version. Therefore, in both project assessments we were able to find compliance issues and risks. These risks were mostly based on the early stages of the projects and on the lack of focus regarding the EU AI. Still these are solvable issues, which do not inherently stop each partner from further development steps as long as significant findings in each report are handled.

Both projects are MVPs, so both audits found gaps, like no AI labels, unclear data transfers and no real human approval step. These are normal at this stage and can be fixed before real users or real data are involved.
The debrief showed a difference: as builders, we judged what we planned to build, so some things felt clear to us. As auditors, we could only judge what was written in the brief, so the same things became open questions. What is not written down is not a control. Self-audits know the system better, but external audits find the gaps.

We also discussed all the qualifying questions regarding my project first:

| # | What I need to know | Why it matters | Provisional assumption if no answer | Answer received (date) |
|---|---|---|---|---|
| Q1 | **Who will pay for and use the system in production?** Only individual job seekers (B2C), or also recruiters, staffing agencies, job boards, outplacement firms or public employment services (e.g. Bundesagentur für Arbeit)? | This decides the tier. Recruiter or job-board use falls under Annex III 4(a). Public employment services could also touch Annex III 5(a). Because the system profiles people, the Art. 6(3) exit is unavailable, so it would be **high-risk**. | B2C only. Job seekers use it for personal decisions. | |
| Q2 | **What exactly does OpenAI do?** Does the LLM calculate or adjust the 0–100 score, or only write explanations and summaries? What happens when the "optional" analysis is off? | It decides which outputs are AI-generated (Art. 50(2) scope) and where accuracy, bias and explainability risks sit. | The score is computed by deterministic or embedding logic; the LLM writes explanations and the report narrative. | |
| Q3 | **Can scores or reports be shared with employers**, for example a "send to recruiter" feature, an API, or users attaching the PDF to an application? | If the score reaches an employer's selection process, the system is in practice used for evaluating candidates (4(a)), and the risk of misuse becomes reasonably foreseeable (Art. 9 logic). | There is no sharing feature, but nothing stops a user from forwarding the PDF. | |
| Q4 | **What personal data goes to which vendor, where it is stored and for how long?** (OpenAI, Tavily, Pinecone; CV upload or structured form only; photo, date of birth or nationality fields?) | GDPR: legal basis, processor agreements, US transfers, retention, special-category data. Age proxies matter for discrimination risk. | The structured profile is sent to OpenAI. Pinecone stores only public research documents. No retention or deletion policy is defined yet. | |
| Q5 | **What does the user see about AI and limitations?** Is the "advisory, not a hiring probability" message shown in the UI and every export? Is there any chat interface? Has the score been tested for bias (career gaps, age, part-time, foreign degrees)? | Art. 50(1)/(2) disclosures, consumer protection (misleading accuracy claims), anti-discrimination (AGG). | A text disclaimer appears in the report. No machine-readable AI marking, no chat, no bias testing yet. | |

### Notes
- All findings in the audit report are based on the brief plus these assumptions. If an answer contradicts an assumption, the related finding is re-assessed. Q1 and Q3 can change the overall recommendation.
- No source code, repository or architecture diagram was provided; the audit is document-based only.

## Answers

## Clarification Questions – Career Intelligence Agent

**Q1 – Who will pay for and use the system in production?**

The initial target audience is individual jobseekers (B2C). The Career Intelligence Agent is designed to help users identify suitable job opportunities, understand their qualifications and plan their careers independently.

Future go-to-market sprints may include partnerships with companies or other organizations to expand the service, for example through job-data integrations. However, employer-side candidate screening, applicant ranking and recruitment decisions are not part of the current intended purpose.

Any future expansion into employer-facing candidate evaluation would require a new AI Act risk assessment.

**Q2 – What exactly does OpenAI do?**

The 0–100 matching score is calculated using deterministic, rule-based logic with predefined weighted criteria. OpenAI does not calculate, modify or override the scores.

The LLM is used exclusively for optional AI-generated career and labour-market intelligence, transforming retrieved evidence and candidate-related context into readable insights.

When this optional feature is disabled, the system continues to operate normally. Job discovery, matching, scoring, evidence-based explanations and deterministic career insights remain available without an OpenAI synthesis request.

**Q3 – Can scores or reports be shared with employers?**

Users can download their career intelligence reports and independently decide whether to share them with third parties, including potential employers.

The current MVP does not provide any direct employer-sharing functionality, recruitment API or automated application submission.

The reports are intended for personal career guidance, not employer-side applicant assessment. If employers were to systematically use the system or its scores for candidate evaluation, that use case would require a separate regulatory assessment.

**Q4 – What personal data goes to which vendor, where is it stored and for how long?**

The current MVP uses synthetic candidate profiles. The Streamlit interface collects structured information directly rather than requiring CV uploads.

Available fields include a display name, professional summary, experience, skills, education, qualifications, career interests, preferred job roles, seniority, location and work preferences.

There are no dedicated fields for photographs, dates of birth or nationality. However, free-text fields could contain additional personal or sensitive information.

The relevant vendor data flows are:

- **OpenAI:** When optional AI synthesis is enabled, candidate-related context, recommendations and retrieved labour-market evidence are processed to generate career insights. OpenAI does not receive the profile for matching-score calculation.
- **Pinecone:** Stores the curated labour-market knowledge base, not candidate CVs. However, retrieval queries may contain candidate-related job titles, skills and identified qualification gaps.
- **Tavily:** Receives company research queries rather than full candidate profiles.
- **ESCO:** Receives occupational and skill lookup terms.
- **Arbeitnow and Himalayas:** Receive job-search requests based on target roles and search parameters.

Candidate information is processed during the active application session. The workflow also writes generated reports, including candidate details and assessments, to the local filesystem.

**Retention:** No formal retention or deletion policy has been implemented for production use. Local report files may remain until explicitly deleted.

**Processing locations and transfers:** The MVP runs locally, but the exact processing regions and retention arrangements of external API providers have not been comprehensively verified. International transfers and applicable safeguards therefore remain open compliance items.

**Q5 – What does the user see about AI and limitations?**

The interface explicitly describes the system as AI-assisted career intelligence. Users review and confirm their profiles before initiating the workflow, and optional external AI services are disabled by default.

The interface already explains that matching scores represent indicative evidence alignment rather than hiring probability. Generated reports also document scoring limitations and distinguish missing qualification evidence from confirmed mismatches.

There is currently **no conversational chat interface**.

The system includes automated functional tests and explainable scoring logic. However, systematic fairness testing across demographic proxies and candidate circumstances, such as career gaps, age-related factors, part-time experience or foreign qualifications, has not yet been completed.

Machine-readable marking of AI-generated content has also not been established.

As this is an MVP, additional privacy safeguards, comprehensive user disclosures, bias evaluation and technical AI-content marking assessments remain part of the planned production-readiness work.

Questions regarding my partners project were discussed next:

**Q1 – Are challenge flags, rejected risks or owner-linked reports ever used in appraisals, productivity monitoring, disciplinary measures or HR decisions?**
No. The intended purpose is process and control governance only: assessing the risk of a business process, not the performance of the person who owns it. However, the MVP does not technically prevent misuse. Answers and challenge flags are currently linked to the named process owner, and there is no written restriction on HR use yet. For production I plan to report challenges per process/risk, not per person, and to document the intended purpose with an explicit exclusion of HR use.

**Q2 – Is second-line sign-off mandatory before reports or ratings enter official systems, and are approvals, overrides and rejections recorded?**
Not yet. Second-line review is part of the design, but the MVP does not enforce an approval step and does not log approvals, overrides or rejections. Ratings remain proposals in the report; the MVP does not write into any official RCSA system.

**Q3 – Which personal or confidential bank data would be sent to the OpenAI API, and under what terms, access controls, retention settings and transfer safeguards?**
In production: the process description, the owner's answers, and relevant loss event and KRI data needed to test the answers. Loss event free text could contain employee names, customer references or sensitive details. The MVP uses synthetic data only. Processing terms, retention settings (e.g. zero data retention), processing region and transfer safeguards have **not been verified**.

**Q4 – Are users told that they interact with AI, and is AI-generated report text technically marked (Art. 50)?**
Users know it is an AI tool from context (it is presented as an AI-supported RCSA agent), but there is no explicit AI notice in the interface and **no machine-readable marking** of AI-generated text in the report.

**Q5 – What tests, thresholds, evidence links and version records support the accuracy of suggested risks, challenge flags and ratings?**
The MVP was tested on synthetic scenarios, i.e. processes with planted loss events and KRI breaches, to check that the challenge logic fires correctly. Each challenge shows the evidence it is based on (the loss event or KRI). There are **no formal accuracy thresholds, no validation report, and no model or prompt version records** yet.