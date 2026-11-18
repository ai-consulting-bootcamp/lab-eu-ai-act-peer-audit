# First-pass classification and role map — VC Startup Screening Agent

**Basis:**
- The teammate's system brief: declared facts, **not** verified against code.
- Annotations in [`brief_annotations_vc_screening_agent.md`](brief_annotations_vc_screening_agent.md).
- Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744.
- Commission Guidelines on Article 50, C(2026) 5054 (non-binding).

**Status:** independent first pass written before the debrief. It is not a legal opinion.

## CFU 1 — Recognize

**Is it an AI system?** Yes. An OpenAI model infers outputs from what it receives: it reads search extracts and returns evidence about where the company is based and its funding stage (Article 3(1)).

**First-pass tier: minimal risk, provisional, with one open Article 50(2) question.**

- **Article 5 — no prohibited practice.** The system assesses **companies** against a fund's criteria. It does not manipulate people, score natural persons on their social behaviour, use biometrics or predict crime.
- **Annex III point 5(b) — the closest entry, but it does not fit.** It covers AI used to evaluate the **creditworthiness of natural persons** or establish their credit score. Here, a fund decides whether to invite a **company** to a first meeting about an **equity investment**:
  - the subject is a legal entity, not a natural person;
  - the decision is not credit;
  - the output is a preparatory input to a human decision.
- **No other Annex III area applies.**
  - Area 4 (employment): founders are not being recruited or managed.
  - Area 5(a): no public benefits are involved.
  - Area 8 (justice and democratic processes): not involved.
- **Annex I:** it is not a safety component of a regulated product.
- **Article 50(1)** is unlikely to apply. There is no conversational interface, and the analyst knowingly uses an AI tool.
- **Article 50(2) is open.** If the report contains model-written text, it may need machine-readable marking, unless the narrow exemption for internal business-to-business outputs applies. The brief's quote check (model quotes must appear in the extracts) reduces the amount of truly synthetic text.

**What would change the tier:**
- Criteria that assess **founders as individuals**: still not Annex III, but profiling under GDPR.
- **Loans or venture debt to natural persons:** Annex III point 5(b).
- **Automatic rejection without human review:** stronger oversight concerns.

These points are the subject of the clarifying questions.

## Phase 2 — Classification table

| Question | Answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No** (provisional). None of the nine practices applies. It assesses companies, not people's social behaviour (5(1)(c)); there is no manipulation (5(1)(a)–(b)), biometrics (5(1)(e)–(h)) or image generation. **Uncertainty:** if criteria scored founders on personal characteristics drawn from unrelated contexts, Article 5(1)(c) would need review (question Q1). |
| Does this system operate in any of the eight Annex III areas? | **No** (provisional). Closest entry: **5(b), creditworthiness of natural persons.** It does not apply because the evaluated party is a company and the decision is an invitation to a meeting about equity, not credit. Areas 1–4 and 6–8: no. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | **Not applicable** (no Annex III area). For context: the output is **preparatory** (an internal report before a first meeting). The analyst decides, and the system sends nothing and decides nothing (as declared). |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **50(1):** unlikely (not conversational; AI use is obvious to the analyst). **50(2): open.** Model-generated text in the report may need machine-readable marking; the narrow B2B / internal-output exemption in the Guidelines may apply (lawyer). **50(3) and 50(4):** no, because the report is internal (assumption, question Q4). |
| First-pass risk tier | **Minimal risk**, with a possible **Article 50(2)** transparency duty to confirm. **Uncertain** until questions Q1–Q3 are answered. |
| One-sentence justification citing the specific article or Annex entry | Screening companies for an equity first meeting is not "evaluating the creditworthiness of natural persons" (Annex III point 5(b)), nor any other Annex III or Article 5 use, so no high-risk duties apply under Article 6(2); Article 4 and possibly Article 50(2) remain. |

**When obligations apply:**
- Today the system is a prototype. Research and development before it is placed on the market or put into service is excluded from the AI Act (Article 2(8)).
- Article 4 (since 2 Feb 2025, amended 27 Jul 2026) and Article 50 (since 2 Aug 2026) would apply from the **pilot with a real investment team**.

## Update after the written answers (17 Nov 2026)
- Q1 (criteria assess companies only) and Q3 (no loans, no individuals) **confirm** the first-pass tier. No Article 5(1)(c) or Annex III point 5(b) concern remains.
- Q2: the GPAI model is **GPT-4o mini** (OpenAI).
- Q5: statuses are set by **Python rules**, and website text does not reach the model.
- Article 50(2) remains the only open AI Act question.

## CFU 3 — Role map

| Role | Entity | Key obligations (non-high-risk) |
|---|---|---|
| **Provider** | **The teammate (builder).** She would be the provider if she put the system into service or offered it under her name. **Assumption:** no client owns the code | Article 4: support AI literacy of users. Article 50(2), if applicable: machine-readable marking. Good practice: instructions for use and a documented classification. No conformity assessment, CE marking or registration |
| **Deployer** | **Puente Ventures** (fictional fund) and its analysts. In a real pilot: the investment team that uses it | Article 4 for staff. Use within the intended purpose (screening companies, not people). Outside the AI Act: GDPR controller duties for founders' data |
| **GPAI model provider** | **OpenAI** (GPT-4o mini, confirmed in Q2) | Article 53: documentation, information for downstream providers, copyright policy, training-data summary. Article 55 if the model is systemic-risk. This does not transfer the provider's product-level duties |
| **Other vendors** | **Tavily** (search API), **Jina Reader** (web page reader), **GDELT** (open news database) | No AI Act role within this system: they are data and tool suppliers. Relevant through their terms of service, GDPR (they receive queries) and copyright (stored extracts) |
| Importer / distributor | Not applicable | The provider is assumed to be established in the EU |
| **Affected parties** | Startups (legal entities) and, indirectly, founders | Not AI Act roles. They are the reason the classification questions matter |
