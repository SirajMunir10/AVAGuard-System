# Hardening: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Hardening

## Scenario / Query
How to secure the MFA registration process against compromised passwords?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant
- **Configuration:** Conditional Access policies, Temporary Access Pass

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
1. If a user's password is compromised, it could be used to register for MFA, taking control of their account.

## Remediation Steps
1. Secure the security registration process with Conditional Access policies requiring trusted devices and locations.
2. Further secure the process by also requiring a Temporary Access Pass.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Confirm that a policy targeting 'Microsoft Azure Multi-Factor Authentication' or 'Security registration' cloud app exists with conditions requiring trusted devices (e.g., 'Device state' set to 'Hybrid Azure AD joined' or 'Compliant') and trusted locations (e.g., 'Locations' configured with 'All trusted locations'). 4. Verify that the policy grants access only when these conditions are met and blocks access otherwise. 5. Additionally, confirm that a separate policy or the same policy requires 'Temporary Access Pass' as an authentication strength (e.g., under 'Grant' > 'Require authentication strength' > select a custom strength that includes 'Temporary Access Pass'). 6. Test by attempting to register for MFA from an untrusted device or location without a Temporary Access Pass; the attempt should be blocked.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy that enforces trusted devices and locations for security registration. 4. Set the policy to 'Off' or delete it. 5. Locate the policy that requires Temporary Access Pass for security registration. 6. Set that policy to 'Off' or delete it. 7. Verify that users can now register for MFA from any device or location without a Temporary Access Pass.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
