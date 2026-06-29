# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to set up combined registration for SSPR and Microsoft Entra multifactor authentication?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Combined registration experience for SSPR and MFA

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Inform users about upcoming changes, registration requirements, and any necessary user actions.
2. Provide communication templates and user documentation to prepare users for the new experience and help ensure a successful rollout.
3. Direct users to https://myprofile.microsoft.com to register by selecting the Security Info link on that page.

## Validation
1. Verify that the combined registration experience is enabled: Navigate to Microsoft Entra admin center > Protection > Multifactor authentication > Registration campaign. Confirm that 'State' is set to 'Microsoft managed' or 'Enabled' and 'Combined registration' is turned on. 2. Test user registration: Sign in as a test user at https://myprofile.microsoft.com, select Security Info, and confirm that both MFA and SSPR methods can be added in a single flow. 3. Check audit logs: In Microsoft Entra admin center > Identity > Monitoring & health > Audit logs, filter by activity 'User registered security info' and verify entries for combined registration.

## Rollback
1. Disable combined registration: In Microsoft Entra admin center > Protection > Multifactor authentication > Registration campaign, set 'State' to 'Disabled' or 'Not configured'. 2. Revert to separate registration experiences: Ensure that SSPR registration remains enabled under Protection > Password reset > Properties, and MFA registration remains available via per-user MFA or Conditional Access. 3. Notify users: Inform users that they must register separately for SSPR and MFA using the previous methods (e.g., https://aka.ms/mfasetup for MFA and https://aka.ms/ssprsetup for SSPR).

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
