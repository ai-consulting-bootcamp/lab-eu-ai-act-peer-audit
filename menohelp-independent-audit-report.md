# Menohelp: independent peer audit

Sergii Rostovskyi | Builder: Ben Mayer | 16 November 2026

Pre-debrief, provisional. Reviewed commit: 89940e85b3f869b888e247a5b9651020b8d6c865.
Evidence IDs and legal links: [evidence register](menohelp-evidence-and-legal-sources.md). Reference file: menohelp-evidence-and-legal-sources.md.

## 1. System summary

Menohelp combines cycle logs, optional laboratory PDFs and symptom answers into a personalised health-information report. Python calculates statistics, Supabase supplies reference/coaching material, and OpenAI writes findings and interpretation. The local prototype displays reports and supports download and optional Resend email delivery. Disclaimers, lab-value confirmation and automated checks exist, but external deployment and clinical validation are not established (E1-E5).

## 2. Risk classification

**Provisional limited risk / transparency** for the stated wellness purpose: Article 50 applies to direct interaction and generated text. No Article 5 practice or Annex III use is identified. Personal lab interpretation creates an unresolved **Article 6(1), Annex I Section A points 11/12** boundary: regulated medical/IVD software requiring third-party conformity assessment would be high-risk. A disclaimer cannot settle qualification; specialist review is required. This is not final medical-device clearance. The current Chapter III Sections 1-3 timetable is December 2027 for Annex III and August 2028 for Annex I; Article 50 generally already applies (L1-L3).

## 3. Role map

Ben's operating entity is the prospective downstream provider: own purpose, transparency, AI literacy support and applicable product duties. A practitioner using reports professionally would be a deployer; personal consumers are not professional deployers. OpenAI supplies the model/API and carries applicable GPAI duties; Supabase and Resend supply database/search and email services. Confirm contractual GDPR roles and the operating entity; upstream services do not absorb product responsibility. High-risk provider/deployer duties remain conditional; planned hosting is not verified deployment (E1, E9; obligations appendix).

## 4. Compliance findings

### Finding 1 - Intended purpose and medical-device boundary

**Severity:** Significant.
**Description:** Personal lab interpretation and possible-cause explanations exceed simple data display; medical qualification is unresolved (E3; L1/L5).
**Recommended action:** Approve intended purpose and claims with a medical-device specialist; determine MDR/IVDR class and assessment route before a real-user pilot.
**Escalation needed?** Yes - medical-device regulatory counsel and clinical specialist.

### Finding 2 - Health-data governance and access

**Severity:** Significant.
**Description:** Local name removal and memory expiry help, but personal health summaries/free text reach vendors. Lawful basis, processor/transfer terms and complete deletion are unverified; API ownership checks are not demonstrated (E4, E6-E7, E10; L4).
**Recommended action:** Establish Article 6/9 grounds, accurate notice, vendor/retention map, DPIA screening and per-user authorisation before external health-data processing. Verify whether public samples described as real data require removal or consent review; no such records were reproduced here.
**Escalation needed?** Yes - privacy lead/legal counsel and security engineer.

### Finding 3 - Failed checks do not prevent release

**Severity:** Significant.
**Description:** Reproduced retry routes continue despite errors; UI code permits report display, download and email without a passing-check gate (E5/E8). Passing numeric checks would not prove clinical accuracy either.
**Recommended action:** Block failed output on every delivery path, provide a safe fallback, and test retry exhaustion plus clinically reviewed representative cases.
**Escalation needed?** Yes - technical owner and clinical reviewer.

### Finding 4 - AI transparency is incomplete

**Severity:** Significant.
**Description:** OpenAI input notices exist, but consistent first-interaction/export disclosure and Article 50(2) marking are not evidenced. The medical disclaimer alone is insufficient (E4-E5; L2).
**Recommended action:** Add clear AI disclosure and verify feasible machine-readable marking across output channels with the supplier. Confirm applicable exceptions and first market date.
**Escalation needed?** Yes - product owner and AI regulatory counsel.

### Finding 5 - Content rights and user claims

**Severity:** Significant.
**Description:** Coaching content is described as demo-only licensed. 'Nothing is stored' and 'verified analysis' exceed demonstrated retention and validation assurances (E1, E4, E8-E9).
**Recommended action:** Confirm pilot/commercial rights or replace content; align claims with actual checks and vendor retention.
**Escalation needed?** Yes - rights holder, legal counsel and product owner.

## 5. Overall recommendation

**Proceed with conditions.** Continue controlled development using synthetic inputs; before any real-user pilot, close Findings 1-5 with signed purpose review, privacy/security evidence, tested release gates, transparency and content permissions. No prohibited practice or presently established blocking legal violation was proved by this repository review. If medical-device scope or an unlawful data-processing basis is confirmed without the required safeguards, stop that deployment and revise the recommendation. Evidence gaps are not launch approval; delayed AI Act dates do not suspend GDPR or sector law.

## 6. What this report is not

This is not a legal opinion, conformity assessment or certification. Legal counsel must verify conclusions before EU market placement. The builder's separate system brief, vendor settings and debrief remain outstanding; this review uses repository documentation and an isolated routing reproduction, not a live clinical or security assessment.
