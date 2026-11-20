# Lab Proof: Audit Your Teammate's Project (Interview Prep Report)

**Auditor:** Ayhan Demir · **System owner (teammate):** Julia Antunes · Ironhack AI Consulting & Integration Bootcamp · 20 Nov 2026
**System audited:** Interview Prep Report, Julia's Project 3 (n8n + OpenAI workflow that writes an interview-prep report for a job seeker)
**Scope:** EU AI Act (Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744)
**Result in one line:** **limited risk** (Art. 50 transparency + Art. 4 AI literacy), not prohibited, not high-risk on its stated purpose; 6 findings (3 Significant, 3 Minor, 0 Blocking); **proceed with conditions**.

## Start here

| Phase | File | Outcome |
|---|---|---|
| Input | [project-3-brief_julia.md](project-3-brief_julia.md) | Julia's system brief, the only material used for the audit |
| 1. Read and annotate | [01_annotated_brief.md](01_annotated_brief.md) | 9 tier marks [T], 4 obligation marks [O], 5 open points (?), each explained in an evidence table |
| 2. First-pass classification | [02_first_pass_classification.md](02_first_pass_classification.md) | Limited risk; uncertainty with Annex III 4(a) stated, with the 3 questions that would resolve it |
| 3. Clarifying questions log | [03_clarifying_questions_log.md](03_clarifying_questions_log.md) | 5 written questions to Julia (17 Nov 2026): what I need, why it matters, provisional assumption |
| 4. Audit report | [04_audit_report.md](04_audit_report.md) | All 6 required sections and joint result (about 1,180 words) |


## Rubric map

| Rubric item | Where the evidence is |
|---|---|
| 4. Only the brief exchanged, ground rules respected | Report header ("Basis: Julia's system brief, my annotations, and the assumptions in the clarifying questions log"); questions asked in writing and logged in [03](03_clarifying_questions_log.md) |
| 5. Tier justified with Article / Annex entry | [02](02_first_pass_classification.md): Art. 5, Art. 6(2), Annex III 4(a), Art. 6(3), Art. 50(1)/(2), Art. 3(12) |
| 6. Questions log: need, why, assumption | [03](03_clarifying_questions_log.md): one column for each, plus how the assumptions affect the tier |
| 7. Role map with obligations | [04 §3](04_audit_report.md#3-role-map): provider, deployer, possible future provider, OpenAI, other vendors |
| 8. Six report sections | [04](04_audit_report.md): §1 summary, §2 classification, §3 role map, §4 findings with severity, §5 recommendation, §6 disclaimer |

## The query: input, evidence, output

**Input:** Julia's system brief ([project-3-brief_julia.md](project-3-brief_julia.md)).

**Query:** the Phase 2 classification questions, applied to the annotated brief.

**Evidence: brief fact → AI Act test → result**

| Brief says | AI Act test | Result |
|---|---|---|
| "A preparation aid, not a hiring tool"; users are job seekers preparing their own interviews | Art. 3(12) intended purpose | Purpose is self-preparation, which decides the tier |
| Summarises a CV, a job description and company research; no manipulation or biometrics | Art. 5 prohibited practices | Not prohibited |
| Compares a job description with the candidate's CV and lists skill gaps; no score, decision or notification | Art. 6(2), Annex III 4(a) | Not high-risk on its stated purpose. Recruiter use would make it high-risk with no Art. 6(3) exception, because it profiles a named person |
| The user receives the AI report directly | Art. 50(1), 50(5) | Users must be told it is AI-generated at first interaction |
| Generates an HTML report | Art. 50(2) | Report needs a machine-readable AI marker |
| Individuals use it for their own interviews | Art. 2(10) | Deployer duties do not apply; the provider carries the obligations |
| Julia built it and integrates OpenAI | Art. 3(3), Art. 4, Art. 53(1)(b) | Julia is the provider (assumed); AI literacy measures; keep OpenAI's model information on file |

**Final output:** first-pass tier **limited risk**, the role map, 6 findings with severity, and the recommendation.

| # | Finding | Severity | Escalation |
|---|---|---|---|
| 1 | No AI notice to the user (Art. 50(1), 50(5)) | Significant | No |
| 2 | No machine-readable marking of the report (Art. 50(2)) | Significant | No, unless widely distributed |
| 3 | No safeguard against employer or recruiter use (Annex III 4(a), Art. 25(1)(c)) | Significant | Yes, to legal counsel if offered to organisations |
| 4 | Non-high-risk assessment not documented | Minor | No |
| 5 | AI literacy (Art. 4) | Minor | No |
| 6 | Model information from OpenAI (Art. 53(1)(b)) | Minor | No |

**Recommendation: proceed with conditions.** Before the tool is offered to other people: (1) a visible AI notice on the input page and the report; (2) a machine-readable AI marker in the HTML; (3) the intended purpose and the ban on assessing candidates stated to users, with an own-CV confirmation.

## Ground rules

- **Only the brief was exchanged.** The audit used Julia's system brief alone. Her self-audit tier, gap analysis and compliance memo were not part of the input.
- **Questions in writing.** All five clarifying questions are logged with the date and recipient in [03_clarifying_questions_log.md](03_clarifying_questions_log.md).
- **Ambiguities stated.** Where the brief is silent (who offers the tool, whether others' CVs can be uploaded, how the report is labelled), I wrote down my assumption and built the report on it.

## Debrief: joint closing note

Written together with Julia, in full in [04_audit_report.md §7](04_audit_report.md#7-joint-closing-note). In short: both audits agreed the system is not high-risk and found the same two core risks, Art. 50 transparency and the line between advice and employment use. The differences came from what each of us knew. A builder auditing their own work fills gaps in the brief from memory. An external auditor turns every unstated assumption into a question or a finding, so is stricter on evidence and ownership. The builder is sharper on which AI Act duties the system actually triggers.

## Failure or limitation I hit

**The brief cannot settle the tier on its own.** What the system does (compare a CV with a job description, name skill gaps) is very close to candidate evaluation under Annex III 4(a). What keeps it out is who uses it and on whose CV. The brief states the right intended purpose, but it describes no control that keeps the system there. So I stated the uncertainty in Phase 2 instead of forcing an answer, made the missing safeguard a Significant finding (Finding 3), and set a trigger to review the classification if the tool is offered to any organisation.

**Parallel laws were out of scope.** The audit covers the EU AI Act only. The brief shows clear GDPR touchpoints that a full review would cover: CVs and GitHub profiles with personal data, n8n execution history that may keep sensitive data, and invalid submissions logged to Notion.

## Assumptions

- Julia would publish the tool under her own name as a free tool for individual job seekers in the EU, so she is the provider and there is no professional deployer.
- There is no check stopping a user from uploading someone else's CV, and the report is shown only to the person who submitted the material.
- Neither an AI notice nor a machine-readable marker is in place, because the brief mentions neither.
- OpenAI is the only AI model provider; the research sources are search and news services.
- The law is checked as of 17 Nov 2026, including the Digital Omnibus on AI (Annex III duties from 2 Dec 2027).
- This is a course assessment, not a legal opinion, conformity assessment or certification.
