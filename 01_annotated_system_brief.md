# Phase 1 – Annotated System Brief: AI Use Case Identifier (Friedrich Tschoepke)

**Source:** system brief provided by Friedrich (repository state 13 Nov 2026, commit d99573f). Received 16 Nov 2026.

**Annotation key** (Markdown has no underline or circle, so I use tags):
- 🔺 **[TIER]**: affects the risk-tier classification (the "underline")
- ❓ **[UNCLEAR]**: needs clarification before I form a view (the "circle")
- 📌 **[OBLIGATION]**: suggests a specific obligation applies (the "mark")

---

### What does the system do?
It prepares an AI consultant for a first meeting with a small or mid-sized company 🔺**[TIER: business-to-business purpose, aimed at companies not persons]**. The consultant types in a company name and website address. The system reads public web pages about that company, writes a short description of how the company earns money and how its work flows from order to delivery, and suggests three places where AI could support that work 📌**[OBLIGATION: generated text → Art. 50(2)]**. It also lists questions to ask in the meeting.

### What inputs does it take?
- Typed in by the user: company name and homepage address. Optionally a contact person's name, email and city 📌**[OBLIGATION: personal data → GDPR]**. These are saved to a separate file and are not used in the analysis ❓**[UNCLEAR: retention period? Never sent to OpenAI?]**.
- Collected automatically: text from the company's homepage, "about" page, careers page and up to five job postings 🔺**[TIER: employment-related content. Is anyone evaluated? Brief says no]**, plus up to 16 web search results (news, company-register and company-profile entries, job ads).
- Built in: three guidance documents and a library of 51 AI-application descriptions with source links.

Personal data: the system does not search for individuals. It also does not filter personal data out 📌**[OBLIGATION: GDPR data minimisation, Art. 5(1)(c)]**. Company pages, news and register entries often name managing directors, founders or HR contacts. That text is sent to the language model 📌**[OBLIGATION: transfer to a non-EU processor]** and saved in the run file ❓**[UNCLEAR: how long, where, who can access it?]**. The optional contact fields are personal data.

### What does it output?
Three files per run: a written brief (company description, three AI applications with rough money estimates ❓**[UNCLEAR: shown to the client company? Basis for the estimates?]**, meeting questions, sources), one AI-generated diagram 📌**[OBLIGATION: synthetic image → Art. 50(2) marking]**, and a data file holding everything collected and produced. Each work step gets a 0–10 "AI potential" rating. The rating is about work steps, not people 🔺**[TIER: rules out evaluating individuals, so not Annex III 4]**. The system takes no decision and sends nothing to anyone 🔺**[TIER: no decision-making]**.

### Who is affected?
- The consultant, who relies on the brief.
- The analysed company, which is described without being asked and may be described wrongly 📌**[OBLIGATION: accuracy, reputational risk, unfair-competition law if shared]**.
- Employees, indirectly. No individual is assessed, ranked or profiled 🔺**[TIER]**.

### Does a human review the output?
Yes, but by habit, not by design ❓**[UNCLEAR: no review gate or record]**. Statements are labelled "documented" (with a link) or "assumption" ✅ *(good practice)*. Nothing forces a review, records one, or stops the brief being passed on unchanged. **The brief and the diagram do not state that they were produced by AI** 📌**[OBLIGATION: Art. 50 transparency gap]**.

### Who built it?
Friedrich alone, as a course project, with his own code 🔺**[TIER: Friedrich = provider]**. It calls OpenAI (language models, embeddings, image generation), Tavily (web search) and Pinecone (vector store, no company text) 📌**[OBLIGATION: vendor and processor agreements]**.

### Who would use it in production?
Today only the builder, preparing his own meetings 🔺**[TIER: Friedrich = provider and deployer; this is professional use, so the personal-use exemption doesn't apply]**.
**Planned, not built:** a public web form where a company owner enters a website, name, email and phone and automatically receives a shorter report with no human reading it 🔺**[TIER: direct interaction with the public → Art. 50(1)]** 📌**[OBLIGATION: GDPR consent and notice, marketing rules, no human review]** ❓**[UNCLEAR: one-shot form or chat? Are contacts used for sales follow-up?]**.
