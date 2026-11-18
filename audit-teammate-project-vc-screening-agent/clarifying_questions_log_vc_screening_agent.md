# Phase 3 — Clarifying questions log

**Rule from the lab:** questions are asked **in writing only** and logged. They form part of the audit trail.

**Log:**
- **Sent:** 17 Nov 2026, in writing, to Sandra Obregón (builder).
- **Answered:** 17 Nov 2026, in writing.
- Answers are summarised from her reply. They are the builder's statements and have **not** been verified against code.

| # | What we need to know | Why it matters | Provisional assumption (before the answer) | Answer received (17 Nov 2026) | Effect on the audit |
|---|---|---|---|---|---|
| **Q1** | Does any criterion assess **founders as individuals**, or only the company? | Founder-level scoring would be profiling under GDPR and would need an Article 5(1)(c) check | Company criteria only | **Company only:** business model, sector, headquarters, funding stage, potential to expand. Founders are not scored on age, nationality, background or social media | Assumption confirmed. No Article 5 or Annex III concern |
| **Q2** | What data goes to OpenAI? Which model and plan? Do Jina or GDELT texts reach the model? | GDPR basis, minimisation and transfers; which GPAI model is used; whether startup-controlled text reaches the model | Extracts may contain founders' names; standard API terms; only Tavily extracts reach the model | **GPT-4o mini** via the OpenAI API. The model receives the startup name and Tavily extracts, which **may include founders' names, bios or news (unverified)**. Jina and GDELT results are **not** sent to OpenAI. **No API plan has been chosen** for the pilot | Assumption confirmed. Finding 1 remains **Significant** |
| **Q3** | Could the report be used for **loans or debt**, or for **individuals**? | Annex III point 5(b) covers creditworthiness of natural persons | Equity screening of companies only | **Company screening only.** Loans, debt and assessments of individuals are outside the intended use and would need a separate review | Assumption confirmed. **Not Annex III** |
| **Q4** | Who sees the report, and how long is it kept? Any **automatic discarding**? | Article 50 internal-use exemption; human oversight; GDPR retention | Internal use; analyst sees every result; no retention rule | Intended reader is the **analyst**; the report is a local Markdown file. **Access and retention are open decisions.** There is **no automatic rejection**: the analyst sees "Does not meet" and "Not verified" results | Human review supported. Retention and access are added as conditions |
| **Q5** | Who sets the status? Is website text untrusted? Any **injection test**? | Prompt injection and self-promotion could bias results | The model sets the status; no injection test | The model extracts evidence; **Python checks the quote and applies rules to assign the status**. The website (Jina) is fetched separately and **labelled as the company's own description**; it does not reach the model. **No injection test** has been recorded | Lower risk than assumed. The injection finding is downgraded to **Minor** (now Finding 3) |
