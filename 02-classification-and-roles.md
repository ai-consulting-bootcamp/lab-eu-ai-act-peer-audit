# Risk classification and role map

## Risk tier classification

| Question | Answer |
|---|---|
| Does this system fall under any prohibited category (Article 5)? | No. It does not infer emotions, does not categorise people biometrically, uses no subliminal or manipulative technique, and does not predict criminal offences. Social scoring under Art. 5(1)(c) needs checking rather than dismissing, because the system does assign a number to a person — but that provision targets evaluation of social behaviour or personal characteristics leading to detrimental treatment in unrelated contexts, by or on behalf of public or private actors. Scoring a candidate against the requirements of the specific job they applied for is neither unrelated nor social behaviour. Not prohibited. |
| Does this system operate in any of the eight Annex III areas? | **Possibly — this is the whole question.** Seven of the eight are plainly out: biometrics, critical infrastructure, education, essential services and creditworthiness, law enforcement, migration, justice. Area 4, employment and worker management, is the one in play. Annex III no. 4(a) covers systems intended to be used for the recruitment or selection of natural persons, and names analysing and filtering job applications and **evaluating candidates** as examples. Evaluating a candidate against a job's requirements is literally what this system does. Whether that puts it inside 4(a) turns on intended purpose, addressed below. |
| If Annex III: does it significantly influence decisions in that area, or is it narrow or preparatory? | The Art. 6(3) filter would be the obvious argument — the output is preparatory to a human decision about whether to apply. It fails regardless, for a reason that admits no argument: the filter is never available where the system performs profiling of natural persons, and scoring a person's suitability for work is profiling. So if the system is inside Annex III, it is high-risk; there is no middle position. |
| Does this system interact with end users or generate content requiring disclosure (Article 50)? | Not in the way Art. 50 targets. Art. 50(1) concerns systems that interact with a person — a web form is not a conversational AI. The report is AI-generated text, but the machine-readable marking duty under Art. 50(2) falls on the model provider, and Art. 50(4) covers deepfakes and text published to inform the public on matters of public interest, neither of which this is. |
| **First-pass risk tier** | **Minimal risk as a self-service tool; high-risk under Annex III no. 4(a) in a coach- or recruiter-operated deployment.** The description supports both, so no single tier can be assigned to the system as it stands. |
| One-sentence justification | Annex III no. 4(a) names the evaluation of candidates as a high-risk purpose, and whether this system serves that purpose depends entirely on who operates it — a question the available material leaves open. |

## Why it becomes high-risk when somebody else operates it

This is the least intuitive conclusion in the audit, and the objection to it is a fair one: the model performs exactly the same computation either way. The same CV, the same job text, the same prompt, the same number out. Why should the identity of the person pressing the button change the legal status of the system?

Because the AI Act does not regulate computation. It regulates **what is done to people with the result**, and the risk it is built around is asymmetry: one party holding information or power over another and using an AI system to exercise it. Annex III is a list of the places where that asymmetry has serious consequences — your job, your education, your credit, your liberty.

Four things change when the operator is not the person being scored.

**There is an affected person distinct from the user.** When a candidate scores their own application, subject and beneficiary are the same human being. Nobody else acts on the output; there is nobody whose interests the regulation needs to protect against the user's. The moment a coach submits someone else's CV, a second person exists who is affected by a decision they did not make and may not know about.

**The output changes function.** The number 42 out of 100 is self-knowledge in the candidate's hands. In a coach's hands it is a filtering criterion — a basis for deciding whom to spend time on, whom to put forward, whom to quietly drop. Annex III no. 4(a) names the evaluation of candidates precisely because that function bears on access to work, and the function is set by the recipient, not by the code.

**Control disappears.** A candidate who disagrees with their own score can ignore it, resubmit, or apply anyway. A candidate scored by someone else may never see the number, cannot contest it, and has no way of knowing it shaped the outcome. That loss of control is the harm the employment entry exists to address: these systems affect career prospects and livelihoods, and the person affected is rarely in the room.

**Recruitment and selection presuppose a chooser.** Those words describe a process in which someone picks among people. A candidate preparing their own application is not selecting anyone. A coach deciding whom to support, and a recruiter deciding whom to shortlist, are — and that is what brings the system inside the Annex.

