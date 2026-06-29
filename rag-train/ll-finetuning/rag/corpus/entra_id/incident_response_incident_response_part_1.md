# Incident Response: Incident Response (50058 â€“ Microsoft Entra ID sign-in error indicating a failed authentication attempt)

**Domain:** Entra ID
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
An administrator reports that a user in your tenant received a suspicious sign-in notification from an unfamiliar location. How do you triage and respond using Entra ID Identity Protection and sign-in logs?

## Environment Context
- **Tenant Type:** Microsoft Entra ID P2 licensed tenant
- **Configuration:** Identity Protection enabled, risky sign-in policies configured to require MFA or block access

## Symptoms
- User reports receiving 'Unusual sign-in activity' email from Microsoft
- Sign-in log shows a failed authentication attempt from an IP address in an unexpected geographic region
- Identity Protection risk detection flagged as 'Anonymous IP address' or 'Unfamiliar sign-in properties'

## Error Codes
- `50058 â€“ Microsoft Entra ID sign-in error indicating a failed authentication attempt`

## Root Causes
1. Attacker obtained user credentials through phishing or credential stuffing
2. No conditional access policy blocking sign-ins from untrusted locations

## Remediation Steps
1. 1. Investigate the sign-in log: Navigate to Azure AD > Sign-in logs, filter by the affected user and time range, review authentication details and risk level.
2. 2. Confirm the user's password has been changed immediately and enforce MFA re-registration if needed.
3. 3. Revoke all refresh tokens and session tokens for the user via Azure AD > Users > [user] > Revoke sessions.
4. 4. Review and strengthen Conditional Access policies: Add a policy to block sign-ins from high-risk locations or require MFA for risky sign-ins.
5. 5. Use Identity Protection to confirm the risk level and dismiss or confirm compromise as appropriate.
6. 6. Enable risk-based policies: Require password change for high-risk users and MFA for medium-risk sign-ins.

## Validation
Confirm that the user can sign in successfully after password reset and that no further anomalous sign-ins appear in the logs. Verify that the Conditional Access policy blocks sign-ins from the suspicious location.

## Rollback
If the user cannot sign in after password reset, temporarily disable the risky sign-in policy to allow access while further investigation is performed. Re-enable the policy once the issue is resolved.

## References
- Microsoft Entra ID documentation: 'Investigate risk detections' â€“ https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk
