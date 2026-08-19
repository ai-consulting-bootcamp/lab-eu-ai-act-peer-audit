# Peer project Audit  - TenderAI Assistant
**Project** - TenderAI Assistant
**Owner** - Vincent
**Auditor** - Akansha
**Audit Date** - August 18, 2026

## Phase 1: Read and annotate

Based on an analysis of the system brief for [TenderAI Assistant](https://github.com/vince-cellular/LAB_TENDERAI_ASSISTANT), key elements are annotated below into evidence categories for classification and compliance mapping.

### Tier Classification Impact
* *"decision-support and document-preparation tool"* — Establishes that the system does not make autonomous binding decisions.

* *"not designed to submit a tender automatically or make the final decision"* — Confirms human-in-the-loop operation.

* *"not designed to make decisions about employees, job applicants, customers, or members of the public"* — Excludes Annex III employment, education, or essential service high-risk classifications.

* *"Users can ask questions through the TenderAI chat interface"* — Triggers Article 50(1) natural person interaction disclosure.

* *"generate a Tender Response Blueprint containing tender requirements... and suggested response directions"* — Triggers Article 50(2) synthetic content generation disclosure.

### Ambiguities & Clarification Points
* *"production deployment could involve personal data... would require separate GDPR/data-protection assessment"* — Unclear how inputs are currently sanitized or if PII filtering exists at ingestion.

* *"AI model and vector database are provided through third-party services"* — Unclear whether vendor terms include Zero Data Retention (ZDR) or permit model training on uploaded tender inputs.

* *"MVP does not contain a formal mandatory approval workflow or a dedicated mechanism for recording every human override"* — Unclear how human oversight will be operationalized in a production environment.

### Specific Obligations Triggered
* *"Streamlit, OpenAI, Pinecone, PDF processing tools"* — Third-party vendor dependencies require data processor addendums and vulnerability management.

* *"generate a Tender Response Blueprint... and suggested response directions"* — Obligations under EU AI Act Article 50 regarding explicit transparency marking of AI-generated content.

## Phase 2: First-pass classification

| Question | Answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No** The system does not employ subliminal techniques, exploit vulnerabilities, perform social scoring, or conduct real-time remote biometric identification. |
| Does this system operate in any of the eight Annex III areas? | **No** The system processes B2B tender documents and company knowledge bases. It does not operate in critical infrastructure, education, employment, essential public services, law enforcement, migration, or administration of justice. |
| If Annex III: does it significantly influence decisions in that area? | **Not applicable** The system does not operate within an Annex III sector. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **Yes.** The system directly interacts with human end-users via a Streamlit chat interface (Art. 50(1)) and generates synthetic text/blueprints (Art. 50(2)). |
| First-pass risk tier | **Limited risk** |
| One-sentence justification citing the specific article or Annex entry | TenderAI Assistant falls under the Limited Risk tier of the EU AI Act because it operates as an AI-enabled document processing and text generation assistant that interacts with humans and generates synthetic text, directly triggering `Article 50` transparency requirements while avoiding all `Article 5` prohibited practices and `Annex III` high-risk domain classifications. |

## Phase 3: Clarifying questions log

1. Does the TenderAI user interface explicitly inform users that they are interacting with an AI system and that generated blueprints are synthetic outputs?

* *What to know:* Presence of visible disclosures in the Streamlit UI and document exports.

* *Why it matters:* Required to verify compliance with `Article 50(1) and 50(2)` transparency mandates.

* *Provisional assumption:* The MVP currently *lacks* explicit `Article 50` transparency notices in the UI and generated PDF/text exports.

2. What specific data retention and usage policies are enforced by the third-party LLM (OpenAI) and vector database (Pinecone) API endpoints?

* *What to know:* Whether third-party vendors store, log, or use uploaded tender text and company knowledge base vectors for model retraining.

* *Why it matters:* Dictates commercial confidentiality exposure and GDPR compliance regarding third-party data processing.

* *Provisional assumption:* Standard commercial API endpoints are used without confirmed Zero Data Retention (ZDR) agreements or enterprise privacy toggles.

3. Are client-side data sanitization or PII/confidentiality redaction mechanisms implemented prior to vector embedding and LLM prompt construction?

* *What to know:* Whether uploaded tender PDFs are screened for personal names, contact info, or proprietary pricing before transmission to third-party services.

* *Why it matters:* Determines GDPR exposure and parallel legal liability regarding commercial trade secrets.

* *Provisional assumption:* Documents are ingested directly into Pinecone and OpenAI without automated pre-ingestion PII or secret redaction.

4. Is there any mechanism planned to enforce mandatory human sign-off before a generated tender response is exported for submission?

* *What to know:* How human oversight will transition from informal expectation to an enforced workflow step.

* *Why it matters:* Validates the "decision-support" premise and ensures deployer accountability under general product safety and liability frameworks.

* *Provisional assumption:* Human review relies entirely on organizational procedure without software-enforced guardrails or audit logging.

## Phase 4: Audit Report 

**System Name:** TenderAI Assistant (LAB_TENDERAI_ASSISTANT)

**Developer / Owner:** Vincent (vince-cellular)

**Auditor:** Akansha Verma 

**Date:** August 18, 2026

### Section 1: System Summary

TenderAI Assistant is a Retrieval-Augmented Generation (RAG) application designed to assist business development and proposal teams in analyzing tender PDFs and drafting bid responses. The tool extracts requirements from tender documents, cross-references them against a company knowledge base stored in a vector database (Pinecone), and outputs compliance matrices, readiness assessments, and response blueprints. It is designed purely as an internal decision-support system, leaving final commercial decisions and bid submissions entirely to human proposal teams.

### Section 2: Risk Classification
* **Risk Tier:** Limited Risk

* **Governing Provisions:** EU AI Act Article 50 (Transparency Obligations)

* **Uncertainties:** If a production deployer relies on TenderAI without human oversight to automatically generate and submit bids in regulated public procurement contexts, misuse could create contract liability risks, though the system itself remains outside Annex III high-risk categories.

### Section 3: Role Map

* **Provider:** vince-cellular (Developer of TenderAI Assistant MVP).
  * **Obligations:** Ensure system design permits Article 50 compliance, provide clear system documentation detailing AI capabilities/limitations, and ensure secure integration of upstream third-party APIs.

* **Deployer:** The purchasing company using TenderAI (bid, sales engineering, and BD teams).
    * **Obligations:** Inform internal staff that they are interacting with AI, ensure human verification of generated response blueprints before external submission, and implement appropriate data handling policies.

* **Third-Party Vendors:** OpenAI (LLM Provider), Pinecone (Vector Database Provider).
    * **Obligations:** Provide enterprise-grade data privacy assurances, secure API access, and comply with EU-US data transfer mechanisms under GDPR.

### Section 4: Compliance Findings
1. **Finding 1 — Absence of Article 50 Transparency Disclaimers**
    
    **Severity:** Significant
    
    **Description:** `EU AI Act Article 50(1)` requires providers to ensure AI systems intended to interact with natural persons are designed so users know they are interacting with AI. `Article 50(2)` requires outputs of text-generating AI to be marked in a machine-readable format and detectably labelled as artificially generated. The brief and repository reveal no user-facing disclaimers in the Streamlit interface or watermark/metadata tags in generated blueprints.

    **Recommended Action:** Add a persistent visual indicator in the Streamlit UI stating that outputs are AI-generated, and inject standard header metadata into generated response blueprints and exported reports.

    **Escalation Needed?:** Yes — Lead Developer (vince-cellular).

2. **Finding 2 — Data Governance and Third-Party API Data Exposure**
    
    **Severity:** Significant

    **Description:** The system ingests raw tender PDFs and company knowledge base materials, transmitting vector embeddings and text prompts to Pinecone and OpenAI. In a production environment, sending unredacted trade secrets, customer lists, or employee personal data to external APIs without verified Zero Data Retention (ZDR) terms violates GDPR data minimization principles and risks proprietary data exposure.

    **Recommended Action:** Execute enterprise ZDR agreements with OpenAI and Pinecone, and implement a local PII/confidentiality sanitization script in the PDF ingestion pipeline prior to embedding.

    **Escalation Needed?:** Yes — Legal / Data Protection Officer (DPO).

3. **Finding 3 — Unenforced Human-in-the-Loop Override & Logging**
    
    **Severity:** Minor

    **Description:** The system brief explicitly positions TenderAI as a decision-support tool, yet the MVP lacks formal mandatory sign-off checkpoints or logging for human edits and overrides. While not a strict violation for Limited Risk systems, lack of auditability weakens deployer risk management.

    **Recommended Action:** Introduce a simple "Human Verified" confirmation checkbox in the Streamlit workflow before allowing export of final response blueprints, and log user approvals.

    **Escalation Needed?:** No.

### Section 5: Overall Recommendation
**Proceed with Conditions.**

TenderAI Assistant presents no blocking Article 5 prohibited practices or Annex III high-risk hurdles. It is a well-scoped decision-support utility. Deployment to production may proceed once two conditions are fulfilled: (1) implementation of Article 50 UI disclaimers and export metadata, and (2) verification of Zero Data Retention API agreements alongside ingestion data-filtering safeguards.

### Section 6: What This Report Is Not
This report is an independent peer audit produced for training purposes. It does not constitute formal legal advice, an official EU AI Act conformity assessment, or regulatory certification. System deployers must verify final compliance strategies with qualified legal counsel before market placement in the European Union.

---

## Phase 5: Debrief conversation

**Debrief Agenda**
1. **Auditor Walkthrough:** Auditor presents findings 1–3 and the "Proceed with Conditions" recommendation without interruption.

2. **Builder Response:** Its aligned with what builder audited in their report apart from data retention.

3. **Classification Alignment:** Compared self-audit vs. peer audit tiers. Both parties confirm alignment on the `Limited Risk` tier due to `Article 50` transparency triggers and absence of autonomous decision-making.

4. Gap Analysis:

- **Builder caught / Peer missed:** Deep code-level implementation details in the Streamlit frontend.

- **Peer caught / Builder missed:** Third-party API data retention implications (ZDR) and formal machine-readable labeling under Article 50(2).

**Joint Closing Note**

> Auditing an external project forces strict reliance on explicit system documentation and regulatory text rather than internal builder intentions. This debrief highlighted that while the developer focused heavily on operational RAG functionality, the external audit brought critical focus to edge-case compliance requirements—specifically Article 50 transparency labeling and upstream vendor data governance—that are easily overlooked from inside the codebase.

## Stretch

**Task: Remediating Article 50 Transparency & Data Governance (Findings 1 & 2)**

| Parameter | Detail |
|---|---|
| Objective | Implement Article 50 compliance controls and secure third-party data processing safeguards for `LAB_TENDERAI_ASSISTANT`. |
| Deliverable | 1. Streamlit UI update containing an AI interaction banner and "AI-Generated Draft" export header. 2. Python pre-ingestion regex/NER PII scrubbing module (`scrubber.py`).3. Executed OpenAI/Pinecone Zero Data Retention (ZDR) API agreement confirmation doc. |
| Responsible Party | Lead Developer (`vince-cellular`) in coordination with Project Legal/DPO. |
| Timeline | **10 Working Days** (Days 1–4: UI & Scrubber Dev; Days 5–8: Vendor ZDR confirmation; Days 9–10: Testing & Sign-off). |
| Verification Evidence | Code pull request containing UI disclaimers and metadata injection; sample PDF export with visible AI attribution; signed ZDR vendor confirmation form.|
