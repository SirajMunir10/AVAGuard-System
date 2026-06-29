# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to enable Microsoft Entra multifactor authentication using security defaults for all Microsoft 365 plans?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** All Microsoft 365 plans support enabling Microsoft Entra multifactor authentication using security defaults.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Microsoft Entra multifactor authentication for all users using security defaults.
2. Manage Microsoft Entra multifactor authentication through the Microsoft 365 portal.
3. For an improved user experience, upgrade to Microsoft Entra ID P1 or P2 and use Conditional Access.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator.
2. Navigate to Identity > Overview > Properties.
3. Under Security defaults, select Manage security defaults.
4. Verify that Security defaults is set to Enabled.
5. Confirm that all users are now prompted to register for Microsoft Entra multifactor authentication (MFA) within 14 days.
6. Optionally, sign in as a test user and verify that MFA registration is required before accessing Microsoft 365 services.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator.
2. Navigate to Identity > Overview > Properties.
3. Under Security defaults, select Manage security defaults.
4. Set Security defaults to Disabled (not recommended).
5. If you have Microsoft Entra ID P1 or P2 licenses, consider creating a Conditional Access policy to enforce MFA instead of disabling security defaults entirely.
6. Monitor user access and authentication logs to ensure no disruption occurs after the change.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing>
