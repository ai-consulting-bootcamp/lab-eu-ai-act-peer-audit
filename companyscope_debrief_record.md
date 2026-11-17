# CompanyScope peer-audit debrief record

**Auditor:** Jedrzej Czarnota<br>
**Builder:** Sean Langsdorf<br>
**Planned date:** 17 November 2026<br>
**Audit report:** [`companyscope_peer_audit_report.md`](./companyscope_peer_audit_report.md)

## 1. Auditor presents

Presentation order:

1. System summary: CompanyScope is a company-research briefing workflow using OpenRegister, Tavily, n8n, and an OpenAI model.
2. Classification: limited risk / transparency on the supplied facts; no Article 5 practice identified; no current Annex III purpose identified.
3. Main uncertainty: actual customer use could change the classification, especially if reports influence employment, credit, essential-service, judicial, or public-interest publication decisions.
4. Top findings: Article 50 controls are not evidenced; source verification and human sign-off are advisory; GDPR/vendor and legal-confidentiality controls are not evidenced.
5. Recommendation: proceed with conditions, including transparency, mandatory human review, data-flow/vendor controls, and strict use-purpose guardrails.

## 2. Builder responds

- Actual model, hosting, and vendor regions: DE, US
- Existing AI notice/output marking: none
- Actual customer or prototype use outside the stated purpose: none
- Existing human review, source checking, and correction process: none
- Existing privacy, confidentiality, and vendor agreements: moderate

## 3 and 4. Compare classifications and gap lists

Jedrzej's top three gaps are:

- Article 50 notice and machine-readable output marking are not evidenced.
- Human source verification and sign-off are advised but not enforced.
- GDPR/vendor data-flow and legal-confidentiality controls are not evidenced.


## 5. Joint closing note

“The external audit made the system's intended-use boundary and evidence gaps visible because the reviewer did not share the builder's assumptions. The self-audit benefits from implementation context, while the peer audit tests whether a new reader can infer the safeguards from the documentation alone. The main lesson is that a control that exists only in the builder's practice is difficult to audit, trust, or transfer to a future deployer.”
