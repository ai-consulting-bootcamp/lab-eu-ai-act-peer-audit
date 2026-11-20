# Phase 1: Annotated Brief: Interview Prep Report

**Brief by:** Julia Antunes · **Audited by:** Ayhan Demir · 17 Nov 2026 · **Scope:** EU AI Act only

**Key**

| Mark | Meaning (lab instruction) |
|---|---|
| <u>underline</u> + **[T]** | Affects the risk tier classification |
| **(?)** | Unclear; needs clarifying before I form a view |
| **[O]** | Suggests a specific obligation applies |

Each mark is numbered and explained in the evidence table below the brief.

---

## System Brief: Interview Prep Report

*Julia Antunes, 17 Nov 2026*

### What does the system do?

This workflow helps <u>a job seeker prepare for an interview</u> **[T1]**. It researches a company and its recent news, <u>compares a job description with information about the candidate</u> **[T2]**, and <u>creates a report</u> **[O1]** with relevant experience to discuss, <u>possible skill gaps</u> **[T3]**, and likely interview questions. <u>It is a preparation aid, not a hiring tool.</u> **[T4]**

### What inputs does it take?

The user provides a company name, a job description, and <u>a PDF CV, a GitHub profile, or both</u> **[T5] (?1)**. The workflow extracts information from the CV and/or gathers repository information from the supplied GitHub profile. It also researches the company and recent news using <u>online sources</u> **(?2)**. A CV can contain personal data such as a person's name, contact details, employment history, education, and skills. A GitHub profile may contain identifying information and public work history. The job description and company research may also identify people, depending on their contents.

### What does it output?

The workflow <u>generates and displays an HTML report</u> **[O2] (?3)**. The report summarizes relevant role requirements and candidate evidence, suggests projects or experience to highlight, identifies potential skill gaps, and lists five likely interview questions. <u>It does not produce a candidate score, hiring decision, or notification.</u> **[T6]**

### Who is affected, and how is the output reviewed?

The job seeker whose CV or profile is submitted is the person most directly affected: the report may shape how they prepare and present their experience. The workflow does not make decisions or take action on the user's behalf. The user can read the report, check its claims and links, and decide what advice to use; <u>there is no separate or mandatory human-review step built into the workflow</u> **[T7]**. Unsupported claims and unverified links are removed during validation, but the user should still verify the report before relying on it.

### Who built it, and who would use it?

<u>Julia Antunes built the workflow</u> **[O3]** by configuring n8n and <u>integrating OpenAI</u> **[O4]** and online research sources. <u>In production, the intended users would be job seekers preparing for their own interviews.</u> **[T8] (?4)** <u>No employer or hiring team is intended to use the report to assess or select candidates.</u> **[T9] (?5)**

This work is part of a lab project in an Ironhack bootcamp, completed in November 2026.

### Data handling

The workflow processes the submitted materials, research results, and generated report. n8n execution history may retain sensitive data, and invalid submissions may also be logged to Notion if that integration is configured. Generated reports are not stored in persistent project storage.

---

## Evidence table

| # | Brief element | Why it matters under the AI Act |
|---|---|---|
| **T1** | Helps a job seeker prepare | Sets the intended purpose (Art. 3(12)), which decides the tier. Help for the candidate, not for the employer. |
| **T2** | Compares a job description with candidate information | Functionally the same activity as candidate evaluation in **Annex III point 4(a)** (recruitment or selection: "analyse and filter job applications, and evaluate candidates"). High-risk if an employer did it. |
| **T3** | Identifies possible skill gaps | An assessment of a person's skills. If used by an employer, this is evaluating a candidate. It also looks like **profiling**, which would block the Art. 6(3) exception if Annex III applied. |
| **T4** | "A preparation aid, not a hiring tool" | A clear intended-purpose statement. Strong evidence for staying outside Annex III. |
| **T5** | CV and/or GitHub profile | The system works on data about a real person's career. Relevant to Annex III 4(a) and profiling. |
| **T6** | No score, decision or notification | Supports "not high-risk": the output does not rank or select anyone. |
| **T7** | No built-in human review | Not required for a limited-risk system; would matter under Art. 14 if it were high-risk. |
| **T8** | Intended users: job seekers for their own interviews | Points to **personal, non-professional use**. Under Art. 2(10), deployer obligations do not apply to individuals using AI for purely personal purposes. Provider obligations still apply. |
| **T9** | No employer intended to use it | Intended purpose again. But the brief describes no control that stops an employer or recruiter from using it. |
| **O1** | Creates a report | Generated text: **Art. 50(2)** machine-readable marking. |
| **O2** | Generates and displays an HTML report | The user receives AI output directly: **Art. 50(1)** disclosure (if not obvious) and **Art. 50(2)** marking. The brief mentions neither. |
| **O3** | Julia built it | Julia is the **provider** if she makes it available under her name (Art. 3(3)). Provider duties: Art. 50(1), 50(2), Art. 4. |
| **O4** | Integrates OpenAI | OpenAI is a **general-purpose AI model provider**: Art. 53 duties, including information for downstream providers like Julia. |
| **?1** | "A PDF CV, a GitHub profile, or both" | Can a user submit someone else's CV or profile? This decides the misuse risk under Annex III 4(a). |
| **?2** | "Online sources" | Which services? Are any of them AI models with their own AI Act role? |
| **?3** | "Displays an HTML report" | Is the report labelled as AI-generated, on screen and in the HTML itself? |
| **?4** | "In production" | Who would offer it: Julia personally, a careers service, a public app? This decides who the provider and deployer are. |
| **?5** | "No employer is intended to use it" | Intended, but how is it enforced (terms of use, a check, nothing)? |
