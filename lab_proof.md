# EU AI Act Peer Audit

**Auditor:** Sandra Obregón  
**Builder:** Jaime Garate Marquerie  
**Project:** Editorial Research Agent for Independent Bookshops

- [Audit report](./editorial_agent_peer_audit.pdf)
- [Code, run summary and saved final dossier](./editorial_agent_code_and_evidence.zip)
- [Project source code and run instructions at the reviewed commit](https://github.com/jaimegmarquerie-ui/proyecto3-agente-editorial/tree/3939562dec432c07f804a5412cf4a8c02dfdccd3)

## Phase 1 — Brief annotations

Source: Jaime's system brief. Short extracts are included here as evidence.

| Mark | Extract | Audit note |
|---|---|---|
| Underline | “She types a request” | The bookseller uses the tool directly. |
| Underline | “labels each book ‘useful’ or not” | The agent influences which titles the bookseller considers. |
| Underline | “does not order books, publish anything to customers or decide what the shop buys” | The intended use is internal support for stock selection. |
| Circle | “the software neither requires nor records that review” | The brief describes the intended human review. How it will work in the pilot is unclear. |
| Mark obligation | “a synopsis and genre written by Gemini” | Check whether the exported text has a machine-readable AI mark under Article 50(2). |
| Mark obligation | “her typed request is not filtered” | Check what personal data can reach vendors and logs, why it is needed and how long it is kept. |
| Circle | “a Catalan edition was labelled ‘Spanish edition verified’” | The builder reported a concrete verification error. Confirm whether it has been fixed and retested. |

## Phase 2 — First-pass classification

| Question | Assessment |
|---|---|
| Does Article 5 apply? | No prohibited use was identified. The system evaluates the fit of books with a shop profile. The brief does not describe scoring people on behaviour or personal traits. |
| Is the use in Annex III? | No listed use was identified. Selecting books for shop stock falls outside the Annex III purposes reviewed. |
| Does it significantly influence a decision in an Annex III area? | Not applicable. The shortlist influences what the bookseller sees, but the underlying stock-selection decision is outside the listed areas. |
| Does Article 50 apply? | The bookseller enters a request and gets a custom report. Under Article 50(1), check whether the use of AI is obvious at first interaction. Gemini drafts synopses and fit explanations, so check marking under Article 50(2) and whether it survives Markdown export. Article 50(4)'s public-interest text disclosure does not arise on the stated internal use. Reassess if the material is published with that purpose. |
| First-pass tier | **Limited risk / transparency**, provisional. |
| One-sentence justification | The agent supports internal book selection and produces generated text for the bookseller, making Article 50(1) and (2) relevant to the first-pass review. |

## Phase 3 — Written clarification log

Written responses received on 17 November 2026. The exact date the questions were sent was not recorded. Source: Jaime’s written response. The first-pass table above records the assessment before clarification.

| What I need to know | Why it matters | Provisional assumption |
|---|---|---|
| What does a new bookseller see when starting the tool? Can you share a screenshot of the startup text? | Whether an AI notice is needed under Article 50(1). | The brief does not confirm a startup notice. |
| What machine-readable AI mark, if any, is included in the report? Can you point to it in a sample? | What carries through to the final output under Article 50(2). | Human-facing headings are present. Machine-readable marking is unverified. |
| Which Gemini terms and data settings will apply in the pilot? Who can access the JSON logs, and when are they deleted? | Personal data could be sent in free-text queries and retrieved material or retained in logs. | The prototype uses the free tier. Pilot configuration and log retention remain unverified. |
| Who will release the agent under their name, and how will each shop check an edition before buying? | Confirms provider/deployer roles and whether the proposed review is practical. | Jaime releases it and each shop uses it professionally. Review is manual and is not recorded by the software. |

### Builder’s written answers and audit impact

| Question | What Jaime confirmed | Audit impact |
|---|---|---|
| 1. Startup notice | The terminal shows results and file paths. It has no AI notice. The README mentions AI. | The absence of an in-tool notice is confirmed. Add a clear notice when the tool starts. |
| 2. Output marking | The dossier displays the Gemini model and labels some interpretations. It has no machine-readable mark, and the generated synopsis has no clear label. Jaime also flagged the synopsis. | Add a visible label to generated sections and assess the technical marking required under Article 50(2). |
| 3. Gemini and logs | Pilot terms are undecided. The prototype uses the free tier. Logs have no application access controls or deletion rule, and 20 test logs are public on GitHub. Jaime plans to use a paid plan for the pilot. | Check the pilot terms and data settings before use. Review the public logs, restrict access to future logs and set a retention rule. |
| 4. Roles and edition review | Jaime plans to release the agent under his own name and use it in his own shop. Other pilot shops would use it professionally. The bookseller checks language, availability and price manually. There is no checklist. | Jaime would be both provider and deployer for his own shop. Other shops would be deployers. Add an edition checklist and test the language check with a Catalan edition. |

**Assessment after clarification.** Limited risk / transparency remains the working tier. The recommendation is **Proceed with conditions**. The answers confirm control gaps and clarify roles. The joint debrief is still pending.

## Phase 4 — Audit report

See the [audit report](./editorial_agent_peer_audit.pdf) for the six required sections and conditions for the pilot.

## Phase 5 — Debrief

**Written debrief, 17 November 2026.** Jaime reviewed my report and shared his self-audit findings.

| Topic | Comparison and outcome |
|---|---|
| Risk tier | I assessed the agent as **Limited risk / transparency**, provisional. Jaime assessed it as **Minimal risk**, with an open question under Article 50(2). I flagged first-use transparency because the bookseller interacts directly with the tool. Jaime considers AI use obvious to the bookseller, who runs the tool herself. We both flagged marking AI-written synopses for review under Article 50(2). Jaime added the startup notice to his plan. |
| Findings and recommendation | Jaime agreed with all three findings and **Proceed with conditions**: improve AI transparency, confirm vendor settings and log controls, and fix and retest edition verification. He questioned whether the model vendor needs to join the marking review. Legal review remains a proposed next step. |
| Additional points from the self-audit | Jaime reported publisher text in public logs and public author information sent to Gemini. He also found no record of the bookseller's decision, no measured accuracy for the judge, no test for hidden instructions in source pages, and no user guide. He raised a possible restriction on using the Gemini free tier for an EEA pilot. Verify the applicable terms before choosing the pilot setup. |
| System-summary clarification | Gemini judges each book and drafts its synopsis. The application fills the dossier from a template. |

### Joint closing note

We agreed that the pilot should proceed only after the three findings are addressed. We differed on whether the bookseller would already know the tool uses AI, but both flagged the marking of AI-written synopses for review. Comparing our audits also showed why we need to check what is sent to the model, what stays in public logs, and how the bookseller's decision is recorded.

**Joint confirmation:** Sandra confirmed that she and Jaime agreed on this wording.

## Run and evidence

**Existing recorded run, 13 November 2026.** Query: `libros escritos por Leila Guerriero`. Author: `Leila Guerriero`. Bookshop profile: `La Insumisa`.

- [JSON evidence](https://github.com/jaimegmarquerie-ui/proyecto3-agente-editorial/blob/3939562dec432c07f804a5412cf4a8c02dfdccd3/evidence/editorial_20261113_093326_829f47ae.json) records five books, five judgements, three judge attempts and no failed tools.
- [Final dossier](https://github.com/jaimegmarquerie-ui/proyecto3-agente-editorial/blob/3939562dec432c07f804a5412cf4a8c02dfdccd3/samples/dossier_20261113_433af978.md) reports a catalogue discrepancy for *Teoría de la gravedad*: 206 pages in Open Library and 224 in Google Books. This evidence shows a discrepancy was captured, and leaves the correct page count to review.
- **Known failure, separate from this recorded run.** The builder's brief reports that a Catalan edition was labelled “Spanish edition verified.” The brief does not identify which run produced it. No fresh run was performed for this audit.

## Regulatory references

- [EU AI Act, Articles 3, 5, 50 and 53 and Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- [GDPR, Articles 5 and 6](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
