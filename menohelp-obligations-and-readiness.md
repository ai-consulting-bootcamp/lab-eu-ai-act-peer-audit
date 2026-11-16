# Menohelp: roles, transparency and conditional readiness

Evidence IDs and legal sources: [register](menohelp-evidence-and-legal-sources.md). Status words describe available evidence, not certification.

## Role map

| Actor | Provisional role | Duties / boundaries |
|---|---|---|
| Ben Mayer / entity offering Menohelp | Prospective downstream AI-system provider if offering or putting it into service under its own name; likely controller for its own consumer service | Own intended purpose, Article 50 design, AI literacy support and product safeguards. Confirm legal entity, market date, contracts and GDPR roles. If high-risk, own applicable provider duties; using OpenAI does not transfer these upstream. |
| Practitioner or clinic using reports professionally | Prospective deployer; separate controller/processor allocation depends on actual service | Follow instructions and operate suitable oversight. Article 26 duties are conditional on a high-risk deployment and applicable dates. Article 27 FRIA is not automatic just because a clinic uses health software: check its Article 6(2) and deployer triggers. |
| Individual using it personally | End user; personal non-professional use excluded from the deployer definition | Do not assign professional deployer compliance duties to consumers. Their personal-use status does not exempt the commercial provider. |
| OpenAI | Upstream model/API supplier; GPAI provider for relevant general-purpose models | Its applicable model-level duties include documentation and downstream information under Article 53; Article 55 depends on systemic-risk status. Confirm actual model/version and terms; no vendor audit performed. |
| Supabase | Reference database/vector-search vendor | Confirm processor terms, region, access and retention; not shown to be the product provider or a model provider. Receives query vectors; patient-table persistence is only planned. |
| Resend | Optional email delivery vendor | Processes recipient address and report/chart; establish terms, recipient controls and retention. Local non-storage claims do not cover mailboxes. |
| Render / Streamlit Cloud | Proposed hosting suppliers | Not verified live processors. Add to the production data map only if adopted. Open-source libraries themselves do not establish a hosted vendor relationship. |
| Sergii as auditor | External reviewer | Provisional assessment and remediation scoping; no certification or provider status merely from this review. |

## Transparency and cross-cutting checks

| Requirement | Evidence-based status | Action |
|---|---|---|
| Article 50(1), (5): clear disclosure at first interaction, unless obvious | **Partial:** input captions mention OpenAI and the disclaimer calls the report generated. Explicit, consistent AI identification across all inputs and exports is not established (E4-E5). | Add an accessible notice before generation and an AI-generated label to report/download/email; test each path. |
| Article 50(2): machine-readable marking/detectability of synthetic text, with applicable exceptions and feasibility qualifications | **Not evidenced:** no demonstrated end-to-end marking solution in report/export/email; vendor capability not checked. | Allocate responsibility with supplier, assess technical feasibility, preserve provenance and verify marking survives output transformations. Do not assume a visible label alone meets this duty. |
| Article 50(3): emotion recognition / biometric categorisation | **Not triggered on evidence.** Symptom self-report is not biometric inference. | Reassess if biometric features are added. |
| Article 50(4): deepfakes / public-interest publication | **Not triggered by private reports on current facts.** | Reassess any public generated health content or deepfake feature and the applicable exceptions. |
| Article 4: AI literacy support | **Not evidenced:** no role-specific operating/training record reviewed. | Name an owner and document training on limits, failed checks, health data and escalation. |
| GDPR | **Partial controls, unresolved legal readiness:** name stripping and local memory help; health information still travels to vendors (E4-E7). | Confirm Article 6 basis + Article 9 condition, notice, processor terms, retention, deletion, access controls and transfer safeguards; screen DPIA necessity. |
| Consumer claims and content rights | **Partial:** disclaimer and demo licence limitation acknowledged; 'verified analysis' and 'nothing stored' may overstate evidence (E1, E4, E8-E9). | Correct claims, verify data provenance and pilot/commercial licence scope before reuse. |

## Conditional 11-provider-obligation review

Included because the medical-device boundary is unresolved. This is a **readiness scenario**, not an assertion that all high-risk obligations currently apply. Met = sufficient reviewed evidence; Partial = some implementation, incomplete compliance evidence; Absent = required evidence not located; N/A = the legal trigger is not established. No item is certified as Met.

| # | Course obligation | Status if high-risk route confirmed | Evidence / next step |
|---|---|---|---|
| 1 | Risk management, Article 9 | Partial | E2 lists risks; no controlled lifecycle risk file, acceptance criteria or approved residual-risk decision reviewed. Create and maintain them. |
| 2 | Data governance, Article 10 | Partial | Normalisation and reference selection exist; representativeness, provenance, subgroup coverage and source-rights evidence need review. Scope duties to the downstream development/testing data; no foundation-model training claimed. |
| 3 | Technical documentation, Article 11 / Annex IV | Partial | README, architecture and tests exist; no complete regulatory technical file reviewed. Version the intended purpose, validation, limitations and change history. |
| 4 | Automatic logging, Article 12; retention Articles 19/26 where applicable | Partial | Errors/retries appear in session output; no durable traceability/retention policy verified. Design minimised logs; six-month rules concern controlled logs, not indiscriminate retention of patient records. |
| 5 | Instructions for use, Article 13 | Partial | Setup guide and disclaimer exist; no complete professional instructions/limitations/performance and maintenance pack reviewed. |
| 6 | Human oversight, Article 14 | Partial | User confirms lab values and is advised to see a doctor; no required qualified review, override workflow or release gate (E5/E8). |
| 7 | Accuracy, robustness, cybersecurity, Article 15 | Partial | Numeric checks, wording guards and tests exist; retry exhaustion and ID-based access require remediation. No clinical validation or representative subgroup performance established. |
| 8 | Conformity assessment, Article 43 | Absent in evidence | No assessment record. Determine sector route with specialist; Annex III internal control is not automatically the right procedure for medical devices. |
| 9 | EU declaration and CE marking, Articles 47-48 | Absent in evidence | No declaration/marking package reviewed; prepare only under the confirmed applicable route. |
| 10 | Registration, Article 49 | N/A for the currently contemplated Annex I-only route | Article 49's Annex III registration duties must not be indiscriminately applied to Annex I medical devices. Determine MDR/IVDR registration obligations separately; reassess if an Annex III use appears. |
| 11 | Post-market monitoring / serious incidents, Articles 72-73 | Absent in evidence | No controlled monitoring plan, complaint owner or reporting procedure reviewed. Align with sector vigilance rules where relevant. |

The teaching list is not exhaustive. If the device/high-risk route is confirmed, legal counsel must also scope quality management (Article 17), documentation retention, corrective action and sector-specific requirements. Deferring applicable AI Act duties does not defer existing GDPR or medical-device obligations.
