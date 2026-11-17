# CompanyScope peer audit report

**Auditor:** independent peer reviewer<br>
**Audited teammate:** Sean Langsdorf<br>
**Audit date:** 17 November 2026<br>
**Evidence reviewed:** `companyscope_system_brief.md` only; no self-audit findings were shared before this audit.

## 1. System summary

CompanyScope takes a German company name and optional register identifier, resolves one OpenRegister match, gathers Tavily results, and asks an OpenAI model to draft a briefing. It returns registry facts, public findings, observations, gaps, follow-up suggestions, and sources as Markdown or a browser page. It is intended for legal, in-house, and business research, not automated hiring, credit, client-acceptance, transaction, or judicial decisions. Human source verification is advised but not enforced.

## 2. Risk classification

**First-pass tier: Limited risk / transparency.**

Nothing in the brief describes an Article 5 prohibited practice. A legal-sector audience is not itself an Annex III use: point 8(a) covers assisting a judicial authority or its behalf in researching/interpreting facts and law or applying law to concrete facts. The brief instead describes preparatory company research and excludes consequential decisions. Reassess if a customer uses it for judicial, employment, credit/essential-service, or comparable Annex III decisions.

Article 50 likely applies: the browser page may interact directly with natural persons and the model generates report text. The brief does not evidence a first-interaction notice or machine-readable output marking. If text is published to inform the public on a public-interest matter, the deployer must assess Article 50(4), including the human editorial-control exception. See the [official AI Act text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng/pdf).

## 3. Role map

| Party | Provisional role | Obligations and control implications |
|---|---|---|
| Sean / entity placing CompanyScope under its name | Provider of the integrated system if placed into service or made available; provisional for this prototype | Define purpose and prohibited uses; provide Article 50 controls; support Article 4 AI literacy; keep vendor/version/source/change records; reassess Article 6/16 if the purpose changes. |
| Law-firm, in-house, or business user | Deployer; Sean may also be deployer | Stay within purpose, verify entity and sources, retain competent human review, protect inputs, and assess Article 50(4) before public-interest publication. |
| OpenAI model/API | Third-party model/system provider; exact role unknown | Confirm model/version, retention/training, region, security, subprocessors, and terms. |
| Tavily; OpenRegister | Search vendor; registry source/API | Minimise queries; review privacy, transfers, confidentiality, source terms, licence, freshness, matching evidence, and corrections. |
| n8n/hosting/authentication | Workflow/hosting vendors; mode unknown | Identify access to prompts, queries, logs, and reports; contract for security, deletion, subprocessors, and data processing. |

## 4. Compliance findings

**Parallel legal issues:** GDPR applies to personal data in queries, web results, prompts, and reports. For law-firm use, German professional secrecy and service-provider rules (BRAO §§ 43a, 43e; § 203 StGB) apply. Consumer-protection/marketing rules matter if the service is offered to consumers or marketed with claims about accuracy or verification; source licences, database rights, and website terms also require review.

**Finding 1 — Article 50 transparency and output provenance**<br>
**Severity:** Significant<br>
**Description:** Direct browser interaction and generated text are described, but no first-interaction notice or machine-readable/detectable output marker is evidenced. “Professional review advised” is not enough. Public-interest publication needs a separate Article 50(4) assessment.<br>
**Recommended action:** Add/test the notice; implement an interoperable output marker; retain generation records; add a publication gate recording human editorial responsibility where an exception is relied upon.<br>
**Escalation needed?** Yes — product owner plus legal/privacy lead before public or paid launch.

**Finding 2 — Unsupported claims and unenforced human review**<br>
**Severity:** Significant<br>
**Description:** Structural/reference checks do not establish claim support or completeness. Human verification is advisory although errors can affect companies and named people.<br>
**Recommended action:** Require entity confirmation, source opening, claim-to-source checking, fact/inference separation, correction/omission, and named sign-off before sharing. Retain stop behavior for unresolved matches and a correction route.<br>
**Escalation needed?** Yes — product owner and the professional-risk owner for each deploying organization.

**Finding 3 — GDPR data governance and vendor chain are not evidenced**<br>
**Severity:** Significant<br>
**Description:** Queries can reveal research activity; results may contain personal data; prompts/reports pass through several services. Controller/processor roles, lawful basis, notices, minimisation, retention, rights, security, DPIA screening, and international transfers are not evidenced. The [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/) applies alongside the AI Act.<br>
**Recommended action:** Map data flows and processing roles; default to necessary public data; complete DPAs/transfer assessments and retention settings; publish privacy information; test access, deletion, correction, and incidents.<br>
**Escalation needed?** Yes — data-protection officer/privacy counsel and vendor-management owner.

**Finding 4 — Legal confidentiality and source-use controls**<br>
**Severity:** Significant<br>
**Description:** A query can disclose which company or matter is being researched, and free-text inputs may contain client information. German lawyers' confidentiality/service-provider rules (BRAO §§ 43a, 43e; § 203 StGB) and source-use terms are relevant. See [BRAO](https://www.gesetze-im-internet.de/brao/BJNR005650959.html) and [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html).<br>
**Recommended action:** Default to public-data-only; prohibit client names, matter references, secrets, and unnecessary personal data; document vendor confidentiality/location/deletion; verify source permissions.<br>
**Escalation needed?** Yes — German-qualified legal counsel or the deploying firm's compliance partner.

**Finding 5 — AI literacy and lifecycle governance**<br>
**Severity:** Minor<br>
**Description:** Article 4 requires provider/deployer AI-literacy measures, but no training, owner, version/change log, incident log, or purpose reassessment is identified.<br>
**Recommended action:** Train operators on source checking and prohibited uses; assign an owner; record versions/incidents; reassess classification when features or customer workflows change.<br>
**Escalation needed?** No — assign to the system owner, with legal review of the training and use standard.

## 5. Overall recommendation

**Proceed with conditions.** The brief supports limited risk and shows no Article 5 practice or current Annex III use, so redesign is not required on these facts. Before deployment, implement Article 50 controls, mandatory human source verification, a GDPR/vendor data-flow assessment, and confidentiality/source-use controls. Prohibit or reassess consequential Annex III uses and record responsibility for final decisions and external publication.

## 6. What this report is not

This is a preliminary peer-audit exercise based on one system brief. It is not a legal opinion, conformity assessment, certification, or finding that the system complies with the EU AI Act, GDPR, German professional rules, or any other law. Sean and any future deployer should verify these conclusions with qualified legal counsel before placing the system on the EU market, putting it into service, or relying on or sharing its reports.

## Sources

- [Regulation (EU) 2024/1689 — Artificial Intelligence Act, official consolidated text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng/pdf)
- [Regulation (EU) 2016/679 — GDPR, official text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/)
- [Bundesrechtsanwaltsordnung — BRAO, official German text](https://www.gesetze-im-internet.de/brao/BJNR005650959.html)
- [German Criminal Code § 203 — violation of private secrets](https://www.gesetze-im-internet.de/stgb/__203.html)
- [Directive 2005/29/EC — unfair commercial practices](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02005L0029-20220528)
