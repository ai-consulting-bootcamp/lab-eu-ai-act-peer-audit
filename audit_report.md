# Peer audit report: Vendor Due Diligence Agent (Pieter, Project 3)

**Auditor:** Elif Yurdakul · **Builder:** Pieter · **Basis:** Pieter's Phase 1 system brief (no self-audit findings seen)

---

## 1. System summary
The system helps a compliance officer at a Dutch regulated firm decide whether to take on a new vendor. It looks the company up in public registers (GLEIF, KvK), then code screens the company, its former names and its parent companies against sanctions and PEP lists. If there is a hit, an AI agent searches the news for negative coverage and pulls in official AML guidance, then proposes a risk rating with sourced red flags; code sets a minimum rating the AI cannot lower and checks the report before saving. The output is a two-page report with a rating and a recommendation; the compliance officer makes the decision.

## 2. Risk classification
**First-pass tier: Minimal risk under the AI Act, with significant obligations under other law (GDPR, sanctions and AML rules).**

- **Not prohibited.** The closest provision is Art. 5(1)(d) (predicting the risk that a person commits a crime based solely on profiling). It does not apply: the system assesses companies, uses objective, verifiable data (official sanctions lists, registers) and supports a human assessment.
- **Not Annex III.** It is not credit scoring of natural persons (5(b)), not employment (4), not law enforcement (6): the user is a private firm doing vendor checks.
- **Not Art. 50.** It does not talk to the public or publish AI-generated text; the report goes to a professional user.

**Uncertainty:** if vendors include **sole traders or freelancers** (natural persons), or the tool is later used for **client** due diligence, the system would evaluate individuals, and both the Art. 5(1)(d) reading and the GDPR picture need a second look. ⚖️

## 3. Role map
| Role | Entity | Key obligations |
|---|---|---|
| Provider | **Pieter** (built it; would offer it to Dutch firms) | AI Act: AI literacy (Art. 4); document the not-high-risk reasoning. GDPR: privacy by design, accuracy, DPIA support for customers. |
| Deployer | **Compliance teams** at law firms, notaries, payment companies | AI Act: AI literacy (Art. 4). GDPR: they are the **controller** for screening data (legal basis, DPIA, data subject rights). |
| Vendor (GPAI) | **OpenAI** (gpt-4o-mini) | GPAI provider duties (Art. 53); GDPR processor (US transfer). |
| Vendors (data and tools) | GLEIF, KvK, OpenSanctions (data); Tavily (news search); Pinecone; **LangSmith (tracing)**; n8n, Streamlit | No AI Act role; GDPR processors or sources; **data licence terms** (OpenSanctions). |

## 4. Compliance findings

**Finding 1: Legal basis for screening people, including criminal-offence data**
**Severity: Significant** (Blocking if no legal basis can be found)
**Description:** the reports contain personal data about PEPs and people named in news in connection with alleged crimes, which is criminal-offence data under GDPR Art. 10, processed without the people knowing. The Dutch AML law (Wwft) requires due diligence on **clients**, not vendors, so it may not give a legal basis for PEP and adverse-media screening of vendors. Sanctions screening has a clearer basis, because EU sanctions rules apply to everyone.
**Recommended action:** confirm a legal basis for each screening type (sanctions vs. PEP vs. adverse media); limit what is stored about individuals to what is needed for the decision.
**Escalation:** Yes, lawyer and data protection officer. ⚖️

**Finding 2: No data protection impact assessment (DPIA)**
**Severity: Significant**
**Description:** systematic screening of people against lists and news, involving criminal-offence data and people who are not informed, is very likely to require a DPIA (GDPR Art. 35). The brief does not mention one.
**Recommended action:** draft a DPIA template customers can complete; describe data flows, retention, accuracy measures and rights handling.
**Escalation:** Yes, data protection officer.

**Finding 3: Personal data sent to US services, including tracing logs**
**Severity: Significant**
**Description:** names, news snippets and red flags pass through OpenAI, Tavily and **LangSmith tracing**, which stores full inputs and outputs of each run. That is a transfer of sensitive personal data to US processors and a second, unmanaged copy of every report.
**Recommended action:** turn off or mask tracing in production; processor agreements and a transfer mechanism for each US vendor; retention limits; consider EU-hosted alternatives.
**Escalation:** Yes, data protection officer.

**Finding 4: Wrong matches can harm people and vendors**
**Severity: Significant**
**Description:** name matching against sanctions/PEP lists and reading news articles can produce false positives (same name, misread article). A wrong red flag can delay or exclude a vendor and damage a person's reputation (GDPR accuracy principle, Art. 5(1)(d)). The source checks are a strength, but they confirm that a source exists, not that it concerns the same person.
**Recommended action:** show match confidence and the matching attributes (date of birth, country, registration number); require the officer to confirm or dismiss each hit; a correction route for vendors.
**Escalation:** No.

**Finding 5: OpenSanctions licence for commercial use**
**Severity: Significant** (for production)
**Description:** OpenSanctions data is free for non-commercial use; offering the tool to firms is likely commercial use and needs a licence. News content also has copyright and terms-of-use limits.
**Recommended action:** check and budget the data licences; keep only links and short quotes from news.
**Escalation:** Yes, lawyer (contract review). ⚖️

**Finding 6: Human oversight and automation bias**
**Severity: Minor**
**Description:** the officer decides, and the code-set minimum rating is a strong design choice: the AI can raise the rating but never lower it. But no one reviews the report before the officer, and a busy officer may follow the recommendation.
**Recommended action:** a documented review procedure (what the officer must check), log every override with a reason, and mark which parts of the report were written by AI.
**Escalation:** No.

## 5. Overall recommendation
**Proceed with conditions.** The AI Act places few obligations on this system, and its design shows good control: fixed code rules, a minimum rating, source checks and a data-limitations section. The real risks sit in data protection and licensing. Before deployment with real firms: (1) a confirmed legal basis for PEP and adverse-media screening of vendors, (2) a DPIA, (3) a production setup without US tracing of personal data, and (4) a commercial data licence.

## 6. What this report is not
This report is not a legal opinion, not a conformity assessment and not a certification. It is based only on the builder's system brief. Conclusions should be verified with legal counsel before any EU market placement.