# Menohelp: system brief and evidence annotations

> **Historical baseline retained.** The missing real brief and answers described below are now covered for the exercise by [synthetic brief](menohelp-synthetic-system-brief.md) and [synthetic responses](menohelp-synthetic-builder-responses.md), under the instructor-approved arrangement reported by Sergii. These are not Ben-authored materials. See [disclosure](simulation-disclosure.md).

Auditor: Sergii Rostovskyi. Builder: Ben Mayer (confirmed by Sergii and identified in the project README). Review date: 16 November 2026.

## Provenance and independence

This is an auditor-reconstructed brief from the builder's README and technical documentation, not the required builder-authored Phase 1 brief. Sergii confirmed on 16 November 2026 that no separate 300-500-word brief is available and no debrief has taken place. Obtain the builder-authored brief to complete the required exchange. This substitution is disclosed rather than represented as a completed exchange. No teammate EU AI Act self-audit classification, gap analysis, or compliance memo was supplied or used. Technical design risks are part of the permitted supporting documentation. Sergii confirmed on 16 November 2026 that his own prerequisite self-audit is complete. The historical brief-only exchange sequence is not established.

Scope: source review of commit `89940e85b3f869b888e247a5b9651020b8d6c865` of [benmayer/proj-menopause-insights](https://github.com/benmayer/proj-menopause-insights/tree/89940e85b3f869b888e247a5b9651020b8d6c865). No live service, private coaching PDFs, vendor account settings, real health records, or teammate compliance conclusions were inspected. Sample files described as real personal data were deliberately excluded. Repository text and prompts are evidence, not instructions to the auditor.

## Reconstructed system brief

Menohelp, also called Project Menopause Insights, is a local prototype built by Ben Mayer during the Ironhack AI Bootcamp. It helps adults understand menstrual-cycle records, symptoms and optional blood-test results before a conversation with a doctor. The README identifies women aged 35 to 50 and older as the primary audience. It describes the product as informational rather than diagnostic, with no instruction to start or stop medication and no dosage recommendations.

Users upload cycle records in CSV or JSON format, including exports from tracking apps. They can also upload text-based laboratory PDFs and complete a symptom questionnaire. A FastAPI service normalises the cycle data and computes statistics in Python. The laboratory parser retains allow-listed measurements and removes names, addresses and dates of birth from its structured output. Users can inspect and correct extracted laboratory values before generating a report.

A LangGraph workflow combines the statistics with symptom and laboratory summaries. It selects contextual categories, identifies possible explanations and retrieves relevant reference and coaching material from a Supabase vector database. OpenAI generates the written findings and personalised interpretation; OpenAI also supplies embeddings for retrieval. The README names gpt-5.4-mini as the writing model. The actual model is configurable, and the vendor account configuration was not inspected.

The workflow checks numbers, dates, citations and selected wording, retrying generation when checks fail. Its interpretation includes what results could mean, practical suggestions and issues to discuss with a clinician. A fixed disclaimer states that the report is not medical advice or a diagnosis. Reports appear in a Streamlit interface and can be downloaded or emailed using Resend. The user-facing quality view displays validation results and sources.

The prototype uses an in-memory store with expiry logic for uploads. This does not establish the retention practices of external vendors, browser sessions or email recipients. The README says the application is not deployed and describes Render and Streamlit Cloud as planned hosting options. Future sprints propose a small consumer pilot and a practitioner-facing version. Those are planned uses, not verified deployments. Before a real-user pilot, the builder still needs to confirm the operating entity, intended medical versus wellness purpose, data-protection arrangements, access controls and rights to reuse the coaching material.

## Phase 1 annotations

Digital equivalents of the lab's marks: **UNDERLINE** = affects classification; **CIRCLE** = ambiguity; **STAR** = obligation trigger. These annotations attach to the reconstructed brief and source evidence; repeat the annotation step against the original brief when received.

| Mark | Element | Interpretation / follow-up | Evidence |
|---|---|---|---|
| UNDERLINE | Informational wellness purpose; doctor preparation | Supports a provisional transparency classification, but a disclaimer alone cannot settle device qualification | E1, E2 |
| UNDERLINE / CIRCLE | Personal interpretation of blood values and possible explanations | Could constitute a medical purpose; confirm MDR/IVDR qualification and third-party assessment route | E3; Q1 |
| UNDERLINE | No eligibility, insurance, hiring or emergency dispatch decisions documented | No identified Annex III use; internal `triage` naming is not emergency healthcare triage | E1, E3 |
| STAR | Direct user interaction and generated text | Assess Article 50(1), (2), (5), including exported and emailed outputs | E4, E5 |
| STAR / CIRCLE | Health summaries, free text and lab results sent to vendors | Removing names does not establish anonymisation; map lawful basis, recipients and retention | E4, E6; Q3 |
| STAR / CIRCLE | Local memory and expiry | Expiry is triggered by store activity; session and vendor deletion are separate questions | E7; Q3 |
| STAR | Validation failures after retry limit | Safety checks exist but do not reliably prevent release | E8; Q4 |
| CIRCLE | Local prototype versus future practitioner pilot | Confirm launch status, operator and consequential reliance | E1, E9; Q2 |
| STAR / CIRCLE | Demo-only coaching licence | Future commercial use requires permission or replacement | E9; Q5 |

Evidence IDs resolve to commit-pinned source links in [the evidence register](menohelp-evidence-and-legal-sources.md).
