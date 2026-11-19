# EU AI Act Audit Report – Career Intelligence Agent
**Auditor:** Murat Çömez · **Builder:** Max · **Project audited:** Ironhack Project 3 · **Date:** 17 Nov 2026
**Basis:** builder's system brief (Phase 1) + written clarifying questions **answered by the builder on 18 Nov 2026** ([log](02_clarifying_questions_log.md)). No code review.

## 1. System summary
The Career Intelligence Agent is a web app (Python, LangGraph, Streamlit) that helps an individual job seeker find suitable jobs. The user enters and checks a structured profile (experience, education, skills, preferences). The system pulls live job ads from Arbeitnow and Himalayas, enriches them with ESCO occupation data, Tavily company research and labour-market publications (retrieved via Pinecone), and optionally uses OpenAI to write analysis. For each job it gives a 0–100 matching score (calculated by **rule-based weighted logic**, not by the LLM) with evidence and gaps, sorts jobs into "recommended" and "needs review", and produces a downloadable report (PDF, Markdown, JSON). The job seeker decides what to do. The system does not apply or decide anything for employers.

## 2. Risk classification
**First-pass tier: Limited risk / transparency (Art. 50), with an open high-risk question (Annex III 4(a)).**
- **Not prohibited (Art. 5):** no manipulation, social scoring, emotion recognition or biometrics.
- **Annex III 4(a), recruitment and selection:** the system evaluates people against jobs, but its stated purpose is the candidate's own career decision, not an employer's selection. As described, it is outside 4(a).
- **Why the question stays open:** the matching score is **profiling** of a natural person. If the system is ever used by or for recruiters, job boards or public employment services, Art. 6(3) last subparagraph makes it **high-risk with no derogation**. The brief leaves the future business model open (§5).
- **Art. 50(2):** LLM-generated text in reports must be marked as AI-generated in a machine-readable way by the provider. Art. 50(1) applies only if there is a conversational interface.

## 3. Role map
| Role | Entity | Key AI Act obligations |
|---|---|---|
| **Provider** | The builder (teammate), and later the "future commercial provider" that offers the app under its name | Art. 50(2) marking of AI-generated output; Art. 4 AI literacy of staff; define and document the intended purpose (B2C career guidance) and prohibit recruiter use. If reclassified high-risk: Art. 9–15, 16–17, 43, 47–49, 72. |
| **Deployer** | Job seekers using it for personal, non-professional purposes | **No deployer obligations** (Art. 2(10) personal-use exemption). Career coaches, outplacement firms or employment agencies using it professionally *would* be deployers (Art. 26, and Art. 50 duties). |
| **Vendor – OpenAI** | GPAI model provider | Its own GPAI obligations (Art. 53: technical documentation, information to downstream providers, copyright policy). Under GDPR: processor, which requires a DPA and a basis for international transfer. |
| **Vendors – Pinecone, Tavily** | Infrastructure / search APIs, not the AI system itself | No AI Act role of their own here. GDPR processors if personal data reaches them. |
| **Data sources – Arbeitnow, Himalayas, ESCO, EC/Cedefop/ILO** | Content providers | No AI Act obligations. Terms of use, licensing and data quality are a vendor-management point. |

## 4. Compliance findings

**Finding 1 – Classification depends on an undefined business model (Annex III 4(a), Art. 6(3))** · **Severity: Significant** (becomes **Blocking** if any recruiter, job-board or employment-service use is planned)
Description: The builder confirmed in writing that the product is B2C and that employer screening, applicant ranking and recruitment decisions are out of scope. However, the intended purpose is still not formally documented. Nothing in the design, terms or architecture prevents use in an employer's selection process (downloadable scores, open commercial model). Because the score profiles people, such use makes it high-risk with no Art. 6(3) exit.
Recommended action: Write a formal intended-purpose statement (B2C career guidance only). Exclude recruiter and employer use in the terms of service. Do not build employer-facing features or APIs. Label exports "for the candidate's personal use, not for selection decisions". Reassess before any B2B deal.
Escalation: **Yes, to a lawyer** (classification confirmation).

