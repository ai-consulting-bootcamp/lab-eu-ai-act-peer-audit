# CompanyScope: Phase 1 evidence annotations

**Auditor:** independent peer reviewer<br>
**Brief reviewed:** `companyscope_system_brief.md`<br>
**Annotation date:** 17 November 2026

This is the second-pass annotation record. It uses the following marks:

- **UNDERLINE — tier factor:** a fact that affects prohibited/high-risk/limited-risk classification.
- **CIRCLE — ambiguity:** a fact that needs client clarification before the conclusion can be final.
- **OBLIGATION — obligation signal:** a fact that points to an AI Act or parallel-law control.
- **GAP — control weakness:** a control that is described as absent, advisory, or not evidenced.

## Annotated evidence

1. **UNDERLINE — tier factor:** “for law-firm staff, in-house legal teams and business researchers preparing for a meeting or an initial counterparty review.” This is a legal/business research context, but it is not stated to be a tool for a judicial authority, employer, lender, insurer, public authority, or critical-infrastructure operator.

2. **UNDERLINE — tier factor:** “It does not decide whether to hire someone, grant credit, accept a client or approve a transaction.” This is a strong intended-purpose boundary: the output is preparatory research rather than a decision or recommendation that determines an individual's access to employment, credit, essential services, or a legal proceeding.

3. **OBLIGATION — human-control signal:** “If the evidence does not identify one match, it stops rather than picking one automatically.” This reduces false-entity matching risk and supports a human operator's control over an important research step.

4. **CIRCLE — ambiguity:** “Once it has a match” does not say who confirms the match, what evidence threshold is used, or whether the operator can inspect all candidate matches before the model receives data. Clarify the confirmation workflow and audit trail.

5. **OBLIGATION — data-protection signal:** “Public websites may nevertheless contain names, professional contact details or other information about identifiable people.” These are potentially personal data. The brief does not identify the controller, lawful basis, notices, retention, data-subject handling, or vendor locations.

6. **OBLIGATION — confidentiality signal:** “The search query can also reveal which company a user or firm is researching.” A query may disclose confidential client or matter information to the search provider even where the company name is not personal data.

7. **OBLIGATION — model-use signal:** “The OpenAI model receives selected registry and web evidence plus those notes.” This confirms a third-party model service is in the processing chain, but the model/version, account, region, retention, training settings, and contractual role are not stated.

8. **OBLIGATION — output signal:** “The output is a Markdown report and, for browser submissions, a styled results page.” The system creates synthetic text and presents it directly to browser users. This raises Article 50(1) notice and Article 50(2) machine-readable output-marking questions.

9. **GAP — accuracy control:** “Those checks do not prove that a cited source supports the claim or that the findings are complete.” This is an explicit limitation in a workflow whose reports may affect companies and named people.

10. **OBLIGATION — human oversight signal:** “A future professional operator would check the registered entity, open the sources, distinguish verified facts from model inferences and correct or omit unsupported statements.” This is a sensible operating control, but it is described as a future operator practice rather than an enforced product control.

11. **GAP — governance:** “The published workflow advises professional review but does not enforce sign-off.” The brief does not establish a mandatory reviewer, a record of review, a publication gate, an incident route, or a restriction against using the report as an automated decision.

12. **UNDERLINE — impact factor:** “The organizations described are directly affected by errors. Named individuals may also be affected if a claim concerns them or is repeated outside the research team.” This increases the severity of unsupported claims and makes privacy, accuracy, correction, confidentiality, and disclosure controls material even though the system is not currently high-risk under Annex III.

## Initial evidence conclusion

The brief supports a provisional **limited risk / transparency** classification. The main unresolved classification issue is not what the prototype currently claims to do, but whether real deployers will use it in an Annex III decision context or publish its generated text for a public-interest audience. Those uses must be ruled out or separately assessed before commercial deployment.
