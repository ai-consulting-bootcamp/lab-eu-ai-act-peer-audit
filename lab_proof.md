# lab_proof.md – LAB | Audit your teammate's project (Week 7)
**Auditor:** Murat Çömez · **Teammate (builder):** Max · **Project audited:** Max's Project 3 – **Career Intelligence Agent** (AI career guidance for job seekers; Python, LangGraph, Streamlit, OpenAI, Pinecone, Tavily)

This is the entry point for the reviewer.

## File map
| File | What it contains |
|---|---|
| [`teammate_system_brief_career_intelligence_agent.pdf`](teammate_system_brief_career_intelligence_agent.pdf) | Input: the builder's Phase 1 system brief (the only material received; shared with his permission) |
| [`01_brief_annotations_and_classification.md`](01_brief_annotations_and_classification.md) | Phase 1 annotations (underline / circle / mark) + Phase 2 classification table and paragraph |
| [`02_clarifying_questions_log.md`](02_clarifying_questions_log.md) | Phase 3: five written questions, why they matter, provisional assumptions, dates |
| [`03_audit_report_career_intelligence_agent.md`](03_audit_report_career_intelligence_agent.md) | Phase 4: 2-page audit report (summary, classification, role map, 6 findings, recommendation, disclaimer) |
| [`04_debrief_and_closing_note.md`](04_debrief_and_closing_note.md) | Phase 5: debrief comparison + **joint closing note** (required) |
| [`05_stretch_work_plan_finding_1.md`](05_stretch_work_plan_finding_1.md) | Stretch: work plan to close Finding 1 |

## 1. Workflow
1. Exchanged **system briefs only** with my teammate (no tiers, gaps or memos), 17 Nov 2026.
2. Read the brief once, then annotated it: 15 elements tagged as tier-relevant, unclear, or obligation-triggering.
3. Ran the classification sequence: Art. 5, then Annex III (+ Art. 6(3)), then Art. 50, then minimal.
4. Logged five clarifying questions in writing, each with a provisional assumption.
5. Mapped roles (provider / deployer / vendors), rated findings by severity, issued a recommendation.
6. Debrief with the builder; compared tiers and gap lists; wrote the joint closing note.

## 2. One run – input
The builder's brief, key sentence used for classification (§1):
> The system "does not make hiring decisions, submit applications, or automatically accept or reject candidates on behalf of employers."

Combined with §3: a 0–100 matching score per job based on the candidate's profile, and §5: "a future commercial provider could offer the application directly to these users."

## 3. Evidence it produced
- Annotation #2 / #9: the score evaluates a natural person, so it is **profiling**.
- Annotation #3: the stated purpose is the candidate's own decision, so it is **outside Annex III 4(a)** as described.
- Annotation #15: the business model is open, so **classification is conditional** (Art. 6(3): Annex III + profiling = always high-risk).
- Questions log Q1 and Q3: B2C-only and no-sharing assumptions recorded.

## 4. Final output
**Tier:** Limited risk / transparency (Art. 50(2)), with Annex III 4(a) flagged for legal review.
**Recommendation:** **Proceed with conditions.** Lock in the B2C intended purpose, add AI-output marking, complete GDPR vendor basics, run a first bias test. This changes to *Do not proceed* if any recruiter or job-board channel is planned. Full report: [`03_audit_report_career_intelligence_agent.md`](03_audit_report_career_intelligence_agent.md).

## 5. Failure or limitation I hit
**I audited a document, not a system.** I had only a 2-page brief, no code, no architecture diagram, no UI. Three of my findings (Art. 50(2) marking, GDPR data flows, bias testing) rest on assumptions about things the brief does not mention. For example, I could not verify whether the LLM influences the score or only writes text, which changes the scope of Art. 50(2) and where accuracy risk sits. The questions log makes these assumptions explicit, but a real engagement would need a code walkthrough before the opinion is final.
