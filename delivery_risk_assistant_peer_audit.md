# Peer Audit — AI Delivery Risk Assistant

**Audited project:** AI Delivery Risk Assistant  
**Builder:** Akansha Verma  
**Auditor:** [Your Name]  
**Audit date:** 18 August 2026

---

## Section 1 — System Summary

The AI Delivery Risk Assistant is a project-management support system that analyzes software delivery documents and identifies current project risks. It retrieves relevant evidence from project documents, uses AI to extract potential risks, validates the supporting citations, assesses severity, and produces a delivery-risk report. High-severity risks or contradictions are routed to a human reviewer through a HITL workflow.

The system can process project reports, stakeholder communications, Slack or stand-up text, incident and retrospective documents, and CSV ticket exports. It also allows users to upload additional documents into a project-specific knowledge base. The resulting information can include risk findings, severity, delivery-health scores, business-impact assessments, and recommendations.

The system is primarily intended for engineering managers, delivery leads, scrum masters, and executives. Based on the brief, it does not directly evaluate employee performance or make employment decisions, although its recommendations could indirectly influence resource allocation. The system uses OpenAI, Pinecone, Cohere, Telegram, Streamlit, FastAPI, and n8n/Notion as part of its architecture.

---

## Section 2 — Risk Classification

| Question | Answer |
| --- | --- |
| Does this system fall under any prohibited category (Article 5)? | No apparent Article 5 prohibited practice is identified from the available system brief. |
| Does this system operate in any of the eight Annex III areas? | No apparent Annex III use case is identified from the available information. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | Provisionally not applicable because no Annex III area has been established. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | Yes. The system provides an interactive Streamlit AI assistant, so Article 50(1) transparency should be assessed. |
| First-pass risk tier | **Limited risk / transparency** |
| One-sentence justification | The system does not appear to fall within an Article 5 prohibited practice or Annex III high-risk use case based on the available information, but its direct interaction with users creates an Article 50(1) transparency requirement unless the AI nature is already obvious from the context. |

---

## Section 3 — Clarifying Questions Log

The following questions should be addressed before the risk classification is considered final.

### Question 1 — Individual employee/resource allocation

**Question:** Does the AI system make recommendations about assigning tasks or allocating resources to named employees based on their behaviour, performance, or personal characteristics?

**Why it matters:** Certain AI systems used in employment and worker-management contexts fall within Annex III. If the system were used for these purposes, the risk classification could change.

**Provisional assumption:** No. Based on the available system brief, the system identifies project delivery risks rather than evaluating individual workers or making employment decisions.

---

### Question 2 — Critical infrastructure

**Question:** Could the system be used as a safety component in the management or operation of critical digital infrastructure?

**Why it matters:** Certain AI systems used as safety components in critical infrastructure can fall within Annex III. Ordinary project-management or software-delivery assistance would not by itself establish this classification.

**Provisional assumption:** No. The available documentation describes a project delivery-risk assistant rather than a system performing a safety function in critical infrastructure.

---

### Question 3 — AI interaction transparency

**Question:** Does the Streamlit interface clearly inform users that they are interacting with an AI system?

**Why it matters:** Article 50(1) requires providers of AI systems intended to interact directly with natural persons to inform those persons that they are interacting with an AI system, unless this is obvious from the circumstances and context.

**Provisional assumption:** Unknown. The documentation confirms an interactive Streamlit interface and AI-generated outputs, but does not establish that a user-facing AI disclosure is displayed.

---

### Question 4 — Production data

**Question:** What categories of personal or confidential information will be processed when the system is used with real client project documents?

**Why it matters:** The production system can accept project artefacts such as communications, tickets and stand-up material. These may contain personal data or confidential business information, creating potential GDPR and data-protection obligations.

**Provisional assumption:** Real production documents may contain personal and confidential information, but the demonstration corpus itself is synthetic. No GDPR violation is assumed without further information.

---

## Section 4 — Role Map

The role mapping below is a first-pass assessment based on the available system brief and repository documentation. The final legal status of each party would depend on the actual deployment model, contracts, and use of the system.

| Role | Entity | Key AI Act obligations / relevance |
| --- | --- | --- |
| Provider | Akansha Verma / the entity placing the AI Delivery Risk Assistant on the market | If the system is placed on the market or put into service under the provider's name, the provider would have the applicable obligations associated with that role, including ensuring compliance with applicable AI Act requirements. The exact provider status should be confirmed against the final commercial arrangement. |
| Deployer | Client organisation using the AI Delivery Risk Assistant in its professional activities | The deployer would be responsible for using the system according to applicable instructions and maintaining appropriate human oversight and organisational controls. The exact obligations depend on the final use case and AI Act classification. |
| AI/model vendor | OpenAI | Provides the AI models used for risk extraction and embeddings. Its legal role depends on the specific model/service and contractual arrangement. The vendor's own obligations should not automatically be attributed to the application provider. |
| Vector database vendor | Pinecone | Provides vector-database infrastructure used to store and retrieve project evidence. Its role is primarily an infrastructure/service dependency; data-protection responsibilities should be assessed separately for production use. |
| Reranking vendor | Cohere | Provides the reranking service used to prioritise retrieved evidence. Its contractual and data-processing role should be assessed as part of the production architecture. |
| Notification/integration vendor | Telegram / n8n / Notion | Used for human-review alerts and downstream reporting. These services should be assessed for their contractual, security and data-protection implications in production. |

### Role-map conclusion

For this first-pass audit, Akansha or the commercial entity placing the AI Delivery Risk Assistant on the market would provisionally be treated as the **provider**, while the organisation using the system for project delivery activities would be treated as the **deployer**.

