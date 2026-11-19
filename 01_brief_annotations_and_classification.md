# Peer audit – Career Intelligence Agent
## Phase 1 – Annotations · Phase 2 – First-pass classification

**Auditor:** Murat Çömez · **Builder:** Max · **Input:** [`teammate_system_brief_career_intelligence_agent.pdf`](teammate_system_brief_career_intelligence_agent.pdf) · **Date:** 17 Nov 2026

---

## Phase 1 – Annotations

Legend: **[U] underline** = affects the risk tier · **[C] circle** = unclear, needs clarification · **[M] mark** = suggests a specific obligation applies

| # | Brief section | Element (paraphrased) | Tag | Why it matters |
|---|---|---|---|---|
| 1 | Header | Industry: "HR Technology / Recruitment & Career Development" | [U] | Recruitment is an Annex III area (point 4(a)); the label alone puts the system close to high-risk. |
| 2 | §1 | Compares job ads with the candidate's background and identifies promising opportunities | [U] | This is an evaluation of a natural person's professional profile, i.e. likely **profiling** (GDPR Art. 4(4)). It matters for Art. 6(3) AI Act. |
| 3 | §1 | Does not make hiring decisions, submit applications, or accept or reject candidates for employers | [U] | This is the main argument **against** Annex III 4(a): the system is used by the job seeker, not by the recruiter. |
| 4 | §2 | Structured profile: experience, education, skills, career level, location | [M] | Personal data, so GDPR applies. Education dates and career level can act as **proxies for age**, which raises an anti-discrimination (AGG) risk. |
| 5 | §2 | Demonstrated with synthetic profiles | [C] | It is unclear how real data will be handled in production: consent, retention, deletion. |
| 6 | §2 | Arbeitnow, Himalayas, ESCO, Tavily, EC/Cedefop/ILO publications | [M] | Third-party data sources raise terms-of-use and data-quality questions. Tavily may receive company or candidate queries. |
| 7 | §2 | OpenAI used for "optional" AI-generated analysis | [C] [M] | It is unclear what is optional and whether the LLM produces the score or only the text. OpenAI is a GPAI model provider; generated text points to **Art. 50(2)**. |
| 8 | §2 | Pinecone retrieves passages from research documents | [C] | Does Pinecone also store candidate profiles or only public research documents? |
| 9 | §3 | Matching score 0–100 per job, with evidence and gaps | [U] [M] | A numeric score about a person is the core profiling output. It is also an accuracy and consumer-protection point: the score could be misread as a qualification assessment. |
| 10 | §3 | A high score alone does not trigger a recommendation; requirements must be supported | [M] | This is a good design control (an evidence-sufficiency rule) and partly addresses accuracy and robustness. |
| 11 | §3 | Downloadable PDF / Markdown / JSON reports | [C] [M] | The reports can travel. Could a user hand the report to an employer? If so, the score enters a recruitment context. Machine-readable AI marking is relevant here. |
| 12 | §3 | Scores are advisory, not hiring probabilities | [M] | This disclaimer exists. Is it shown in the UI and in every export? |
| 13 | §4 | Users review and correct the profile before the run, then decide independently | [U] | The human in the loop is the affected person, which is acceptable for a consumer tool. There is no organisational oversight. |
| 14 | §4 | No independent reviewer approves reports | [M] | Not required unless the system is high-risk (Art. 14). The builder flags it openly. |
| 15 | §5 | "A future commercial provider could offer the application directly to these users" | [C] [U] | The business model decides the tier. B2C only versus licensing to recruiters, job boards or public employment services changes the classification. |

---

## Phase 2 – First-pass classification

| Question | My answer |
|---|---|
| Does this system fall under any prohibited category (Art. 5)? | **No.** No manipulation or exploitation of vulnerabilities, no social scoring, no emotion recognition, no biometric categorisation. Recommendations are transparent and the user decides. |
| Does this system operate in any of the eight Annex III areas? | **Borderline: Area 4 (employment), point 4(a).** That point covers systems intended for *recruitment or selection of natural persons*, including placing targeted job ads and evaluating candidates. This system evaluates candidates against jobs, but **for the candidate's own use**, not for the employer's selection decision. As described, the intended purpose sits outside 4(a). |
| If Annex III: significant influence, or narrow/preparatory? | If it ever falls under 4(a), the **Art. 6(3) derogation cannot be used**, because the system profiles natural persons (a 0–100 score from professional profile data). So any recruiter-side use = high-risk. |
| Does it interact with end users or generate content requiring disclosure (Art. 50)? | **Yes, partly.** It generates synthetic text (LLM explanations, report narrative), so the **provider must mark outputs in a machine-readable, detectable way (Art. 50(2))**. Art. 50(1) (informing people they are interacting with AI) applies if the Streamlit UI has a chat or conversational element; this needs clarification. |
| **First-pass risk tier** | **Limited risk / transparency**, with an open **high-risk question under Annex III 4(a)** that depends on the business model. |
| One-sentence justification | As a consumer-facing career guidance tool used by job seekers for their own decisions, it falls outside Annex III 4(a) (recruitment or selection *of* persons) but generates AI text and triggers Art. 50(2). Any use by or for employers, recruiters or public employment services would make it high-risk with no Art. 6(3) exit, because it profiles natural persons. |

**Uncertainty to resolve:** the classification turns on **who uses the score and for what** (see questions Q1 and Q3 in the log). If the brief's B2C purpose is locked in by design and contract, it stays limited risk. If not, it becomes high-risk.

### First-pass paragraph (CFU 1)
I classify the Career Intelligence Agent as **limited risk with transparency obligations**. It is not a prohibited practice under Art. 5. It evaluates natural persons against job requirements, which sounds like Annex III point 4(a), but its intended purpose is career guidance for the job seeker, not recruitment or selection by an employer, and it makes no employment decision. Because it generates text with an LLM, the provider must mark AI-generated output under Art. 50(2). Two facts keep the classification provisional: the score is profiling, so any recruiter-side use would make it high-risk without the Art. 6(3) derogation; and the brief leaves the future business model open. This needs legal confirmation.
