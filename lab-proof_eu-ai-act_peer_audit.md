# EU AI Act peer audit â€” Green Warehouse Network

**Auditor:** Sabrina Urriola 
**Builder / teammate:** Fatma Meray 
**Assessment date:** 24 November 2026  
**Evidence reviewed:** `Audit_eu-ai-act_system_brief.md`, `README.md`, and the project description supplied with the brief. The deployed interface and runtime outputs were not independently tested.

## Phase 1: Read and annotate

**Elements affecting classification:** The system plans warehouse networks in Germany; assigns primary and backup warehouses to customer records; optimizes cost/emissions; simulates failures; and is intended for logistics planners. A deterministic PuLP/CBC solver calculates assignments; an OpenAI model parses requests, explains results, and may write an HTML report. A planner reviews outputs; the system does not automatically change operations. These stated purposes do not appear to match an Article 5 prohibited practice or an Annex III category.

**Unclear / requiring clarification:** Whether customer records or coordinates can identify natural persons; whether the client or project team will deploy/brand the system; whether the chat visibly identifies itself as AI; whether AI-generated text is machine-readably marked; whether reports will be published; and whether the tool could be used for critical infrastructure safety or worker decisions. The brief describes an MVP, not a confirmed production deployment.

**Potential obligations:** AI interaction with planners (Article 50(1)); generated chat/report text (Article 50(2)); provider/deployer AI literacy (Article 4). GDPR may apply if customer names, precise locations, chat, or linked outputs identify natural persons.

## Phase 2: First-pass classification

| Question | Auditorâ€™s answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | **No apparent prohibited practice** for the stated warehouse-planning purpose. The brief describes optimization and scenario analysis, not a listed prohibited use. |
| Does this system operate in any of the eight Annex III areas? | **No on the stated purpose.** Warehouse planning is not itself an Annex III area. Annex III point 2 concerns AI intended as a safety component in management/operation of critical digital infrastructure, road traffic, or water, gas, heating, or electricity supply; none is described. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | **Not applicable on current facts.** The system may influence business planning, but no Annex III use has been identified. Human review alone would not exclude a future use from high-risk classification. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | **Potentially yes.** Natural-person planners use the AI-assisted chat; Article 50(1) notice should be assessed unless the interaction is obvious. LLM-written chat/report text should be assessed under Article 50(2), including feasibility and applicable exceptions. The brief does not evidence either control. |
| First-pass risk tier | **Limited risk / transparency obligations** (lab shorthand); not prohibited or Annex III high-risk on the stated intended purpose. |
| One-sentence justification citing the specific article or Annex entry | The stated warehouse-planning purpose does not fall within Article 5 or Annex III point 2, while the planner-facing AI chat and generated narrative require assessment under Article 50(1) and (2). |

The conclusion is provisional because actual intended purpose and interface behavior are not independently verified. Article 6 classification must be revisited if deployment adds a listed use or safety-critical function.

## Phase 3: Clarifying questions log

| What I need to know | Why it matters | Provisional assumption pending an answer |
|---|---|---|
| 1. Will the product ever be used to manage or operate safety functions in road traffic or critical digital infrastructure, or water/gas/heating/electricity supply? | Could bring it within Annex III point 2 and change the tier and obligations. | No: current brief describes ordinary warehouse-network planning only. |
| 2. Will assignments affect individual workers, sole traders, or a person's access to or price of an essential service? | Could change the Annex III/Article 6 analysis and raise significant individual-impact concerns. | No: customer-to-warehouse assignments are business planning outputs, reviewed by a planner. |
| 3. What exact notice appears in the chat before first use, and does it clearly identify interaction with AI? | Determines whether Article 50(1) is met or whether the interaction is obvious in context. | The brief does not evidence a notice; treat it as not confirmed. |
| 4. Which output fields are LLM-generated, and do chat responses/downloaded reports preserve machine-readable AI marking? | Determines Article 50(2) scope, feasibility, exceptions, and implementation status. | Narrative may be AI-generated; marking status is unknown. |
| 5. Who will place the integrated system into service, under whose name, and where will generated reports be distributed? | Establishes provider/deployer roles and whether further transparency duties or other laws apply. | Project team is likely provider if branded/placed under its name; client planners are likely deployers; reports remain internal. |

## Phase 4: Audit report

### Section 1: System summary

