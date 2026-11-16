# LAB | Audit your teammate's project

## First-pass classification 

*The answers are a preliminary read of those stated facts against the EU AI Act—not a legal determination. They could change if the system is used differently or more details emerge.*

| Question | Answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | No, based on the brief. It does not use a prohibited practice such as social scoring or workplace emotion recognition. |
| Does this system operate in any of the eight Annex III areas? | No, based on the described purpose. It supports internal process improvement; it does not assess or make decisions about employees. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow/preparatory? | Not applicable: the described system is not in an Annex III area. Its recommendations may inform internal workflow choices, but do not determine decisions about people. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | Yes. Employees interact directly with it, so they should be informed they are interacting with AI (Article 50(1), unless this is obvious). Article 50(2)'s marking rules for generated content depend on the content and its use; they do not automatically apply to every internal report. |
| First-pass risk tier | Limited risk / transparency obligations, based on the brief; not prohibited or high-risk on the facts provided. |
| One-sentence justification citing the specific article or Annex entry | The system provides internal workflow recommendations rather than making decisions in an Annex III area (including employment, Annex III, point 4), and no Article 5 prohibited practice is described; its direct employee interaction brings Article 50(1) transparency into scope. |

## Clarifying questions log

1. **Does the system ever infer emotions or sensitive traits about employees, or score people based on behavior or personal characteristics?**
   - **What I need to know:** Whether it analyzes biometric or other personal signals, or creates individual/social scores.
   - **Why it matters:** These uses could change the Article 5 prohibited-practice assessment, including workplace emotion recognition or social scoring.
   - **Provisional assumption:** No; it assesses proposed AI use cases and workflow problems, not employees.

2. **Are its recommendations used to recruit, assign tasks to, monitor, evaluate, promote, or otherwise make decisions about workers?**
   - **What I need to know:** Whether the tool or its outputs affect employment decisions or workers' terms and conditions.
   - **Why it matters:** Such intended uses may fall under Annex III, point 4; the exact purpose and effect on people determine whether the high-risk rules apply.
   - **Provisional assumption:** No; it recommends process fixes and tools, without evaluating or making decisions about workers.

3. **Who decides whether a proposed AI use is allowed, and can a person meaningfully review or override the system's green/amber/red rating before action is taken?**
   - **What I need to know:** Whether ratings are advisory, automatically acted on, or relied on by the Board or managers, and what the human review entails.
   - **Why it matters:** This clarifies the system's actual influence and whether its use extends into an Annex III area or materially affects decisions about people.
   - **Provisional assumption:** The ratings guide an internal pipeline decision; the Board reviews red cases, and no employment decision is made from the ratings.

4. **Are employees clearly told they are interacting with AI, and are generated outputs ever published to inform the public or used to create deepfakes?**
   - **What I need to know:** What disclosure users see and how generated text is distributed or presented.
   - **Why it matters:** Article 50(1) generally requires notice for direct interaction with an AI system; Article 50(2), (4), and (5) cover marking certain generated content and disclosures for deepfakes or certain public-interest text.
   - **Provisional assumption:** The tool is used internally; assume a clear AI notice is provided and reports are not published to the public or used to create deepfakes.

## Audit report

**Scope and evidence basis — 16 November 2026.** This is a preliminary peer audit of the system brief and clarifying-question log only. The prototype is not currently used by Kleinanzeigen, and the four internal documents are fictional; conclusions should be rechecked against the production design and contracts.

### Section 1: System summary

Fix My Process is a prototype internal assistant intended to help employees describe workplace process problems and receive a recommended, policy-aware fix. It searches external sources and four internal reference documents, then uses an AI model to classify the proposed use as green, amber, or red and produce an employee-facing fix plus a use-case card for internal governance teams. Red cases are sent to an AI Governance Board, while green and amber ratings may be acted on without a documented human check. The system stores case data and free text, has no login, and sends some information to external AI and search providers.

### Section 2: Risk classification

