# Independent EU AI Act Audit: Raw Materials Procurement Risk

**Audited project:** Raw Materials Procurement_Project.md  
**Audit date:** 24 November 2026  
**Scope:** Independent first-pass review of the system brief and the described MVP

## Section 1: System summary

The system prepares a sunflower-oil procurement risk report for an industrial bakery's buying team. Ordinary code calculates exposure and performs database queries, quote checks and unsupported-claim removal; an AI model drafts report text and may process web search results. The report is an 17-section, human-readable recommendation package and optional PDF, with possible supplier names clearly marked as unverified. The system does not approve suppliers, place orders or change contracts.

The current MVP uses fictional company data, real public information, and real web/news services in live runs. In the intended production setting, a procurement manager in Spain would use the report, with a Procurement Director approving actions where company policy requires it. Completed or partial reports are saved automatically to Notion as unreviewed drafts, while e-mail sending requires a click.

## Section 2: Risk classification

| Question | Independent answer |
|---|---|
| Prohibited category (Article 5)? | **No evidence of a prohibited practice.** The brief describes decision support, not manipulation, exploitation, social scoring or biometric/real-time law-enforcement use. |
| Operation in an Annex III area? | **No confirmed Annex III use.** Procurement is not one of the eight listed high-risk areas. It could affect contracts or business partners, but no broad employment, education, public-benefit, law-enforcement, migration, justice or essential-service decision is described. |
| Significant decision influence, if relevant? | **No material Annex III decision is made.** The report only recommends procurement risk treatments and is subject to human review. It does not approve, rank for a prohibited purpose or execute a transaction. |
| Direct interaction or generated content (Article 50)? | **Likely relevant.** The user receives AI-generated report text through a web application. Transparency should make clear that text is AI-generated. Publication or distribution of synthetic audio, images or deep-fake-like content is not described. |
| First-pass tier | **Limited-risk / transparency (provisional).** |
| Justification | Procurement is not expressly identified as a high-risk Annex III area, and the system is preparatory rather than making a final decision. The most relevant issue is transparency for AI-generated content and the interface, subject to Article 50. |

**Key uncertainty:** The Article 50 analysis depends on whether the output is presented as AI-generated and whether the system is considered to interact directly with an end user. The final tier should also consider the jurisdiction and exact production workflow.

## Section 3: Clarifying questions log

| # | Information requested | Why it matters | Provisionally assumed |
|---|---|---|---|
| 1 | Is the procurement report used only by named staff in Spain, or may outputs go to suppliers, authorities or other natural persons? | User scope affects GDPR, transparency and potential disclosure obligations. | Internal staff use only; supplier names are organizational or unverified leads. |
| 2 | Will reports, searches or supplier records contain names, identification details or sole-trader personal data, and for what purpose? | This determines whether GDPR applies and whether a lawful basis, data-processing record, retention rule and DPIA are needed. | GDPR may apply because sole traders or news subjects could be identifiable; no lawful-basis or retention decision is shown. |
| 3 | Does the UI clearly disclose that report text is AI-generated, and is the disclosure retained in the PDF and Notion copy? | Article 50 requires appropriate transparency for AI-generated or AI-interaction content in relevant use cases. | It is not disclosed consistently; the UI warning concerns human review, not AI authorship. |
| 4 | Is output ever used to make or prepare a legal/contractual supplier decision with significant consequences, or solely as an internal risk briefing? | This affects whether a different EU/sector rule or high-risk classification could apply and whether human oversight is adequate. | It remains an internal advisory report with no automated action. |
| 5 | Where is the company placing or making the system available, and who controls the production deployment and model configuration? | The answer identifies providers/deployers and which EU obligations attach. | The author or deploying bakery organization is the production deployer, with OpenAI as the model provider and listed SaaS vendors as processors/subprocessors. |

## Section 4: Role map

| Role | Current evidence | Key obligations and controls |
|---|---|---|
| **Provider** | The author designed and controls the report logic and MVP, but the production provider/deployer relationship is **NOT DEFINED**. | Assess and document the AI system, maintain traceability and technical documentation, provide appropriate AI-user transparency, and cooperate with market surveillance or competent authorities where applicable. If the system becomes high-risk, provider obligations under Articles 16-27 must be tested. |
| **Deployer** | Intended: an industrial bakery procurement manager, under Procurement Director policy. | Monitor use and data subjects, supervise human decision-makers, provide user instructions, maintain effective oversight, and report serious incidents or malfunction as applicable. |
| **Professional human reviewer / approver** | Procurement manager, and potentially Procurement Director. The named approver sign-off is **PLANNED, not built**. | Exercise meaningful review, avoid over-reliance, and document review or approval outside the system. The system should not present unapproved drafts as final. |
| **Third-party model/data vendors** | OpenAI (`gpt-5.4-mini` and embeddings), Tavily, GDELT, Supabase, LangGraph, Gradio, n8n, Notion and Gmail. | Supply suitable terms, security measures and data-processing documentation. OpenAI and relevant model providers may have GPAI-provider obligations depending on their role and contractual model. |

