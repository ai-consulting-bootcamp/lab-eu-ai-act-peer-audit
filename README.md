# Independent EU AI Act Peer Audit — MIRA

**Track:** Module 7 — EU AI Act  
**Lab:** Audit your teammate's project  
**Auditor:** Gretel Ceballos  
**Project builders:** Maria Cavalli and Elza Paegle  
**Project audited:** MIRA  
**Date:** 20 August 2026  
**Overall recommendation:** **Proceed with conditions**

---

## Submission map

This repository contains only the materials required for this lab:

- `README.md` — complete MIRA peer audit, including classification, clarifying questions, role map, compliance findings, debrief and closing note
- `instructions.md` — original lab instructions
- `rubric.md` — original grading rubric

No unrelated project files or personal data have been added.

---

# Audit basis and independence

The first-pass assessment was formed from the MIRA system brief and supporting technical documentation prepared for independent peer review.

Evidence reviewed included:

- `MIRA_SYSTEM_BRIEF_FOR_PEER_AUDIT.md`
- `docs/MIRA_ARCHITECTURE_FOR_AUDIT.md`
- `docs/MIRA_AI_AND_DATA_INVENTORY.md`
- supporting current-state documentation in the MIRA Project 3 repository

The builders' self-audit conclusions were not used to form the initial classification.

After the independent assessment had been formed, the prior team debrief with the MIRA builders and Paola Hintze's peer review were used as a quality-control and comparison step. They did not replace the independent analysis below.

---

# Phase 1 — Read and annotate

## Classification-relevant evidence

The following elements of the system brief materially affect the AI Act classification:

- MIRA is an authenticated creative-direction and brand-recognition application.
- MIRA V4 uses model-backed chat completions, identified in the implementation as `gpt-5-mini`, to generate adaptive questions and synthesize a structured Creative DNA record.
- MIRA uses an AI image-generation service, identified as GPT Image 2 in the implementation, to create visual directions and a final five-image moodboard.
- The user selects and refines creative directions before final generation.
- The intended purpose is creative exploration and brand development.
- The documented use case does not make decisions about employment, education, credit, essential services, law enforcement, migration, justice or other Annex III domains.
- MIRA directly interacts with users and generates synthetic text and images.

## Uncertainties requiring clarification

The brief does not fully establish:

- the final legal entity that will place MIRA on the EU market or put it into service;
- the exact user-facing AI disclosure at first interaction;
- whether machine-readable AI provenance survives storage, refinement and export;
- the final production vendor and responsibility allocation;
- the formal AI-literacy measures for people operating MIRA professionally.

## Obligations flagged

The evidence points primarily to:

- Article 3(1) — AI system definition;
- Article 4 — AI literacy;
- Article 50(1) — disclosure of direct interaction with an AI system;
- Article 50(2) — machine-readable marking of synthetic content where applicable;
- parallel GDPR obligations for personal data processed by the system.

---

# Phase 2 — First-pass classification

| Question | Assessment |
| --- | --- |
| Does this system fall under any prohibited category under Article 5? | **No.** No documented MIRA feature constitutes prohibited manipulation, social scoring, prohibited biometric categorisation or another Article 5 practice. |
| Does this system operate in any of the eight Annex III areas? | **No.** Its documented intended purpose is creative direction and brand development rather than a consequential Annex III use. |
| If Annex III applies, does the system significantly influence decisions in that area, or is it narrow/preparatory? | **Not applicable.** No Annex III use has been identified. |
| Does this system interact with end users or generate content requiring disclosure under Article 50? | **Yes.** MIRA directly interacts with users through model-generated conversational content and generates synthetic text and images. |
| First-pass risk tier | **Limited risk / transparency** |
| One-sentence justification | MIRA does not fall within Article 5 or an Annex III high-risk area, but its direct AI interaction and generation of synthetic text and images make Article 50 transparency obligations relevant. |

## Classification rationale

MIRA's documented intended purpose is creative exploration and brand development. Nothing in the reviewed evidence places that purpose within an Article 5 prohibited practice or an Annex III high-risk domain.

The implemented system also provides strong evidence that MIRA falls within the Article 3(1) concept of an AI system: model-backed services infer from user inputs to generate adaptive questions, a structured Creative DNA and synthetic visual outputs.

The appropriate first-pass classification is therefore **limited risk / transparency**.

Human selection and refinement are useful product controls, but they are not the reason MIRA falls outside Annex III. The decisive factor is its documented creative intended purpose.

---

# Phase 3 — Clarifying questions log

