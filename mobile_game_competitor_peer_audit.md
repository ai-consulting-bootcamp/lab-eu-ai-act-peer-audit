# Independent EU AI Act peer audit
**Mobile Game Competitor Snapshot mk.III | 17 November 2026**

**Builder:** Jędrzej Czarnota · **Reviewer:** Sean Langsdorf
**Status:** Pre-debrief · **Recommendation:** Do not proceed with hosted private uploads as configured.

## 1. System summary

A product or marketing manager enters a competitor name and an email address and can upload a strategy PDF. The workflow gathers web, news and Apple storefront data and uses a language model to draft an internal competitive briefing against the user’s strategy or a fictional default playbook. It emails the report automatically. A manager may verify the material afterward and decides whether to act.

## 2. Risk classification

**Limited risk / transparency.** Article 50(2) is the main issue because the system generates substantive synthetic text. No prohibited practice or Annex III purpose appears in the brief. The fixed form and one emailed report likely lack the two-way exchange relevant to Article 50(1), although the form already says the briefing is AI-generated. Article 50(4) is not indicated for internal email. Confirm if a later version converses with users or publishes public-interest text. [1, 2]

## 3. Role map

**Hosted service:** Jędrzej or his service entity is the likely provider if it supplies the finished system under its name. The workflow operator deploys it, and the client studio may be a deployer where it uses the system under its authority. **Imported workflow:** The client runs it as deployer. If the client commissions and puts the system into service under its own name, check whether it instead also assumes provider duties. Provider owns Article 50(2) marking and detectability, and provider and deployer each address Article 4 literacy. OpenAI is upstream model/API supplier with applicable model-provider duties. Pinecone, n8n, Gmail, Tavily, GNews and Apple have component, hosting, delivery or data roles. They do not by that fact become the finished-system provider. No finished-system importer is identified. [1]

<!-- page -->

## 4. Compliance findings

**1 | Blocking — Hosted strategy isolation.** Insertion writes to the fixed `custom-strategy` namespace with clearing enabled. Retrieval is routed to that same namespace for custom uploads. If hosted customers share the backing index, overlapping requests could replace or retrieve another studio’s confidential material. Offline replay verifies the shared configuration target, not a live exposure or deletion. **Action:** Disable hosted private PDFs until per-studio authorization and per-run scoping are enforced. Verify isolation under overlapping submissions and delete uploads, vectors and related logs on a defined schedule. **Escalate:** privacy and platform-security owners. [3]

**2 | Blocking for launch unless resolved — Article 50(2) output marking.** The form gives users a visible warning, but the Markdown-to-HTML and email nodes show no verified machine-readable marking and detectability for the generated report. The email footer describes automated generation, not technical detection. **Action:** Verify upstream support and implement a technically feasible marking and detection approach. Test the actual email, plain text and forwarding. Keep a clear draft label as a separate control. **Escalate:** AI counsel and provenance specialist. [1, 2]

**3 | Significant — Delivery and retention.** The workflow sends to the submitted address and contains a fallback address. The brief does not establish recipient verification, documented retention or processing terms. Recipient emails and some public snippets may be personal data. **Action:** Remove the fallback, bind delivery to a verified studio recipient and fail closed. Document data flows, retention and vendor roles, assess transfer safeguards, and verify corrections and deletion. **Escalate:** privacy lead or DPO and counsel. [3]

**4 | Significant — Claims arrive before review.** The system generates commercial estimates and recommendations and emails them without a person checking the sources. **Action:** Label estimates and incomplete evidence, retain source links, and require trained human review before commercial reliance or external forwarding. **Escalate:** product lead, with counsel for external publication or unsupported adverse claims. [1]

## 5. Overall recommendation

**Do not proceed** with hosted private uploads or launch as configured. Use only controlled demonstrations with fictional playbooks while isolation, verified delivery and marking are tested, and reassess any independently isolated client deployment on its own evidence.

## 6. What this report is not

This is not a legal opinion, conformity assessment or certification. Verify the conclusions with counsel before EU market placement.

[1] [EU AI Act, Articles 3–6, 50 and Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [Commission Article 50 guidelines](https://publications.europa.eu/resource/cellar/caabe0cd-de39-11f1-ba80-01aa75ed71a1.0006.01/DOC_1) · [3] [GDPR, Articles 5, 6, 28, 32 and Chapter V](https://eur-lex.europa.eu/eli/reg/2016/679).