Third-party categories and specific contractual roles require confirmation. For example, Supabase may process records; Tavily/GDELT may supply personal or news content; Notion and Gmail are system destinations. GDPR processors and subprocessors should be mapped through contracts and transfer analysis.

## Section 5: Compliance findings

### Finding 1 — Article 50 AI transparency

**Severity:** Significant  
**Description:** The system uses AI to draft reports and process/publicly search content, but the brief describes human-review warnings rather than an explicit disclosure that text is AI-generated or that the user is interacting with an AI system. Depending on the final interface and distribution, Article 50 may require clear disclosure.  
**Recommended action:** Add a visible disclosure at the start and end of the web and PDF outputs, and label any AI-drafted text on Notion drafts. Keep the disclosure in any downloaded or forwarded copy. Confirm whether the report is intended to interact directly with natural persons.  
**Escalation needed?** Yes — to EU AI Act legal/compliance counsel and the product owner.

### Finding 2 — Human oversight and draft governance

**Severity:** Significant  
**Description:** A human is shown the report before external action, but reports are already saved to Notion before review. There is no in-system reject, edit or flag workflow, and recorded sign-off is only planned. A draft could be mistaken for an approved procurement recommendation.  
**Recommended action:** Add clear draft/unapproved status labels across every channel, prevent export or e-mail until review is recorded, add reviewer identity and timestamp, and add reject/return and amendment functions. Define prohibited actions and escalation procedures.  
**Escalation needed?** Yes — to the production business owner and procurement compliance lead.

### Finding 3 — GDPR and data protection traceability

**Severity:** Significant  
**Description:** The system may process personal data through sole-trader supplier identities or quoted news passages. The brief does not document lawful basis, purpose limitation, minimization, retention/deletion, data-subject rights, processor terms or international transfers. The system may write reports containing external passages to Supabase and Notion.  
**Recommended action:** Complete a data inventory and record of processing, classify the affected people and fields, select and document lawful bases, add retention/deletion rules, verify processor agreements and transfers, and assess whether a DPIA is required. Remove data not necessary for the procurement task.  
**Escalation needed?** Yes — to the organization's data protection officer or external privacy counsel.

### Finding 4 — Supplier/claim integrity and over-reliance

**Severity:** Significant  
**Description:** Unsupported claims are removed and listed, but potential suppliers from web searches are only marked unverified. The brief does not explain what due diligence or secondary verification is required before an unverified supplier is contacted or considered. Real news/search content can also be stale or misleading.  
**Recommended action:** Define human due diligence criteria, require independent verification of supplier identity and sanctions/reputation information, preserve source provenance and retrieval dates, and prevent the report status from implying supplier suitability.  
**Escalation needed?** Yes — to procurement leadership and sanctions/supplier-risk compliance.

### Finding 5 — Production security and incident governance

**Severity:** Significant  
**Description:** The brief documents tools and live runs but does not define access control, secret management, model/log retention, vulnerability testing, incident reporting, model drift or emergency shutdown. This matters even for a limited-risk system because reports involve business data and external services.  
**Recommended action:** Complete a threat model, least-privilege access and secret controls, retention policies for prompts/logs/reports, monitoring and alerting, incident and service-provider escalation procedures, and a rollback/shutdown plan.  
**Escalation needed?** Yes — to the production security owner and the vendor-management lead.

### Finding 6 — MVP-to-production traceability

**Severity:** Minor  
**Description:** The MVP contains fictional company data and production statements are explicitly intended rather than implemented. There is no evidence of a legal/technical sign-off process distinguishing prototype from production.  
**Recommended action:** Publish a deployment gate that requires confirmation of real data sources, users, interfaces, vendor terms and this audit's conditions. Keep the synthetic-data label in MVP environments.  
**Escalation needed?** No, unless real deployment proceeds without the stated conditions.

## Section 6: Overall recommendation

**Proceed with conditions.** The current prototype is provisionally limited-risk rather than high-risk or prohibited, provided it remains preparatory and staff-only and does not execute procurement or affect natural persons in a significant manner. Before production deployment, the team must add an appropriate AI-transparency disclosure, stronger draft and approval controls, a GDPR data map and DPIA assessment, supplier verification controls, and production security/incident governance.

## Section 7: What this report is not

This report is not a legal opinion, conformity assessment or certification. It is an independent, evidence-limited first-pass audit based only on the supplied system brief. Final classification and compliance conclusions should be verified with qualified EU legal counsel and the relevant competent authorities before placing or making the system available in the EU.

## Phase 5: Debrief status

A live, five-step debrief could not be conducted for this draft because no builder context or meeting has been supplied. The required comparison of self-audit and peer-audit classifications, the gap list and the builder's explanations therefore remain **pending**.

The audit is ready for debrief, but no joint closing note should be invented. Once the builder participates, record:

1. The builder and auditor walk-through sequence.
2. The builder's five-minute response and any clarified facts.
3. Agreed/disputed classifications and reasons.
4. Findings shared by both audits and independently identified findings.
5. A joint two-to-three-sentence closing note on the difference between self-audit and independent peer review.