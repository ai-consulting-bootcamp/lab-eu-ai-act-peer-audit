# Independent EU AI Act Audit Report

**Auditor:** Roodabeh Seif  
**Teammate:** Armin  
**System:** Case 1 — AI-assisted quotation preparation for industrial equipment  
**Status:** Provisional; based only on the supplied brief

## 1. System summary

The system compares customer requirements with supplier quotations and approved historical records. It flags discrepancies and drafts technical and commercial proposals, including new explanations and supplier-selection reasoning. A qualified expert checks the evidence, confirms the supplier and final price, and controls sending. Sending stops when an essential claim lacks reliable evidence or a discrepancy remains unresolved.

## 2. Risk classification

| Question | Answer |
| --- | --- |
| Article 5 prohibited practice? | No. None of the described purposes or functions falls under Article 5. |
| Annex III high-risk area? | No. Commercial quotation preparation and supplier comparison are not listed in Annex III. |
| Direct interaction under Article 50(1)? | Apparently no. Staff use the system internally and a human sends the proposal. |
| Synthetic text under Article 50(2)? | Potentially yes. The provider should confirm machine-readable marking or document why an exception applies. |
| Public-interest disclosure under Article 50(4)? | Apparently no. This is a private commercial proposal, not public-interest publication. |
| First-pass tier | Limited risk / transparency obligations, because the system generates new text and the provider must assess the Article 50(2) machine-readable marking requirement. |

**Justification:** The system is neither prohibited under Article 5 nor listed as high-risk under Article 6(2) and Annex III. It generates new proposal text, so the provider should assess the Article 50(2) requirement to mark synthetic text in a machine-readable format and document whether an exception applies. The customer-facing disclosure rules in Article 50(1) and Article 50(4) do not appear to apply on the facts given. Its possible financial and equipment-safety consequences remain important, but do not alone make it high-risk under the EU AI Act.

## 3. Role map

| Actor | Likely role and responsibility |
| --- | --- |
| Software vendor or integrator | **Provider:** define intended purpose, supply documentation, assess Article 50(2), explain limitations, and support safe use. |
| Trading company | **Deployer:** train staff, protect data, maintain expert review, and monitor output quality. |
| General-purpose model vendor | **Third-party model provider:** meet applicable model obligations and provide information to the downstream provider. |
| Cloud or document vendors | **Technical vendors/processors:** meet contractual security, confidentiality, retention, and data-processing requirements. |
| Commercial and technical expert | **Human reviewer:** verify evidence, resolve discrepancies, confirm suitability, supplier, and price, and control sending. |

If the trading company develops or markets the system under its own name, it may become the provider. This must be confirmed contractually.

## 4. Compliance findings

### Finding 1 — AI literacy is not documented

**Severity:** Significant  
**Description:** Article 4 requires measures supporting adequate AI literacy, but no staff training is described.  
**Action:** Train users and reviewers on hallucinations, evidence checks, confidentiality, escalation, overrides, and sending controls. Keep training records.  
**Escalation:** No; provider and deployer owners should implement it.

### Finding 2 — Roles and vendor responsibilities are unclear

**Severity:** Significant  
**Description:** The provider, model vendor, hosting provider, and responsibility for documentation, security, monitoring, and incidents are not identified.  
**Action:** Produce a role map, data-flow diagram, and responsibility matrix. Review vendor contracts and audit rights.  
**Escalation:** Yes; procurement, information security, data protection, and legal counsel.

### Finding 3 — Article 50(2) compliance is unconfirmed

**Severity:** Significant  
**Description:** The system generates new proposal text, but no evidence confirms machine-readable marking or an applicable exception.  
**Action:** Require the provider to document compliance or the exception and preserve any marking during export.  
**Escalation:** Yes; provider compliance owner or legal counsel.

### Finding 4 — Data controls are not described

**Severity:** Significant  
**Description:** Inquiries, emails, prices, transaction records, and supplier documents may contain personal data, confidential information, and trade secrets. Data transfers, retention, model training, and deletion are unknown.  
**Action:** Map data flows; minimise data; restrict access and model training; confirm lawful processing, processor terms, transfer safeguards, retention, and deletion.  
**Escalation:** Yes; Data Protection Officer, security, procurement, and legal counsel.

### Finding 5 — Human review is strong but not verified

**Severity:** Significant  
**Description:** Source references, expert review, discrepancy checks, and stop conditions are good safeguards, but the brief does not show whether they are enforced, tested, or logged.  
**Action:** Add a mandatory approval gate; require citations for essential claims; log sources, changes, discrepancies, overrides, approval, and the final version; test missing, conflicting, and outdated documents. Mark internal drafts as AI-assisted and unapproved.  
**Escalation:** Yes; technical lead and quality or safety owner.

## 5. Overall recommendation

**Proceed with conditions.** No prohibited or Annex III high-risk use is apparent, and the human review design is strong. Deployment should require documented expert approval, evidence traceability, AI-literacy training, a confirmed role and vendor map, data and confidentiality controls, and an Article 50(2) assessment. The system must not automatically send proposals or make final supplier, price, or equipment-suitability decisions.

## 6. What this report is not

This educational audit is not a legal opinion, conformity assessment, or final legal classification. Qualified legal counsel should verify the conclusions before EU market use.

## References

- Regulation (EU) 2024/1689, Articles 3–6 and 50, and Annex III: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Regulation (EU) 2016/679 (GDPR): https://eur-lex.europa.eu/eli/reg/2016/679/oj
