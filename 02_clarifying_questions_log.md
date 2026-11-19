# Phase 3 – Clarifying questions log (audit trail)

**Auditor:** Murat Çömez · **Client / builder:** Max · **System:** Career Intelligence Agent
**Channel:** written only (Slack / email) · **Information requested from client on:** 17 Nov 2026 · **Answers received:** 18 Nov 2026

| # | What I need to know | Why it matters | Provisional assumption if no answer | Answer received |
|---|---|---|---|---|
| Q1 | **Who will pay for and use the system in production?** Only individual job seekers (B2C), or also recruiters, staffing agencies, job boards, outplacement firms or public employment services (e.g. Bundesagentur für Arbeit)? | This decides the tier. Recruiter or job-board use falls under Annex III 4(a). Public employment services could also touch Annex III 5(a). Because the system profiles people, the Art. 6(3) exit is unavailable, so it would be **high-risk**. | B2C only. Job seekers use it for personal decisions. | 18 Nov – **confirmed** (B2C; employer screening excluded; future B2B needs new assessment) |
| Q2 | **What exactly does OpenAI do?** Does the LLM calculate or adjust the 0–100 score, or only write explanations and summaries? What happens when the "optional" analysis is off? | It decides which outputs are AI-generated (Art. 50(2) scope) and where accuracy, bias and explainability risks sit. | The score is computed by deterministic or embedding logic; the LLM writes explanations and the report narrative. | 18 Nov – **confirmed** (score is rule-based; LLM only for optional insights, off by default) |
| Q3 | **Can scores or reports be shared with employers**, for example a "send to recruiter" feature, an API, or users attaching the PDF to an application? | If the score reaches an employer's selection process, the system is in practice used for evaluating candidates (4(a)), and the risk of misuse becomes reasonably foreseeable (Art. 9 logic). | There is no sharing feature, but nothing stops a user from forwarding the PDF. | 18 Nov – **confirmed** (no sharing feature; users may share reports themselves) |
| Q4 | **What personal data goes to which vendor, where it is stored and for how long?** (OpenAI, Tavily, Pinecone; CV upload or structured form only; photo, date of birth or nationality fields?) | GDPR: legal basis, processor agreements, US transfers, retention, special-category data. Age proxies matter for discrimination risk. | The structured profile is sent to OpenAI. Pinecone stores only public research documents. No retention or deletion policy is defined yet. | 18 Nov – **partly different:** reports with candidate details are written to local files; Pinecone queries contain job titles, skills and gaps; no retention policy |
| Q5 | **What does the user see about AI and limitations?** Is the "advisory, not a hiring probability" message shown in the UI and every export? Is there any chat interface? Has the score been tested for bias (career gaps, age, part-time, foreign degrees)? | Art. 50(1)/(2) disclosures, consumer protection (misleading accuracy claims), anti-discrimination (AGG). | A text disclaimer appears in the report. No machine-readable AI marking, no chat, no bias testing yet. | 18 Nov – **better than assumed:** UI states AI-assisted and score limits; still no marking, no fairness testing |

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
## Impact of the answers on the audit (auditor's note, 18 Nov 2026)
| Finding | Before | After answers |
|---|---|---|
| F1 Business model / Annex III 4(a) | Significant | **Significant, partly mitigated:** B2C purpose and the exclusion of employer screening are now confirmed in writing. Still needs a formal intended-purpose statement, terms of use, and a label on reports, because users can forward reports to employers. |
| F2 Art. 50(2) marking | Significant | **Significant, narrower scope:** applies only to the optional LLM insights, not to the rule-based score. A visible AI notice already exists in the UI; machine-readable marking is still missing. |
| F3 GDPR data flows | Significant | **Significant:** confirmed local storage of reports with candidate details, no retention policy, unverified transfers. Pinecone/Tavily queries contain candidate-related terms. |
| F4 Bias testing | Significant | **Significant:** confirmed not done. Rule-based scoring makes testing easier. |
| F5 Score misreading | Minor | **Minor, largely addressed:** the UI and reports explain the score's limits. |
| F6 Data sources / AI literacy | Minor | Minor, unchanged |
| Overall | Proceed with conditions | **Proceed with conditions** (unchanged) |
