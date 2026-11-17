# AI Act Audit Report — Unioptt University Programme Fact-Checker

**System owner:** Elif Yurdakul (Unioptt) · **Auditor:** Pieter Albrecht · **Date:** 17 November 2026
**Basis:** Elif's Phase 1 system brief only. Open questions and assumptions: [classification_and_questions_log.md](classification_and_questions_log.md)

## 1. System summary

The system helps a Turkish student and their family check the facts about one university programme before applying. It searches official university pages, uses an OpenAI model to extract facts such as tuition, deadlines and language requirements, and stores each fact with its source sentence and link. Code, not the model, labels each fact Verified, Needs Review, Inferred or Unknown, adds national admission rules from 15 reference documents and converts costs to Turkish lira. It then compares the requirements with the student's profile (grades, test scores, budget, citizenship) and produces a one-page report of met / gap / check items and next steps, with no score, ranking or admission prediction.

## 2. Risk classification

**First-pass tier: not high-risk for the B2C MVP (minimal risk, with possible Art. 50 transparency duties); likely high-risk (Annex III 3(c)) for the planned B2B version used by private high schools and counsellors.**

The system sits in the education area of Annex III. It doesn't decide admission (3(a)), but its met/gap comparison assesses which programmes an individual can access (3(c)). Offered directly to families, it is outside an institutional context and preparatory (Art. 6(3)(d)). Used by schools to advise students, it moves inside 3(c). Because it evaluates a person's grades, language level and budget (profiling), the Art. 6(3) exemption would then fall away.

**Main uncertainties:** whether the AI Act applies at all (Q1, territorial scope) and how schools would use the output (Q2).

## 3. Role map

| Actor | Role | Key obligations |
|---|---|---|
| Elif / Unioptt | **Provider** (builds it, offers it under its own name); also **deployer** in B2C | AI literacy (Art. 4). Documented Art. 6(3) assessment (Art. 6(4)) + EU database registration (Art. 49(2)) if relying on the exemption. Art. 50 disclosures where applicable. If high-risk: Arts. 9–15, 17, conformity assessment (Art. 43), declaration and CE marking (Arts. 47–48), registration (Art. 49), post-market monitoring (Art. 72). |
| Private high schools, counsellors (future) | **Deployers** | If high-risk: use per instructions, human oversight, inform students, keep logs (Art. 26); AI literacy (Art. 4). |
| Students and families | **Affected persons**, not deployers (personal, non-professional use) | Right to explanation if high-risk (Art. 86) |
| OpenAI | **GPAI model provider** | Art. 53: technical documentation and information for downstream providers, copyright policy |
| Tavily, Jina, Pinecone, Frankfurter, n8n, Telegram, Airtable | Third-party vendors (no AI Act role) | GDPR processors; contractual and transfer duties |

**High-risk readiness, for the B2B version** (11 provider obligations; evidence from the brief only):

| Obligation | Status |
|---|---|
| Risk management system (Art. 9) | Absent |
| Data governance (Art. 10) | Partial: curated 15 official documents, sourced facts |
| Technical documentation (Art. 11) | Partial: brief and course documentation |
| Record-keeping / logging (Art. 12) | Partial: Airtable logging; content unknown |
| Transparency & instructions for use (Art. 13) | Partial: every fact has a status and source |
| Human oversight (Art. 14) | Absent: no review before the student sees the report |
| Accuracy, robustness, cybersecurity (Art. 15) | Partial: rule-based statuses; no accuracy metrics known |
| Quality management system (Art. 17) | Absent |
| Conformity assessment (Art. 43) | Absent |
| EU database registration (Art. 49) | Absent |
| Post-market monitoring (Art. 72) | Absent |

## 4. Compliance findings

**Finding 1 — Classification and scope not documented (Arts. 2, 6(3)–(4), 49(2))** · Severity: **Significant** (Blocking for the B2B launch)
*Description:* The brief contains no risk-tier analysis or territorial-scope assessment. Even if the B2C version isn't high-risk, a provider of an Annex III system relying on Art. 6(3) must document that before placing it on the market and register it. The 2026 AI Omnibus kept this duty. The planned school version likely is high-risk.
*Recommended action:* Write a short classification memo for both versions now; register if relying on Art. 6(3); make "re-classify before B2B launch" a product gate.
*Escalation:* **Yes**, to legal counsel.

**Finding 2 — Minors' personal data across non-EU vendors (GDPR / KVKK)** · Severity: **Significant**
*Description:* Production profiles hold grades, budget and citizenship, often of minors, and pass through OpenAI, Tavily, Pinecone, Airtable and Telegram (largely US or non-EU). No consent model, age handling, DPAs or transfer mechanisms are described.
*Recommended action:* DPIA before real profiles are used; parental consent below the applicable age; DPAs and transfer mechanisms; keep the student profile out of LLM prompts (the comparison is done by code); reconsider Telegram for minors.
*Escalation:* **Yes**, to a DPO or privacy counsel.

**Finding 3 — No human oversight of high-stakes facts** · Severity: **Significant**
*Description:* Families may spend money and time based on deadlines and costs nobody checked. "Inferred" and "Unknown" facts can mislead if not prominent. Wrong information to consumers is a consumer-protection risk (misleading commercial practices) in both the EU and Turkey.
*Recommended action:* Sample-based human review of reports in production; never show an "Inferred" deadline or cost without a warning; a "last verified on" date; a clear "not advice, confirm with the university" line.
*Escalation:* No

**Finding 4 — Transparency to users (Art. 50)** · Severity: **Minor** (Significant if Telegram is conversational)
*Description:* Users aren't told that AI extracts the facts. If Telegram works as a chat, Art. 50(1) requires that disclosure.
*Recommended action:* One line on every report and in the Telegram bot: "Facts extracted by AI from official sources; status checked by rules."
*Escalation:* No

**Finding 5 — AI literacy (Art. 4)** · Severity: **Minor**
*Description:* Applies since February 2025 to providers and deployers. Nothing is in place for Unioptt staff or future counsellors.
*Recommended action:* A short guide for counsellors on what the statuses mean and the system's limits.
*Escalation:* No

## 5. Overall recommendation

**Proceed with conditions.** The B2C MVP can launch once Findings 1–3 are addressed: a documented classification (and registration if relying on Art. 6(3)), a GDPR-compliant handling of minors' data, and safeguards against wrong deadlines and costs. **The B2B version for high schools must not launch** until it has been re-classified. If it is high-risk, it needs the full provider regime, which applies from 2 December 2027, and deploying schools take on their own duties.

## 6. What this report is not

This report is not a legal opinion, not a conformity assessment and not a certification. It is based on a 300-word brief and stated assumptions. Conclusions should be verified with legal counsel before any EU market placement.
