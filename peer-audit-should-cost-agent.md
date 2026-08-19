# Peer Compliance Audit — Autonomous Should-Cost Benchmarking Agent

**Auditor:** Anand Narasipuram
**System audited:** `should-cost-benchmarking-agent` (JayAIConsultant), Module 3 Capstone
**Source reviewed:** Repository README, `stack_decision.md`, and `gtm_future_sprints.md` (no self-audit or compliance memo was viewed prior to writing this report)

---

## Section 1: System Summary

The system takes a plain-language description of a manufactured part (material, weight, features, ship-from/ship-to) and produces a fully-cited should-cost estimate for internal procurement use. A LangGraph pipeline classifies shape/material via RAG (Pinecone), estimates cycle time from physics-based formulas, pulls live material pricing and freight/geocoding data, runs the cost math through a deterministic (non-LLM) engine, and has an LLM generate the narrative write-up with an anti-hallucination guardrail. Output is delivered via n8n to a Notion page and an editable Google Sheet. It is scoped to metal manufacturing only; plastics/injection molding are explicitly out of scope for this MVP.

## Section 2: Risk Classification

| Question | Answer |
|---|---|
| Prohibited category (Article 5)? | No — nothing resembling social scoring, manipulation, biometric categorization, or real-time biometric ID. |
| Operates in an Annex III area? | No — should-cost estimation for manufactured parts does not fall into biometrics, critical infrastructure, education, employment/worker management, essential services (credit/insurance/benefits), law enforcement, migration, or administration of justice. |
| If Annex III: significant influence vs. narrow/preparatory? | N/A |
| Interacts with end users / generates content requiring disclosure (Article 50)? | Partially — it generates an LLM-written narrative report. Whether Article 50 applies in practice depends on who receives that report (see clarifying questions). |
| **First-pass risk tier** | **Minimal risk**, with an Article 50 transparency question flagged for follow-up. |
| **Justification** | The system supports an internal procurement cost-analysis decision; it does not make or materially influence decisions about natural persons' employment, credit, essential services, safety, or legal status, so none of the Annex III high-risk triggers apply, and nothing in Article 5's prohibited list is implicated. The one open question is whether the LLM-generated narrative content triggers the Article 50 AI-generated-content disclosure obligation, which turns on audience/distribution, not on risk tier. |

I have moderate, not full, confidence in this tier — the brief doesn't state who ultimately reads the Notion report, which is the one fact that could change the analysis (see Q1 below).

## Section 3: Clarifying Questions Log

1. **Who receives the final report — internal procurement staff only, or is it shared with suppliers/external counterparties in negotiation?**
   Why it matters: Article 50 disclosure obligations for AI-generated content are far more relevant if the narrative leaves the company and could be mistaken for human-authored analysis.
   Assumption in absence of answer: Internal use only, given the "procurement teams" framing in the Problem section.

2. **Does any personal data (negotiator names, supplier contact details) pass through OpenAI, Pinecone, CommodityPriceAPI, or OpenCage?**
   Why it matters: This is a GDPR question, not an AI Act tier question, but it's a parallel legal issue the lab asks me to flag. Geocoding in particular could carry address-level data tied to a person rather than a facility.
   Assumption: Inputs are part/material/logistics data, not personal data, based on the described input schema (material, weight, features, ship-from/to).

3. **Is this intended to stay an internal capstone/demo tool, or is there a path to commercial deployment (e.g., as a vendor product sold to procurement teams)?**
   Why it matters: Determines who is "provider" vs. "deployer" under the Act, and whether market-placement obligations (even the lighter minimal-risk ones) become relevant at all.
   Assumption: Current state is pre-commercial (0 stars/forks, single commit, capstone framing); `gtm_future_sprints.md` suggests forward intent but no confirmed launch.

4. **Is there a human review step before a should-cost estimate is acted on in a real negotiation?**
   Why it matters: Even outside high-risk classification, absence of human sign-off is a governance gap worth surfacing, and matters more if scope later expands.
   Assumption: Yes, implicitly — the tool's output is a Notion page/Sheet for a human procurement analyst to use, not an autonomous action-taker.

5. **What model version(s) of OpenAI's LLM are used, and is that documented anywhere retained by the team?**
   Why it matters: Downstream integrators of GPAI models are expected to retain baseline documentation about the underlying model for their own audit trail.
   Assumption: Not currently documented in the repo beyond "OpenAI" in the tools list.

## Section 4: Role Map

| Role | Party | Key obligations |
|---|---|---|
| **Provider** (of this specific system) | The builder/team (JayAIConsultant) — they design, build, and would place the system into service | Maintain technical documentation, ensure no prohibited practices, address transparency (Article 50) if triggered, keep records sufficient to explain the system's logic. *MVP scenario:* if the builder runs the tool themselves as a managed service on client data, they hold this role concurrently with Deployer below. *SaaS scenario:* if the tool is licensed for the client's own staff to operate, the builder holds only this role. |
| **Deployer** | Whoever actually operates the tool in a professional context — unclear if this is the builder's own team or a future customer (see Q3) | Use the system per its intended purpose, provide any required disclosures to end users, human oversight. *MVP scenario:* the builder's own team is the deployer, since the client only sends inputs and receives a deliverable without ever operating the system. *SaaS scenario:* the client's team is the deployer, since they run the tool under their own authority. |
| **GPAI component provider** | OpenAI (LLM reasoning) | Own separate obligations under Article 53 as a GPAI model provider; the integrator's obligation is to retain adequate documentation of what was used |
| **Third-party data/service vendors** | Pinecone (vector store), CommodityPriceAPI, OpenCage (geocoding), Google Sheets API, Notion API, n8n | Not AI Act "providers" of this system, but relevant to GDPR processor obligations if any personal data flows through them |

