# LAB | Audit your teammate's project

## First-pass classification 

*The answers are a preliminary read of those stated facts against the EU AI Act—not a legal determination. They could change if the system is used differently or more details emerge.*

| Question | Answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | No prohibited practice is described in v2. The brief does not describe social scoring or workplace emotion recognition; confirm that no such functions exist in the implemented system. |
| Does this system operate in any of the eight Annex III areas? | No Annex III use is described. It advises staff on process problems; it is not described as monitoring/evaluating worker performance or making employment decisions. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | Not applicable on the stated purpose. Confirm that recommendations are not used to make or materially influence employment decisions under Annex III, point 4. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | Yes. Employees interact with it, and the report is labelled AI-generated, which is relevant to Article 50(1); confirm the notice is provided at the required point. Because it generates text, assess Article 50(2)'s machine-readable marking duty and its exceptions; the brief does not establish whether the report label meets that technical duty. The described internal use does not indicate the deepfake or public-interest publication disclosures in Article 50(4)–(5). |
| First-pass risk tier | Limited risk / transparency obligations, based on the brief; not prohibited or high-risk on the facts provided. |
| One-sentence justification citing the specific article or Annex entry | On the stated purpose, the system supports process improvement rather than employment decisions in Annex III, point 4, and no Article 5 practice is described; its employee interaction and generated text make Article 50(1) and (2) transparency duties relevant. |

## Clarifying questions log

1. **Does the system infer emotions from biometric data in the workplace, or evaluate or score workers across contexts?**
   - **What I need to know:** Whether it performs workplace emotion recognition or creates scores that evaluate people across contexts.
   - **Why it matters:** Certain workplace emotion-recognition and social-scoring practices are prohibited by Article 5, subject to the Act's specific scope and exceptions.
   - **Provisional assumption:** No; it assesses proposed AI use cases and workflow problems, not employees.

2. **Are its recommendations used to recruit, promote, terminate, monitor or evaluate workers, or allocate tasks based on an individual's behavior or personal traits?**
   - **What I need to know:** Whether the tool or its outputs inform employment decisions or assess/monitor worker performance or behavior.
   - **Why it matters:** Such intended uses may fall under Annex III, point 4; the exact purpose and effect on people determine whether the high-risk rules apply.
   - **Provisional assumption:** No; it recommends process fixes and tools, without evaluating or making decisions about workers.

3. **What evidence validates the green/amber/red flags and the High/Medium/Low confidence percentages, and what should users do when a result is uncertain or wrong?**
   - **What I need to know:** Evaluation results, confidence calibration, escalation thresholds, and a correction or appeal route for employees.
   - **Why it matters:** The employee receives the report before any Board review and may act on it; unsupported compliance ratings could mislead users and weaken the system's claimed safeguards.
   - **Provisional assumption:** The flags and confidence scores are advisory outputs; no independent validation or correction process is established in the brief.

4. **Does the employee see an AI notice before or at the start of the interaction, and are generated reports technically marked in a machine-readable way?**
   - **What I need to know:** The notice's wording and timing, how the AI-generated label is implemented, and whether the output carries a detectable machine-readable marker.
   - **Why it matters:** Article 50(1) covers informing people that they are interacting with AI; Article 50(2) separately addresses machine-readable marking of synthetic text, subject to specified exceptions.
   - **Provisional assumption:** The report label is visible to employees, but its timing and technical marking are unverified; the tool is used internally, not to publish public-interest text or create deepfakes.

## Audit report

**Scope and evidence basis — 17 November 2026.** This is a preliminary peer audit based on *Fix My Process Systembrief_v2.md* and the clarifying-question log only. The prototype is not currently used by Kleinanzeigen, and the four internal documents are fictional; conclusions should be rechecked against the implemented design and vendor contracts.

### Section 1: System summary

Fix My Process is a prototype intended to help employees get practical fixes for slow or manual work tasks using company-approved tools. It takes department and problem details, searches external sources and four fictional internal documents, and generates an employee-facing fix and a summary for the AI enablement team. It also assigns a green/amber/red policy flag and a confidence score; employees receive the AI-labelled report before review, green cases are not reviewed, amber cases are shared for information, and red cases go to the Board afterward. The brief names the connected model, search, storage, workflow, messaging, and hosting services, but does not detail each service's data flows or safeguards.

### Section 2: Risk classification

**First-pass tier: Limited risk / transparency obligations; not prohibited or high-risk on the stated facts.** The stated purpose is internal process improvement, not a decision about a natural person in an Annex III area such as employment (Annex III, point 4), and no Article 5 practice is described. The employee-facing report is labelled AI-generated, but verify that the Article 50(1) notice is given at the appropriate time. Since the system generates text, assess Article 50(2)'s machine-readable marking duty and whether an exception applies; a visible label alone does not establish technical marking. Article 4 AI-literacy measures also apply to staff operating or using AI systems. Confirm the system is not repurposed for worker assessment or employment decisions. [EU AI Act, Articles 4 and 50](https://eur-lex.europa.eu/eli/reg/2024/1689)

### Section 3: Role map

