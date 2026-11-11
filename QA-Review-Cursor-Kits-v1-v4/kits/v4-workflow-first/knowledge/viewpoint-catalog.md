# Viewpoint Catalog (starter; review and approve per project)
Owner: QA Lead (assign a real owner before production). Version: 0.1 DRAFT.
Each viewpoint has: VP-ID, domain, category, relevant AC, technique, risk score, evidence, status (APPROVED/PROPOSED/RETIRED), owner.
| Family | Applicability triggers | Typical checks |
|---|---|---|
| Business rule | Conditions/calculations | Decision table, valid/invalid branches |
| Input/Boundary | min/max/required/format | EP, BVA, empty, Unicode when relevant |
| State/Time | lifecycle, deadlines | permitted/forbidden transitions, timezone |
| Authorization | multiple roles/tenants | roles, direct URL, cross-tenant data |
| Payment/Financial | money, coupon, wallet | amount, retry, idempotency, settlement |
| Data integrity | DB write, migration, deletion | old/new mapping, orphan records, rollback |
| Integration | API/webhook/mail/Stripe | error, timeout, retry, duplicate callback |
| Resilience | user interruptions | double submit, reload, network loss |
| Localization | Japanese/English/Traditional Chinese | exact approved strings, formatting |
| User journey | persona goals, cross-channel | completion without help, recovery after errors |
Only activate relevant families. Proposed VPs are visible as potential debt but excluded from the approved VP coverage denominator until reviewed. A test case can map to multiple VPs, with one primary VP when the team's reporting format requires it.