| Question | Why it matters | Provisional assumption |
| --- | --- | --- |
| **1. Which legal entity will place MIRA on the EU market or put it into service under its name?** | Provider and deployer status determine who owns the relevant AI Act obligations. | The final production provider entity is **TBD**. |
| **2. What exact notice does a user see before or at the first AI interaction?** | Article 50(1) requires disclosure that the user is interacting with AI unless this is obvious from the circumstances. | No sufficiently explicit and evidenced Article 50(1) notice is assumed to be in place. |
| **3. Do generated text and images contain machine-readable AI provenance, and does that signal survive MIRA's storage, refinement and export flow?** | Article 50(2) addresses machine-readable marking of artificially generated or manipulated outputs where applicable. | No end-to-end provenance implementation or preservation test is evidenced. |
| **4. Which AI and infrastructure vendors will be used in production, and how are responsibilities allocated?** | The final provider/deployer/vendor chain affects responsibility, transparency evidence, incident handling and parallel privacy obligations. | The production role and vendor matrix remains **TBD**. |
| **5. What AI-literacy and appropriate-use measures apply to people operating MIRA professionally?** | Article 4 requires providers and deployers to take measures to ensure a sufficient level of AI literacy among relevant personnel and operators. | No formal role-based AI-literacy programme is evidenced. |

---

# Phase 4 — Audit report

## Section 1 — System summary

MIRA is a private, authenticated creative-direction and brand-recognition application. Its V4 Project 3 journey collects project and audience context, creative preferences, recognition responses, a creative brief, birth details and, optionally, an inspiration image. Model-backed services generate adaptive questions and synthesize a structured Creative DNA, while a deterministic campaign compiler and an AI image-generation service create visual directions and a final five-image moodboard. The user selects and refines creative directions before final generation.

## Section 2 — Risk classification

**First-pass classification: Limited risk / transparency.**

The documented intended purpose does not fall within an Article 5 prohibited practice or an Annex III high-risk area. MIRA does, however, directly interact with users through AI-generated conversational content and produce synthetic text and images, making Article 50 particularly relevant.

The current implementation also gives strong grounds to treat MIRA as an AI system under Article 3(1), because model-backed components infer from user inputs to produce generated questions, structured Creative DNA and visual outputs.

No high-risk conformity assessment is indicated on the documented intended purpose.

## Section 3 — Role map

| Role | Provisional entity | Key obligations / issues |
| --- | --- | --- |
| **Provider** | MIRA product team / future legal entity placing the configured product on the EU market under its name | Article 50 transparency, Article 4 AI-literacy measures, appropriate system and vendor documentation, and evidence of applicable controls |
| **Deployer** | MIRA operating business and, depending on the commercial model, professional clients operating the system | Appropriate use, relevant AI-literacy measures and any deployer-side transparency obligations |
| **AI-component vendors** | Forge-backed chat-completion and image-generation services | Capabilities, limitations, provenance support and contractual responsibilities should be documented |
| **Infrastructure vendors** | Authentication, MySQL/TiDB and S3-backed storage services | Mainly parallel GDPR, security and contractual obligations rather than independent high-risk AI duties |
| **Optional service** | Dakidarts numerology service in V3 when enabled | Role and responsibilities depend on activation, data flow and final production configuration |

The final allocation cannot be completed until the production legal entity, customer model and vendor contracts are confirmed.

## Section 4 — Compliance findings

> **Finding 1 — Direct AI-interaction transparency**  
> **Severity:** Significant  
> **Description:** MIRA directly interacts with users through model-generated conversational content. The reviewed evidence does not demonstrate a clear and accessible disclosure, delivered at or before first interaction, that the user is interacting with an AI system. Article 50(1) is therefore not yet evidenced as operationally satisfied.  
> **Recommended action:** Add a concise AI-interaction notice at the start of the journey and test its placement, accessibility, timing and language handling. Keep release evidence showing the notice before first interaction.  
> **Escalation needed?** **Yes — Product Owner and EU legal/compliance.**

> **Finding 2 — Synthetic-content provenance**  
> **Severity:** Significant  
> **Description:** MIRA generates synthetic text and images. The reviewed materials do not evidence an end-to-end mechanism demonstrating that applicable machine-readable AI-generation marking is created and preserved through storage, refinement and export. A visible user label may improve transparency but should not be treated as evidence of the technical marking requirement by itself.  
> **Recommended action:** Confirm vendor provenance capabilities, define the applicable Article 50(2) technical requirement, and test representative outputs from generation through download/export. Record any relied-upon exception.  
> **Escalation needed?** **Yes — Engineering, vendor owner and EU legal/compliance.**

