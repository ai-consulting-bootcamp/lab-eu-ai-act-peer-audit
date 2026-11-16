# Lab proof: independent audit of Menohelp

**Reviewer entry point.** Auditor: Sergii Rostovskyi. Teammate: Ben Mayer, named in the source README. Project: [Menohelp / Project Menopause Insights](https://github.com/benmayer/proj-menopause-insights). Review date: 16 November 2026.

**Status:** Independent repository-based audit package prepared. **Prepared for submission using disclosed synthetic substitutes:** Sergii reports instructor approval because the colleague could not provide the required inputs. No actual builder-authored brief, written answers or real debrief is claimed; see [disclosure](simulation-disclosure.md). No commit, push or pull request has been made as part of this work.

## Final audit output

Read the [two-page audit report](menohelp-independent-audit-report.pdf), with [editable Markdown](menohelp-independent-audit-report.md). Recommendation: **Proceed with conditions**, limited to controlled synthetic development until the stated pre-pilot conditions are met. First-pass tier: provisional limited risk / transparency; medical-device qualification unresolved.

## Workflow export

1. Read the supplied course materials, repository instructions and rubric; identify the additional portal proof requirement.
2. Inspect the builder's system documentation without receiving a regulatory self-audit. Record the missing original brief and provisional assumptions.
3. Freeze the source at commit `89940e85b3f869b888e247a5b9651020b8d6c865` and annotate classification-relevant evidence.
4. Map Article 5, Article 6 / Annexes I and III, Article 50, roles and parallel legal issues; check official legal sources.
5. Reproduce the two retry-routing functions locally with synthetic states; inspect the separate UI delivery paths.
6. Produce the report, five-question log, conditional obligations review and one remediation work plan.
7. After the independent audit, complete the instructor-approved simulation: substitute brief, written answers, builder-perspective comparison and five-step debrief with a labelled three-sentence closing note.

This is an audit workflow, not a claim that the full application was executed.

## One reproducible run: input, evidence and output

**Question:** Does retry exhaustion prevent a report with validation errors from progressing?

**Input:** Reviewed source commit above; `{"passed": false, "retries": 3}` for the findings route and `{"guard_errors": ["unsupported claim"], "i_retries": 3}` for the guardrail route. `MAX_RETRIES` is 2. These are artificial state dictionaries, not patient data or actual model output.

**Code:** [reproduce_release_routes.py](evidence/reproduce_release_routes.py). It extracts and executes only the two reviewed routing functions and constant, without importing or starting the application. Clone the colleague repository outside this lab repository and check out the recorded commit, then run:

```text
python evidence/reproduce_release_routes.py /path/to/proj-menopause-insights
```

**Produced evidence:** [route-check-results.json](evidence/route-check-results.json) includes source commit, source-file SHA-256, inputs and observed outputs, including retry-available and success controls.

**Observed output:** Failed findings with exhausted retries return `interpret`; failed guardrails with exhausted retries return `end`. Source inspection separately shows normal rendering, download and email routes without a passing-check gate (E5/E8). This supports Finding 3; it does not prove a particular harmful medical response was produced or that an exposed live endpoint exists.

**Failure / limitation encountered:** The retry-exhaustion safety expectation is not met by the reviewed routing code. The live application, private RAG corpus and vendor settings were unavailable to this review, so there was no end-to-end generation, clinical validation or penetration test. EUR-Lex direct HTML also returned an access challenge; official Commission article text was used with that limitation recorded.

## Deliverable map and rubric coverage

| Requirement | File / evidence | Status |
|---|---|---|
| Phase 1: system brief and annotations; independence | [Brief and annotations](menohelp-system-brief-and-annotations.md) | Reconstructed baseline + linked synthetic brief; real exchange not claimed |
| Phase 2: classification table and specific legal justification | [Classification and questions](menohelp-classification-and-questions.md) | Complete provisionally |
| Phase 3: 3-5 questions with rationale and assumptions | [Five-question log](menohelp-classification-and-questions.md) | Five questions + linked synthetic written answers; real responses not claimed |
| Phase 4: six-section report, severity, actions, escalation, recommendation and disclaimer | [Two-page PDF](menohelp-independent-audit-report.pdf) | Prepared, pre-debrief |
| Role map, transparency and conditional 11-obligation review | [Obligations and readiness](menohelp-obligations-and-readiness.md) | Complete provisionally |
| Evidence trail and legal references | [Evidence register](menohelp-evidence-and-legal-sources.md) | Complete within stated scope |
| Phase 5: ordered debrief, comparison and joint 2-3-sentence note | [Debrief record](menohelp-debrief-and-joint-note.md) | Complete as disclosed simulation; actual conversation not claimed |
| Optional stretch: half-page work plan | [Remediation plan](menohelp-remediation-work-plan.md) | Prepared |
| Portal: workflow, run/input, evidence, final output and limitation | This file and linked script/results | Prepared |

The ordinary rubric's real exchange and debrief are replaced by disclosed simulations under the instructor permission reported by Sergii. This is not a claim that those real-world events occurred or that a grade has been awarded. Sergii confirmed his prerequisite self-audit is complete.

## Synthetic-input manifest

| Missing input | Substitute | Provenance |
|---|---|---|
| Builder's 300-500-word brief | [Synthetic brief](menohelp-synthetic-system-brief.md) | Generated from documented prototype description; not Ben-authored |
| Written answers to five questions | [Synthetic responses](menohelp-synthetic-builder-responses.md) | Explicit assumptions; no actual correspondence |
| Builder self-audit for comparison | [Simulated comparator](menohelp-synthetic-builder-self-audit.md) | Generated after the independent audit |
| Debrief and joint closing note | [Completed simulation](menohelp-debrief-and-joint-note.md) | Five ordered stages and three-sentence note; no real meeting or approval |

The frozen two-page report remains the audit output. The debrief records the final exercise disposition: no finding is closed by synthetic evidence, and the recommendation remains Proceed with conditions. No additional clinical or full-application runs are claimed.
