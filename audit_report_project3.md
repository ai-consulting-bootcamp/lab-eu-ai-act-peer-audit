# Project 3 Audit Report

Project: TestVet - https://github.com/Parisa-QA/Project-3
Author: Mudit Airan
Assessment: First-pass EU AI Act compliance audit

Scope note: This report is not a legal opinion, not a conformity assessment, and not a certification. Conclusions should be checked with legal counsel before any EU market placement.

## Project: TestVet

### Phase 1: System summary
TestVet is an autonomous QA tool evaluation agent. A user enters a QA tool name, an evaluation context, and optionally a GitHub repo URL or `owner/repo` slug. The workflow resolves the repo, pulls evidence from GitHub, News API, and Hacker News, then loads a local QA rubric and turns all of that into a structured report. It scores the tool against predefined criteria and produces an adoption recommendation. The output is meant to support human review rather than replace it.

The setup is clearer if you split it into plain pieces:
- Inputs: tool name, evaluation context, and optional GitHub repository reference.
- Outputs: evidence summary, criterion scores, and a recommendation.
- Human review: the report is advisory and meant to support a person or team making the final tool-selection decision.
- Who uses it: an internal team evaluating testing tools or a similar decision-making group.
- Personal data: not inherent to the design, although user-entered context could include names or other project details.

### Phase 2: First-pass classification

| Question | Your answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | No. |
| Does this system operate in any of the eight Annex III areas? | No. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | N/A. It is a QA tool-selection assistant, not a hiring, credit, law-enforcement, or similar Annex III decision system. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | Yes. The interface is user-facing, and Parisa says the system is AI-assisted but the disclosure is not yet explicit enough at first contact. |
| First-pass risk tier | Limited risk / transparency |
| One-sentence justification citing the specific article or Annex entry | The system is not in an Annex III area, but it is an AI-assisted user-facing evaluation agent, so the key issue is Article 50-style transparency rather than high-risk classification. |

Private note: Parisa’s clarification resolves the main ambiguity. The system is intended to be AI-assisted, but its use is limited to QA tool evaluation, not employment or other Annex III decisions.

### Phase 3: Clarifying questions log

1. Which AI component is used, and where is it called from?
   - Why it matters: the transparency wording should match the actual AI behavior, not just the marketing label.
   - Parisa’s answer: TestVet is AI-assisted. The exact model/provider is not documented here, but the system uses AI to research and evaluate QA tools.
   - Provisional assumption: The AI layer exists and supports the evaluation workflow, but the exact model/provider still needs to be documented.

2. Is TestVet only used internally, or is it offered to external users/customers?
   - Why it matters: deployment context affects transparency, documentation, and who carries the deployer obligations.
   - Parisa’s answer: It is a QA tool evaluation system, not a recruitment tool. The brief indicates it is used to help make QA tool adoption decisions.
   - Provisional assumption: It is an internal or team-facing evaluation tool.

3. Does the system store user inputs, API responses, or generated reports?
   - Why it matters: this affects privacy, retention, and security duties even if the AI Act scope stays limited.
   - Parisa’s answer: TestVet does not use a chat history or database. Inputs and collected results live temporarily in LangGraph workflow state, then the report is displayed in Gradio. Third-party services may still retain query or access logs.
   - Provisional assumption: TestVet itself does not persist them, but third-party logging may still exist.

### Role map

| Role | Who it is | Key obligations |
|---|---|---|
| Provider | The project team building and publishing TestVet | The provider should ensure the AI disclosure is visible at first contact, describe limitations, and keep the decision-support framing accurate. |
| Deployer | The team using TestVet to choose QA tools | The deployer should verify the recommendation is only advisory, not an automatic procurement decision, and should control what data users enter. |
| Third-party vendor | GitHub, News API, Hacker News/Algolia, Gradio, LangGraph, and any external model provider if one exists | These are data or infrastructure vendors unless one of them is actually providing the AI model. Their retention and logging terms still matter. |

### Phase 4: Compliance findings

**Finding 1 - First-contact AI disclosure is missing or under-specified**  
**Severity:** Significant  
**Description:** Parisa says the interface describes TestVet as an autonomous agent, but it does not explicitly tell users at first contact that the recommendations are AI-generated or may contain errors. For a user-facing AI-assisted evaluation tool, that is the main transparency gap.  
**Recommended action:** Add a visible first-contact disclosure such as: "TestVet uses AI to research and evaluate QA tools. Its recommendations are advisory and should be reviewed by a qualified person before making an adoption decision." Owner: product. Trigger: before external release. Escalation needed? No, unless legal wants to approve the final wording.

**Finding 2 - User-facing output should state that recommendations are advisory only**  
**Severity:** Minor  
**Description:** The output is a scored recommendation, but the interface does not currently make the advisory nature obvious enough. That creates a risk that users over-trust the result, even though the system is intended to support human judgment rather than replace it.  
**Recommended action:** Add a short note on the start page and results page that the output is a recommendation, not a final decision, and should be reviewed by a qualified person. Owner: product. Trigger: before external release. Escalation needed? No.

**Finding 3 - Data-handling and third-party retention are not documented**  
**Severity:** Minor  
**Description:** TestVet does not persist conversation history, but it does send search queries to GitHub, News API, and Hacker News through Algolia. Those third parties may retain logs or queries under their own policies, so the privacy and retention story is still incomplete.  
**Recommended action:** Document what is sent to each third-party service, what TestVet itself retains, and what users should avoid entering in the context field. Owner: privacy or engineering. Trigger: before production use. Escalation needed? Yes - privacy review if real user data or confidential project data is involved.

### Overall recommendation
Proceed with conditions. On Parisa’s clarification, TestVet is not a prohibited or Annex III system; it is a limited-risk, AI-assisted QA tool evaluation system. The blocker is not the use case itself, but the missing first-contact AI disclosure and the incomplete privacy/retention documentation. I would allow deployment only after those transparency and data-handling gaps are closed.

### Section 6: What this report is not
This report is not a legal opinion, not a conformity assessment, and not a certification. Conclusions should be verified with legal counsel before any EU market placement.

### Phase 5: Debrief conversation

1. **Auditor presents** — The audit concluded that TestVet is a limited-risk, AI-assisted QA tool evaluation system, not a recruitment or other Annex III decision system. The main concerns were the missing first-contact AI disclosure and the incomplete explanation of temporary data handling and third-party retention.

2. **Builder responds** — Parisa clarified that TestVet evaluates QA tools like Cypress or Playwright against predefined technical criteria and a local QA corpus. The system is advisory, not a decision-maker, and it does not store conversation history or use a persistent database; inputs and results only live temporarily in workflow state.

3. **Compare classifications** — Parisa’s self-audit tier and the external audit tier both land on limited risk / transparency. The difference was not about the regulation itself. It was mostly about whether the interface makes the AI role explicit enough at first contact and whether the documentation makes the temporary data flow clear.

4. **Compare gap lists** — Parisa’s main gaps were the missing visible disclosure and the need to warn users not to enter personal or confidential information. The external audit caught the same disclosure issue and added a separate privacy concern: third-party services may still retain query or access logs even if TestVet itself does not persist the data.

5. **Joint closing note** — Auditing your own work tends to normalize the system’s intended behavior, so it is easier to miss where the user-facing story is incomplete. An external audit is better at spotting what the interface actually communicates, where retention is undocumented, and where a user could reasonably misunderstand the system’s role.
