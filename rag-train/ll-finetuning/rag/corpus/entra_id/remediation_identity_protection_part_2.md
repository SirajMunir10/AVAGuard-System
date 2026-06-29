# Remediation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Remediation

## Scenario / Query
How does a user self-remediate their user risk by performing a secure password change in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection enabled
- **Configuration:** User risk policy with 'Require password change' grant control configured

## Symptoms
- User is prompted to perform a secure password change
- User risk state shows 'At risk' before remediation

## Error Codes
N/A

## Root Causes
1. User risk policy with 'Require password change' grant control is configured
2. User is at risk and needs to remediate by changing password

## Remediation Steps
1. User must first complete multifactor authentication
2. User then changes their password
3. This process does not use the self-service password reset (SSPR) flow
4. Once the password is changed, user risk is remediated and the user can proceed to sign in with their new password

## Validation
Risk state updates from 'At risk' to 'Remediated'; Risk detail updates from '-' to 'User performed secured password reset'

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