**Finding 2 – AI-generated content not marked (Art. 50(2))** · **Severity: Significant**
Description: Only the **optional** LLM insights are AI-generated text (off by default; the score is rule-based). The UI already describes the system as AI-assisted, but there is no machine-readable marking (metadata in PDF/JSON, a field in JSON output) and no clear statement of which parts are AI-written. Art. 50 obligations apply from 2 Aug 2026.
Recommended action: Add an `ai_generated: true` field and model name to JSON. Add PDF metadata and a visible note ("Explanations generated by AI (OpenAI model); score calculated by [method]"). Make the same notice visible in the Streamlit UI.
Escalation: No.

**Finding 3 – Personal data processing not yet designed (GDPR)** · **Severity: Significant**
Description: Real profiles are personal data. When AI synthesis is on, candidate context goes to OpenAI (US). Pinecone queries contain the candidate's job titles, skills and gaps, and **reports with candidate details are written to local files with no retention policy** (builder's answer Q4). The brief does not cover legal basis, privacy notice, processor agreements, transfer mechanism, retention or deletion, or minimisation (for example, birth date or photo not needed). The score is profiling (GDPR Art. 4(4)), so users need transparent information on the logic (Art. 13(2)(f) is engaged even if Art. 22 does not apply).
Recommended action: Create a data-flow map per vendor, a privacy notice, DPAs, zero-retention API settings, auto-delete of profiles, and pseudonymisation before LLM calls. Assess whether a DPIA is needed.
Escalation: **Yes, to a data protection officer / privacy counsel.**

**Finding 4 – No bias or fairness testing of the matching score** · **Severity: Significant**
Description: Education dates, career level, gaps, part-time work and foreign qualifications can act as proxies for age, gender or origin. A biased score could systematically steer groups away from jobs. This is a consumer-harm and AGG / EU Charter Art. 21 issue even if the system is not high-risk.
Recommended action: Test synthetic profile pairs that differ only in a proxy variable. Document the results. Give gap or "needs verification" fields neutral wording.
Escalation: No (specialist input helpful).

**Finding 5 – Accuracy claims and misreading of the score (consumer protection)** · **Severity: Minor**
Description: Largely addressed: the UI and reports explain that the score shows evidence alignment, not hiring probability. Residual risk: a 0–100 number still looks precise. A marketing claim like "find your perfect job" or an implied hiring probability would be misleading (UCPD).
Recommended action: Use score bands (High / Medium / Low) or show the score with its basis. Keep the disclaimer on every export. Review marketing copy.
Escalation: No.

**Finding 6 – Third-party data sources and AI literacy** · **Severity: Minor**
Description: Job APIs and research content come with terms and freshness limits. Art. 4 AI literacy applies to the provider's staff.
Recommended action: Check API terms and licences, and show the date and source of each job ad. Write a short AI-literacy note for anyone operating the tool.
Escalation: No.

**Contingent check – if reclassified high-risk (Annex III 4(a))**, based on the brief:
Art. 9 risk management **Gap** · Art. 10 data governance **Partial** (curated sources, no bias testing) · Art. 11 technical documentation **Gap** · Art. 12 logging **Gap** (none described) · Art. 13 instructions for use **Partial** (disclaimer only) · Art. 14 human oversight **Partial** (user review, no independent reviewer, which the builder notes) · Art. 15 accuracy/robustness **Partial** (evidence-sufficiency rule) · Art. 43 conformity assessment, Art. 47–48 declaration and CE marking, Art. 49 registration, Art. 72 post-market monitoring: all **Gap**.

## 5. Overall recommendation: **Proceed with conditions**
There are no blocking findings for the B2C use, which the builder confirmed in writing on 18 Nov. Before any launch with real users: (1) lock in and document the B2C intended purpose and exclude recruiter use (F1); (2) implement Art. 50(2) marking and visible AI notices (F2); (3) complete the GDPR basics with vendor DPAs (F3); (4) run and document a first bias test (F4). If the client plans any employer, job-board or public-employment-service channel, the recommendation changes to **Do not proceed** until a high-risk compliance programme is in place.

## 6. What this report is not
This report is a first-pass, document-based compliance review for training purposes. It is **not a legal opinion, not a conformity assessment and not a certification**. It relies on the builder's brief and the stated assumptions. Conclusions must be verified with legal counsel before any placement on the EU market.
