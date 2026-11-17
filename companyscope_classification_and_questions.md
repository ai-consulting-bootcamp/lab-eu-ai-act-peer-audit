# CompanyScope: classification and clarifying-questions log

**Auditor:** independent peer reviewer<br>
**Date:** 17 November 2026<br>
**Source available:** system brief only; Sean's self-audit findings were not provided.

## Phase 2 — first-pass classification

| Question | My answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No indication on the brief.** It does not describe subliminal/manipulative exploitation, social scoring, biometric categorisation, emotion recognition, or another Article 5 practice. This remains subject to the stated purpose and actual deployment. |
| Does this system operate in any of the eight Annex III areas? | **Not on the described intended purpose.** Company research for counterparty preparation is not itself one of the listed use cases. The legal audience alone does not make it “administration of justice.” |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | **Not applicable on current facts.** If a law firm later uses it for a judicial authority, or a customer uses it to make employment, credit, client-acceptance, or transaction decisions about people, reassess. The current brief expressly says it does not make those decisions. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **Likely yes.** The browser form/results page may interact directly with natural persons, and the model generates report text. Article 50(1) notice and Article 50(2) machine-readable marking should be implemented or documented as satisfied. Article 50(4) should be checked if generated text is published to inform the public on a matter of public interest. |
| First-pass risk tier | **Limited risk / transparency.** |
| One-sentence justification citing the specific article or Annex entry | On the supplied intended purpose, CompanyScope is not an Article 5 practice and is not an Annex III use; it is instead a transparency case under Article 50 because it presents AI-generated text to users, subject to reassessment if the deployment purpose changes. |

**Legal basis used:** Regulation (EU) 2024/1689, Articles 4–6 and 50, and Annex III point 8(a), which covers systems intended for a judicial authority or its behalf to research/interpret facts and law or apply law to concrete facts. The [official AI Act text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng/pdf) is the controlling source for this preliminary exercise.

## Phase 3 — clarifying questions log

### 1. Will any deployer use the report to make or materially influence a decision about a natural person or a legal proceeding?

- **Need to know:** Whether the actual use includes hiring, credit, insurance, essential services, client acceptance, transaction approval, litigation strategy, judicial work, or alternative dispute resolution.
- **Why it matters:** The actual intended purpose and material influence can move the system into an Annex III area, including employment, essential private services, or Annex III point 8(a) administration of justice. A disclaimer alone would not cure a product designed or routinely used for that purpose.
- **Provisional assumption:** No. The system is limited to company research and the operator remains responsible for decisions, as the brief states.

### 2. Where and how are users told that they are interacting with AI, and how are generated reports marked?

- **Need to know:** Whether the browser page gives a clear Article 50(1) notice at first interaction and whether Markdown/HTML outputs carry a machine-readable, detectable AI-generated marker. Also confirm whether any public-interest publication receives the Article 50(4) disclosure or qualifies for the human editorial-control exception.
- **Why it matters:** The brief describes a browser results page and generated text but gives no evidence of either transparency control.
- **Provisional assumption:** Neither control is implemented unless Sean can produce interface screenshots, output samples, and technical evidence.

### 3. What exact model, account, hosting arrangement, and vendor regions are used?

- **Need to know:** The OpenAI model/version, n8n hosting mode, Tavily and OpenRegister endpoints, retention/training settings, subprocessors, transfer mechanism, and whether data are sent outside the EEA.
- **Why it matters:** This determines the operator/provider chain, contractual due diligence, GDPR processor/controller roles, international-transfer safeguards, and confidentiality exposure.
- **Provisional assumption:** At least one external vendor receives query or evidence data; no compliant data-processing and confidentiality assessment is evidenced.

### 4. What personal, confidential, or client-matter data can enter the workflow, and how long are they retained?

- **Need to know:** Whether the workflow accepts only public company identifiers or also free text, names, contact details, client instructions, matter references, or sensitive facts; retention/deletion and access controls for n8n logs, vendor logs, reports, and backups.
- **Why it matters:** GDPR principles and legal-professional confidentiality apply to personal or confidential material even when the source is public. Data minimisation, lawful basis, transparency, security, rights handling, and DPIA screening depend on these facts.
- **Provisional assumption:** Public company research is allowed, but personal data and confidential client information can be transmitted; minimisation and deletion controls are not yet proven.

### 5. Is output ever published outside the research team, and who has editorial responsibility?

- **Need to know:** Whether reports remain internal, are sent to clients/counterparties, or are published publicly; whether a named competent reviewer verifies each claim and source before release.
- **Why it matters:** Public-interest publication can trigger Article 50(4), while external circulation increases GDPR accuracy/correction, confidentiality, defamation, consumer-protection, and professional-liability risk.
- **Provisional assumption:** Reports are internal working documents and should not be shared externally until a documented human review has occurred.