| Role | Party on current facts | Key obligations / implications |
|---|---|---|
| Provider | Ayhan Demir built the prototype alone. The legal provider for any future market placement or deployment is not established by the brief. | Confirm which person or entity places the system on the market or puts it into service, and assign applicable provider responsibilities. In particular, verify Article 50(1) user information and Article 50(2) output marking. |
| Deployer | No current deployer: the brief says Kleinanzeigen does not use the prototype. If adopted, Kleinanzeigen would likely deploy it for internal work. | Define operational ownership and AI-literacy measures under Article 4; preserve applicable transparency information and use the system within the stated purpose. Do not treat its flags as independently validated approvals. |
| Third-party vendors | The brief names OpenAI (language model), Cohere (ranking), Pinecone (document search), Tavily, GNews and OpenAlex (research), Airtable (case records), Notion (summaries), Slack (reviews/alerts), n8n (workflow), and Gradio/Render (interface/hosting). | Map which data each service receives, processing locations, retention, access, and contractual terms; verify security, deletion, secondary-use, and international-transfer safeguards. The brief names services but does not establish these controls or where processing occurs. |

### Section 4: Compliance findings

> **Finding 1 — Article 50 user transparency is not fully evidenced**
>
> **Severity:** Significant  
>
> **Description:** Employees receive the report labelled AI-generated, which is evidence of a disclosure. The brief does not show whether employees are informed at or before the interaction as Article 50(1) requires, or whether the generated text has the machine-readable marking addressed by Article 50(2).
>
> **Recommended action:** Verify the timing and clarity of the Article 50(1) notice and test the output for Article 50(2) marking, documenting whether an exception applies.
>
> **Escalation needed?** Yes — to the AI governance owner and legal/privacy counsel.

> **Finding 2 — Personal-data and international-transfer exposure is unassessed**
>
> **Severity:** Significant  
>
> **Description:** Free text may contain names, no login is requested, and the system connects to external AI, search, storage, and hosting services. The brief does not map which data goes to each vendor, processing locations, access controls, retention, processor terms, lawful basis, or transfer safeguards. These are principally GDPR/security questions and cannot be resolved from the brief.
>
> **Recommended action:** Minimise or redact personal data before external calls; map data flows, vendor locations, and access; set retention/deletion rules; and complete privacy and transfer assessments with the DPO before deployment.
>
> **Escalation needed?** Yes — to the DPO/privacy counsel and information-security owner.

> **Finding 3 — Compliance ratings and confidence scores lack documented validation**
>
> **Severity:** Significant  
>
> **Description:** Employees receive reports before any review; green cases receive no review, amber cases are shared for information, and the Board reviews red cases afterward. The brief gives no evidence validating the flags or confidence percentages. An employee could act on an incorrect green rating, although the described purpose does not itself make this a high-risk employment system.
>
> **Recommended action:** Keep ratings clearly advisory, substantiate confidence scores with representative evaluation, set escalation criteria for uncertainty or policy-sensitive cases, and provide a correction route. Consider review before action where the recommendation could create material policy or privacy consequences.
>
> **Escalation needed?** Yes — to the AI Governance Board and policy owner.

> **Finding 4 — Provider/deployer accountability and vendor data flows are undocumented**
>
> **Severity:** Significant  
>
> **Description:** The brief identifies the builder and connected services, but not the legal provider for future use, data flows, processing locations, or allocation of incident and monitoring responsibilities. Without these details, applicable duties and data-protection controls cannot be verified.
>
> **Recommended action:** Create a system record naming the provider/deployer, intended purpose, model/version, data flow per vendor, owners, retention, and escalation route; obtain and review written vendor terms.
>
> **Escalation needed?** Yes — to procurement, legal/privacy, security, and the AI Governance Board.

> **Finding 5 — Prohibited and employment-use boundary is not technically enforced**
>
> **Severity:** Minor  
>
> **Description:** The brief describes process-improvement advice and says no applicants or members of the public are involved; it does not describe worker assessment or an Article 5 practice. However, open-ended employee submissions could raise employment-related use cases, and the brief does not explicitly rule out every form of worker monitoring, scoring, task allocation, or evaluation.
>
> **Recommended action:** Encode and test use-case exclusions, add user-facing warnings, require Board review for employment-related proposals, and reclassify before any such use.
>
> **Escalation needed?** No — unless a prohibited or employment-related use is proposed; then escalate to legal counsel and the Board.

### Section 5: Overall recommendation

**Proceed with conditions.** No prohibited or high-risk use is evidenced in v2, but before deployment the team should verify Article 50(1) notice timing and Article 50(2) marking, confirm provider/deployer accountability, map vendor data flows and safeguards, and validate the compliance flags and confidence scores. Keep the system advisory and outside employment decisions; any change to that boundary requires a fresh risk classification and legal review.

### Section 6: What this report is not

This report is not a legal opinion, conformity assessment, or certification. It is a preliminary evidence-based peer review and does not establish compliance with the EU AI Act, GDPR, employment law, or security requirements. Conclusions should be verified with qualified legal counsel before any EU market placement or operational deployment.
