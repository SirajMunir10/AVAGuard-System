# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
How to configure Microsoft Entra multifactor authentication registration policy using Microsoft Entra ID Protection to prompt users to register at next interactive sign-in?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with ID Protection enabled
- **Configuration:** Microsoft Entra ID Protection registration policy for MFA

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Microsoft Entra ID Protection to configure the Microsoft Entra multifactor authentication registration policy.
2. Set the policy to prompt users to register the next time they sign in interactively.

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Browse to Protection > Identity Protection > MFA registration policy. 3. Verify that the policy is set to 'On' and that the assignment includes 'All users' or the intended target users. 4. Confirm that the policy control is set to 'Require Azure AD Multi-Factor Authentication registration'. 5. As a test user, sign out and then sign in interactively. Verify that the user is prompted to register for MFA during the sign-in flow. 6. Check the Identity Protection reports (e.g., Risky sign-ins, Users flagged for risk) to ensure no unexpected blocks or errors occur.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Browse to Protection > Identity Protection > MFA registration policy. 3. Set the policy to 'Off' to disable the MFA registration requirement. 4. Alternatively, if the policy should remain on but with different assignments, modify the assignments (e.g., exclude specific users or groups). 5. If users were already prompted and completed registration, no further action is needed. If the policy caused sign-in issues for excluded users, verify their access is restored by having them sign in interactively.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
