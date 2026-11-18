# Lab Proof — Audit Your Teammate's Project

**Lab:** Ironhack Module 7 — EU AI Act, Lab 3  
**Auditor:** Martha  
**Builder:** Barsha Mishra  
**System:** AI Search Visibility Agent  
**Review status:** Audit drafted; joint closing note agreed; self-audit comparison awaiting confirmation

## 1. Reviewer entry point and supporting files

- **Source/input:** [Barsha's system brief](./barsha_system_brief.md)
- **Phase 1:** [Annotated brief](./phase1_annotated_system_brief.md)
- **Phase 2:** [Risk classification](./phase2_risk_classification.md)
- **Phase 3:** [Clarifying questions and written answers](./phase3_clarifying_questions_log.md)
- **Phase 4 / final audit output:** [Independent audit report](./phase4_peer_audit_report.md)
- **Phase 5:** [Debrief and agreed joint closing note](./phase5_debrief.md)
- **Repository overview:** [README](./README.md)

## 2. One documented review query and input

**Audit question:** Does Barsha's AI Search Visibility Agent fall into a prohibited or high-risk EU AI Act category, and what compliance gaps should be addressed before production use?

**Input evidence:** Barsha's system brief describes an n8n form collecting brand/competitor names, country, up to six search questions and an email address. The system compares Google results and OpenAI answers, calculates brand visibility scores in code, writes a report, checks selected claims using a LangGraph agent and emails the output. The follow-up written questions established the intended internal audience, current n8n logging and fact-checker failure behaviour. See [brief](./barsha_system_brief.md) and [question log](./phase3_clarifying_questions_log.md).

## 3. Evidence produced and final output

- **Classification:** minimal risk on the described internal marketing use; no identified Article 5 or Annex III use. [Phase 2](./phase2_risk_classification.md)
- **Findings:** undefined retention/privacy governance (Significant); source-dependent validation and unchecked report delivery (Significant); absent AI-generation notice (Minor); undocumented operating controls (Minor). [Phase 4](./phase4_peer_audit_report.md)
- **Final consulting recommendation:** **Proceed with conditions** — document GDPR/data flows and retention, improve reliability/failure handling, add an AI-generation notice, and confirm responsibilities. [Full report](./phase4_peer_audit_report.md)

## 4. Failure or limitation encountered

**Evidence limitation:** The auditor did not have access to Barsha's n8n workflow export, live execution logs, vendor contracts or an independently observed sample report. Accordingly, findings are based on the builder's brief and written responses rather than technical verification. Barsha also confirmed a system limitation: if the LangGraph fact-checker is unavailable, the unchecked report is sent with a warning; and the checker cannot detect errors already present in the source data.

## 5. Workflow export / executable run evidence

**Not supplied to the auditor.** The audit is a documentary compliance assessment, not an execution of Barsha's agent. The lab's generic submission guideline requests code/workflow export and one run/query with input and output. This file supplies the documented *audit query, evidence and audit output*, but **does not claim to include a workflow export or observed execution**. If the reviewer requires technical execution evidence, obtain a sanitised export and a redacted test example from Barsha and link them here.

## 6. Required debrief and submission status

The [Phase 5 debrief](./phase5_debrief.md) must be completed with Barsha after comparing the independent report with her self-audit. The joint closing note was proposed by Barsha and accepted by Martha. Barsha’s self-audit classification and formal gap list for her own agent are not yet recorded, and the shortened three-sentence version of the note is not separately approved. **Confirm these before marking Phase 5 fully complete.**

**Privacy:** Do not commit real recipient emails, credentials, API keys, tokens or personal reports.
