# Phase 1 — Annotated reading of the teammate's system brief

**System audited:** VC Startup Screening Agent (teammate's Project 3)
**Input received:** the teammate's system brief only (324 words). No self-audit, classification, gap analysis, memo or code was seen.
**Method:** first reading without notes; second reading with annotations.
**Legend** (replaces underline, circle and mark):

| Tag | Original mark | Meaning |
|---|---|---|
| **[R]** | underline | affects the risk tier |
| **[?]** | circle | unclear; needs clarification |
| **[O]** | mark | suggests a specific obligation or parallel legal issue |

Everything below is what the brief **declares**. The auditor has **not** seen or run the code.

| # | Brief statement (paraphrased) | Tag | Auditor's note |
|---|---|---|---|
| 1 | Prototype to help an investment analyst at a VC fund review startups | [R] | The purpose is screening **companies** for equity investment, not individuals for credit, so it is a key fact for Annex III point 5(b) |
| 2 | Input: the startup's name and official website | [R] | The subject is a legal entity. No founder data is entered directly |
| 3 | Output: an internal report that helps decide whether to invite the startup to a **first meeting** | [R] [O] | A preparatory step before an investment decision. "Internal" matters for Article 50 and confidentiality |
| 4 | Criteria of a fictional fund (Puente Ventures) read from a local file | [?] | Which criteria? The brief names only headquarters and funding stage. Are there criteria about founders as people? |
| 5 | Tavily finds sources; Jina Reader reads the website; GDELT finds news | [?] | The brief says the model receives only the name and **Tavily** extracts. What are the Jina and GDELT outputs used for: shown in the report, or used in the assessment? |
| 6 | The OpenAI model receives the company name and short Tavily extracts | [R] [O] | This is the inferring component, so it is an AI system (Article 3(1)). OpenAI is the provider of the general-purpose (GPAI) model. Personal data reaches a provider outside the EU, so GDPR and international transfers come into play |
| 7 | The model looks for evidence on where the company is based and its funding stage | [R] | Narrow factual extraction about the company |
| 8 | Public sources may contain personal data (founders' names); whether the saved test sent personal data is **unverified** | [?] [O] | Admitted by the creator. GDPR: legal basis, data minimisation, information to the people concerned, terms of the OpenAI API |
| 9 | The code checks that quotes returned by the model appear in the extracts | — | **Strength**: protects against invented evidence. It does not protect against true but misleading or planted text |
| 10 | Each criterion is marked "Meets", "Does not meet" or "Not verified" | [?] [R] | Who sets the mark: the model or a rule? Is "Does not meet" based on evidence, or on missing evidence? Are startups filtered automatically? |
| 11 | Lawra report: headquarters and stage "Not verified"; the news search failed; the report was saved anyway | — | **Strength**: honest failure handling, declared by the creator |
| 12 | Users: analysts and associates at a fund | [O] | Deployer. Article 4 AI literacy applies once the system is in use |
| 13 | Startups may be affected (influence on who gets a first meeting) | [R] | They are affected parties, but they are not natural persons. Possible indirect effect on founders |
| 14 | The analyst runs it, checks sources, reviews gaps and decides; the system sends no invitations and makes no investment decision | [R] | Declared human-in-the-loop. Unclear whether it is recorded or enforced |
| 15 | Tested with Kalipso and Lawra; the pilot is a future step | [?] | Only two cases. No accuracy figures. Not placed on the market or put into service, so Article 2(8) excludes development activity |
| 16 | Not stated: the OpenAI model and plan, the framework, retention of reports, who can access them | [?] | Missing information, logged as clarifying questions |
| 17 | The startup's own website is read by the system | [R] [?] | The evaluated party **controls an input**. Risk of prompt injection or self-promotion. No mitigation is described |

## Elements that drive the classification
1, 2, 3, 6, 7, 10, 13, 14 and 17.

## Unknowns that could change it
- 4: founder-level criteria.
- 10: automatic filtering.
- Type of financing (equity or loans).
- Use of the report outside the fund.
