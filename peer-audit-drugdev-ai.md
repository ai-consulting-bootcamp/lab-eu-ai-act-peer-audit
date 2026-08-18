# Peer Audit: DrugDev-AI (Nevena's Project)

**Auditor:** Zahra Moghaddasi
**System audited:** [DrugDev-AI](https://github.com/nevena-mi/DrugDev-AI), Nevena's Ironhack AI Consulting Bootcamp capstone project
**Source material:**
1. Nevena's own system brief, "System Brief – DrugDev-AI.md," pulled from her self-audit lab submission ([PR #9](https://github.com/ai-consulting-bootcamp/lab-eu-ai-act-self-audit/pull/9), commit `b77b34a`), quoted in full below.
2. Technical documentation from the public repository (`README.md`, `project_plan.md`, `AGENT.md`, and source files `src/app.py`, `src/monitor.py`), reviewed 2026-08-18.

**Ground-rule note:** The same PR also contains `DrugDevAI_audit.md`, which is Nevena's own self-audit findings (risk tier, gap analysis, compliance memo). I did not open that file. Per the lab's ground rules, only the system brief should be exchanged before Phase 5, so I kept this audit independent and worked from the brief plus public technical docs only.

### System brief (verbatim)

> **DrugDev-AI System Overview**
>
> DrugDev-AI is an educational AI assistant for pharmaceutical professionals. The system operates in three modes: Ask (answers questions using regulatory documents), Learn (provides structured lessons and quizzes), and Monitor (tracks updates from ClinicalTrials.gov, EMA, and openFDA).
>
> **Key characteristics:** The platform accepts natural language queries and user background information to personalize content. It draws from "a curated knowledge base built from publicly available regulatory documents issued by organizations including the EMA, FDA, ICH, WHO, and the European Commission."
>
> Output consists of explanatory text, cited answers, AI-generated educational material, quizzes, and regulatory summaries. Importantly, the system "does not produce scores about people, approve or reject applications, rank individuals, or make automated decisions that directly affect legal rights."
>
> **Intended audience** includes regulatory specialists, clinical researchers, quality assurance staff, students, and industry professionals, not patients or the general public making healthcare decisions.
>
> **Human oversight** remains central: "All outputs produced by DrugDev-AI are reviewed by the user before any action is taken." Users must verify information against original sources and retain responsibility for application decisions.
>
> The system was developed as a bootcamp project integrating OpenAI, Cohere, and Pinecone services with public regulatory data for potential deployment by pharmaceutical organizations or training providers.

---

## CFU 1: Recognize

First-pass risk tier, from the brief alone: **Limited risk, transparency obligations.** DrugDev-AI does not fall under any Article 5 prohibited practice, no manipulation, exploitation, social scoring, or biometric identification is present. It also does not appear to sit inside an Annex III high-risk area: the brief states directly that it "does not produce scores about people, approve or reject applications, rank individuals, or make automated decisions that directly affect legal rights," and its audience is professionals rather than patients or the general public. That rules out the closest candidate, Annex III(3)(b) on evaluating learning outcomes, since Learn mode's quizzes read as informal and non-binding by the brief's own description. What does apply is **Article 50(1)**: the system interacts directly with natural persons through Ask mode's conversational Q&A, so it needs to disclose that users are talking to an AI system. That single transparency obligation, not an Annex III high-risk designation, is what governs this system on a first read of the brief.

---

## Phase 1: Read and annotate

**Elements that affect the risk tier classification:**
- Three modes: Ask, Learn, Monitor (as described in the brief, and confirmed against `src/monitor.py`: Monitor is non-evaluative, it only dedupes, sorts, and filters, no scoring or recommendations).
- The brief's own claim: *"does not produce scores about people, approve or reject applications, rank individuals, or make automated decisions that directly affect legal rights."* This is a direct, self-declared statement against Annex III style automated decision-making.
- The brief's own claim: intended audience is professionals, *"not patients or the general public making healthcare decisions."* This narrows exposure to the essential-services and consumer-facing angles of the Act.
- `gtm_future_sprints.md` (repo) roadmap includes a Sprint 4 "Enterprise SaaS (B2B)" tier with "compliance dashboards." This is not mentioned in the brief itself, and signals a possible future move from educational tool toward professional decision support.

**Elements that are unclear or need clarification:**
- The brief states *"All outputs... are reviewed by the user before any action is taken,"* but this reads as a stated design intent or policy, not something I could verify against the actual UI. `src/app.py` shows no built-in reminder, checkbox, or disclaimer that would technically enforce or prompt this review step.
- Whether Learn-mode quiz results or progress tracking are ever used for formal credentialing (CE credits, employer training records). The brief does not address this.
- Whether the GTM roadmap's "compliance dashboards" (repo only, not in the brief) change the human-review picture described in the brief.
- Server-side data retention for the "user background information" the brief says the platform collects to personalize content. `src/app.py` only shows Streamlit session state, backend persistence is not visible from this file.
- Whether the system is already "placed into service" for any EU-based users, or is still a non-public bootcamp demo.

**Elements that suggest a specific obligation applies:**
- `project_plan.md` (repo) says directly: *"The document contains no explicit disclaimer about medical or regulatory advice."* This sits oddly next to the brief's own emphasis on human oversight and user responsibility, since a disclaimer is usually how that expectation gets communicated to the user.
- `src/app.py` shows no AI-interaction notice in the UI.
- The brief confirms the platform collects "user background information," which is personal data, so GDPR applies.
- The system uses three third-party AI and data vendors (OpenAI, Pinecone, Cohere, from the repo), which brings sub-processor and GPAI-component due-diligence obligations.

---

## Phase 2: First-pass classification

| Question | Answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | No. There is no subliminal manipulation, exploitation of vulnerabilities, social scoring, or biometric or emotion-recognition functionality. |
| Does this system operate in any of the eight Annex III areas? | Unlikely. The brief explicitly states the system does not score people, approve or reject applications, rank individuals, or make automated decisions affecting legal rights, and its audience is professionals, not patients. This argues against any Annex III area, including the education one I initially flagged from Learn mode's quiz and progression features. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow or preparatory? | Narrow or preparatory, based on the brief's own description. Still a self-declared claim rather than something I independently verified, so I am treating it as strong evidence, not proof. |
| Does this system interact with end users or generate content that requires disclosure (Article 50)? | Yes. Ask mode is a conversational system that generates text directly for users. I did not find an AI-interaction notice in the reviewed UI code, so Article 50(1) transparency does not look satisfied yet. |
| First-pass risk tier | **Limited risk, transparency obligations.** The brief's own denial of automated decision-making and its narrow professional audience make me fairly confident this stays out of Annex III. |
| One-sentence justification citing the specific article or Annex entry | The brief's stated design (no scoring, no automated legal-rights decisions, human review before action) keeps the system out of Annex III's high-risk categories, but since it interacts directly with natural persons, it still falls under the transparency obligation in **Article 50(1)**. |

---

## Phase 3: Clarifying questions log

**1. How is the "reviewed by the user before any action is taken" safeguard actually enforced or prompted in the product, since I could not find any UI element for it in `src/app.py`?**
- Why it matters: The brief leans on this human-oversight claim as a key mitigation. If it is only a stated policy and not something the interface actually surfaces to users, the practical protection is weaker than the brief suggests.
- My assumption for now: The safeguard is currently a stated intent or offline expectation, not something enforced in the UI. This is now the basis of Finding 1 below, alongside the missing AI-interaction disclosure.

**2. Is Learn-mode quiz or progress output ever used for formal credentialing, CE credits, or employer-mandated training records?**
- Why it matters: The brief does not address this. If yes, it would revive the Annex III(3) education question even with the brief's general "no automated decisions" statement, since formal credentialing is a more specific trigger.
- My assumption for now: No. Treating this as informal, non-binding self-study, consistent with the brief's "educational assistant" framing.

**3. Does the GTM roadmap's Sprint 4 "compliance dashboards" and enterprise B2B tier (repo only, not mentioned in the brief) change any of the human-oversight or decision-support boundaries the brief describes?**
- Why it matters: The brief describes today's system. The roadmap points toward something that sounds closer to decision support for compliance teams, which could shift the risk profile even if the current build stays inside the brief's stated limits.
- My assumption for now: Current build matches the brief (informational and educational only), the roadmap is prospective and not yet built.

**4. What server-side data is kept from the "user background information" the brief says the platform collects, and is any of it shared with OpenAI, Pinecone, or Cohere beyond normal API service delivery (for example, model training)?**
- Why it matters: Needed to check GDPR lawful basis, retention period, and sub-processor risk. This is a parallel legal issue, not an AI Act question.
- My assumption for now: No persistent server-side storage of user data beyond the vector index of source *documents* (not user queries). Still needs confirming.

**5. Is DrugDev-AI already placed into service or marketed to any EU-based users or organizations (even an informal free beta), or is it strictly a non-public bootcamp capstone right now, as the brief's "potential deployment" phrasing suggests?**
- Why it matters: This decides whether AI Act obligations already apply legally ("placing on the market" or "putting into service") or are still prospective, tied to the GTM roadmap.
- My assumption for now: Still a non-public capstone demo, consistent with the brief's "potential deployment" wording. I am treating most findings below as prospective, to be resolved before any real launch.

---

## Phase 4: Audit report

### Section 1: System summary
DrugDev-AI is an educational AI assistant for pharmaceutical and regulatory professionals, built as an Ironhack AI Consulting Bootcamp capstone. It has three modes: Ask (grounded Q&A over EMA, FDA, ICH, WHO, and European Commission documents), Learn (structured lessons and quizzes), and Monitor (aggregates live updates from ClinicalTrials.gov, EMA, and openFDA). By the builder's own description, it does not score people, approve or reject applications, or make automated decisions affecting legal rights, is aimed at professionals rather than patients, and expects the user to review all outputs before acting on them. Technically, it runs on OpenAI, Pinecone, and Cohere, with a stated roadmap toward paid B2B deployment.

### Section 2: Risk classification
First-pass tier: **Limited risk, transparency obligations** (Article 50(1)). The brief's own statements, no scoring, no automated legal-rights decisions, a professional (not patient) audience, and human review before action, point away from any Annex III high-risk category, including the education angle I first considered from Learn mode's quiz and progression features. I am treating these as strong evidence rather than settled fact, since they are the builder's self-description and I have not independently verified them against the running product or its actual user base. The main confirmed obligation is Article 50(1), since Ask mode talks directly to users and no AI-interaction disclosure is visible in the code.

### Section 3: Role map
- **Provider:** Nevena, as the developer putting the system into service. If the GTM roadmap moves ahead to a commercial B2B offering, this role becomes formal, with full Article 50 obligations attaching at that point, and Annex III should be re-checked if the product starts supporting real compliance decisions rather than education.
- **Deployer:** Any organization or person using the tool under their own authority, for example a pharmaceutical organization or training provider, as the brief itself names. Deployers would need to make sure their own end users get the Article 50 AI-interaction notice, and keep the human-review step the brief describes as an actual practice, not just an assumption.
- **Third-party vendors:** OpenAI (LLM and GPAI model provider), Pinecone (vector database hosting), Cohere (reranking model). As a downstream integrator of third-party GPAI components, DrugDev-AI's provider should keep documentation from these vendors as part of normal due diligence. ClinicalTrials.gov, openFDA, and EMA are public data sources, not AI vendors, so no AI Act obligation flows from them directly, but responsibility for the accuracy and freshness of what gets surfaced still sits with DrugDev-AI.

### Section 4: Compliance findings

> **Finding 1: Missing AI-interaction disclosure, and no in-app support for the brief's own human-review claim**
> **Severity:** Significant
> **Description:** Article 50(1) requires that people be told they are talking to an AI system, unless this is obvious from context. Ask mode is a direct conversational interface, and I found no disclosure notice in `src/app.py`. This also undercuts the brief's stated safeguard that "all outputs are reviewed by the user before any action is taken," since nothing in the UI currently prompts or reminds the user to do that review.
> **Recommended action:** Add a clear, always-visible notice in the UI (for example: "You are interacting with an AI-generated response, not a human regulatory expert. Verify before acting.").
> **Escalation needed?** Yes, to the builder, before any wider release.

> **Finding 2: No reliance or liability disclaimer, despite the professional decision-support framing**
> **Severity:** Significant
> **Description:** `project_plan.md` (repo) confirms no medical or regulatory-advice disclaimer exists yet. Target users include people who may lean on outputs for real regulatory work. Even though the brief says the system does not make automated decisions and expects human review, wrong or hallucinated regulatory guidance can still mislead the human reviewer, which carries real professional-liability and unfair-commercial-practice risk if the tool is positioned as authoritative. This is a parallel legal issue, not an AI Act obligation on its own.
> **Recommended action:** Add a clear "informational only, not a substitute for regulatory or legal counsel" disclaimer, and keep leaning on the existing source-citation behavior in Ask mode.
> **Escalation needed?** Yes, a legal or compliance review is recommended before any commercial (GTM) launch.

> **Finding 3: Annex III education-category question, now mostly resolved by the brief, still worth a direct confirmation**
> **Severity:** Minor, pending confirmation
> **Description:** Learn mode's quizzes and progression tracking initially looked close to Annex III(3)(b) language on evaluating learning outcomes. The brief's own statement that the system does not make automated decisions affecting legal rights, combined with its educational framing, argues this stays out of Annex III. I have not verified this independently, so I am keeping it open pending confirmation on formal credentialing use (see Clarifying Question 2).
> **Recommended action:** Confirm with the builder whether Learn-mode outputs are ever used for formal credentialing, CE credits, or employer-mandated training records.
> **Escalation needed?** No, pending confirmation. Becomes Yes if formal use is confirmed.

> **Finding 4: GDPR, personal data collected without a visible privacy notice**
> **Severity:** Significant
> **Description:** The brief confirms the platform collects "user background information" to personalize content. This is personal data under GDPR. I found no privacy notice, consent mechanism, or documented retention policy in the reviewed files. This is a parallel legal issue rather than an AI Act finding.
> **Recommended action:** Add a privacy notice, define the lawful basis (likely consent or legitimate interest), document retention, and confirm data-processing agreements with OpenAI, Pinecone, and Cohere as sub-processors.
> **Escalation needed?** Yes.

> **Finding 5: Undocumented third-party data flows**
> **Severity:** Minor
> **Description:** User queries and background information are sent to OpenAI, Pinecone, and Cohere (per the repo's architecture). I found no documentation on data residency or whether this data is used for third-party model training.
> **Recommended action:** Document sub-processor data flows and confirm opt-out of training use where possible (for example, OpenAI API zero-retention settings).
> **Escalation needed?** No, this is Minor, but it should be resolved before a commercial launch.

### Section 5: Overall recommendation
**Proceed with conditions.** I found no Blocking findings. Nothing here looks like a prohibited practice, and the builder's own brief argues fairly convincingly against an Annex III high-risk trigger. That said, three Significant findings (missing AI-interaction disclosure and unsupported human-review claim, missing reliance or liability disclaimer, and the GDPR privacy-notice gap) should be fixed before the system moves beyond its current bootcamp or demo context, and definitely before any step toward the paid B2B GTM roadmap. The Annex III education question (Finding 3) should be settled with the builder directly as a quick confirmation, not left as an assumption.

### Section 6: What this report is not
This report is not a legal opinion, not a conformity assessment, and not a certification. I wrote it from Nevena's own system brief plus public technical documentation, without seeing her self-audit findings, and without a completed debrief. Conclusions should be checked with the builder and, before any EU market placement, with qualified legal counsel.

---

## Phase 5: Debrief conversation

Held 2026-08-18, see `debrief-notes.md` for the notes and joint closing note. This audit report and the debrief notes stayed separate deliverables until then, in line with the lab's ground rules (no discussing findings before Phase 5).

---

## Stretch: Work plan for Finding 1 (missing AI-interaction disclosure)

**Deliverable:** An in-app AI-interaction and reliance notice: a persistent banner (sidebar or footer, visible on every screen) plus a short reminder line under each Ask-mode response, both stating that responses are AI-generated and should be verified before acting on them. This closes the Article 50(1) gap directly and gives the brief's "reviewed before any action is taken" claim something real to point to in the product.

**Who is responsible:** Nevena writes and implements the banner copy and the Streamlit component, since it is a small, self-contained UI change. A compliance-minded reviewer, even an informal one such as a bootcamp mentor, signs off on the final wording before it ships, to confirm it actually informs users of AI interaction rather than reading as generic boilerplate.

**Timeline:** About one week. Draft copy: 1 day. Implement the banner and the per-response reminder in `src/app.py`: 1 to 2 days. Review and sign-off: 1 day, with a small buffer. Realistic to close before any Sprint 1 GTM work starts.

**Evidence needed to verify it is closed:** A screenshot or short live demo showing the notice visible on first load and staying on-screen during Ask-mode use, confirmation the wording covers both the AI-interaction disclosure and the reliance reminder, and a short note in `project_plan.md` or the README recording that the transparency notice was added and where it lives in the code.
