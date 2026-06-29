# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to remediate and unblock users flagged by Entra ID Identity Protection risk detections?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Identity Protection risk policies configured

## Symptoms
- Users are blocked due to sign-in risk or user risk detections

## Error Codes
N/A

## Root Causes
1. User or sign-in activity flagged as risky by Identity Protection

## Remediation Steps
1. Review the risk detections in the Identity Protection reports
2. Confirm whether the detected risk is genuine or a false positive
3. If genuine, perform password reset or require MFA to remediate user risk
4. If false positive, dismiss the risk or confirm the user as safe
5. Unblock the user by allowing sign-in after remediation

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky users. 3. Verify that the user's risk level is 'None' or that the user no longer appears in the list. 4. Navigate to Protection > Identity Protection > Risky sign-ins. 5. Confirm that the user's recent sign-ins are not flagged as risky. 6. Optionally, use the Microsoft Graph API: GET /identityProtection/riskyUsers?$filter=id eq '{user-object-id}' and check that 'riskLevel' is 'none'.

## Rollback
1. If the user was dismissed as safe but later found to be compromised, re-flag the user as risky: In the Microsoft Entra admin center, go to Protection > Identity Protection > Risky users, select the user, and choose 'Confirm compromised'. 2. If a password reset was performed and the user cannot sign in, reset the password again via Entra admin center > Users > select user > Reset password. 3. If MFA was required and the user cannot register, temporarily disable MFA for the user via Entra admin center > Users > select user > Authentication methods > Require re-register. 4. If the user was unblocked but the risk persists, re-block the user by enabling the risk policy or manually confirming the user as compromised.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
