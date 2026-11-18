# System summary

Restated in my own words, to confirm I understood the description before assessing it.

## What the system does

The Application Prep Agent turns a job application into a prepared application pack. A person fills in a web form with their CV, the job description they are applying for, and up to 15,000 characters of free text about their achievements. An n8n workflow reads the job posting, compares it against the CV, and produces a package: a fit score from 0 to 100, each job requirement marked as strong, partial or gap, rewritten CV bullet points, a cover letter and interview preparation notes. The draft is fact-checked against the CV and public company information, then emailed to the address given on the form.

One behaviour matters more than the rest. If the fit score comes out below 50, the system does not send the pack. It sends a short note saying the match is weak. Nobody reviews that outcome before the email goes out.

## Who uses it, and who is affected

The description names two users: the job seeker applying for themselves, and a career coach submitting on a candidate's behalf. That distinction turns out to decide the entire assessment.

The person affected is the candidate — the one whose CV is read, whose suitability is scored, and who either receives the full pack or does not. In the first scenario the affected person is also the user. In the second they are not, and may not know a score about them exists.

## What it is built from

n8n orchestrates the workflow, on an instance hosted by the course provider. OpenAI's models do the reading, scoring and writing, in up to five calls per run. Gmail sends the result. Jina Reader fetches the job posting, Tavily and NewsAPI add company context, and Pinecone holds writing guidelines that contain no candidate data.

## Where a human sits

Nowhere, in the path that matters. The description is explicit: nobody reviews the sub-50 decision before the email goes out. The candidate reviews the output afterwards and decides whether to apply — but by then the system has already decided what they received.

The builder's own description notes that the decisions that matter, whether to apply and what to send, stay with the candidate, while adding that a coach or recruiter using the score to decide whom to support or put forward would directly influence decisions about people. I read that second sentence as the most consequential statement in the whole document, and I have treated it as the hinge of this audit.

## What I could not determine

- Which deployment is actually intended: the self-service tool, the coach-operated version, or both.
- Whether the candidate is told a score was produced, in the coach scenario.
- Whether a candidate can obtain the full pack after a sub-50 result, by any route.
- Whether an intended purpose is recorded anywhere in the project.

Each of these changes the classification rather than merely refining it, which is why they appear as findings rather than as caveats.
