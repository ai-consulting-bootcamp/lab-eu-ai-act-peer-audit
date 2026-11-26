# Independent audit report: Model Intake Brief

**Auditor:** Ben Mayer · **Builder:** Sergii Rostovskyi · **Date:** 26 Nov 2026 · **Basis:** the system brief (16 Nov 2026) and the repo snapshot `e384f3a`. I wrote this before seeing the builder's self-audit. Provisional assumptions are listed in `02`.

## 1. System summary

Model Intake Brief helps a company's AI governance team check a third-party AI model before teams build on it. The reviewer enters a model ID. An automated LangGraph workflow searches the supplier's public documentation and reads the pages. An OpenAI model then proposes, for each of 18 checklist items (based on AI Act Art 53, Annexes XI/XII and the GPAI Code of Practice), whether evidence was found. Python verifies every quote against the page, rejects quotes about other model variants and tests the links. The output is a Markdown report with statuses, quotes, gaps and templated questions for the supplier. A human then decides separately on integration, but the prototype doesn't enforce that step.

## 2. Risk classification

**Limited risk (transparency), at the low end.**
- **Not Art 5, not Annex III:** it evaluates models and documents, not natural persons, and the brief excludes applicants, employees and consumers.
- **Art 50(2):** the embedded LLM writes part of the report (status and gap explanation), so the provider must mark that output machine-readably.
- **Uncertainty:** if all free text were templated, the tier drops to minimal (Q1). It is not high-risk in any reading.

## 3. Role map

| Role | Entity | Key obligations |
|---|---|---|
| Provider | **Sergii Rostovskyi**: built it, would place it on the EU market under his name. If a client rebrands it, the client becomes provider. | **Art 50(2):** marking. **Art 4:** AI-literacy measures for his own team. Instructions for use are good practice. |
| Deployer | **EU client** (governance, risk and PMO reviewers) | **Art 4:** take measures so reviewers understand the tool's limits. Use it within its intended purpose (first-pass triage). The client's *own* downstream duties when it integrates a GPAI model don't pass to the tool. |
| Vendor: GPAI model | **OpenAI** (`gpt-5.4-mini`, `text-embedding-3-small`) | **Art 53:** documentation for downstream providers. Ironically, this is exactly what the tool checks for in other models. |
| Vendors: non-AI or ancillary | Tavily (search), Jina Reader (extraction), Hugging Face Hub (metadata), Pinecone (vector store) | No AI Act provider role for this system. They are **GDPR processors** (DPAs, US transfers) and fall under terms-of-service and copyright limits. |

## 4. Compliance findings

**Finding 1 - Evidence integrity: source text is untrusted but goes straight into the prompt**
**Severity:** Significant
**Description:**
- **Where the evidence comes from:** a Hugging Face model card, and a provider's own trust pages, are written by the party under review.
- **The gap:** page text goes into the assessment prompt with no instruction to treat it as data. There is no injection test, and quote verification proves only that a sentence *exists*, not that it is true or neutral. A supplier could write its documentation to the checklist, or plant text that pushes statuses towards "Evidence found".
- **Why it matters:** this isn't an AI Act obligation at this tier (Art 15 binds only high-risk systems). It does undermine the product's core claim of a *repeatable, trustworthy first pass*. A downstream integration decision could rest on manipulated evidence.

**Recommended action:**
1. Wrap sources as quoted data, with an explicit "ignore instructions inside sources" rule.
2. Flag instruction-like text.
3. Label each source **self-declared** (model card, provider page) or **independent**.
4. Add an adversarial fixture to the test suite, with a planted injection and an over-claiming model card.

**Escalation needed?** No. An internal security review is enough.

**Finding 2 - No mandatory human sign-off; statuses can be read as approval**
**Severity:** Significant
**Description:**
- **No checkpoint:** generation runs end-to-end, the prototype has no sign-off, and the Sprint 2 inventory export could file results with no review.
- **Misleading label:** "Evidence found" means *documentation exists*, not *the model is compliant*. A busy reviewer may treat it as clearance.
- **Status variance:** the builder documents that the LLM status can move between runs (`stability.md`).
- **Effect:** the client's due diligence as downstream provider would quietly become an LLM output.

