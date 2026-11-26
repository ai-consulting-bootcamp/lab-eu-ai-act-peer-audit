# Phases 2–3: First-pass classification and clarifying-questions log - Model Intake Brief

Auditor: Ben Mayer · System: Model Intake Brief (builder: Sergii Rostovskyi) · Date: 26 Nov 2026 · Baseline: the AI Act as amended by the Digital Omnibus on AI (Reg. (EU) 2026/1744). ⚖️ = confirm with counsel.

## CFU 1 - Recognize

Model Intake Brief is a professional research tool. It turns public documentation about an AI model into a checklist report for a governance reviewer.
- **Not Art 5:** there is no manipulation, scoring of people, biometrics or emotion recognition.
- **Not Annex III:** it evaluates *AI models and their suppliers' documentation*, not natural persons. It is not used for employment, credit, essential services or any other listed area, and the brief explicitly excludes applicants, employees and consumers.
- **Art 50(2), narrowly:** the LLM proposes each item's status and writes a short **gap explanation**, which is synthetic text in the report. As provider, the builder must mark that output machine-readably. No exemption applies: the system does more than "standard editing" of input provided by the deployer, because the deployer supplies only a model ID.
- **Art 50(1):** not triggered, because there is no conversational interaction with natural persons.

**First-pass tier: limited risk (transparency), at the low end.** The only AI Act-specific duty is Art 50(2) marking. The material risks are outside the AI Act's tiers: integrity of the evidence, over-reliance, GDPR and legal-services regulation.

## Phase 2 - Classification table

| Question | Your answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No.** None of 5(1)(a)–(h) is engaged. It processes documents about models, not people's behaviour, biometrics or emotions. |
| Does this system operate in any of the eight Annex III areas? | **No.** Its subject is AI models and their documentation. §4 (employment) and §5 (essential services) are excluded by design ("does not assess applicants, employees, or consumers"). |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | Not applicable. For completeness: it is **preparatory** (first-pass triage before a separate human integration decision), so the Art 6(3) derogation would be available even if an area applied. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **Art 50(2), yes, narrowly.** The LLM-written status and gap explanation are generated text. Quotes are verbatim and checked, and provider questions are templated in code, so those parts are *not* synthetic. **Art 50(1):** no chat-style interaction. **Art 50(3)/(4):** no. |
| First-pass risk tier | **Limited risk (Art 50(2) only)**, which in practice sits close to minimal. |
| One-sentence justification citing the specific article or Annex entry | It is outside Art 5 and every Annex III area because it assesses models rather than people, but it embeds a GPAI model that writes part of the report, so Art 50(2) machine-readable marking applies to the provider. |

**Uncertainty:** minimal vs limited depends on how much of the report the LLM writes (Q1 below). If the gap explanations were templated, the system would be **minimal risk**, leaving only Art 4 AI-literacy measures. Either way the outcome is **not high-risk**. The tier question is low-stakes, and the findings in `03` matter more.

## CFU 2 / Phase 3 - Clarifying questions log

Sent in writing to the builder on **26 Nov 2026**, *information requested from the client*. I wrote the provisional assumptions before any answer arrived.

| # | What I need to know | Why it matters | Provisional assumption |
|---|---|---|---|
| Q1 | Which parts of the report does the LLM write in free text (status, gap explanation, headline, provider questions)? | It decides whether Art 50(2) applies (limited) or not (minimal), and what has to be marked. | From the schema: the LLM writes the status and a short gap explanation, and code writes the rest. **Art 50(2) applies to those fields.** |
| Q2 | Will the client's process require a named reviewer to sign off before an integration decision, or can a report be filed straight into the AI inventory (GTM Sprint 2)? | Over-reliance. If "Evidence found" feeds the inventory unreviewed, an LLM proposal becomes a governance decision. This affects the client's own downstream obligations (Art 25/53 due diligence) and liability. | **No mandatory sign-off.** The prototype has none, and the Sprint 2 export could bypass review. |
| Q3 | Which sources can be written by the party under review (Hugging Face model cards, provider trust pages), and is source text ever treated as instructions by the model? | Integrity of evidence: a supplier could write its documentation to the checklist, or plant instructions. Quote verification proves only that the text exists. | **Sources are untrusted but not treated that way.** The prompt says "use only the provided provider evidence" and nothing about ignoring instructions inside it, and there is no injection test. |
| Q4 | How will it be sold (SaaS to EU companies, consulting deliverable, internal tool), in which member states, and with what claims ("EU AI Act compliance")? | Provider status, a possible legal-services issue (e.g. the German RDG), contract liability, and whether the client becomes provider by rebranding it. | It is sold as a **SaaS information tool** under the builder's name, EU-wide, including Germany, with the "information, not legal advice" notice. |
| Q5 | In production, where are reports and source extracts stored, for how long, and are contributor names or contact addresses removed? | GDPR: Art 14 information, minimisation, retention, and the US transfer to OpenAI, Tavily, Jina and Pinecone. | **Stored by the client** in its inventory, with no retention rule and no redaction. Personal data appears only occasionally. |
