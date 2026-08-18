# Independent EU AI Act peer audit — MIRA

**Auditor:** Paola Hintze · **Teammate:** Maria Cavali (`mariacavali`) · **Date:** 18 August 2026

## 1. System summary

MIRA is an authenticated, owner-scoped creative-direction application. Its V4 journey collects brand and project context, creative preferences, conversational responses, optional inspiration, and birth details; it generates Creative DNA, campaign structure, visual directions, and a five-image moodboard. The user selects and refines a direction before final generation. MIRA therefore supports creative exploration and does not, on the documented intended purpose, decide access to employment, education, credit, essential services, justice, or another consequential domain.

## 2. Risk classification

**First-pass tier: limited risk / transparency.** No documented feature falls within the prohibited practices in Article 5 or the high-risk systems in Article 6 and Annex III. Human approval strengthens control but is not the reason MIRA is outside Annex III; the decisive point is its creative intended purpose. Article 50 is relevant because users interact directly with an AI system and MIRA generates synthetic text and images. Under Article 50(1), the AI interaction must be disclosed unless obvious. Under Article 50(2), synthetic outputs require machine-readable marking, subject to the provision's technical and editing exceptions. Article 50(4) would additionally matter if output qualifies as a deep fake or if AI-generated public-interest text is published. The main uncertainty is how the system and outputs will be offered and reused in production.

## 3. Role map

| Role | Provisional entity | Key duties relevant here |
|---|---|---|
| Provider | MIRA product team / legal entity placing the configured application on the EU market under its name | Article 50 interaction disclosure and synthetic-output marking; instructions and technical/vendor documentation appropriate to the system; AI-literacy measures under Article 4. |
| Deployer | MIRA operating business and, depending on the contract, a professional client using it with end users | Use according to instructions; deliver any Article 50(4) deep-fake/public-interest disclosure; apply human review and internal acceptable-use controls. |
| AI-component vendors | Forge/model and image-generation services; optional OpenAI embeddings; optional Dakidarts context service | Their separate status depends on the supplied component and contract; document capabilities, provenance support, limitations, and data use. |
| Other processors | OAuth/authentication, S3-compatible storage, MySQL/TiDB hosting and infrastructure services | Primarily GDPR/security contractual duties rather than independent AI-provider duties. |

## 4. Compliance findings

> **Finding 1 — Direct-interaction disclosure**  
> **Severity:** Significant  
> **Description:** Article 50(1) requires users to be informed that they are interacting with AI unless this is obvious. The reviewed flow uses phrases such as “Mira” and “private conversation,” but the evidence does not show a clear, timely AI notice at first interaction.  
> **Recommended action:** Add a concise pre-interaction notice: “You are interacting with an AI-assisted creative-direction system. It can make mistakes; review all outputs before use.” Record the approved copy, placement, language versions, and UI test.  
> **Escalation needed?** Yes — product owner and EU legal/compliance.

> **Finding 2 — Synthetic-output provenance**  
> **Severity:** Significant  
> **Description:** Article 50(2) requires providers of systems generating synthetic text, audio, images, or video to mark outputs in a machine-readable and detectable manner. The repository documents image generation, but not a provenance specification or export-preservation test. A visible “AI-generated” label is useful, but it does not replace the technical marking duty.  
> **Recommended action:** Confirm vendor support; implement and test durable metadata/content credentials or another applicable state-of-the-art marking method; preserve it through download and document exceptions. Add a visible label as user-centred good practice.  
> **Escalation needed?** Yes — engineering, vendor manager, and legal.

> **Finding 3 — Privacy governance for personal inputs and inferred profiles**  
> **Severity:** Significant  
> **Description:** MIRA processes account data, conversations, birth details, inspiration images, preferences, generated inferences, and outputs. Image consent controls exist in V3, but the reviewed materials do not evidence a complete production privacy notice, lawful-basis map, retention schedule, data-subject deletion/export workflow, processor contracts, or DPIA screening. Free-text conversations may reveal special-category data even when MIRA does not request it.  
> **Recommended action:** Create a data inventory and purpose/lawful-basis matrix; minimize optional fields; define retention and verified deletion across backups/vendors; complete processor/subprocessor reviews; screen for a DPIA; and add a route for access, correction, deletion, and withdrawal where consent is used.  
> **Escalation needed?** Yes — privacy counsel/DPO and security lead.

> **Finding 4 — Production role and vendor allocation**  
> **Severity:** Significant  
> **Description:** The technical boundary lists model, image, storage, authentication, database, embedding, and optional birth-context services, but production contracts and responsibility allocation are not evidenced. Calling every third party an “AI provider” would be inaccurate; some are processors only.  
> **Recommended action:** Approve a provider/deployer/controller/processor matrix, name the production legal entities, maintain a vendor register and data-flow diagram, and make provenance, incident support, deletion, and model-data-use terms contractual acceptance criteria.  
> **Escalation needed?** Yes — legal, procurement, privacy, and product.

> **Finding 5 — Scope control and user reliance**  
> **Severity:** Minor  
> **Description:** MIRA states that its outputs are creative rather than diagnostic or consequential, but a formal acceptable-use boundary and release test are not evidenced for V4. Brand recommendations may still be over-relied upon or repurposed.  
> **Recommended action:** Publish intended-use and prohibited-use statements, keep confirmation/refinement gates, provide correction/regeneration controls, and re-run classification when features or customer use cases change.  
> **Escalation needed?** No, unless a proposed use enters a regulated or Annex III domain.

## 5. Overall recommendation

**Proceed with conditions.** Controlled private testing may continue, but external or client-facing EU deployment should wait until Findings 1–4 have owners and verifiable closure evidence. Minimum release conditions are: a tested Article 50(1) notice, a documented and tested Article 50(2) provenance mechanism, an approved privacy/retention/deletion package, and a signed production role/vendor matrix. No conformity assessment is indicated on the current limited-risk classification.

## 6. What this report is not

This report is not a legal opinion, conformity assessment, or certification. It is a first-pass educational review based on the available brief and repository evidence. Conclusions should be verified with qualified legal counsel before placing the system on the EU market or putting it into service.

**Legal source:** [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng).
