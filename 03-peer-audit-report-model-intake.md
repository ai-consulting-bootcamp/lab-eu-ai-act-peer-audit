# Independent audit report: Model Intake Brief

**Auditor:** Ben Mayer · **Builder:** Sergii Rostovskyi · **Date:** 26 Nov 2026 · **Basis:** system brief (16 Nov 2026) and repo snapshot `e384f3a`, reviewed before seeing the builder's self-audit. Assumptions: see `02`.

## 1. System summary

Model Intake Brief helps an AI governance team check a third-party AI model before teams build on it. The reviewer enters a model ID, and a LangGraph workflow reads the supplier's public documentation. An OpenAI model then proposes a status for each of 18 GPAI checklist items (Art 53, Annexes XI/XII). Python verifies quotes and links. The output is a Markdown report with statuses, quotes, gaps and templated supplier questions. A human integration decision is intended but not enforced.

## 2. Risk classification

**Limited risk (transparency), at the low end.** It is not covered by Art 5 or Annex III: it assesses models and documents, not people. The LLM writes the status and gap explanation, so Art 50(2) machine-readable marking applies. If that text were templated, the tier would be minimal (Q1). It is not high-risk in any reading.

## 3. Role map

| Role | Entity | Key obligations |
|---|---|---|
| Provider | Sergii Rostovskyi (a client that rebrands the tool becomes the provider) | Art 50(2) marking; Art 4 AI-literacy measures |
| Deployer | EU client's governance and risk reviewers | Art 4 measures for reviewers; use only for first-pass triage |
| Vendor: GPAI model | OpenAI (`gpt-5.4-mini`, embeddings) | Art 53 documentation for downstream providers |
| Other vendors | Tavily, Jina Reader, Hugging Face Hub, Pinecone | No AI Act role; GDPR processors (DPAs, US transfers) |

## 4. Compliance findings

**Finding 1 - Evidence integrity: untrusted source text goes straight into the prompt**
**Severity:** Significant
**Description:** Model cards and provider pages are written by the party under review. Their text enters the prompt with no "treat as data" rule and no injection test. Quote verification proves only that a sentence exists, not that it is true. Art 15 doesn't bind at this tier, but the product's core claim of a trustworthy first pass fails if a supplier can steer the statuses.
**Recommended action:** Pass sources as quoted data and flag instruction-like text. Label each source *self-declared* or *independent*. Add an adversarial test fixture.
**Escalation needed?** No; an internal security review is enough.

**Finding 2 - No mandatory sign-off; statuses can read as approval**
**Severity:** Significant
**Description:** Runs go end-to-end with no sign-off, and the planned inventory export could skip review. "Evidence found" means the documentation exists, not that the model is compliant. Statuses also vary between runs (`stability.md`).
**Recommended action:** Make the export require a named reviewer and a decision. Rename the status to "Documentation found" and show the run-to-run variance.
**Escalation needed?** No.

**Finding 3 - Art 50(2): AI-written fields aren't marked**
**Severity:** Minor (a legal duty, but low harm in internal use)
**Description:** The LLM-proposed statuses look the same as code-verified facts, and the export has no machine-readable marker.
**Recommended action:** Add front-matter metadata (`ai_generated`, model, date) and a per-field label: "status proposed by AI, quote verified by code".
**Escalation needed?** Light: counsel confirms that the marking method follows the code of practice.

**Finding 4 - Legal-services rules and liability for a "compliance" product**
**Severity:** Significant before any paid offer
**Description:** The tool applies legal criteria to a client's case. In some member states (for example Germany's RDG), doing that for others can be a regulated legal service. A fixed corpus of 13 passages can also go stale when the law changes.
**Recommended action:** Get counsel's view per target market and keep "documentation review" wording. Version the corpus with a "legal baseline as of" date, and cap liability in the terms.
**Escalation needed?** Yes, a lawyer.

**Finding 5 - GDPR: third-party personal data in sources**
**Severity:** Minor
**Description:** Contributor names and contact addresses can be sent to US services and copied into reports. There is no documented lawful basis, redaction or retention rule.
**Recommended action:** Record a legitimate-interest assessment and the Art 14 position. Redact personal details in excerpts and sign DPAs.
**Escalation needed?** Yes, the DPO.

**Finding 6 - AI literacy (Art 4, as amended)**
**Severity:** Minor
**Description:** The user guide explains the controls but not the limits: variance, self-declared sources, and what "not found" means.
**Recommended action:** Add a one-page "when not to rely on this report" to the guide and to onboarding.
**Escalation needed?** No.

## 5. Overall recommendation

**Proceed with conditions.** No finding blocks launch: the system is neither prohibited nor high-risk, and Art 50(2) marking is cheap to add. But the product sells trustworthy evidence, and Findings 1 and 2 undermine that. Close both before the inventory pilot, and Finding 4 before any paid offer. Handle Findings 3, 5 and 6 alongside.

## 6. What this report is not

This report is not a legal opinion, not a conformity assessment and not a certification. Conclusions should be verified with legal counsel before any EU market placement.