**First-pass tier: Limited risk / transparency obligations; not prohibited or high-risk on the stated facts.** The described purpose is internal process improvement, not a decision about a natural person in an Annex III area such as employment, and no Article 5 practice is described. Direct employee interaction brings Article 50(1) transparency into scope: users must be told they are interacting with AI unless that is obvious. Article 50(2) may also matter if the system generates synthetic text, subject to its scope and technical applicability. This classification is uncertain until the team confirms that the system never infers emotions or sensitive traits, scores workers, or influences recruitment, task allocation, monitoring, evaluation, promotion, or other employment decisions. Article 4 AI-literacy measures also apply to staff operating or using AI systems. [EU AI Act, Articles 4 and 50](https://eur-lex.europa.eu/eli/reg/2024/1689)

### Section 3: Role map

| Role | Party on current facts | Key obligations / implications |
|---|---|---|
| Provider | The project team or future operating company that develops and makes the assistant available; the brief does not identify a legal entity. | Define intended purpose, risk controls, documentation, user instructions, AI notice, monitoring, and vendor arrangements. If the system is materially modified or presented under another entity's name, reassess whether that entity becomes a provider under the Act. |
| Deployer | No current deployer: the brief says Kleinanzeigen does not use the prototype. If adopted, Kleinanzeigen would likely deploy it for internal work. | Use it according to its intended purpose, provide AI literacy, ensure meaningful human review of consequential use, implement data/security controls, and preserve Article 50 notices. Confirm that outputs do not become employment decisions. |
| Third-party vendors | External AI/model and web-search, news, and research services; hosting/database and Slack may also be vendors, but are not identified. Some services are in the US. | Identify each vendor and data flow; contract for confidentiality, security, retention, incident support, permitted use, and deletion; assess international transfers and whether vendor outputs can support the claimed confidence and compliance ratings. |

### Section 4: Compliance findings

> **Finding 1 — Article 50 user transparency is not evidenced**  
> **Severity:** Significant  
> **Description:** The system directly interacts with employees, so the provider must ensure a clear AI disclosure at or before first interaction unless the interaction is obvious. The brief mentions only a notice/instruction in the data-risk description; it does not show the interface, wording, timing, accessibility, or testing.  
> **Recommended action:** Add and test a prominent first-interaction notice, identify the AI-generated fix and use-case card where appropriate, and document the decision on Article 50(2) marking for generated text.  
> **Escalation needed?** Yes — to the AI governance owner and legal/privacy counsel.

> **Finding 2 — Uncontrolled personal-data and international-transfer exposure**  
> **Severity:** Significant  
> **Description:** Free text may contain names, the app has no login, and case data is sent to external AI/search services, some in the US. The evidence shows only a notice and an instruction to the model to guard against names; it does not establish minimisation, access control, retention, processor terms, a lawful basis, transfer safeguards, or a DPIA where required. These are principally GDPR/security issues, but they are a material deployment gate.  
> **Recommended action:** Add authentication and role-based access; minimise or redact personal data before external calls; map all processors and locations; set retention/deletion rules; complete the privacy and transfer assessment with the DPO; and prevent vendor training or secondary use unless expressly approved.  
> **Escalation needed?** Yes — to the DPO/privacy counsel and information-security owner.

> **Finding 3 — Green/amber ratings lack mandatory human review and reliable assurance**  
> **Severity:** Significant  
> **Description:** The system decides whether a use is allowed and which tool to recommend, while only red cases go to the Board. The 15-case test scored 79%, and 2 of 5 “High” reports were wrong. Even if this is not high-risk AI on the stated purpose, an unchecked “green” could cause an employee to breach policy and could gradually influence employment or governance decisions.  
> **Recommended action:** Make green/amber outputs advisory; require a named, trained reviewer before action, with override and audit logging; route low-confidence or policy-sensitive cases to the Board; define prohibited uses and stop conditions; and retest accuracy by use case before launch.  
> **Escalation needed?** Yes — to the AI Governance Board and policy owner.

> **Finding 4 — Provider, deployer, and vendor accountability is undocumented**  
> **Severity:** Significant  
> **Description:** The brief does not identify the legal provider, a current deployer, model/search vendors, hosting location, or allocation of incident and monitoring responsibilities. Without this map, the team cannot reliably assign AI Act transparency and literacy duties or verify contractual and data-protection controls.  
> **Recommended action:** Create a system record naming each role, intended purpose, model/version, data flow, vendor, owner, reviewer, retention period, and escalation route; obtain written vendor terms and maintain change and incident logs.  
> **Escalation needed?** Yes — to procurement, legal/privacy, security, and the AI Governance Board.

> **Finding 5 — Prohibited and employment-use boundary is not technically enforced**  
> **Severity:** Minor  
> **Description:** The brief says the system does not assess people, infer emotions, or make employment decisions, which supports the first-pass classification. However, the clarifying questions remain unanswered and the system accepts open-ended problem text and tool requests. A future user could repurpose it for worker monitoring, scoring, allocation, or evaluation, changing the classification.  
> **Recommended action:** Encode and test use-case exclusions, add user-facing warnings, require Board review for employment-related proposals, and reclassify before any such use.  
> **Escalation needed?** No — unless a prohibited or employment-related use is proposed; then escalate to legal counsel and the Board.

### Section 5: Overall recommendation

**Proceed with conditions.** No prohibited or high-risk use is evidenced in the brief, but deployment should wait until the team implements the Article 50 notice, confirms the provider/deployer/vendor map, completes privacy and international-transfer review, and adds human review and confidence-based escalation for green/amber outputs. The system must remain advisory and out of employment decisions; any change to that boundary requires a fresh risk classification and legal review.

### Section 6: What this report is not

This report is not a legal opinion, conformity assessment, or certification. It is a preliminary evidence-based peer review and does not establish compliance with the EU AI Act, GDPR, employment law, or security requirements. Conclusions should be verified with qualified legal counsel before any EU market placement or operational deployment.
