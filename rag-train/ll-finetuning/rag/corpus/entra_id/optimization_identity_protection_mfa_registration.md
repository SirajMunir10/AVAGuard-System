# Optimization: Identity Protection â€“ MFA Registration

**Domain:** Entra ID
**Subdomain:** Identity Protection â€“ MFA Registration
**Incident Type:** Optimization

## Scenario / Query
How can I optimize my tenant by identifying and reducing stale or unused MFA registration states to improve security posture and reduce administrative overhead?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) P2
- **Configuration:** Identity Protection MFA registration policy enabled; users may have registered MFA methods that are no longer used or valid

## Symptoms
- High number of users with registered MFA methods that have not been used in over 90 days
- Users with multiple registered methods (e.g., phone, authenticator app, FIDO2 key) where some methods are outdated or unused
- Administrative overhead from managing stale MFA registrations

## Error Codes
N/A

## Root Causes
1. Users do not remove old or unused authentication methods after changing devices or phone numbers
2. No automated process to detect and prompt users to review or remove stale MFA methods
3. Identity Protection MFA registration policy does not include a mechanism to enforce periodic re-registration or cleanup

## Remediation Steps
1. Use the Microsoft Graph API or Entra admin center to run a report of users' registered authentication methods and their last used dates
2. Identify users whose MFA methods have not been used in the last 90 days and consider removing those methods or prompting users to re-register
3. Configure the Identity Protection MFA registration policy to require re-registration after a defined period (e.g., 180 days) to ensure methods are current
4. Implement a user communication campaign to encourage removal of unused methods and adoption of phishing-resistant methods (e.g., FIDO2 security keys or Windows Hello for Business)

## Validation
After cleanup, run the same report and confirm that no registered authentication method has a last used date older than 90 days. Verify that the MFA registration policy is set to require re-registration every 180 days.

## Rollback
If a user is unable to authenticate after method removal, the administrator can re-add a temporary authentication method via the Entra admin center or guide the user through self-service password reset (SSPR) to re-register.

## References
- Microsoft Learn: 'Manage authentication methods for Microsoft Entra ID' â€“ https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage
- CIS Microsoft Azure Foundations Benchmark v2.0.0 â€“ Control 1.10: 'Ensure that Microsoft Entra ID Identity Protection MFA registration policy is enabled'
