# Findings and remediation

Severity follows the convention used in the peer-review labs: **Blocking** means the system should not be deployed in that form; **Significant** means deployment can continue but the risk is material; **Minor** means good practice.

## Finding 1 — The intended purpose is not fixed, so the tier cannot be assigned

**Severity: Blocking**

- **Current state:** the description supports two deployments — a job seeker using it on their own application, and a career coach submitting on a candidate's behalf. Nothing records which is intended.
- **Required state:** classification under Art. 6 turns on intended purpose. A system whose purpose is undetermined has no determinable tier, and every other finding depends on this one.
- **Remediation:** write one paragraph stating who the system is for, who may operate it, and which uses are excluded. If the self-service reading is intended, say so and close off the coach pathway — do not simply leave it unbuilt. If the coach deployment is intended, treat the system as high-risk from today.
- **Escalation:** yes, to whoever will be the provider in production. This is a product decision before it is a legal one.

## Finding 2 — Automated decision with no human in the path

**Severity: Blocking in the coach deployment, Significant otherwise**

- **Current state:** a fit score below 50 withholds the full pack and sends a short note instead. Nobody reviews this before it goes out.
- **Required state:** in a high-risk deployment, Art. 14 requires human overseers who can intervene before a decision takes effect, with the authority and the time to do it. In any deployment, Art. 22 GDPR gives the person a right to human intervention where an automated decision has a significant effect on them.
- **Remediation:** make the full pack reachable. Show the score and the reasons with the weak-match note, and give a route to request the full output. A one-click request answered by a person satisfies both regimes and costs little.
- **Escalation:** yes, if the coach deployment goes ahead.

## Finding 3 — In the high-risk scenario, none of the eleven provider obligations is met

**Severity: Blocking in that deployment**

- **Current state:** the conditional checklist shows gaps across all eleven, from risk management through to post-market monitoring.
- **Required state:** a high-risk system may not be placed on the market until conformity assessment is complete and the system is registered.
- **Remediation:** do not approach this as eleven tasks. Approach it as one decision — whether the coach-facing product is worth roughly a year of compliance work — and answer that before writing more code. If the answer is yes, start with Art. 10 data governance and Art. 14 oversight, because those shape the architecture; the documentation obligations follow design rather than preceding it.
- **Escalation:** yes. Conformity assessment involves a third party for some routes, and the provider role should be confirmed by counsel.

## Finding 4 — The person scored may never know

**Severity: Significant**

- **Current state:** where a coach submits, the candidate is not the user. Nothing in the description tells them a score was produced or what it said.
- **Required state:** in a high-risk deployment, deployers must inform affected persons, and Art. 86 gives a right to an explanation of decisions taken on the basis of a high-risk system's output. Under the GDPR, Art. 14 applies to data obtained other than from the data subject.
- **Remediation:** if the coach deployment proceeds, require the coach to have the candidate's agreement and to share the score with them. Build it into the product rather than the terms, because a term nobody reads will not produce the behaviour.
- **Escalation:** no, if the self-service reading is adopted. Yes otherwise.

## Finding 5 — The fit score has no known accuracy

**Severity: Significant**

- **Current state:** the system outputs a number from 0 to 100 and acts on it at a threshold of 50. Nothing establishes what that number measures or how reliable it is.
- **Required state:** Art. 15 requires appropriate accuracy for high-risk systems and the declaration of metrics. Outside that regime it is simply a design question with real consequences: a threshold applied to an unvalidated score is an arbitrary cut-off presented as a measurement.
- **Remediation:** test the score against known outcomes, or remove the automatic threshold and let the candidate see the score alongside the full pack. The second option costs nothing and removes Finding 2 at the same time.
- **Escalation:** no.

## Finding 6 — Bias in scoring is unexamined

**Severity: Significant**

- **Current state:** CVs differ systematically by background, education system and native language, and a language model rating them will carry those differences into the score. Nothing in the description examines this.
- **Required state:** Art. 10 requires high-risk training and input data to be examined for bias. Below that tier it remains a straightforward fairness and product-quality issue.
- **Remediation:** run the same job against a set of CVs that differ in ways that should not matter — phrasing, non-German qualifications, career gaps — and compare the scores. This is an afternoon's work and is the most informative thing on this list.
- **Escalation:** no, but it is the finding most likely to surface something surprising.

## Finding 7 — Generated text presented as the candidate's own work

**Severity: Minor, and outside the AI Act**

- **Current state:** the system writes a cover letter and rewrites CV bullets, which the candidate sends to an employer under their own name.
- **Required state:** nothing under the AI Act. Art. 50(4) covers deepfakes and public-interest publication, neither of which applies. This is a question between candidate and employer.
- **Remediation:** none required. Worth a line in the output encouraging the candidate to make the text their own — which also improves the application.
- **Escalation:** no.

---

## Questions I would put to the builder

1. Which deployment is intended — self-service, coach-operated, or both? Provisional position in the absence of an answer: both are supported, so the high-risk reading has to be planned for.
2. Can a candidate obtain the full pack after a sub-50 score by any route? Provisional position: no, as the description states nobody reviews it.
3. In the coach scenario, does the candidate know a score exists? Provisional position: no.
4. Is the fit score validated against anything? Provisional position: no.

## Where I expect us to disagree

**On the sub-50 gate.** From inside the system it is trivial — the candidate can resubmit with a different job. From outside it is an automated decision that withholds a service from a person on the basis of a score. Both readings are defensible and the coach scenario is what settles it.

**On whether Annex III applies at all.** The builder's position will reasonably be that this is a tool for candidates, not for recruiters, and that Annex III no. 4(a) is aimed at employers. That is a good argument. My counter is that the Annex describes functions rather than business models, and that the description itself names the coach deployment — so the argument holds only once the purpose is fixed in writing and the other pathway closed.

**On severity.** Calling Finding 1 blocking may look harsh for a course project. It is blocking in the specific sense that the tier cannot be determined without it, and every other judgement in this audit inherits that uncertainty.
