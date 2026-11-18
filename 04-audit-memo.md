# Audit memo

**To:** Head of Product, Application Prep Agent
**From:** Friedrich Tschoepke, external review
**Date:** 18 November 2026
**Re:** EU AI Act assessment

## Classification

The system has no single risk tier, because it has no settled purpose. Used by a job seeker on their own application, it is **minimal risk** and the AI Act asks almost nothing of you. Used by a career coach or a recruiter to evaluate candidates, it is **high-risk** under Annex III no. 4(a), and the full provider obligation set attaches — including conformity assessment and registration before it may be placed on the market.

Your own description says both are possible. That is the finding.

## Roles

You are the **provider**: you built it and would place it on the market under your own name. You are also the deployer today. In the coach scenario the coach becomes the deployer, and the heavier obligations stay with you rather than moving to them. OpenAI supplies the models and carries its own duties as a model provider.

## Key findings

**The purpose decides everything, and it is not written down anywhere.** The same code is lightly regulated or heavily regulated depending on who presses the button. Fixing this is a paragraph of writing and it unlocks every other decision.

**The sub-50 gate runs with nobody in the path.** A score withholds the full pack, and no person reviews it before the email goes out. In a high-risk deployment that fails the human oversight requirement; in any deployment it engages the GDPR's rule on automated decisions. Showing the score with its reasons and offering a one-click route to the full pack closes it cheaply.

**The score itself is unvalidated and unexamined for bias.** You act on a threshold of 50 without knowing what the number measures or whether it moves with things that should not matter — phrasing, a foreign qualification, a career gap. This is not primarily a legal problem. It is a product problem that the law would also notice.

## Recommended next steps

1. **Decide the purpose, this week.** Self-service or coach-operated. Write it into the repository, and if it is self-service, close the other pathway rather than leaving it unbuilt.
2. **Remove the automatic gate**, or make the full output reachable on request. One change, two regimes satisfied.
3. **Run a bias check** on the score before anything else is built on top of it. An afternoon, and the most informative thing on the list.
4. **Only if the coach product is the goal:** treat the system as high-risk from today and budget accordingly. The gap between where it is and where that regime requires it to be is substantial, and it is cheaper to design for than to retrofit.

## Caveats

This is not a legal opinion, not a conformity assessment and not a certification. It is an external first-pass assessment made from a written system description, by someone who has not seen the workflow. Several conclusions rest on assumptions recorded in the findings document and would change if those assumptions are wrong. Obtain legal review before relying on this for a decision that commits budget or ships a product.
