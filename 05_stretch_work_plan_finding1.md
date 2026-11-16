# Stretch – Work Plan for Finding 1 (personal data in scraped content)

**Deliverables that close the gap**
1. **Technical change:** a redaction step before every LLM call. A named-entity filter replaces personal names with their role ("[Managing Director]"), and only the redacted text is stored in run files.
2. **Retention policy:** run files and contact fields are deleted automatically after 90 days, using a scheduled clean-up script.
3. **Vendor paperwork:** signed DPAs with OpenAI and Tavily, and zero-data-retention requested where offered.
4. **Legal documentation:** a one-page legitimate-interest assessment, an entry in the record of processing activities, and a decision on whether GDPR Art. 14 notices are needed.

**Who is responsible**
- **Friedrich (builder):** items 1–2.
- **Friedrich, with a privacy counsel or data protection officer review:** items 3–4.

**Realistic timeline**
- **Week 1:** redaction step and retention script.
- **Week 2:** DPAs and the legitimate-interest assessment drafted.
- **Week 3:** counsel review and sign-off.

All of this must be done before anyone other than the builder uses the system.

**Evidence that it's closed**
- **Test runs:** run files from 10 test companies with no personal names left in them, checked by an automated scan plus a manual sample.
- **Deletion:** a log from the deletion script showing removed files.
- **Signed paperwork:** signed DPAs and a signed legitimate-interest assessment.
- **Updated register:** an updated record of processing activities.
