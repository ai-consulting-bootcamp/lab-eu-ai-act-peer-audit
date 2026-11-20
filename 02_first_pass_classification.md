# Phase 2: First-pass Classification: Interview Prep Report

**Based on:** Julia's system brief (annotations in [01_annotated_brief.md](01_annotated_brief.md)) · **Law:** EU AI Act (Regulation (EU) 2024/1689) as amended by the Digital Omnibus on AI (Regulation (EU) 2026/1744)

| Question | Your answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No.** It does not manipulate users, exploit vulnerabilities, score people socially, recognise emotions or use biometrics. It summarises a person's own CV and public profile so that person can prepare. |
| Does this system operate in any of the eight Annex III areas? | **No, on its intended purpose, but it sits right next to one.** The task (comparing a CV with a job description and naming skill gaps, T2, T3) matches **Annex III point 4(a)**, recruitment or selection, which covers systems used to "analyse and filter job applications, and to evaluate candidates". What keeps it out is **who it is for**: the job seeker, preparing their own interview, with no score or decision (T1, T4, T6, T8). Annex III is defined by intended purpose (Art. 3(12)), and this purpose is self-preparation, not selection. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | **Not applicable on the stated purpose.** If an employer or recruiter used it to assess applicants, it would **not** fit the Art. 6(3) "narrow or preparatory" exception: an analysis of a named person's skills and gaps is profiling, and Art. 6(3) never applies to a system that profiles people. So a recruiter's use would make it high-risk with no exception. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **Yes.** **Art. 50(1):** the user submits material and receives AI output directly, so the provider must make sure they know it comes from an AI, unless that is obvious. **Art. 50(2):** the HTML report is AI-generated text, so it must be marked in a machine-readable way. The brief mentions neither (O1, O2, ?3). Art. 50 has applied since 2 Aug 2026. |
| First-pass risk tier | **Limited risk** (Art. 50 transparency), plus Art. 4 AI literacy for the provider. |
| One-sentence justification citing the specific article or Annex entry | The system is not prohibited under Art. 5 and not high-risk under Art. 6(2) and **Annex III point 4(a)**, because its intended purpose is a job seeker's own interview preparation with no score or selection decision, but it generates text for the user, so the provider's transparency duties under **Art. 50(1) and 50(2)** apply. |

## Uncertainty between tiers

I am uncertain between **limited risk** and **high-risk (Annex III 4(a))**. The deciding factor is not what the system does (that is close to candidate evaluation) but **who uses it and on whose CV**. The brief states the right intended purpose, but it describes no control that keeps the system there.

**Clarifying questions that would resolve it** (full log in [03_clarifying_questions_log.md](03_clarifying_questions_log.md)):

1. Who would offer the system in production: Julia personally, a careers service, or a public web app?
2. Can a user submit a CV or GitHub profile that is not their own, for example a recruiter or a coach?
3. Is the report ever shared with, or produced for, an employer or recruiter?

If a recruiter or employer can use it to assess candidates, that organisation would put it to a high-risk use. Under **Art. 25(1)(c)** it could then become a provider of a high-risk system itself, and the Annex III duties would apply from **2 Dec 2027** (the Digital Omnibus deadline).

## A second, smaller point

**Personal use exemption.** Under **Art. 2(10)**, the AI Act's deployer duties do not apply to individuals using an AI system in a purely personal, non-professional activity. A job seeker preparing their own interview probably falls under this. So the **provider** (Julia, or whoever offers it) carries the obligations, not the job seekers.
