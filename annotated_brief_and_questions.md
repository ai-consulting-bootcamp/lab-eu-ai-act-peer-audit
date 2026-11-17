# Mobile Game Competitor Snapshot · Independent audit trail

**Builder:** Jędrzej Czarnota · **Pre-debrief analysis:** 17 November 2026
**Sources reviewed:** The [builder’s system brief](evidence/builder_system_brief.md) and [redacted n8n export](evidence/workflow_redacted.json) from [PR #30](https://github.com/ai-consulting-bootcamp/lab-eu-ai-act-self-audit/pull/30), head `00099b7`. The PR’s risk assessment, gap analysis, compliance memo and proof of the builder’s own assessment were not read.

## Brief annotations

**Key:** <u>Risk-classification fact</u> · ◯ Clarification needed · § Obligation signal.

- <u>Researches competitor game studios, not individuals.</u> It proposes experiments for product and marketing staff. It does not execute their choices.
- <u>A one-shot web form requests a report, which is emailed.</u> § Substantive generated recommendations and summaries point to Article 50(2). ◯ Is there any conversational follow-up interface beyond the export?
- **Uploaded studio strategy and KPI PDF.** § Confidentiality, GDPR where identifiable people are involved, vendor access and retention. ◯ Is each hosted customer technically isolated?
- **Autonomous delivery and only post-delivery review.** § Review before forwarding or relying on it is a proposed product control, not an Article 14 duty for this tier. ◯ Can users obtain company-specific reports or uploads using an unverified address?
- **Hosted and imported operation.** § Article 3 provider and deployer roles depend on actual supply and branding. ◯ Who controls each mode, and under whose name is it put into service?

## First-pass classification

| Question | Independent answer |
| --- | --- |
| Prohibited under Article 5? | None identified. Company-level research and internal recommendations do not match a prohibited practice on the evidence reviewed. |
| Annex III area? | None identified among the eight areas. Ranking company-level game metrics is not recruitment, worker management, natural-person credit scoring or another listed intended purpose. No identified Annex I safety function. |
| Significant influence or preparatory? | Not applicable because no Annex III purpose was identified. The conclusion does not rely on the Article 6(3) exception or simply on the existence of human review. |
| Direct interaction or generated content? | The flow gathers inputs in a fixed form and sends one email, so Article 50(1) is probably not triggered on the stated scope. The form already describes the output as AI-generated. Article 50(2) likely applies to the substantive synthetic text. Article 50(4) public-interest publication is not indicated for internal emails. |
| First-pass tier | **Limited risk / transparency**, in lab terminology. |
| One-sentence basis | The system writes substantive competitive research and strategy suggestions, so Article 50(2) is the main applicable provision for the intended professional rollout, with no identified Article 5 or Annex III use. |

## Written questions to send to the builder

**Prepared 17 November 2026. Not sent and no answers recorded.**

| Question | Why it matters | Provisional assumption |
| --- | --- | --- |
| Is there a dedicated Pinecone index or isolated namespace per studio and submission, and what happens when two PDFs arrive close together? | A shared write/clear target can mix or replace customer strategy. | Export is the baseline. No separate tenancy or queue isolation verified. |
| How are form submissions authorized, recipient addresses verified, and delivery failures handled? | Tool can email confidential inferences, including through a fallback path. | Email field is present. No production recipient binding or fallback controls verified. |
| What marks generated text at the model, rendering and email stages, and what survives forwarding or plain text conversion? | Article 50(2) requires marking and detectability, not just a visible form notice. | No verified solution across the delivery path. |
| Who supplies and operates the hosted and imported versions, under whose name, and is any conversational mode available? | Resolves role allocation and possible Article 50(1) duties. | Builder operates hosted mode. Client operates imports. Export is one-shot. |
| Which content reaches each vendor, where is it kept, and who can delete it? | GDPR roles and retention depend on the actual processing chain. | Vendor terms, PDF/vector cleanup and host execution retention are unverified. |

## Debrief record

**Pending a real exchange.** After the independent presentation, record the builder’s responses, reveal both classifications, compare top findings, and write the required two- to three-sentence joint closing note together. No conversation, agreement, or joint note is represented as completed.
