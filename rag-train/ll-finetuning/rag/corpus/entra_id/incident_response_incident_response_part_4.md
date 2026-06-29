# Incident Response: Incident Response

**Domain:** Entra ID
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I respond to a detected sign-in risk event indicating a user account may be compromised in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID P2 licensed tenant with Identity Protection enabled
- **Configuration:** Sign-in risk policies set to medium and above; user risk policies enabled

## Symptoms
- Identity Protection reports a sign-in risk event (e.g., atypical travel, anonymous IP address, or unfamiliar sign-in properties) for a user account
- User reports suspicious activity or inability to sign in
- Security team receives an alert from Microsoft Defender for Cloud Apps or Microsoft Sentinel correlating the risk event

## Error Codes
N/A

## Root Causes
1. User credentials may have been compromised through phishing, password reuse, or malware
2. Attacker may have gained access to the user's device or network and performed a sign-in from an unusual location or device

## Remediation Steps
1. Confirm the risk event in the Microsoft Entra admin center under Identity Protection > Risky sign-ins
2. If the sign-in is confirmed as risky, immediately revoke the user's sessions and require a password reset by navigating to Identity Protection > Risky users, selecting the user, and choosing 'Confirm user compromised' then 'Reset password'
3. Enable multi-factor authentication (MFA) for the user if not already enforced, following guidance in 'Plan your Microsoft Entra ID MFA deployment'
4. Investigate and remediate any compromised devices using Microsoft Intune or Microsoft Defender for Endpoint
5. Review and revoke any suspicious application permissions or delegated admin roles granted to the user

## Validation
Verify that the user can sign in with the new password and that no further risky sign-ins are reported for that user within 24 hours. Check Identity Protection reports for zero new risk events.

## Rollback
If the password reset was performed in error, the user can be allowed to use their previous password only if it was not compromised; otherwise, a new password must be set. Session revocation can be reversed by reissuing tokens via a new sign-in.

## References
- Microsoft Learn, 'Plan your Microsoft Entra ID MFA deployment' - https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted
