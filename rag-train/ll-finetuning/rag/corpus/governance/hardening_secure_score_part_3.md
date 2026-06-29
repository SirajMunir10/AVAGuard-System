# Hardening: Secure Score

**Domain:** Governance
**Subdomain:** Secure Score
**Incident Type:** Hardening

## Scenario / Query
A security team notices that their Microsoft Secure Score has dropped by 15 points after a recent tenant-wide policy change. They suspect that a critical security control was disabled or misconfigured. How can they identify which control was affected and restore the recommended hardening state?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft 365 Defender portal, Secure Score dashboard

## Symptoms
- Sudden drop in Secure Score without a corresponding change in user activity or threat detections
- One or more improvement actions show a status of 'Not configured' or 'Excluded by policy'

## Error Codes
N/A

## Root Causes
1. A conditional access policy or device compliance policy was modified or deleted, reducing the security posture
2. An administrator intentionally or unintentionally disabled a recommended security setting

## Remediation Steps
1. Navigate to the Microsoft 365 Defender portal > Secure Score > Improvement actions
2. Filter by 'Status: Not configured' and sort by 'Score impact' descending to identify the highest-impact control
3. Select the affected improvement action and review the 'Configuration' tab to see the exact setting that needs to be enabled
4. Follow the documented remediation steps provided by Microsoft for that specific improvement action (e.g., enable multi-factor authentication, enable audit logging, etc.)

## Validation
After applying the remediation, verify that the improvement action status changes to 'Completed' and the Secure Score recovers to the expected level within 24 hours.

## Rollback
If the remediation causes unintended side effects, revert the specific setting to its previous state using the same configuration interface, then reassess the Secure Score impact.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/microsoft-secure-score>
