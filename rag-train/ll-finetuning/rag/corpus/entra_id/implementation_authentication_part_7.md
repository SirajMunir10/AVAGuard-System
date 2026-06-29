# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to determine which Microsoft Entra multifactor authentication license is needed for an organization?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Licensing options include Microsoft Entra ID Free, Microsoft Entra ID P1, Microsoft Entra ID P2, Microsoft 365 Business Premium, EMS E3/E5, Microsoft 365 E3/E5, and Office 365 free tier.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the available versions of Microsoft Entra multifactor authentication based on your organization's needs.
2. Check if your tenant is entitled to basic multifactor authentication features by using security defaults.
3. Determine if you have a license that includes advanced Microsoft Entra multifactor authentication, such as Microsoft Entra ID P1 or P2.
4. For Microsoft Entra External ID, note that the first 50,000 monthly active users can use MFA and other Premium P1 or P2 features for free.
5. Refer to the table in the documentation for details on different ways to get Microsoft Entra multifactor authentication and features for each license.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator. 2. Navigate to Identity > Overview > Properties. 3. Under 'Licenses', review the list of assigned licenses (e.g., Microsoft Entra ID P1, P2, Microsoft 365 Business Premium). 4. Go to Identity > Users > All users, select a test user, and under 'Licenses' confirm the user has a license that includes Microsoft Entra multifactor authentication (e.g., Microsoft Entra ID P1 or P2). 5. Navigate to Identity > External Identities > Overview and verify that the tenant's monthly active users for External ID are within the first 50,000 (if applicable) to confirm free MFA entitlement. 6. Check Identity > Security > Security defaults to see if basic MFA is enabled (indicates entitlement to basic MFA features).

## Rollback
1. If an incorrect license was assigned, remove the license from the user: In the Microsoft Entra admin center, go to Identity > Users > All users, select the user, select 'Licenses', then 'Remove license'. 2. If security defaults were enabled incorrectly, disable them: Navigate to Identity > Security > Security defaults, set 'Enable security defaults' to 'No', and save. 3. If a license purchase was made in error, contact your licensing partner or Microsoft support to cancel or downgrade the subscription. 4. Revert any changes to External ID configuration by adjusting the monthly active user settings or disabling the external collaboration features if they were enabled for MFA testing.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing>
