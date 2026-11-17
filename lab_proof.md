# Lab proof — Audit your teammate's project (EU AI Act)

**Auditor:** Pieter Albrecht
**Teammate:** Elif Yurdakul
**Project audited:** Elif's Project 3, the **Unioptt university programme fact-checker** (checks programme facts and compares them with a Turkish student's profile)

This is the entry point for the reviewer. Each section below links to the supporting file.

## 1. Workflow

```
Elif's system brief (only input, per lab rules)
        │
        ▼
Phase 1  Annotate  ([T] tier · [?] unclear · [O] obligation)
        │
        ▼
Phase 2  First-pass classification (Art. 5 → Annex III → Art. 6(3) → Art. 50)
        │
        ▼
Phase 3  Clarifying questions log (5 questions + provisional assumptions)
        │
        ▼
Phase 4  Audit report (summary · tier · role map · findings · recommendation · disclaimer)
        │
        ▼
Phase 5  Debrief with Elif ──► joint closing note      Stretch: work plan for Finding 1
```

## 2. One run: input → evidence → output

**Input:** Elif's 300-word Phase 1 system brief. The key sentence was *"compares the requirements with the student's profile"*, producing *"met / gap / check"* items, plus *"Later, school counsellors and private high schools could use it."*

**Evidence produced:**
- 13 annotated passages ([annotations](brief_annotations_Elif_Unioptt.md)).
- The classification table ([classification + log](classification_and_questions_log.md)):

| Check | Result |
|---|---|
| Art. 5 | Not prohibited |
| Annex III | Education, point 3(c), borderline |
| Art. 6(3) | Preparatory in B2C; **profiling override** likely bites in B2B |
| Art. 50 | Minimal unless Telegram is conversational |
| Tier | Not high-risk (B2C) / likely high-risk (B2B) |

**Final output:** [audit report](AI_Act_audit_report_Unioptt_programme_checker.md). **Proceed with conditions** for B2C; **re-classify before launch** for B2B. Five findings: 3 Significant (classification and registration, minors' data, no human oversight) and 2 Minor (transparency, AI literacy).

## 3. Failure / limitation I hit

- **Brief-only audit:** 300 words can't settle territorial scope (Q1) or how schools would use the output (Q2), and those two answers decide the tier. My classification is provisional and the assumptions are logged.
- **"Not a decision" ≠ "not high-risk".** The brief stresses there's no score or prediction, but the met/gap comparison still evaluates a person. The hardest call was whether that counts as profiling under Art. 6(3); I flagged it rather than resolve it.
- **Moving law:** the 2026 AI Omnibus moved Annex III obligations to 2 December 2027 but kept registration after relying on Art. 6(3). I checked current sources rather than course notes.

## 4. Supporting files

- [brief_annotations_Elif_Unioptt.md](brief_annotations_Elif_Unioptt.md) — Phase 1: annotated brief
- [classification_and_questions_log.md](classification_and_questions_log.md) — Phases 2–3: classification table, clarifying questions log
- [AI_Act_audit_report_Unioptt_programme_checker.md](AI_Act_audit_report_Unioptt_programme_checker.md) — Phase 4: audit report
- [debrief_with_Elif.md](debrief_with_Elif.md) — Phase 5: debrief, joint closing note, Reinforce
- [stretch_work_plan_finding1_classification.md](stretch_work_plan_finding1_classification.md) — Stretch: work plan for Finding 1
