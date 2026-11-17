# Phases 2–3 — First-pass classification and clarifying questions log

**System:** Elif Yurdakul's Project 3, the Unioptt university programme fact-checker
**Auditor:** Pieter Albrecht · **Date:** 17 November 2026

## CFU 1 — Recognize: first-pass classification

| Question | My answer |
|---|---|
| Does this system fall under any prohibited category (Art. 5)? | **No.** No manipulation, no exploitation of minors' vulnerabilities (Art. 5(1)(b)), no social scoring, no emotion recognition or biometrics. It informs; it doesn't distort behaviour. |
| Does it operate in any of the eight Annex III areas? | **Yes, education (Annex III point 3), borderline.** Not 3(a): universities make every admission decision. The relevant entry is **3(c)**: *"assessing the appropriate level of education that an individual will receive or will be able to access, in the context of or within educational and vocational training institutions."* The met/gap comparison assesses whether a student can access a programme. |
| If Annex III: significant influence, or narrow/preparatory? | **Mostly preparatory in the MVP** (Art. 6(3)(d)): it prepares the family's own decision and decides nothing. **But** the met/gap step evaluates a person's grades, language level and budget, which is arguably **profiling**, and Art. 6(3) says a system that profiles natural persons is *always* high-risk if it falls in Annex III. |
| Interaction or content requiring disclosure (Art. 50)? | **Probably limited.** The report is assembled by code from quoted source sentences, not generated text. If Telegram is a chat interface, Art. 50(1) requires telling users they're interacting with AI. |
| **First-pass risk tier** | **Not high-risk in the B2C MVP (minimal risk, with possible Art. 50 duties). Likely high-risk under Annex III 3(c) once private high schools and counsellors use it.** |
| One-sentence justification | Annex III 3(c) covers assessing which education an individual can access *in the context of or within educational institutions*; a consumer platform used by families sits outside that context and is preparatory (Art. 6(3)(d)), but deployment by high schools brings it inside, where the profiling override in Art. 6(3) removes the exemption. |

**Uncertainty:** the tier depends on (a) whether the AI Act applies at all (territorial scope), and (b) how the B2B version is used. Even in the "not high-risk" reading, a provider relying on Art. 6(3) must **document the assessment (Art. 6(4)) and register the system (Art. 49(2))**. The 2026 AI Omnibus (Reg. (EU) 2026/1744) kept that registration duty.

## Phase 3 — Clarifying questions log (CFU 2 — Probe)

*Sent to Elif in writing on 17 November 2026. Answers to be logged below each question.*

**Q1 — Where is Unioptt established, and where are its users?**
- *Need to know:* the legal seat of Unioptt (Turkey, Netherlands or elsewhere) and whether users are only in Turkey or also in the EU (e.g. Turkish students already living in the EU).
- *Why it matters:* the AI Act applies to providers placing systems on the EU market and to output used in the EU (Art. 2(1)). A Turkey-only service may fall outside it entirely. It also decides GDPR vs. Turkish KVKK.
- *Provisional assumption:* Unioptt is or will be EU-established (Elif is based in the EU), and some users are in the EU. **The AI Act applies.**
- *Answer:* _…_

**Q2 — In the B2B version, how will high schools and counsellors use the met/gap output?**
- *Need to know:* will schools use it to decide or steer which programmes a student applies to (shortlists, "don't apply" advice, counselling files)?
- *Why it matters:* this is the line between a preparatory information tool and Annex III 3(c) "assessing the appropriate level of education … within educational institutions".
- *Provisional assumption:* yes, schools would use it to steer advice. **Treat the B2B version as high-risk.**
- *Answer:* _…_

**Q3 — What does the student see and interact with?**
- *Need to know:* is Telegram a chat with free-text answers, or just delivery of a finished report? Is any text (e.g. "next steps") written by the LLM?
- *Why it matters:* Art. 50(1) (disclose AI interaction) and Art. 50(2) (mark AI-generated text).
- *Provisional assumption:* delivery only; next steps are template text. **Art. 50 duties minimal**, but disclosure recommended as good practice.
- *Answer:* _…_

**Q4 — Who enters the student profile, and how are minors handled?**
- *Need to know:* does the student, a parent or a counsellor enter the data? Age verification? Parental consent?
- *Why it matters:* vulnerable users (AI Act recitals, Art. 9(9) risk management if high-risk); GDPR Art. 8 / KVKK consent for minors.
- *Provisional assumption:* students enter their own data, with no age check. **Gap.**
- *Answer:* _…_

**Q5 — What is shown for "Inferred" and "Unknown" facts, and is any human review planned for production?**
- *Need to know:* are those facts clearly labelled or hidden? Will anyone check deadlines and costs before a report goes out?
- *Why it matters:* accuracy (Art. 15 if high-risk), human oversight (Art. 14), and consumer-protection exposure for wrong deadlines or tuition.
- *Provisional assumption:* statuses are shown per fact; no human review planned.
- *Answer:* _…_
