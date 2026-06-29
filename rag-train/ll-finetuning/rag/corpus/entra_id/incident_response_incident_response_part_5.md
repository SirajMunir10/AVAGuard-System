# Incident Response: Incident Response

**Domain:** Entra ID
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security administrator receives an alert that a user account in Entra ID has been used to sign in from an anonymous IP address and then immediately performed a high-risk operation (e.g., adding a new conditional access policy). How should the administrator triage, investigate, and remediate this potential compromise using Microsoftâ€™s documented incident response guidance?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Entra ID P2 license required for Identity Protection; Audit logs enabled; Microsoft Sentinel or Microsoft 365 Defender integrated for advanced hunting

## Symptoms
- Sign-in from an anonymous IP address flagged by Identity Protection
- User added a new conditional access policy shortly after the anomalous sign-in
- Alert generated in Microsoft 365 Defender or Microsoft Sentinel

## Error Codes
N/A

## Root Causes
1. User credentials compromised and used by an attacker
2. Attacker leveraged the compromised account to escalate privileges by modifying conditional access policies

## Remediation Steps
1. Confirm the user account is compromised: review sign-in logs and Identity Protection risk detections (Microsoft Learn: 'Investigate risk with Identity Protection' â€“ https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk)
2. Disable the user account immediately to prevent further actions (Microsoft Learn: 'Respond to a compromised user account' â€“ https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-respond-compromised-user-account)
3. Revoke all refresh tokens and session tokens for the user (Microsoft Learn: 'Revoke user access in an emergency' â€“ https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access)
4. Reset the userâ€™s password and require multi-factor authentication re-enrollment (Microsoft Learn: 'Respond to a compromised user account' â€“ same URL as above)
5. Review and revert any unauthorized changes to conditional access policies (Microsoft Learn: 'What are Conditional Access policies?' â€“ https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)
6. Investigate lateral movement or other compromised accounts using Microsoft 365 Defender advanced hunting (Microsoft Learn: 'Advanced hunting in Microsoft 365 Defender' â€“ https://learn.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-overview)

## Validation
Verify that the user account is disabled, all sessions revoked, password reset, and unauthorized conditional access policies removed. Confirm no further anomalous sign-ins from the same IP or user.

## Rollback
If the user was incorrectly disabled, re-enable the account and restore previous conditional access policies from backup or audit logs. Ensure MFA is still enforced.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
- <https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access>
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-overview>
