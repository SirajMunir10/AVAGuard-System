# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate and remediate a leaked credentials detection in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Identity Protection risk detections

## Symptoms
- Leaked credentials detection fired for a user
- High risk detection indicating confirmed credential exposure

## Error Codes
N/A

## Root Causes
1. User credentials were exposed in a known data breach or leak

## Remediation Steps
1. Assess the scope of exposure by reviewing the user's risk history and sign-in logs to determine if the leaked credential was used for unauthorized access.
2. Look for correlated sign-in risk events such as sign-ins from unfamiliar locations, anonymous IP addresses, or atypical travel.
3. Check if the password was already changed by verifying whether the user changed their password after the date the leak was detected.
4. If the password was changed, the risk might already be self-remediated. If not, confirm the user as compromised and initiate a password reset.
5. If sign-in logs show unauthorized access, or if an attacker has the ability to reset the password or perform MFA, block the user, reset the password, and revoke all refresh tokens.
6. Review for lateral movement by checking the user's recent activity for signs of privilege escalation, new app registrations, mailbox rule changes, or access to sensitive resources.
7. Verify connected accounts: if the user reuses passwords across services, advise the user to change passwords on other services where they use the same credential.

## Validation
A cloud-based password reset triggered by a Microsoft Entra Conditional Access policy fully remediates the user risk for this detection.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
