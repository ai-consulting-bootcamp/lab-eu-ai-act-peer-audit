# Audit Report - RegGuard-Mini

Auditor: Nelly Pourmehr
System owner: Kimia Asgari
Date: 2026-08-18

## Section 1: System summary

RegGuard-Mini is a design-support assistant for car exterior designers. A designer uploads a 3D geometry file. The system measures the shape, checks it against a mix of legal and internal design rules, and flags likely problem areas with a confidence figure. The designer can ask follow-up questions in plain language and gets suggested fixes. Every suggestion stays a preview until the designer explicitly saves it. The designer can hand-assemble a report to send to an engineering colleague. The system never changes geometry on its own and never approves anything.

## Section 2: Risk classification

**First-pass tier:** Minimal risk

**Justification:** The system does not fall under any Article 5 prohibited practice. It does not operate in any of the eight Annex III high-risk areas, it evaluates a vehicle shape, not a person. It is not a safety component embedded in the final vehicle under Annex I product-safety legislation, since it operates upstream of the design, advisory only, with a human deciding every change.

**Areas of uncertainty:** Confidence is moderate on whether the tool could function as a de facto compliance check if used carelessly downstream, and on whether the Article 50 disclosure duty is already satisfied by the professional framing of the interface. Both are logged as open questions.

## Section 3: Role map

- **Provider:** Onyx Dynamics, if the system moves to production as described. Currently, the individual builder for the course version.
- **Deployer:** The car manufacturer's design studio using the tool.
- **Third-party vendor:** The commercial LLM provider supplying the language and reasoning layer via API.

**Key obligations by role:** Even at minimal risk, the provider carries GDPR obligations for any personal data processed (designer name, questions, report recipient details). The deployer carries obligations around confidential geometry handling and internal data governance. The LLM vendor's data processing terms need review to confirm no vehicle geometry or personal data is retained or used for vendor-side training.

## Section 4: Compliance findings

**Finding 1 - Article 50 disclosure clarity**
Severity: Minor
Description: The interface is described as a plain-language chat assistant. It is not confirmed whether the tool explicitly states it is an AI system on first use. Professional context may already satisfy the "obvious" exception, but this should be confirmed, not assumed.
Recommended action: Add a one-line disclosure on first use, low cost, removes any ambiguity.
Escalation needed? No.

**Finding 2 - Scope creep from advisory to the actual sign-off**
Severity: Significant
Description: The brief frames the tool as advisory and upstream of the real simulation. If, in practice, teams start treating a clean RegGuard-Mini result as sufficient and skip or shorten the downstream simulation, the actual risk profile becomes higher than the current tier reflects.
Recommended action: Add an explicit, persistent disclaimer in the report output stating the tool does not replace formal simulation or type-approval assessment.
Escalation needed? Yes, to the product team defining how the report is used downstream.

**Finding 3 - Personal data and retention undefined**
Severity: Significant
Description: The brief confirms personal data is collected (names, questions, report recipient details) but does not state retention period or storage location.
Recommended action: Define a retention policy and confirm storage location before production use.
Escalation needed? Yes, to whoever owns data governance for the production build.

**Finding 4 - Confidential geometry handling via third-party LLM**
Severity: Significant
Description: Unreleased vehicle geometry is described as highly confidential. The system uses a commercial LLM via API for the language and reasoning layer. It is not stated whether geometry data is exposed to that vendor, or only the measurement outputs are.
Recommended action: Confirm and document what data reaches the LLM vendor, and secure contractual terms preventing retention or training use.
Escalation needed? Yes, to legal and to whoever manages the LLM vendor contract.

## Section 5: Overall recommendation

**Proceed with conditions.** No blocking findings. Three significant findings need resolution before production use: the downstream scope-creep risk, personal data retention, and confidential geometry exposure to the LLM vendor. None of these require a redesign of the system's core logic, they require documentation, disclaimers, and vendor terms.

## Section 6: What this report is not

This report is not a legal opinion, not a conformity assessment, and not a certification. Conclusions should be verified with legal counsel before any EU market placement.