Green Warehouse Network helps logistics planners compare warehouse-network options in Germany. It uses customer and warehouse planning inputs to calculate primary and backup assignments, capacity, cost, emissions, distances, and failure scenarios. A deterministic optimizer calculates the plan, while an LLM supports natural-language requests, explanations, and an optional HTML report. A planner reviews results, and the brief says the system does not automatically change operations.

### Section 2: Risk classification

**First-pass tier: limited risk / Article 50 transparency; not high-risk on the stated purpose.** No Article 5 prohibited practice is apparent. General warehouse and supply-chain planning is not an Annex III category; Annex III point 2 is limited to specified critical infrastructure and road-traffic safety-component purposes, which the brief does not describe. Article 50(1) should be addressed for planner-facing AI interaction, and Article 50(2) should be assessed for synthetic text in chat and reports. Confirm the actual UI, generated fields, marking feasibility, and intended deployment. See the questions above.

### Section 3: Role map

| Role | Entity and obligations |
|---|---|
| **Provider â€” integrated system** | Likely the project team if it places the system into service or makes it available under its name. Address Article 4 AI-literacy measures and provider-side Article 50 obligations; high-risk provider duties are not indicated by the current classification. |
| **Deployer** | Likely the logistics organization whose planners use the tool professionally; no named client or live deployment is evidenced. Support Article 4 literacy and follow the intended-purpose instructions. Reassess if use changes. |
| **Model/API vendor** | OpenAI is identified for `gpt-4o-mini`. Its model-provider/GPAI obligations are a separate track and do not discharge the integrated-system provider's duties. Confirm the contracting entity and model/API configuration. |
| **Other vendors/components** | OpenRouteService and Climatiq provide distance/emissions data; Streamlit and LangGraph/LangChain support the app; PuLP/CBC performs deterministic optimization. The materials do not show these as separate AI-system providers for the stated functions. Revisit if a vendor AI feature is added. |

### Section 4: Compliance findings

> **Finding 1 â€” Article 50(1): notice of AI interaction**  
> **Severity:** Significant  
> **Description:** The system has a planner-facing chat with an LLM helper, but the brief does not establish that users are told they are interacting with AI or that this is obvious in the actual interface.  
> **Recommended action:** Inspect the chat entry point; add a clear AI-assistant notice before the first interaction unless the provider documents why the interaction is obvious in context.  
> **Escalation needed?** No, unless relying on the â€œobviousâ€ exception; then seek legal review.

> **Finding 2 â€” Article 50(2): machine-readable marking of generated text**  
> **Severity:** Significant  
> **Description:** The LLM explains results and may write an HTML report. The brief does not evidence machine-readable marking. The report appears to generate narrative, so an exception for standard editing or unaltered content is not established. Feasibility and any exception must be assessed.  
> **Recommended action:** Inventory generated text, select and test a machine-readable marking approach through chat and HTML download/export, and document feasibility and exception analysis. Confirm any transitional timing applicable to the systemâ€™s actual placement date.  
> **Escalation needed?** Yes â€” technical owner for implementation; legal reviewer for feasibility/exception and transitional timing.

> **Finding 3 â€” Article 4: AI literacy for relevant staff**  
> **Severity:** Minor  
> **Description:** Human review is described, but no staff AI-literacy measure is evidenced. Relevant provider/deployer staff should understand the AI and deterministic components, limits, and context of use.  
> **Recommended action:** Provide a short operator guide and onboarding covering LLM-generated content, solver status/warnings, input checks, and human responsibility for planning decisions.  
> **Escalation needed?** No â€” provider and deployer owners can implement and record this.

> **Finding 4 â€” Parallel privacy issue: personal data and vendor flows**  
> **Severity:** Minor (for the current course MVP; reassess before live data)  
> **Description:** Customer labels, precise locations, chat, or linked outputs may identify natural persons, but the brief does not verify this or document vendor retention/transfer details. This is a GDPR review item, not an AI Act risk-tier finding.  
> **Recommended action:** Validate sample fields, minimize/pseudonymize where feasible, and complete GDPR role, lawful-basis, transparency, retention, and transfer review before personal data is sent to vendors.  
> **Escalation needed?** Yes â€” privacy lead/DPO or counsel before production personal-data use.

### Section 5: Overall recommendation