> **Finding 3 — AI literacy and appropriate use**  
> **Severity:** Significant  
> **Description:** No formal AI-literacy programme or role-based operating guidance is evidenced for people who may operate MIRA professionally. Article 4 requires proportionate AI-literacy measures taking account of the operators' knowledge, experience, context of use and affected persons.  
> **Recommended action:** Introduce concise role-based guidance covering system limitations, hallucinations, image-generation risks, appropriate reliance, correction, escalation and prohibited repurposing. Retain evidence that relevant operators completed it.  
> **Escalation needed?** **Yes — Product Owner / compliance.**

> **Finding 4 — Production role and vendor allocation**  
> **Severity:** Significant  
> **Description:** MIRA integrates model-generation, image-generation, authentication, database and object-storage services, while the final operating entity and production responsibility allocation remain unconfirmed. This makes accountability difficult to demonstrate and could create gaps between product, vendor, compliance and privacy responsibilities.  
> **Recommended action:** Approve a provider/deployer/vendor matrix identifying the production legal entities, component responsibilities, evidence owners, incident routes and vendor capabilities relevant to transparency and provenance.  
> **Escalation needed?** **Yes — Product, legal and procurement.**

> **Finding 5 — Parallel GDPR readiness**  
> **Severity:** Significant  
> **Description:** MIRA processes user identity, conversations, birth details, preferences, inspiration images, generated inferences and stored outputs. The reviewed technical documentation does not establish the complete production lawful-basis map, retention and deletion rules, processor regions, international-transfer position or end-to-end data-subject-rights workflow. These issues do not change the AI Act risk tier but materially affect production readiness.  
> **Recommended action:** Complete the production GDPR governance package before external production use, including purpose-specific lawful bases, processor/subprocessor review, retention and deletion, transfer assessment, rights handling and DPIA screening.  
> **Escalation needed?** **Yes — Privacy counsel / DPO.**

> **Finding 6 — Intended-use boundary and human review**  
> **Severity:** Minor  
> **Description:** MIRA is documented as a creative-direction system rather than a tool for consequential individual decisions. User selection and refinement provide useful quality controls. Article 14 high-risk human-oversight requirements do not directly apply on the current classification. The remaining concern is future over-reliance or repurposing into a regulated use case.  
> **Recommended action:** Document intended and prohibited uses, preserve correction and refinement controls, and trigger a new classification assessment whenever material features, target users or customer use cases change.  
> **Escalation needed?** **No — unless the intended use changes.**

## Section 5 — Overall recommendation

### PROCEED WITH CONDITIONS

Controlled development and private testing may continue.

Before external or client-facing EU deployment, MIRA should have verifiable closure or approved controls for the significant findings above, particularly:

1. Article 50 interaction transparency;
2. synthetic-content provenance;
3. Article 4 AI-literacy measures;
4. production provider/deployer/vendor allocation; and
5. parallel GDPR production readiness.

The current evidence does not support a prohibited or Annex III high-risk classification, so no high-risk conformity assessment is indicated on the documented intended purpose.

The release decision should nevertheless be evidence-based: a control should not be considered complete merely because it is intended or described; it should be observable, testable and owned.

## Section 6 — What this report is not

This report is a first-pass educational compliance review based on the available MIRA system brief and supporting Project 3 evidence.

It is **not**:

- a legal opinion;
- a conformity assessment;
- a certification of compliance; or
- a substitute for qualified EU legal advice.

The final classification and production controls should be validated before placing MIRA on the EU market or putting it into service.

---

# Phase 5 — Debrief conversation

The MIRA builders' self-audit was reviewed only after the independent peer assessment had been formed.

The debrief was conducted at team level. Paola Hintze, working on the same peer-audit exercise, presented the external findings to Maria, and Maria provided the builder-side comparison. The conclusions below record that real debrief evidence rather than attributing the conversation to the individual auditor.

## 1. Auditor presents

The external peer assessment classified MIRA as:

**Limited risk / transparency — Proceed with conditions.**

The principal external concerns were:

- Article 50 interaction transparency;
- machine-readable provenance for synthetic outputs;
- privacy and retention governance;
- production provider/deployer/vendor allocation;
- intended-use and reclassification controls.

This independent audit additionally separates **AI literacy under Article 4** as a specific operational finding.

## 2. Builder responds

The team debrief confirmed that Maria's MIRA self-audit also classified the system as:

**Limited risk / transparency — Proceed with conditions.**

The builder's principal concerns included:

- AI transparency and provenance;
- GDPR and data retention;
- the production security boundary; and
- making human review auditable.