The external technology providers should not automatically be classified as AI Act providers of the complete Delivery Risk Assistant. Their individual legal roles depend on what component they provide and how that component is placed on the market or integrated into the overall system.

The final provider/deployer allocation should be confirmed against the production architecture and contractual arrangements before commercial deployment.

---

## Section 5 — Compliance Findings

### Finding 1 — AI Interaction Transparency

**Severity:** Significant

**Description:**

The system provides an interactive Streamlit interface through which users can interact with AI-generated risk analysis and recommendations. Article 50(1) requires users to be informed that they are interacting with an AI system unless this is already obvious from the circumstances and context. The available system brief and README do not establish that a clear AI disclosure is displayed in the user interface.

This is therefore a transparency control that should be treated as not demonstrated based on the available evidence, rather than assuming that the requirement is satisfied.

**Recommended action:**

Add a clear and visible notice to the Streamlit interface informing users that they are interacting with an AI system. The notice should appear before or at the beginning of the interaction and should explain that AI-generated findings should be reviewed before being relied upon for important project decisions.

The team should also retain evidence of the implemented disclosure, such as a UI screenshot or interface specification.

**Escalation needed?**

No for the technical implementation. Legal/compliance review is recommended to confirm the final wording and applicability before production deployment.

---

### Finding 2 — Human Review and Override Traceability

**Severity:** Minor

**Description:**

The system has a positive human-in-the-loop control for SEV-1/high-severity risks and status contradictions. These cases are routed to Telegram for human review and the workflow can return a pending approval state.

However, the system brief explicitly states that there is no universal human approval gate for ordinary delivery findings and no UI for recording an override rationale. This means that lower-severity AI-generated findings can proceed to report generation without evidence of a documented human approval decision.

Because the system is not currently identified as high-risk under Annex III, this does not establish a failure of the Article 14 high-risk human-oversight requirements. It is nevertheless an important governance and reliability control for a system whose recommendations may influence project decisions.

**Recommended action:**

Define a documented review procedure for material AI-generated delivery findings. Consider recording the reviewer, review date, decision, and reason for any modification or override. The team should determine which categories of findings require mandatory human approval before being communicated or acted upon.

**Escalation needed?**

No for the initial workflow design. The client should determine internally which project decisions require mandatory human approval.

---

### Finding 3 — Production Data Protection Assessment

**Severity:** Significant

**Description:**

The demonstration corpus is synthetic, but the system supports live uploads of project documents and can process Slack/stand-up material, stakeholder communications, ticket exports, incident records and other project artefacts. These materials may contain personal data and confidential business information.

The available documentation does not establish the production data flows, lawful basis, retention periods, deletion procedures, access controls, processor arrangements, or international transfer arrangements for this information. The system also relies on external services including OpenAI, Pinecone, Cohere and Telegram.

This is a parallel GDPR/data-protection issue rather than an AI Act risk-tier finding. The available information is insufficient to conclude that GDPR requirements are being violated, but it is also insufficient to demonstrate that production data-protection requirements have been addressed.

**Recommended action:**

Before processing real client data, document the production data flows and categories of information processed. Assess the roles of the relevant parties, vendor/processor arrangements, retention and deletion rules, access controls, security measures, and any international data transfers. The client should also determine whether a Data Protection Impact Assessment or other formal privacy review is required.

**Escalation needed?**

Yes — client Data Protection Officer, privacy specialist, or legal counsel.

---

## Section 6 — Overall Recommendation

### Proceed with conditions

The AI Delivery Risk Assistant can provisionally proceed as a prototype or controlled demonstration, but production deployment should be conditional on addressing the identified transparency and data-protection issues.

In particular, the team should:

1. Implement and verify an appropriate AI interaction disclosure in the user interface.
2. Complete a production GDPR/data-protection assessment before processing real client project data.
3. Strengthen the human-review workflow by documenting review and override decisions for material findings.

The current evidence does not indicate an Article 5 prohibited practice or an Annex III high-risk use case. However, the classification should be reassessed if the system is later used for individual employee evaluation or resource allocation, or as a safety component in critical infrastructure.

---

## Section 7 — What This Report Is Not

This report is a first-pass peer compliance review based on the system documentation and information available to the auditor.

It is **not**:

- a legal opinion;
- a formal EU AI Act conformity assessment;
- a certification; or
- a final determination of the legal responsibilities of the parties.

The conclusions should be verified with appropriate legal, privacy, or compliance specialists before EU market placement or production deployment involving real client data.

---

## Section 8 — Debrief Conversation

**Status:** To be completed after discussion with the system builder.

The auditor will compare the findings in this peer audit with the builder's self-audit.

The debrief will cover:

1. The auditor's risk classification and reasoning.
2. The builder's self-audit classification.
3. Areas where the two assessments agree.
4. Areas where the two assessments differ.
5. Findings identified by the builder but not by the auditor.
6. Findings identified by the auditor but not by the builder.
7. Any additional information provided by the builder that changes the provisional assessment.

### Debrief notes

**Builder's self-audit classification:**  
_To be completed after debrief._

**Auditor's classification:**  
**Limited risk / transparency**

**Points of agreement:**  
_To be completed after debrief._

**Points of disagreement:**  
_To be completed after debrief._

**Additional information provided by builder:**  
_To be completed after debrief._

---

## Section 9 — Joint Closing Note

_To be completed jointly with Akansha after the debrief conversation._

> The peer audit demonstrated the difference between reviewing a system as its builder and reviewing it as an independent auditor. The external perspective made it easier to identify assumptions that were not explicitly documented, particularly around transparency and production data protection. The debrief also helped distinguish genuine compliance questions from areas where additional system information was simply needed.