So the right mental model is not "the tool is dangerous" but "the tool sits inside a decision". A thermometer used at home is self-care; the same thermometer at a checkpoint deciding who may enter is a screening system. The device is identical. What the reading is used for is not.

Two honest qualifications. First, a strict reading cuts against the builder: Annex III describes functions, and "evaluate candidates" is a fair description of what this system does in either deployment — which is why the self-service reading needs to be stated and defended, not assumed. Second, where a coach merely helps a client they already represent, the case is weaker than where a recruiter filters a pool; the coach scenario sits closer to the line than to either side of it. Both qualifications point the same way: write the purpose down, and close off the pathway you do not intend to support.

## How the two deployments differ in practice

**The candidate applying for themselves.** The person evaluated is the person asking. No employer is selecting anyone; nobody's access to work is being decided by the tool. This is closer to a CV template or a coaching conversation than to a recruitment system, and Annex III no. 4(a) is written around systems used in the course of recruiting and selecting. Minimal risk.

**The coach or recruiter submitting on someone's behalf.** The person evaluated is not the user. A score about them is generated, delivered to a third party, and may inform that third party's decision about whom to support or put forward. That is the evaluation of candidates in a selection process, which is what Annex III no. 4(a) names. High-risk.

Same code, same model, same prompt. The regulation attaches to purpose, not to architecture — which is why the intended purpose has to be written down rather than assumed.

## Role map

| Role | Entity | Key AI Act obligations |
|---|---|---|
| Provider | Nicolò Marseu — developed the system and would place it on the market under his own name | Minimal-risk deployment: AI literacy among operators (Art. 4). High-risk deployment: the full provider set — risk management, data governance, technical documentation, logging, transparency to deployers, human oversight by design, accuracy and robustness, quality management, conformity assessment, declaration of conformity and CE marking, EU database registration, post-market monitoring |
| Deployer | Nicolò today. A career coach or recruitment firm in the second scenario | High-risk deployment: use according to instructions, assign human oversight to competent people with the authority and time to exercise it, ensure input data relevance, retain logs, inform affected candidates, and — for a private actor providing a service of this kind — consider the fundamental rights impact assessment under Art. 27 |
| Vendor | OpenAI — supplies the models performing the scoring and drafting | Provider of a general-purpose AI model: own obligations under Arts. 53–55, including technical documentation and marking of synthetic output. Not the builder's duties, but the builder relies on them |
| Vendor | n8n (orchestration), Jina Reader, Tavily, NewsAPI, Pinecone | Infrastructure and retrieval rather than AI systems in the relevant sense. No AI Act obligations flow from them here |

The uncomfortable implication: in the high-risk scenario the obligations do not land mainly on the coach who runs it. They land on the builder, as provider, including conformity assessment and registration before the system may be placed on the market at all.

## Conditional obligation checklist

Completed for the high-risk scenario, since that is the one that would need it. Every row is a gap — which is the expected result for a course project and is recorded here as a measure of distance, not as criticism.

| Obligation | Article | Status | Note |
|---|---|---|---|
| Risk management system | 9 | Gap | No risk management process described |
| Data and data governance | 10 | Gap | No examination of the scoring for bias across protected groups; CVs vary systematically by background |
| Technical documentation | 11 | Gap | A README is not technical documentation in the Annex IV sense |
| Record-keeping and logging | 12 | Gap | n8n execution history is incidental retention, not designed logging |
| Transparency and user information | 13 | Gap | No instructions for use; a coach deploying it would have nothing to rely on |
| Human oversight | 14 | **Gap — the material one** | The sub-50 gate runs with no review and no route to contest |
| Accuracy, robustness, cybersecurity | 15 | Gap | No accuracy metric defined for the fit score, so its reliability is unknown |
| Conformity assessment | 43 | Gap | Not performed |
| Declaration of conformity and CE marking | 47–48 | Gap | Not performed |
| Registration | 49 | Gap | Not registered |
| Post-market monitoring | 72 | Gap | No plan |

The point of this table is not that a student project fails it. It is that the distance between the current system and the high-risk regime is roughly a year of work — which is exactly why the deployment question has to be answered before anyone builds the coach-facing version, not after.
