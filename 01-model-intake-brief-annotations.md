# Phase 1: Read and annotate - Model Intake Brief (Sergii Rostovskyi)

## Exchange log (ground rules)

| Date | What | Notes |
|---|---|---|
| 26 Nov 2026 | **Received:** the teammate's system brief, [`deliverables/model-intake-system-brief.md`](https://github.com/s-rostovskyi/lab-eu-ai-act-self-audit/blob/main/deliverables/model-intake-system-brief.md) | Their self-audit repo keeps the brief in its own file. I opened **only that file**. |
| 26 Nov 2026 | **Received:** technical documentation at the [reviewed snapshot `e384f3a`](https://github.com/s-rostovskyi/model-intake-brief/tree/e384f3a41b5c74119786f55865ebe4e7e6cfb73c) | README (architecture, tools), `stack_decision.md`, `gtm_future_sprints.md`, and the assessment prompt and output schema in `src/intake/assessment.py`. The brief links this snapshot as its project evidence. |
| Not opened before the debrief | `model-intake-eu-ai-act-assessment.md`, `model-intake-compliance-memo.md`, `model-intake-transparency-notice.md` | These are the teammate's tier, gaps and memo. I saw the filenames in a directory listing but did not open them until Phase 5. |
| 26 Nov 2026 | **Clarifying questions** sent in writing (see `02`) | The teammate wasn't available today, so the answers in the debrief are **simulated** (see `04`). |

## Annotations

The brief is quoted in parts. **Key:** 🟦 **[T]** = affects the risk tier (underline) · 🟠 **[?]** = unclear, needs clarifying (circle) · 🟩 **[O]** = suggests a specific obligation.

| # | Brief text (excerpt) | Mark | Annotation |
|---|---|---|---|
| 1 | "helps a company review a third-party AI model before deciding whether to integrate it" | 🟦 T | The **purpose** is procurement and governance support. The decisions concern *models*, not natural persons, so it points away from Annex III. |
| 2 | "AI governance lead, risk reviewer, or project management lead" | 🟦 T · 🟩 O | **Professional users**, which makes the client a **deployer**. The literacy measures under Art 4 apply to the client's reviewers. |
| 3 | "This brief assumes a future professional deployment by an EU client" | 🟦 T · 🟠 ? | This is the basis for treating the builder as **provider** placing the system on the EU market. Unclear: sold as SaaS, licensed, or built bespoke for one client? |
| 4 | "sends selected source text and the model details to an OpenAI model to assess the evidence" | 🟦 T · 🟩 O | A **GPAI model inside the system**, so the builder is the downstream provider and OpenAI the GPAI model provider (Art 53). It is also a GDPR transfer. |
| 5 | "labels each item as evidence found, partial, not found, or not checked" | 🟦 T · 🟠 ? | Is the label an **AI-generated output**? Yes: the schema shows that the LLM proposes it. Is it shown as AI-proposed? The brief doesn't say. |
| 6 | "suggests questions for the model supplier" | 🟠 ? | Does the LLM write these, or a template? The code shows they are **templated by code**, which matters for Art 50(2). |
| 7 | "gives source links and excerpts", "checks the proposed quotes against the source text" | 🟩 O | A strong accuracy control, but it checks that a quote *exists*, not that the page is *trustworthy*. |
| 8 | "A live run searches for public model cards … Hugging Face repository" | 🟠 ? · 🟩 O | **Who writes the evidence?** A Hugging Face model card is written by the party under review. Source text goes into the prompt, which opens a **prompt-injection and self-serving-evidence** risk. |
| 9 | "Report generation runs automatically … The prototype does not require sign-off" | 🟦 T · 🟩 O | No human checkpoint, which creates an **over-reliance** risk. It doesn't change the tier (not high-risk), but it is a key design gap. |
| 10 | "In the proposed client workflow, the governance reviewer would verify … and record a separate integration decision" | 🟠 ? | This is proposed, not built. Will the client's process *require* it? |
| 11 | "A repository identifier can include an individual's account name … list a contact address" | 🟩 O | **GDPR:** personal data of third parties, collected indirectly (Art 14), sent to the US and reproduced in reports. |
| 12 | "The interface can also display previously saved reports" | 🟠 ? | Where are reports stored, for how long, and who can see them? The code shows two bundled samples, but production storage is undefined. |
| 13 | "The workflow does not assess applicants, employees, or consumers" | 🟦 T | The builder explicitly rules out Annex III §4 and §5 uses. I accept this, but I would put it in the terms of use. |
| 14 | README: "checks it against a fixed 18-item checklist based on the EU AI Act … Information, not legal advice" | 🟠 ? · 🟩 O | It is **marketed around legal criteria**. That raises a legal-services and liability question (for example the German RDG), and a staleness risk after the Digital Omnibus. |
