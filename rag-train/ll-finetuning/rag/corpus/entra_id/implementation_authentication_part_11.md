# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to enable Microsoft Entra multifactor authentication for users in a Microsoft Entra ID Free tenant?

## Environment Context
- **Tenant Type:** Microsoft Entra ID Free
- **Configuration:** Security defaults enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you use a Microsoft Account, register for multifactor authentication.
2. If you aren't using a Microsoft Account, turn on multifactor authentication for a user or group in Microsoft Entra ID.

## Validation
1. Sign in to the Microsoft Entra admin center as a Global Administrator.
2. Browse to Identity > Users > All users.
3. Select the user(s) for whom MFA was enabled.
4. Under the user's profile, select 'Authentication methods'.
5. Verify that 'Multifactor authentication' status shows 'Enabled' or 'Enforced'.
6. Alternatively, run the following PowerShell command to confirm MFA status for a user:
   Get-MsolUser -UserPrincipalName <user@domain.com> | Select-Object -Property UserPrincipalName, StrongAuthenticationRequirements
   If the StrongAuthenticationRequirements property is not empty, MFA is enabled.
7. Test by signing in as the user and verifying that an MFA prompt (e.g., phone call, text, or authenticator app) is presented.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Global Administrator.
2. Browse to Identity > Users > All users.
3. Select the user(s) for whom MFA was enabled.
4. Under the user's profile, select 'Authentication methods'.
5. Click 'Manage' next to 'Multifactor authentication' and select 'Disabled'.
6. Alternatively, run the following PowerShell command to disable MFA for a user:
   Set-MsolUser -UserPrincipalName <user@domain.com> -StrongAuthenticationRequirements @()
7. If MFA was enabled via a conditional access policy, remove or disable the policy:
   - Browse to Identity > Protection > Conditional Access.
   - Locate the policy that enforces MFA.
   - Set the policy to 'Off' or delete it.
8. Verify that the user can now sign in without an MFA prompt.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing>
