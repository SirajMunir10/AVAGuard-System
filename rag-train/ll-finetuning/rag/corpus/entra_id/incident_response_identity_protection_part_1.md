# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate and remediate user risk detected by Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based Conditional Access policy configured

## Symptoms
- Risk detected for a user account
- Suspicious sign-in activity identified

## Error Codes
N/A

## Root Causes
1. User activity may be anomalous or compromised

## Remediation Steps
1. First, attempt self-remediation via self-service password reset or risk-based Conditional Access policy flow
2. If self-remediation is not an option, administrator should remediate by invoking a password reset
3. Require user to reregister for MFA
4. Block the user
5. Revoke user sessions

## Validation
Check the sign-in logs and validate whether the activity is normal for the given user. Look at the user's past activities including: Application, Device (registered or compliant), Location, IP address, User agent string.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
