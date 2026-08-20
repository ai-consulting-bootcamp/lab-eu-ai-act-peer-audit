# Audit Report: Proactive Incident Agent
## Section 1: System summary

The Proactive Incident Agent is an AI-assisted decision-support system intended to help cruise-company claims, legal, and risk/compliance teams process passenger incident reports more efficiently. It extracts information from incident and medical reports, identifies missing information, and—where cases are sufficiently complete—classifies incident severity, claim risk and customer impact from Low to Critical, with an explanation and suggested follow-up questions. The system stores case information and AI audit data in Airtable and can generate weekly risk reports for publication to Notion. The stated design keeps a human claims or risk professional responsible for interpreting the output and making any consequential claims or liability decision.

## Section 2: Risk classification

First-pass tier: High impact / potentially high-risk; formal AI Act classification remains uncertain.

On the evidence provided, the system does not clearly fall within the enumerated Annex III high-risk use cases merely because it assists with cruise-claim processing. In particular, the memo does not establish that it is used for employment, access to essential services, credit, law enforcement, or another listed high-risk purpose. Nor is it described as a safety component of a regulated product. Therefore, a conclusion that it is automatically “high-risk AI” would be premature.

However, the system processes potentially sensitive health information and produces risk classifications concerning identifiable passengers. Its outputs could materially influence subsequent claims handling, escalation and potentially liability decisions. The distinction between “decision support” and a high-impact automated decision therefore requires documented assessment of the actual intended purpose and foreseeable use, rather than relying solely on the statement that a human remains in the loop.

The principal uncertainty is whether the proposed production use could cause the system to become subject to additional AI Act requirements through its actual deployment context, and whether GDPR requirements—particularly those concerning special-category health data, profiling, automated decision-making and DPIAs—apply.

## Section 3: Role map

*Provider:* Andreas Papachristophorou is currently the developer of the MVP. If he develops and places the system on the market or into service as an AI system under his own name, provider responsibilities may arise. If a cruise company substantially modifies, rebrands or deploys the system under its own name, the allocation of provider/deployer responsibilities must be reassessed.

*Deployer:* The production cruise company using the system for claims, legal, risk, compliance or guest-service activities would normally be the deployer. It would remain responsible for appropriate organisational controls and human use of the system. High-risk deployers, where applicable, have specific obligations concerning human oversight, input data, monitoring and use according to provider instructions.

*Third-party vendors:* The memo identifies Airtable and Notion as storage/reporting services and an LLM provider as an external processing component, but does not identify the actual LLM, hosting location, contractual arrangements, data-processing terms, retention settings or international transfer mechanisms. These vendors must therefore be mapped before production deployment.

## Section 4: Compliance findings
*Finding 1 — Formal AI Act risk classification and intended-purpose assessment*

Severity: Significant

Description: The memo describes the system as decision support but does not document a formal assessment against the AI Act's prohibited-practice and high-risk classification rules. The output includes claim-risk and customer-impact classifications concerning individual passengers. Human review reduces automation risk but does not, by itself, determine the AI Act classification.

Recommended action: Produce and retain a documented intended-purpose and AI Act classification assessment covering Articles 5 and 6, Annex III, foreseeable misuse and the actual decisions that may subsequently rely on the output. Explicitly define that the system cannot make or automatically trigger claims, liability or customer decisions.

Escalation needed? Yes — compliance/legal counsel.

*Finding 2 — Health and other sensitive personal data*

Severity: Significant

Description: The system may process medical reports and injury information. Health data constitute a special category of personal data under GDPR and require both an Article 6 lawful basis and an applicable Article 9 condition. The memo does not identify either.

Recommended action: Complete a GDPR data-flow and lawful-basis assessment before any production use. Minimise medical information sent to the LLM, document the Article 9 condition, define retention periods, access controls and deletion procedures, and confirm that pseudonymisation is genuine and appropriately protected.

Escalation needed? Yes — DPO/privacy counsel.

*Finding 3 — DPIA and fundamental-rights impact assessment*

Severity: Significant

Description: The memo contains no evidence of a DPIA or equivalent privacy-risk assessment. GDPR specifically identifies processing involving special-category data and systematic/extensive evaluation of individuals as circumstances requiring particular DPIA consideration.

Recommended action: Conduct a DPIA before production deployment, addressing the passenger data lifecycle, profiling/classification, LLM processing, vendor transfers, risks to passengers and mitigation measures. If the AI Act classification ultimately becomes high-risk, perform the corresponding fundamental-rights risk assessment where applicable.

Escalation needed? Yes — DPO/privacy counsel.

*Finding 4 — Third-party LLM data flow and contractual controls*

Severity: Significant

Description: The system records “the details sent to the LLM” but the memo does not identify which details are sent, which provider receives them, where processing occurs, whether data are retained or used for model training, or what contractual safeguards apply. This is particularly material because the source material may contain health data.

Recommended action: Create a complete data-flow diagram and vendor register identifying the LLM provider, Airtable, Notion and any hosting providers. Confirm DPAs, processor/subprocessor arrangements, retention, training-use restrictions, security controls and international-transfer mechanisms before real passenger data are introduced.

Escalation needed? Yes — DPO and information security/procurement.

*Finding 5 — Human oversight and automation bias*

Severity: Minor currently; Significant if production decisions rely on the classifications

Description: The stated human-in-the-loop design is a strong control: the claims officer reviews extracted information, missing fields, risk flags and explanations. However, the memo does not specify training, authority to override the system, procedures for detecting errors, or controls against automation bias. These are particularly important if the system is ultimately classified as high-risk. The AI Act requires effective human oversight for high-risk systems, including the ability to understand limitations and disregard or override outputs.

Recommended action: Establish written human-oversight procedures, user training, mandatory review of classifications, an explicit override mechanism and logging of material overrides. Monitor disagreement/error rates.

Escalation needed? No, unless classification changes to high-risk.

*Finding 6 — Accuracy, validation and audit evidence*

Severity: Significant

Description: The memo describes the functionality but provides no evidence of validation accuracy, false-positive/false-negative rates, testing against representative incident types, bias testing, or defined acceptance thresholds. A risk classification that influences claims handling could create material harm even where a human formally makes the final decision.

Recommended action: Establish a documented test set and acceptance criteria covering extraction accuracy, completeness detection, severity classification and consistency across relevant passenger/injury scenarios. Maintain versioned evaluation results and incident/error logs.

Escalation needed? Yes — product owner/risk owner; DPO where testing involves real personal data.

## Section 5: Overall recommendation

Proceed with conditions. The MVP should not move into production processing of real passenger information until the team documents the AI Act classification and intended purpose, establishes a GDPR lawful basis for processing health data, completes the required DPIA assessment, and documents the complete third-party data flow and contractual safeguards. Production use should also be conditional on validated model performance, defined human-oversight procedures, access/retention controls and clear restrictions preventing the system from making or automatically executing claims or liability decisions. The current human-in-the-loop design is a positive control, but the memo does not yet provide sufficient evidence to demonstrate that the overall system is safe and compliant for production use.

## Section 6: What this report is not

This report is not a legal opinion, conformity assessment, or certification. It is a first-pass compliance audit based on the information supplied in the system brief. The conclusions should be verified against the final technical implementation, contractual arrangements, intended use and applicable national/EU law, with legal counsel and the relevant DPO consulted before EU market placement or production deployment.