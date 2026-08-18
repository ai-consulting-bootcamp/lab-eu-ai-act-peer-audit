# MIRA peer audit — evidence and questions log

**Auditor:** Paola Hintze  
**Teammate:** Maria Cavali (`mariacavali`)  
**System audited:** MIRA Project 3 (V4 creative-direction journey; shared platform boundaries noted where relevant)  
**Independent review date:** 18 August 2026

## Independence record

The provisional classification, questions, and findings below were formed from the exchanged system brief and technical repository before the teammate's self-audit conclusions were opened. The self-audit branch was reviewed only afterward for the Phase 5 comparison.

## Phase 1 — annotated brief

Legend: <u>risk-tier evidence</u>; **[CLARIFY]** missing information; **[OBLIGATION]** evidence that may trigger a duty.

MIRA is a private, authenticated creative-direction system. It collects project context, audience, mood, style cues, optional inspiration, design preferences, and birth details, then conducts a bounded adaptive conversation. It synthesises those inputs into Creative DNA, a campaign plan, visual directions, and a final five-image editorial moodboard. <u>The outputs are creative recommendations, not employment, education, credit, public-benefit, biometric, law-enforcement, migration, or justice decisions.</u>

The user reviews the generated direction, selects a preferred path, and may refine it with preserve/avoid instructions before the final moodboard is created. <u>This human choice means MIRA supports a creative decision rather than making a legally or similarly significant decision about a person.</u> **[CLARIFY]** Could a future client use MIRA outputs for hiring, eligibility, or assessment outside the documented purpose?

MIRA uses authenticated owner-scoped journeys and persistence. Its React/Vite client calls Express/tRPC services; model, image, storage, authentication, and optional provider integrations sit behind server-side boundaries. **[OBLIGATION]** Natural persons interact directly with model-generated questions and recommendations. **[OBLIGATION]** The system generates synthetic images and text. **[CLARIFY]** Does the active interface explicitly disclose AI interaction, and do exported images retain machine-readable provenance?

The repository identifies Forge-backed model/image services, optional OpenAI embeddings, S3-compatible storage, OAuth, a MySQL/TiDB database, and an optional Dakidarts birth-context integration for V3. **[OBLIGATION]** These services create processor/subprocessor and vendor-allocation questions. **[CLARIFY]** Which vendors receive production personal data, under what terms, in which locations, and for how long?

The system is currently private staging rather than public deployment. <u>Private staging affects readiness and exposure, but it does not by itself change the system's intended-purpose classification.</u> The system brief states that user review and refinement occur before final generation. **[OBLIGATION]** A production release still needs Article 50 disclosures and GDPR information, retention, deletion, and lawful-basis controls.

## Phase 2 — first-pass classification

| Question | Auditor answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | No evidence of manipulation causing significant harm, social scoring, prohibited biometric categorisation, untargeted facial scraping, prohibited emotion recognition, or another Article 5 practice. |
| Does this system operate in any of the eight Annex III areas? | No. Its intended purpose is creative direction and moodboard generation. |
| If Annex III: does it significantly influence decisions, or is it narrow/preparatory? | Not applicable on the documented intended purpose. Reassess if it is repurposed for a consequential Annex III decision. |
| Does it interact with end users or generate content requiring disclosure (Article 50)? | Yes. It directly converses with natural persons and produces synthetic text and images. |
| First-pass risk tier | **Limited risk / transparency** |
| One-sentence justification | MIRA is outside Article 5 and Annex III on its creative intended purpose, but Article 50(1) applies to direct AI interaction and Article 50(2) is relevant to machine-readable marking of synthetic outputs. |

Reference: [Regulation (EU) 2024/1689, Articles 5, 6, 50 and Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng).

## Phase 3 — clarifying-questions log

These questions were recorded in writing on 18 August 2026. Repository evidence supplied provisional answers; direct builder confirmation remains the preferred evidence.

| # | What I need to know | Why it matters | Provisional assumption without an answer |
|---|---|---|---|
| 1 | At the first model-generated interaction, is the user explicitly told that MIRA is an AI system? | Article 50(1) requires disclosure unless AI interaction is obvious to a reasonably informed user. | No sufficient disclosure: “Mira” and “private conversation” do not expressly identify AI. |
| 2 | Are final images and other synthetic outputs marked in a machine-readable, interoperable, robust, and reliable way, and is that provenance preserved on export? | Article 50(2) places a marking duty on providers of systems generating synthetic content. | No documented provenance control; vendor metadata may be absent or stripped. |
| 3 | Can MIRA depict an identifiable real person, place, or event so that the result could appear authentic? | This determines whether the deployer's deep-fake disclosure duty in Article 50(4) may apply in addition to provider marking. | Standard moodboards are fictional; if personal portraits are transformed, a case-by-case deep-fake check is required. |
| 4 | Which legal entity offers MIRA, which entity uses it for clients, and which model/image vendors process each data category? | Provider/deployer allocation and GDPR controller/processor contracts depend on the real production arrangement. | MIRA team is provider; the operating business is deployer; Forge/model/image/storage/auth services are vendors or processors. |
| 5 | What are the lawful basis, privacy notice, retention periods, deletion workflow, data locations, and special-category safeguards for conversations, birth details, uploads, inferences, and outputs? | GDPR Articles 5, 6, 9, 13/14, 17, 25, 28 and possibly 35 may apply. | These controls are not sufficiently evidenced; no production rollout should occur until documented and tested. |

## Evidence reviewed

- Teammate's `mira-system-brief.md` on the self-audit branch, used as the exchanged brief.
- MIRA `README.md`, `docs/MIRA_V4_CURRENT_STATE.md`, `docs/MIRA_TECHNICAL_HANDOFF_FOR_CODEX.md`, `docs/ENVIRONMENT_VARIABLES.md`, and relevant V4 client flow.
- V3 documentation only where the shared platform or optional personal-data pathways affect vendor and privacy boundaries.
- No self-audit risk classification, gap analysis, or memo was read until the provisional audit above had been completed.
