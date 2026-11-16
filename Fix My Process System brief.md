# System Brief: Fix My Process

*Ayhan Demir · 16 Nov 2026*

## What is it?

Fix My Process is my Ironhack Project 3: a prototype internal assistant for Kleinanzeigen, Germany's largest classifieds marketplace. Kleinanzeigen does not use it. The four company documents it reads (AI policy, approved tools list, works council agreement, past AI projects) are fictional.

## What problem does it solve?

Employees face daily friction and often use personal AI chatbots the company cannot control or measure. Leadership lacks evidence on which AI use cases matter. One submission gives the employee a safe, approved fix and leadership a checked use case.

## Who uses it?

| User | What they get or do |
|---|---|
| **Employees and team leads** (primary) | Describe a problem, get a fix, give feedback |
| **Operational Effectiveness and Enablement team** | Reads the fix reports |
| **AI enablement team** (under the Chief Product Officer) | A use-case card for every case: evidence, compliance, effort and impact |
| **AI Governance Board** | Sees every case, decides on red ones |
| **Workflow owner** | Error alerts in Slack |

## How does it work?

1. The employee gives their department, the problem and how often it happens. No name is asked for.
2. It searches the web, news, research papers and the four internal documents.
3. An AI model rates the described use: green (allowed), amber (allowed with conditions) or red (not allowed yet).
4. It writes the employee's fix, internal tools first, and the use-case card, each rated High, Medium or Low confidence.
5. The employee gets the fix in about a minute. Red cases then go to the Board to add to the pipeline or dismiss.

## What data does it keep?

Every case becomes one database record: reference code, department, how it was submitted, problem text, tools named, how often it happens, compliance level with the policy rules cited, recommended tools, a flag when no internal tool fits, both reports, confidence, feedback and the Board's decision. The use-case card is also saved as a shared page. Free text can still contain names; only a notice and an instruction to the AI guard against this. The text goes to outside AI and search services, some in the US. The app has no login.

## What does it decide?

Nothing about people. With no human check, it decides whether a green or amber use is allowed and which tool to recommend.

## What happens when it is wrong?

In a 15-case test of an earlier version, reports scored 79% on my rubric; 2 of 5 "High" reports were wrong. A wrong "green" could lead an employee to break policy unknowingly.

