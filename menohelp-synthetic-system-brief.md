# Menohelp: synthetic substitute system brief

**SYNTHETIC EDUCATIONAL MATERIAL.** Not written or approved by Ben Mayer. Generated under the instructor-approved substitution reported by Sergii; see [disclosure](simulation-disclosure.md). The description below supplies the missing brief for the exercise and stays within the documented prototype scope. Repository-derived facts remain distinguishable through the original evidence register. The brief body is 300-500 words.

## Brief

Menohelp, also called Project Menopause Insights, is a local prototype built by Ben Mayer during the Ironhack AI Bootcamp. It helps adults understand menstrual-cycle records, symptoms and optional blood-test results before a conversation with a doctor. The README identifies women aged 35 to 50 and older as the primary audience. It describes the product as informational rather than diagnostic, with no instruction to start or stop medication and no dosage recommendations.

Users upload cycle records in CSV or JSON format, including exports from tracking apps. They can also upload text-based laboratory PDFs and complete a symptom questionnaire. A FastAPI service normalises the cycle data and computes statistics in Python. The laboratory parser retains allow-listed measurements and removes names, addresses and dates of birth from its structured output. Users can inspect and correct extracted laboratory values before generating a report.

A LangGraph workflow combines the statistics with symptom and laboratory summaries. It selects contextual categories, identifies possible explanations and retrieves relevant reference and coaching material from a Supabase vector database. OpenAI generates the written findings and personalised interpretation; OpenAI also supplies embeddings for retrieval. The README names gpt-5.4-mini as the writing model. The actual model is configurable, and the vendor account configuration was not inspected.

The workflow checks numbers, dates, citations and selected wording, retrying generation when checks fail. Its interpretation includes what results could mean, practical suggestions and issues to discuss with a clinician. A fixed disclaimer states that the report is not medical advice or a diagnosis. Reports appear in a Streamlit interface and can be downloaded or emailed using Resend. The user-facing quality view displays validation results and sources.

The prototype uses an in-memory store with expiry logic for uploads. This does not establish the retention practices of external vendors, browser sessions or email recipients. The README says the application is not deployed and describes Render and Streamlit Cloud as planned hosting options. Future sprints propose a small consumer pilot and a practitioner-facing version. Those are planned uses, not verified deployments. Before a real-user pilot, the builder still needs to confirm the operating entity, intended medical versus wellness purpose, data-protection arrangements, access controls and rights to reuse the coaching material.

## Annotation mapping

The original [Phase 1 annotation table](menohelp-system-brief-and-annotations.md) applies to this same description: wellness purpose and personalised interpretation affect classification; external services and generated reports trigger obligations; intended use, legal entity, retention and permissions remain ambiguities. The synthetic answers resolve assumptions only within the exercise.
