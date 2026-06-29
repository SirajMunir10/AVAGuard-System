# Remediation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Remediation

## Scenario / Query
How to generate a temporary password to remediate a risky user in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** User Administrator role required for password reset from user details; Security Operator and User Administrator roles required from ID Protection

## Symptoms
- User risk state is 'At risk'
- User needs immediate remediation to bring identity back to safe state

## Error Codes
N/A

## Root Causes
1. User identity is compromised or at risk as detected by Identity Protection

## Remediation Steps
1. Sign in to the Microsoft Entra admin center.
2. Browse to Protection > Identity Protection > Risky users, and select the affected user. Alternatively, browse to Users > All users, and select the affected user.
3. Select Reset password.
4. Review the message and select Reset password again.
5. Provide the temporary password to the user. The user must change their password the next time they sign-in.

## Validation
Risk state changes from 'At risk' to 'Remediated'; Risk detail changes from '-' to 'Admin generated temporary password for user'

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
