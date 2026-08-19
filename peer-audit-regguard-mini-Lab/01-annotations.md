# Phase 1 - Annotated Read

System audited: RegGuard-Mini
Builder: Kimia Asgari
Auditor: Nelly Pourmehr

## Underlined: affects risk tier

- Compares 3D vehicle shape against rules, some of them "legal requirements for road vehicles."
- Output is advisory only. System never changes geometry. Never approves anything.
- Designer must explicitly save any suggested change. Nothing happens automatically.
- No consumer, applicant, employee-under-assessment, or member of the public is evaluated.
- Built by an individual for a course. In production it would be sold by Onyx Dynamics and used inside a car manufacturer's design studio.
- Report includes a colleague's name and address, sent by the designer, by hand.

## Circled: unclear, needs a client question

- "Some legal requirements for road vehicles" is not specific. Which regulation, which type-approval rules, is not named.
- Not stated whether the tool is ever used as the basis for an actual compliance sign-off, or stays strictly pre-engineering.
- Not stated whether session data (questions, geometry, report recipients) is stored, and for how long.
- Not stated whether the plain-language chat makes clear to every user that they are talking to an AI system, or whether that's assumed obvious.

## Marked: suggests a specific obligation

- Personal data collected: designer's name, typed questions, and the report recipient's name and address. GDPR applies regardless of AI Act tier.
- Confidential, unreleased vehicle geometry is processed. This is a trade secret / confidentiality obligation, not an AI Act one, but material to a compliance review.
- Plain-language Q&A interface with users. Possible Article 50 relevance, needs a decision on whether disclosure is required or already obvious from context.