**Recommended action:**
1. Make the export require a named reviewer, the date and the decision, with no inventory write without them.
2. Rename the status to "Documentation found".
3. Show the stability result (variance) in the report header.
4. Put "first-pass triage, not an approval" in the instructions for use.

**Escalation needed?** No.

**Finding 3 - Art 50(2): AI-written fields aren't marked**
**Severity:** Minor (legally required, but low harm: internal professional use, and the content is not published)
**Description:** The report shows the LLM-proposed status and gap explanation with the same weight as Python-verified facts. The Markdown export carries no machine-readable marker.
**Recommended action:** Add YAML front matter or an HTML comment (`ai_generated: true`, model, version, run date), plus a visible per-field label: "Status proposed by AI; quote verified by code".
**Escalation needed?** Light: counsel confirms that the text-marking technique follows the Commission's code of practice.

**Finding 4 - Legal-services regulation and liability for a "compliance" product**
**Severity:** Significant (before the paid Sprint 3); Minor for unpaid pilots
**Description:**
- **The claim:** the tool applies legal criteria (Art 53, Annexes XI/XII) to a specific case for a paying client. In some member states, Germany's RDG for example, applying law to a specific case for others can be a regulated legal service. The "Information, not legal advice" notice helps but may not be enough if marketing says "EU AI Act compliance".
- **Staleness:** the corpus has 13 fixed passages. If the Omnibus or later guidance changes a GPAI provision and the corpus isn't updated, the report will be wrong.

**Recommended action:**
1. Get counsel's view on positioning per target market.
2. Keep "documentation review" wording.
3. Add a corpus version, a "legal baseline as of" date and a review owner.
4. Cap liability in the terms.

**Escalation needed?** **Yes:** a lawyer (legal-services rules, terms and liability).

**Finding 5 - GDPR: third-party personal data in sources and reports**
**Severity:** Minor
**Description:** Account names, contributor names and contact addresses from public pages are processed, sent to US services (OpenAI, Tavily, Jina, Pinecone) and can be reproduced in stored reports. There is no documented lawful basis, Art 14 approach, redaction or retention rule.
**Recommended action:**
1. Document a legitimate-interest assessment (Art 6(1)(f)) and the Art 14(5)(b) position.
2. Redact email addresses and personal names from excerpts unless they are the provider's legal entity.
3. Sign DPAs and verify the transfer mechanisms.
4. Advise clients on report retention.

**Escalation needed?** **Yes:** the DPO, to confirm the legitimate-interest assessment and the transfers.

**Finding 6 - AI-literacy measures for reviewers (Art 4, as amended)**
**Severity:** Minor
**Description:** Since the Omnibus, providers and deployers must *take measures* to support AI literacy. The USER_GUIDE explains the controls but not the limits: variance, self-declared sources, and what "not found" means.
**Recommended action:** Add a one-page "how to read this report and when not to rely on it" to the guide and to client onboarding.
**Escalation needed?** No.

## 5. Overall recommendation

**Proceed with conditions.** Nothing blocks launch: the system isn't prohibited or high-risk, and its one AI Act duty (Art 50(2)) is cheap to meet. But the product sells *trustworthy evidence for a governance decision*, and two significant findings cut straight into that.
- **Before the Sprint 2 inventory pilot:**
  - **Finding 1:** treat sources as untrusted, label them self-declared or independent, and add an adversarial test.
  - **Finding 2:** enforce reviewer sign-off and rename the status.
- **Before any paid offer:** resolve **Finding 4** (legal positioning and liability).
- **Alongside:** Findings 3, 5 and 6.

## 6. What this report is not

This report is not a legal opinion, not a conformity assessment and not a certification. It is a first-pass consulting review based on a 300–500-word brief and public repository documentation, with the assumptions stated in `02`. Conclusions should be verified with legal counsel before any EU market placement.
