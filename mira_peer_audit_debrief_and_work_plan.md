# MIRA peer-audit debrief and remediation work plan

**Auditor:** Paola Hintze  
**Builder:** Maria Cavali (`mariacavali`)  
**Debrief evidence reviewed:** MIRA self-audit branch `eu-ai-act-self-audit`, opened only after the independent provisional audit was completed.

## Phase 5 — debrief record

### 1. Auditor presents

The auditor classified MIRA as **limited risk / transparency**. The main findings were: missing explicit Article 50(1) interaction disclosure; no evidenced Article 50(2) machine-readable provenance for synthetic output; incomplete GDPR governance for conversations, birth details, uploads, and inferred profiles; incomplete production role/vendor allocation; and a minor need for intended-use controls.

### 2. Builder responds

Maria confirmed that her audit classified MIRA as **Limited risk / transparency** with **Proceed with conditions**. Her main findings were AI transparency and provenance, GDPR and data retention, the production security boundary, and making human review auditable.

**Builder response received:** 18 August 2026.

### 3. Compare classifications

| Assessment | Tier | Reason |
|---|---|---|
| Builder self-audit | Limited risk / transparency | Creative tool outside Article 5 and Annex III; direct interaction and generated visuals make Article 50 relevant. |
| Independent peer audit | Limited risk / transparency | Same classification; Article 50(1) and 50(2) require separate controls. |

There is no tier disagreement. Both reviews rely on MIRA's documented creative intended purpose and absence of Annex III decision-making. Both also recognise that private staging does not eliminate future production obligations.

### 4. Compare gap lists

| Area | Agreement or difference |
|---|---|
| AI interaction notice | Agreement: both identify a missing clear notice before user interaction. |
| Generated-output disclosure | Agreement on the gap. The peer audit adds legal precision: Article 50(2) focuses on machine-readable marking; a visible label alone is good practice but may not satisfy that technical duty. |
| Privacy and retention | Agreement. The peer audit expands the gap to lawful basis, processor terms, deletion across vendors/backups, special-category spillover, and DPIA screening. |
| Provider/deployer mapping | Agreement. The peer audit distinguishes AI-component providers from ordinary infrastructure processors and asks for named legal entities. |
| Production security boundary | The builder's audit makes this an explicit finding. The peer audit addresses it through production vendor allocation, processor contracts, data flows, and security ownership; the debrief confirms that the boundary must be documented and tested before external deployment. |
| Human review | Agreement that selection/refinement gates are valuable. The builder adds that review must be auditable; the peer audit clarifies that human review does not determine the risk tier, because intended purpose does. Closure evidence should therefore include reviewer actions, approvals, overrides, and retained logs. |
| Acceptable use/reclassification | Mainly external-audit addition: document prohibited repurposing and re-run the assessment when use cases change. |

### 5. Joint closing note

Comparing the two audits showed that the core conclusion was consistent: both reviewers classified MIRA as limited risk / transparency and recommended proceeding only with conditions. The self-audit contributed deeper implementation context, particularly around the production security boundary and auditable human review, while the external audit sharpened the evidence needed for transparency, provenance, privacy, and role allocation. Together, the exercise showed that self-audit explains how safeguards were intended to work, whereas peer audit tests whether those safeguards are sufficiently documented and verifiable.

**Joint acceptance required before submission:**

- [x] Paola confirms this note reflects the auditor's view.
- [ ] Maria confirms this note reflects the builder's view.
- [ ] Any corrections from the live conversation are recorded below.

**Corrections / additional context:** _None recorded yet._

## Stretch — work plan for a significant finding

### Gap selected

Article 50 transparency and synthetic-output provenance.

### Deliverable that closes the gap

An **AI Transparency and Output Provenance Release Pack** containing:

1. approved Article 50(1) user notice and screenshots showing it before first AI interaction;
2. an output inventory identifying generated text and image types;
3. a technical design for machine-readable marking under Article 50(2), including vendor capability and export preservation;
4. visible-label rules for generated images and any deep-fake/public-interest cases;
5. automated and manual test evidence across creation, refinement, download, and sharing; and
6. a legal sign-off record describing any relied-upon exception.

### Responsibility

| Owner | Responsibility |
|---|---|
| Product lead | Notice placement, output inventory, acceptance criteria |
| Engineering lead | Provenance implementation and preservation tests |
| Design/content | Clear and accessible disclosure copy |
| Vendor/procurement owner | Confirm model/image-provider marking capabilities and contract terms |
| EU legal/privacy reviewer | Validate Article 50 interpretation and related GDPR notice language |

### Timeline

**Three weeks:** Week 1 for inventory, vendor confirmation, and legal requirements; Week 2 for implementation and copy; Week 3 for end-to-end tests, remediation, and sign-off. If the image provider cannot support adequate provenance, external release remains paused until an alternative control or provider is approved.

### Closure evidence

The gap is closed only when the notice is visible and tested before first interaction; representative text and image outputs retain the approved machine-readable signal after download; automated tests detect regressions; vendor evidence is filed; legal signs off; and the release checklist links to all evidence.
