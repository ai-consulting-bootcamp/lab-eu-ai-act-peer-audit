# Lab 3 — EU AI Act Peer Audit

This repository documents a peer compliance review of an **AI Search Visibility Agent**. The review follows the five lab phases, from analysing the system brief to discussing findings with the builder.

**Start here:** [Lab evidence and reviewer guide](lab_proof.md).

## Audit at a glance

The agent compares brands across Google search results and AI-generated answers, calculates visibility scores, and emails an AI-written marketing report. A LangGraph fact-checker checks narrative claims against collected data before delivery where available.

- **Provisional EU AI Act tier:** Minimal risk for the stated SEO/marketing use; no prohibited Article 5 practice or Annex III high-risk purpose identified.
- **Overall recommendation:** **Proceed with conditions** before production deployment.
- **Priority findings:** Personal-data governance and retention; limits of fact-checking and delivery of unchecked reports; assessment of AI output transparency; operational documentation.

## Lab phases

| Phase | Evidence |
|---|---|
| 1 — Annotated system brief | [Phase 1](phase1_annotated_system_brief.md) and [original system brief](barsha_system_brief.md) |
| 2 — First-pass classification | [Phase 2](phase2_risk_classification.md) |
| 3 — Clarifying questions log | [Phase 3](phase3_clarifying_questions_log.md) |
| 4 — Structured audit report | [Phase 4](phase4_peer_audit_report.md) |
| 5 — Debrief and joint reflection | [Phase 5](phase5_debrief.md) |

## Evidence and limitations

The audit is based on the system brief, written clarifications, and the peer debrief material. It does **not** claim independent inspection of workflow code, vendor contracts, n8n execution logs, or access settings. The Phase 5 record contains the jointly agreed closing note; Barsha's formal self-audit tier and gap list were not supplied in the source material, and any live five-minute builder response remains to be confirmed.

For the complete evidence trail and limitations, see [lab_proof.md](lab_proof.md). Technical documentation for the system under review is available in [the builder's project repository](https://github.com/barsha-mishra/ai-search-visibility-agent).

## Disclaimer

This is an educational peer audit, **not** a legal opinion, conformity assessment, or certification. Any applicable EU AI Act and GDPR obligations should be confirmed before production deployment or EU market placement.