## Section 5: Compliance Findings

**Finding 1 — Article 50 disclosure for AI-generated narrative content**
Severity: Minor (would become Significant if reports are shared externally)
Description: `report_generator.py` produces an LLM-written narrative alongside Python-built tables, with an anti-hallucination guardrail noted — a good practice signal. However, nothing in the brief indicates the output is labeled as AI-generated.
Recommended action: Add a visible "AI-generated analysis" notice on the report if there's any chance it leaves internal procurement hands.
Escalation needed? No, pending answer to Clarifying Question 1.

**Finding 2 — Personal data flow through third-party AI/API vendors is undocumented**
Severity: Significant
Description: No data-mapping or processor-agreement documentation is visible for what data reaches OpenAI, Pinecone, CommodityPriceAPI, or OpenCage. This is a GDPR issue rather than an AI Act tier issue, but the lab asks that parallel legal risks be flagged regardless of tier.
Recommended action: Do a data-mapping pass confirming exactly what fields transit each vendor; confirm DPAs/SCCs are in place before any deployment involving real supplier or company data.
Escalation needed? Yes — to legal/DPO, before production use with real data.

**Finding 3 — No retained documentation of the underlying GPAI model**
Severity: Minor
Description: The README lists "OpenAI" as a tool but doesn't record model name/version or any system-card information.
Recommended action: Record model identifier and version in the repo as part of the audit trail; update as the model is upgraded.
Escalation needed? No.

**Finding 4 — Human oversight step is implied but not documented**
Severity: Minor
Description: The pipeline runs end-to-end (input → Notion + Sheet) with no described checkpoint before a human uses the estimate in a live negotiation.
Recommended action: State explicitly in the README that the output is a decision-support artifact requiring human review before use, not an autonomous negotiating action.
Escalation needed? No.

**Finding 5 — Deployment market/scope not stated**
Severity: Minor
Description: No statement of intended market or whether this is meant to go beyond the capstone stage.
Recommended action: Add one line to the README on intended scope (internal capstone vs. path to product) to make Question 3 answerable for future auditors.
Escalation needed? No.

## Section 6: Overall Recommendation

**Proceed with conditions.** There are no blocking findings — nothing here triggers a prohibited practice or an Annex III high-risk obligation. But Finding 2 (undocumented personal-data flow to third-party APIs) is Significant and should be resolved — via a short data-mapping exercise and confirmation of vendor DPAs — before this moves past demo/capstone use into any deployment touching real supplier or company data. The Article 50 question (Finding 1) similarly needs resolving once the audience for reports is confirmed. Findings 3–5 are good-practice cleanup, not blockers.

## Section 7: What This Report Is Not

This report is not a legal opinion, not a conformity assessment, and not a certification. It is a peer classroom exercise in applying the EU AI Act's risk-tiering framework. Any real-world conclusions here should be verified with qualified legal counsel before this system (or a description of it) is placed on the EU market.

---

## Debrief Prep (Phase 5 — to complete with your teammate)

Space left intentionally — fill in after comparing tiers and gap lists with your teammate's self-audit:

- **Self-audit tier:** Minimal risk
- **This audit's tier:** Minimal risk (Article 50 question open)
- **Where we agreed:** Both audits landed on Minimal risk — no Article 5 prohibited practice, no Annex III high-risk trigger, and the same open Article 50 question on whether the LLM-generated narrative needs an AI-generated-content disclosure depending on who reads the report.
- **Where we disagreed, and why:** The self-audit named the builder's own team as deployer outright, consistent with the MVP/managed-service scenario (the team runs the tool themselves on client data). This peer audit left the deployer role open (Q3), because the brief doesn't confirm whether the tool stays a managed service the builder operates (provider and deployer held concurrently by the same entity) or becomes a licensed product the client's own staff run (deployer shifts to the client). The self-audit's answer is plausible given current MVP status, but it assumes away the commercial-path branch rather than flagging it as a fact still to be confirmed.
- **Joint closing note (2–3 sentences on what this reveals about self- vs. peer-auditing):** The self-audit, written from inside the project, defaulted to the scenario the team actually intends (they run it themselves) and treated that as settled; the peer audit, reading only the repo artifacts, had no basis to assume future commercial intent and so treated the same fact as an open question. This is a useful illustration of how self-audits can under-flag ambiguity that hasn't been made explicit in the documentation — the team's shared understanding of "how we'll actually run this" doesn't automatically show up in a README or architecture doc for an outside auditor (or future team member) to rely on.