**Proceed with conditions.** The course MVP has no apparent prohibited or Annex III high-risk purpose, but the brief does not verify Article 50 notices or marking on the actual interface and outputs. Before a production launch, inspect the chat/report, implement applicable Article 50 measures, and give relevant staff role-appropriate AI-literacy guidance. Reclassify if the intended purpose expands, and complete the parallel GDPR review before processing personal data.

### Section 6: What this report is not

This report is a provisional peer review of the supplied brief, not a legal opinion, conformity assessment, or certification. The UI and runtime outputs were not tested. Verify the facts and conclusions with qualified legal counsel before EU market placement or production use.

**Reference:** [Regulation (EU) 2024/1689 â€” EUR-Lex consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727); [European Commission: Navigating the AI Act](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act).

## Phase 5: Debrief conversation


1. **Auditor presents:** The provisional classification is limited risk / Article 50 transparency, not high-risk, because the described purpose is ordinary warehouse-network planning and does not match Article 5 or Annex III. The main open items are the first-use AI notice in the planner chat, machine-readable marking for LLM-written chat/report text, and Article 4 literacy measures. Confirm the intended use does not extend to critical-infrastructure safety or decisions about workers.

2. **Builder responds (simulated):** Fatma’s brief describes a course MVP with static planning data, a deterministic optimizer, and an LLM for request parsing, explanations, and optional report writing. A planner reviews the recommendations, and the tool does not change operations. No production client, deployed interface, notice, or generated-text marking is evidenced in the brief. The builder would therefore treat the transparency items as implementation checks before any production deployment, rather than claim that they are already satisfied.

3. **Compare classifications:** Fatma’s self-audit and this peer audit both place the stated system outside Article 5 and Annex III high-risk categories, with Article 50 transparency to address. This agrees with the auditor’s own procurement-risk mitigation agent audit: its advisory procurement use was also assessed outside Annex III, with Article 50 relevant to AI interaction and generated reports. The two systems differ in their data flows and outputs: the procurement agent uses supplier/news research and downstream report destinations, while Green Warehouse Network uses customer/site locations, optimization scenarios, and an optional HTML report. Those differences change the privacy and implementation questions, but do not change the stated AI Act tier.

4. **Compare gap lists:** Both audits identify Article 50 controls and AI literacy as follow-up actions. The peer review makes the evidence request more operational: inspect the actual first-use chat surface, identify which report fields are LLM-generated, and test whether marking survives HTML export. It also calls out the need to verify intended use and the separate GDPR question of whether customer labels or precise coordinates identify people. These are evidence and scoping refinements, not a disagreement about the current classification.

5. **Joint closing note:** “The self-audit benefits from detailed knowledge of how the system is built, but that familiarity can make undocumented assumptions feel settled. An independent review turns those assumptions into specific questions about user-facing notices, output marking, actual data flows, and evidence. Comparing the two projects also shows that similar risk tiers can still require different compliance work because their data and outputs differ.”

### Reinforce reflection 

The available record does not contain questions Fatma asked about the auditor’s own system, so the simulated debrief does not invent them. A useful question for this comparison is: “Which supplier/news details are retained or sent to the model in the procurement agent, and what controls prevent personal data from appearing in reports?” The auditor’s own brief and audit identified possible names/contact details in public search results, stored run files, downstream report copies, and vendor-location unknowns; those are more prominent GDPR questions than in Fatma’s static-data MVP.

No disagreement is recorded in the available audits: both assessments identify the same first-pass EU AI Act tier and Article 50/Article 4 topics. The simulated builder accepts the findings as open implementation/evidence checks because the brief does not demonstrate deployed controls. In a real debrief, replace this simulated account with Fatma’s actual response and note any disagreement that emerges.
## Stretch: Work plan for a Significant finding

**Finding selected:** Article 50(2) marking of LLM-generated chat/report text.

| Item | Work plan |
|---|---|
| Deliverable | A generated-content inventory, documented Article 50(2) applicability/feasibility and exception assessment, and tested implementation that marks applicable generated text in the chat and exported HTML. |
| Owner | Project technical lead implements; product owner inventories output surfaces; legal reviewer confirms applicability and exceptions. |
| Timeline | 1 week to inventory surfaces and agree the approach; 1â€“2 further weeks to implement and test, before production launch. Adjust to actual deployment and applicable transitional dates. |
| Closure evidence | Screenshots/sample chat and exported HTML showing the user-facing treatment; machine-readable inspection/test results; implementation notes; signed-off applicability/feasibility decision. |

