# lab_proof — Audit your teammate's project (independent EU AI Act review)

**Auditor:** Jaime Garate Marquerie · **Project audited:** Sandra Obregón, VC Startup Screening Agent (Project 3)
**Status:** prepared locally on 17 Nov 2026. Written debrief completed. **Not published, not submitted, not accepted.**
**Lab repository:** `ai-consulting-bootcamp/lab-eu-ai-act-peer-audit`. The AI reviewer grades against its `rubric.md`; the mapping is in [`README.md`](README.md).

This is the entry point for the reviewer.

| Lab phase | File | Status |
|---|---|---|
| Phase 1 · Read and annotate | [`brief_annotations_vc_screening_agent.md`](brief_annotations_vc_screening_agent.md) | Draft |
| CFU 1–3 · Phase 2 · Classification table and role map | [`first_pass_classification_and_role_map_vc_screening_agent.md`](first_pass_classification_and_role_map_vc_screening_agent.md) | Draft |
| CFU 2 · Phase 3 · Clarifying questions log (5 questions) | [`clarifying_questions_log_vc_screening_agent.md`](clarifying_questions_log_vc_screening_agent.md) | Sent and answered 17 Nov 2026 |
| Phase 4 · Audit report (6 sections, 2 pages) | [`independent_audit_report_vc_screening_agent.md`](independent_audit_report_vc_screening_agent.md) | Draft |
| Phase 5 · Debrief and joint closing note | [`debrief_and_joint_closing_note.md`](debrief_and_joint_closing_note.md) | Complete: written debrief, five steps, joint note |

## 1. Code / workflow
**Not reviewed by the auditor.** Only the system brief was exchanged, as the lab requires. The workflow below is **as declared by the builder**:

`startup name + website → Tavily (public sources) · Jina Reader (website) · GDELT (news) · fund criteria (local file) → OpenAI model (company name + Tavily extracts: headquarters, funding stage) → quote check against extracts → report (findings, source links, questions; Meets / Does not meet / Not verified)`

**Open point:** how the Jina and GDELT outputs are used is not stated (Q2).

## 2. One run, with input, evidence and output
**Declared by the builder, not executed or observed by the auditor.**
- **Input:** startup "Lawra" (name and official website; the URL is not given in the brief).
- **Output and evidence, as described in the brief:**
  - a saved report;
  - headquarters and funding stage both marked "Not verified";
  - the news search (GDELT) failed and this was recorded;
  - the report was saved using the other sources.
- **Evidence status:** builder's statement. The report file and run log were not provided to the auditor. Request them at the debrief if the lab allows; until then this run cannot be traced by the reviewer.

**Audit evidence produced by the auditor:**
- two-pass annotation of the brief (17 annotated statements);
- the classification table;
- five clarifying questions with provisional assumptions;
- the two-page report, checked by rendering to PDF.

## 3. Failure / limitation
**Main limitation of this audit:**
- It rests on a 324-word self-reported brief plus the builder's written answers (17 Nov 2026). No code was inspected.
- The answers resolved the classification questions: company criteria only, no loans or individuals.
- They also confirmed two gaps that the auditor cannot close from outside:
  - whether personal data reaches OpenAI is still unverified;
  - there are no accuracy figures for the criterion status.

**Limitation of the system declared in the brief:**
- In the Lawra run, both checked criteria ended as "Not verified" and the news source failed.
- This shows honest failure handling, but gives no evidence yet that the system can verify these criteria reliably.

## 4. Who did what
- **The auditor (student):** directed the audit.
- **Claude** (AI tutor): drafted the documents from the builder's brief, under the student's direction. The student must review and defend them before submission.
- **Code and self-audit:** the builder's code and self-audit were **not** accessed before the debrief. Her written answers (17 Nov 2026) are recorded as her statements.
