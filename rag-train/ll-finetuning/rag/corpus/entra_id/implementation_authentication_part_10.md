# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to enable multifactor authentication for Office 365 free Microsoft Entra ID Free tenants?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Office 365 free Microsoft Entra ID Free tenants can use security defaults to prompt users for multifactor authentication.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use security defaults to prompt users for multifactor authentication as needed.
2. Note that you don't have granular control of enabled users or scenarios, but it does provide that additional security step.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator. 2. Navigate to Identity > Overview > Properties. 3. Under Security defaults, select Manage security defaults. 4. Verify that Security defaults is set to Enabled. 5. Sign out and sign in again as a test user. 6. Confirm that the user is prompted to register for multifactor authentication (MFA) and then to provide a second verification method during sign-in. 7. Check the sign-in logs (Identity > Monitoring & health > Sign-in logs) for the test user to see that MFA was required.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator. 2. Navigate to Identity > Overview > Properties. 3. Under Security defaults, select Manage security defaults. 4. Set Security defaults to Disabled. 5. Confirm the change by selecting Yes. 6. Notify users that MFA prompts will no longer be enforced by security defaults.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing>
