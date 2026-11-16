# Audit Report – AI Use Case Identifier (Project 3)

**Builder:** Friedrich Tschoepke · **Auditor:** Nicolò · **Basis:** system brief (commit d99573f, 13 Nov 2026), the questions log and stated assumptions · **Date:** 16 Nov 2026

## 1. System summary
The tool prepares an AI consultant for a first meeting with an SME. From a company name and website, it gathers public web content (company pages, job postings, news, register entries), and has OpenAI models write a brief: how the company makes money, how its work flows, three AI use cases with rough value estimates, and meeting questions. It also generates a process diagram. Statements are labelled "documented" or "assumption", work steps get a 0–10 "AI potential" rating, and nothing is decided or sent automatically. Today only the builder uses it; a public self-service form that would email reports to company owners is planned but not built.

## 2. Risk classification
**Limited risk / transparency.**
- **Not prohibited:** no practice under Art. 5.
- **Not high-risk:** the system assesses companies and work steps, not natural persons, so it falls outside Annex III. Employment (point 4) is the nearest area, and it's excluded because nobody is recruited, evaluated or monitored.
- **Transparency duty:** it generates synthetic text and images, so Art. 50(2) machine-readable marking applies to the provider.
- **Planned form:** Art. 50(1) disclosure would also apply.
- **Uncertainty:** how far Art. 50(2) text marking is "technically feasible" for a downstream builder, and the transition period added by the Digital Omnibus. If counsel finds OpenAI's marking sufficient, the system as built today is effectively minimal risk.

## 3. Role map

| Role | Entity | Key obligations |
|---|---|---|
| Provider | **Friedrich**: wrote the code and would make it available | Art. 50(2) marking of text and image outputs. Art. 50(1) disclosure once the public form exists. Clear documentation of intended use. |
| Deployer | **Friedrich**, today (professional use as a consultant). Later, **company owners** using the public form. | Use within intended purpose. Under GDPR, Friedrich is the **controller** for the scraped personal data and the contact fields. |
| Vendor: models | **OpenAI** (LLMs, embeddings, image generation) | General-purpose AI model provider duties (Art. 53). It already embeds provenance metadata in API-generated images. GDPR processor for prompts. |
| Vendor: search | **Tavily** | Retrieval service. GDPR processor for queries and results. |
| Vendor: vector store | **Pinecone** | Stores only the AI-application library. No personal data, so low relevance. |

## 4. Compliance findings

**Finding 1 – Personal data scraped, sent to the model and kept without limits (GDPR)**
**Severity:** Significant
**Description:** names of managing directors, founders and HR contacts are scraped and sent to OpenAI unfiltered, and stored in run files with no retention period. There's no documented legal basis (likely legitimate interest, which needs a balancing test), no information to the people concerned (GDPR Art. 14, unless the "disproportionate effort" exemption is justified), and no processor agreements with OpenAI or Tavily.
**Recommended action:**
- Add a step that redacts personal names before the LLM call, keeping roles ("managing director").
- Set a 90-day deletion rule for run files.
- Sign DPAs, using OpenAI's zero-data-retention option where available.
- Write a short legitimate-interest assessment.
**Escalation needed?** **Yes:** data protection officer or privacy counsel.

**Finding 2 – AI-generated text not marked or disclosed (Art. 50(2))**
**Severity:** Significant
**Description:** the brief carries no machine-readable marking and no visible statement that it was AI-generated. The diagram likely carries OpenAI's C2PA metadata, but this hasn't been checked through the pipeline.
**Recommended action:**
- Add an "AI-generated" field to the brief's file metadata and a visible header line.
- Check that the diagram's metadata survives export.
- Keep the "documented / assumption" labels: they're good practice.
**Escalation needed?** **Yes:** a lawyer, on scope and transition date.

**Finding 3 – Human review by habit, not by design**
**Severity:** Minor today, **Blocking for the planned public form**
**Description:** Art. 14 human oversight is a high-risk requirement, so it isn't mandatory here. But unreviewed briefs can misdescribe a real company and attach invented money estimates. The planned form would send exactly that to the public automatically.
**Recommended action:**
- Today: add a "reviewed by consultant" checkbox and a timestamp in the run file.
- For the form: a human review step before sending, or a much narrower, clearly labelled output with no money estimates.
**Escalation needed?** No.

**Finding 4 – Planned public form: consent, notice and AI disclosure**
**Severity:** Significant (pre-launch condition)
**Description:** the form collects name, email and phone, and would send unreviewed AI output. That requires:
- an Art. 50(1) notice that the user is interacting with an AI system;
- a GDPR privacy notice;
- separate opt-in consent for any sales follow-up (§7 UWG);
- abuse protection, because anyone could request a report on a company that isn't theirs.

**Recommended action:**
- Design the form with the AI notice, the privacy notice and a separate marketing tick-box.
- Verify that the requester owns the domain or works at the company (an email domain check).

**Escalation needed?** **Yes:** privacy counsel.

**Finding 5 – Scraping and storing third-party web content**
**Severity:** Minor
**Description:** full page text and job ads are stored in run files. Text and data mining is allowed unless the rights holder has opted out (§44b UrhG), so robots.txt and site terms should be respected.
**Recommended action:** honour robots.txt opt-outs, and store excerpts and links instead of full page copies.
**Escalation needed?** No.

## 5. Overall recommendation
**Proceed with conditions.** There are no blocking findings for the system *as used today*. It isn't prohibited or high-risk, and the builder is its only user. Before any wider use, three conditions apply: (1) personal-data redaction, retention limits and processor agreements (Finding 1); (2) AI marking and a visible label on all outputs (Finding 2); (3) no public form until a review step or reduced output, plus consent and notices, are in place (Findings 3 and 4).

## 6. What this report is not
This report is not a legal opinion, a conformity assessment or a certification. It's a first-pass review based on a written brief and stated assumptions, without access to the code or live runs. Conclusions should be verified with legal counsel before any placement on the EU market.
