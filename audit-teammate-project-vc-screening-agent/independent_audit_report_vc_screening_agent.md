# Independent AI Act Audit Report — VC Startup Screening Agent

**Auditor:** Jaime Garate Marquerie · **System owner:** Sandra Obregón · **Date:** 17 Nov 2026 · **Basis:** the owner's system brief and her written answers to five clarifying questions (17 Nov 2026). No code was inspected and no run was observed.

## 1. System summary
The system helps a venture capital analyst prepare a first look at a startup. The analyst enters the company's name and website. Tavily finds public sources, Jina Reader fetches the website (shown in the report as the company's own description) and GDELT looks for news. GPT-4o mini receives the name and Tavily extracts and returns possible evidence of headquarters and funding stage. Python checks that each quote appears in the extract and applies rules to mark each criterion "Meets", "Does not meet" or "Not verified". The analyst sees every result and decides whether to invite the startup to a first meeting; nothing is rejected or sent automatically.

## 2. Risk classification
- **First-pass tier: minimal risk**, with an open **Article 50(2)** question.
- **Article 5:** not triggered. Criteria assess companies only (Q1), and there is no manipulation, social scoring or biometrics.
- **Annex III:** not triggered. Point 5(b) covers the creditworthiness of **natural persons**. The system screens **companies** for an equity first meeting, and loans or individuals are out of scope (Q3).
- **Article 50(2):** model output in an internal report may need machine-readable marking unless the narrow internal B2B exemption applies.
- **Timing:** today it is a prototype, so development is excluded (Article 2(8)). Articles 4 and 50 would apply from a pilot. The tier must be reviewed if the use ever extends to loans or individuals.

## 3. Role map
- **Provider:** Sandra (builder; would offer it under her name). Duties: Article 4; Article 50(2) if applicable.
- **Deployer:** the fund (Puente Ventures, fictional; later the pilot team). Duties: Article 4 for analysts; use within the intended purpose; GDPR controller duties.
- **GPAI model provider:** OpenAI (GPT-4o mini). Its Article 53 duties do not replace the provider's.
- **Data and tool vendors:** Tavily, Jina Reader, GDELT. No AI Act role here; their terms, GDPR and copyright apply.

## 4. Compliance findings

**Finding 1 — Founders' personal data sent to OpenAI · Significant**
- **Description:** Tavily extracts may contain founders' names, bios or news, and this was not verified for the saved test (Q2). No API plan, legal basis, minimisation or retention is defined (GDPR).
- **Recommended action:** map the data per field; minimise personal data before the call; choose an API plan with suitable processing and transfer terms; set retention and access rules (Q4).
- **Escalation needed?** Yes, to a DPO or privacy lawyer.

**Finding 2 — Reliability of the criterion status · Significant**
- **Description:** statuses come from Python rules applied to verified quotes, which is a strength. But only two test cases are reported, and in Lawra both criteria were "Not verified". There are no accuracy figures, so it is unknown how often a wrong status occurs.
- **Recommended action:** measure accuracy on about 20 startups with known answers; never derive "Does not meet" from missing data; show the evidence behind each status.
- **Escalation needed?** No.

**Finding 3 — Self-reported or planted text in search results · Minor**
- **Description:** the website text does not reach the model and is labelled as the company's own description (Q5). However, Tavily results can still include the startup's own pages or press releases, and no injection test is recorded.
- **Recommended action:** label self-reported sources in the report; add one test with a page containing hidden instructions.
- **Escalation needed?** No.

**Finding 4 — Possible marking of AI-generated text · Minor**
- **Description:** model output in the report may need machine-readable marking (Article 50(2), from service). The internal B2B exemption may apply, and the quote check limits synthetic text.
- **Recommended action:** label model-derived fields and add a metadata flag.
- **Escalation needed?** Yes, to a lawyer (short check).

**Finding 5 — Analyst review not recorded · Minor**
- **Description:** the analyst sees every result (Q4), but the review and decision are not recorded. This is good practice; Article 14 applies only to high-risk systems.
- **Recommended action:** a decision log per report.
- **Escalation needed?** No.

**Finding 6 — User training and vendor terms · Minor**
- **Description:** Article 4 applies once in use. Vendor terms and copyright in stored extracts are not addressed.
- **Recommended action:** a one-page user guide; review vendor terms and what is stored.
- **Escalation needed?** No.

## 5. Overall recommendation: **Proceed with conditions**
There are no blocking findings. The written answers confirm the system is neither prohibited nor high-risk. Before a pilot with a real investment team:
1. Complete the data map, choose an API plan and obtain DPO review; define report access and retention (Finding 1).
2. Measure the accuracy of the criterion status on known startups (Finding 2).

## 6. What this report is not
This report is not a legal opinion, not a conformity assessment and not a certification. It relies on the builder's brief and written answers; no code was inspected and no run was observed. Conclusions should be verified with legal counsel before any EU market placement.
