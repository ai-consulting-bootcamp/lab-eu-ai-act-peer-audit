# Phases 2–3 – First-Pass Classification and Clarifying Questions Log

**System:** AI Use Case Identifier (Project 3) · **Builder:** Friedrich Tschoepke · **Auditor:** Nicolò · **Date:** 16 Nov 2026

## Phase 2 – First-pass classification

| Question | My answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No.** No manipulation, no exploitation of vulnerabilities, no social scoring, no biometric processing, no emotion recognition. People named in scraped pages are passed through, not profiled. |
| Does this system operate in any of the eight Annex III areas? | **No.** The nearest is Annex III 4 (employment), because it reads careers pages and job postings and suggests changes to how work is done. But it rates *work steps*, not people. It doesn't recruit, select, evaluate, monitor or allocate tasks to individuals. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | Not applicable. Even if it were read as touching employment, the output is a discussion aid for a first sales meeting, not input to a decision about any worker. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **Yes.** It generates synthetic **text** (the brief) and a synthetic **image** (the diagram) → **Art. 50(2)**: the provider must mark outputs in a machine-readable way. **Art. 50(1)** doesn't apply today (the builder is the only user), but would for the planned public form. Art. 50(4) doesn't apply: no deepfake, and the text isn't published to inform the public. |
| **First-pass risk tier** | **Limited risk / transparency** |
| One-sentence justification | The system is outside Art. 5 and Annex III because it analyses companies and work steps rather than people, but it generates text and images, so Art. 50(2) machine-readable marking applies, and Art. 50(1) disclosure will apply once the planned public form exists. |

**Uncertainty:**
- **Text marking.** How much text marking is "technically feasible" for a downstream builder, and the effect of the transition period added by the Digital Omnibus on AI, need legal confirmation.
- **Tier could drop.** If counsel held that Art. 50(2) is met by OpenAI's own marking, the system *as built today* would be effectively minimal risk. The GDPR findings would stay the same.

## Phase 3 – Clarifying questions log

*Asked in writing on 16 Nov 2026. Provisional assumptions apply until answered.*

| # | What I need to know | Why it matters | Provisional assumption |
|---|---|---|---|
| Q1 | Will the brief or diagram ever be **shared outside the consultant**: sent to the analysed company, used as a sales leave-behind, or posted? | Decides how much Art. 50 disclosure matters in practice, and brings in unfair-competition and accuracy risk for the money estimates. | **Yes, eventually.** The planned public form sends reports directly to company owners. |
| Q2 | How long are **run files and contact fields kept**, where (local disk, cloud), and who can access them? | Run files hold names of managing directors, founders and HR contacts. This decides the GDPR storage-limitation and security findings. | Kept indefinitely on the builder's laptop or repo, with no deletion routine. |
| Q3 | Which **OpenAI API terms** apply: data-processing agreement, data retention, region? Does the generated diagram keep its provenance metadata in the final output? | Decides the GDPR transfer finding, and whether OpenAI's image marking already covers Art. 50(2) for the diagram. | Default API terms, no DPA signed. The diagram is saved as a separate image file, so its metadata probably survives, but this hasn't been checked. |
| Q4 | For the **planned public form**: is it one-shot or conversational? Are reports emailed automatically? Will the name, email and phone be used for sales follow-up? | Art. 50(1) applies to direct interaction. Email marketing needs consent under the unfair-competition law (§7 UWG). An unreviewed report to the public raises the accuracy risk. | One-shot form, report emailed automatically, contacts used for follow-up. |
| Q5 | Do the optional contact fields or any scraped names **ever enter a prompt or search query** in a way that targets an individual? | If the system searched for or summarised individuals, it would move toward profiling, with a different GDPR (and possibly AI Act) picture. | No. The brief says the contact fields aren't used in the analysis, and there are no person searches. |