No evidence has been recorded that the builders disputed the overall risk-tier classification.

## 3. Compare classifications

| Assessment | Classification | Rationale |
| --- | --- | --- |
| **Builder self-audit** | Limited risk / transparency | Creative system outside Article 5 and Annex III; direct AI interaction and generated visuals make Article 50 relevant |
| **Independent peer audit** | Limited risk / transparency | Same core conclusion, with Article 50(1) and Article 50(2) treated as distinct evidence requirements |

### Conclusion

There is **no material disagreement on the risk tier**.

Both assessments depend on MIRA's documented creative intended purpose and the absence of consequential Annex III decision-making.

Private staging does not remove the obligations that become relevant when the system is externally deployed.

## 4. Compare gap lists

| Area | Comparison |
| --- | --- |
| **AI interaction notice** | **Agreement.** Both assessments identify the need for a clear disclosure before or at first AI interaction. |
| **Synthetic-output provenance** | **Agreement, with external-audit precision.** The peer review distinguishes visible disclosure from machine-readable provenance and asks for preservation testing. |
| **Privacy and retention** | **Agreement.** The external review makes lawful basis, processor governance, deletion, transfer assessment and DPIA screening more explicit. |
| **Provider/deployer/vendor mapping** | **Agreement.** The external review places stronger emphasis on named legal entities and evidence ownership. |
| **Production security boundary** | **Builder-side strength.** The self-audit surfaced this more explicitly; the peer audit connects it to vendor allocation, data flows and accountability. |
| **Human review** | **Agreement with legal clarification.** Selection and refinement are useful controls, but Article 14 high-risk human oversight does not directly apply to MIRA on the current classification. |
| **AI literacy** | **External-audit strengthening.** This audit separates Article 4 literacy into its own operational finding rather than leaving it implicit. |
| **Acceptable use / reclassification** | **Mainly external-audit addition.** The intended-use boundary should be documented and classification revisited if MIRA is repurposed. |

## 5. Joint closing note

The self-audit and external audit reached the same overall classification of MIRA as **limited risk / transparency** and both support proceeding only with conditions. The self-audit contributed deeper implementation context, particularly around the production security boundary and auditable human review, while the external review made evidence gaps around transparency, provenance, privacy and role allocation more explicit. The comparison shows that controls which feel clear from inside a product still need to be documented, owned and testable when reviewed independently.

---

# Reinforce — documentation lesson

The external review highlights a recurring consulting issue: a control may exist conceptually without being sufficiently evidenced for an independent reviewer.

The main documentation gaps are not necessarily missing product features. They are missing answers to operational questions such as:

- Who owns the control?
- Where is it implemented?
- How is it tested?
- What evidence proves it works?
- What happens when a provider, use case or regulation changes?

This distinction matters because compliance claims need verifiable evidence rather than implementation intent alone.

---

# Stretch — remediation work plan

## Significant finding selected

**Article 50 transparency and synthetic-output provenance**

## Deliverable

Create an **AI Transparency and Output Provenance Release Pack** containing:

1. the approved Article 50(1) interaction notice and evidence of its placement;
2. an inventory of AI-generated text and image outputs;
3. the technical approach to applicable machine-readable marking;
4. confirmation of relevant vendor provenance capabilities;
5. tests showing whether provenance survives generation, storage, refinement and export;
6. visible-disclosure rules where appropriate; and
7. legal/compliance sign-off on the final implementation and any relied-upon exception.

## Ownership

| Owner | Responsibility |
| --- | --- |
| Product lead | Notice placement, output inventory and release acceptance criteria |
| Engineering | Provenance implementation and end-to-end preservation testing |
| Design / content | Clear, accessible disclosure copy |
| Vendor / procurement owner | Provider capability and contractual evidence |
| EU legal / compliance | Validate interpretation and release conditions |

## Indicative timeline

**Three weeks**

- **Week 1:** inventory, legal interpretation and vendor confirmation;
- **Week 2:** implementation and disclosure design;
- **Week 3:** end-to-end testing, remediation and release sign-off.

## Closure evidence

The finding should only be considered closed when:

- the AI interaction notice is visible and tested before first interaction;
- representative outputs retain the approved machine-readable signal where required;
- regression tests exist;
- vendor evidence is recorded;
- owners are assigned; and
- legal/compliance approval is documented.

---

# Final audit position

**MIRA: LIMITED RISK / TRANSPARENCY — PROCEED WITH CONDITIONS**

The product may continue controlled development and testing. External EU deployment should be evidence-gated against the significant findings identified above.
