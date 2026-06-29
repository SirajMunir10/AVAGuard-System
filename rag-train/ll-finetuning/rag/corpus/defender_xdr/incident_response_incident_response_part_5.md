# Incident Response: Incident Response

**Domain:** Defender XDR
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I investigate and remediate a suspicious sign-in from an unfamiliar location that triggered an automated investigation in Microsoft 365 Defender?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Office 365 Plan 2
- **Configuration:** Automated investigation and response (AIR) enabled for Office 365

## Symptoms
- User reports receiving multiple MFA prompts
- Microsoft 365 Defender alerts on 'Atypical travel' or 'Unfamiliar sign-in properties'
- Automated investigation created an incident with high severity

## Error Codes
N/A

## Root Causes
1. Compromised user credentials used from an unfamiliar IP address or location
2. No conditional access policy blocking sign-ins from untrusted locations

## Remediation Steps
1. Review the automated investigation details in the Microsoft 365 Defender portal under Incidents & alerts > Incidents
2. Confirm the user account is compromised and reset the user's password immediately
3. Revoke all refresh tokens and sessions for the affected user via Azure AD PowerShell: Revoke-AzureADUserAllRefreshToken -ObjectId <user-object-id>
4. Enable MFA if not already enforced
5. Create a conditional access policy to block sign-ins from untrusted locations as documented in 'Conditional Access: Block access by location'

## Validation
Verify that the user can sign in with the new password and that no further suspicious sign-ins appear in the Azure AD sign-in logs.

## Rollback
If the password reset was performed in error, the user can be re-enabled with their previous password only if it is still known and the account is not compromised; otherwise, a new reset is required.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/investigate-compromised-accounts?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-location>
