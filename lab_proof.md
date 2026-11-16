# Lab Proof – Audit Your Teammate's Project (EU AI Act)

**Auditor:** Nicolò · **Teammate:** Friedrich Tschoepke · **Project audited:** Friedrich's Project 3, the *AI Use Case Identifier* (commit d99573f, 13 Nov 2026) · **Date:** 16 Nov 2026

This file is the entry point for the reviewer.

## File map

| File | What it contains | Lab phase |
|---|---|---|
| [01_annotated_system_brief.md](01_annotated_system_brief.md) | Friedrich's brief with tier, unclear and obligation annotations | Phase 1 |
| [02_classification_and_questions_log.md](02_classification_and_questions_log.md) | Classification table and the clarifying questions log (5 questions with provisional assumptions) | Phases 2–3 |
| [03_audit_report_ai_use_case_identifier.md](03_audit_report_ai_use_case_identifier.md) | Two-page audit report: summary, tier, role map, 5 findings, recommendation, disclaimer | Phase 4 |
| [04_debrief_and_closing_note.md](04_debrief_and_closing_note.md) | Debrief comparison with Friedrich's self-audit, and the joint closing note | Phase 5 |
| [05_stretch_work_plan_finding1.md](05_stretch_work_plan_finding1.md) | Work plan to close Finding 1 | Stretch |

## 1. Workflow

1. Received Friedrich's system brief only, not his self-audit.
2. Read it once, then annotated it (Phase 1).
3. Classified it independently against Art. 5, Annex III and Art. 50 (Phase 2).
4. Logged five clarifying questions with provisional assumptions (Phase 3).
5. Checked one technical fact against the vendor's documentation (see Evidence).
6. Wrote the audit report (Phase 4).
7. Held the debrief with Friedrich and recorded the joint closing note (Phase 5).

## 2. One run: input → evidence → output

**Input:** two sentences from Friedrich's brief: *"one AI-generated diagram of the company's work steps"* and *"The brief and the diagram do not state that they were produced by AI."*

**Analysis:**
- Synthetic image and text output → Art. 50(2) machine-readable marking duty on the provider.
- Does the image already comply through the model vendor?

**Evidence:**
- OpenAI's documentation states that images generated through its API carry C2PA metadata and SynthID watermarks.
- OpenAI also notes that the metadata can be lost when files are processed or shared.
- So the diagram is probably marked, but the text brief isn't.

**Output:** Finding 2 in the audit report. Mark the text brief and add a visible label. Verify that the diagram's metadata survives the export pipeline.

## 3. Final output
- **Tier:** limited risk / transparency.
- **Recommendation:** proceed with conditions.
- **Conditions:** personal-data redaction and retention limits; AI marking on all outputs; no public form until review, consent and notices are in place.

See [03_audit_report_ai_use_case_identifier.md](03_audit_report_ai_use_case_identifier.md).

## 4. Failure / limitation

I audited from a written brief only, with no access to the code, prompts or real run files. Two findings depend on assumptions rather than evidence:
- **Retention and storage (Q2):** I assumed run files are kept indefinitely with no deletion routine.
- **Vendor terms (Q3):** I assumed default OpenAI API terms with no DPA signed.

If Friedrich's answers differ, the severity of Finding 1 may drop. A real engagement would include a code walkthrough and one sample run file before the report was finalised.
