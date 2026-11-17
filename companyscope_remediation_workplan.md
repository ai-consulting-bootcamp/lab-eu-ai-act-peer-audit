# CompanyScope stretch work plan: close Article 50 and review-gate gaps

**Owner:** Sean / CompanyScope system owner, with legal/privacy review<br>
**Priority:** Significant<br>
**Target:** before any public or paid deployment

## Deliverable

An approved transparency-and-review package containing: (1) an Article 50 assessment; (2) a first-interaction AI notice; (3) machine-readable/detectable marking for generated Markdown and HTML; (4) a publication rule for public-interest text; (5) a mandatory source-verification and reviewer sign-off step; and (6) an updated user standard prohibiting consequential Annex III uses unless separately assessed.

## Responsibility and timeline

- **Week 1:** Sean inventories the model, workflow, output formats, deployment surfaces, and all points where a report can be exported or shared.
- **Week 2:** Engineer implements the notice, output marker, review gate, and refusal/stop state for unresolved entity matches.
- **Week 3:** Privacy/legal reviewer checks Article 50(1), (2), and (4), the intended-purpose boundary, and any applicable German professional obligations.
- **Week 4:** Run acceptance tests with ambiguous entities, unsupported claims, personal-data inputs, and attempted external publication; approve or defer launch.

## Closure evidence

Screenshots and test logs for each interface, representative marked outputs, the signed Article 50/use-purpose assessment, reviewer checklist and completed sample reports, training record, model/workflow version record, and legal/privacy sign-off. A gap remains open if the system can export an unmarked report or bypass human verification.
