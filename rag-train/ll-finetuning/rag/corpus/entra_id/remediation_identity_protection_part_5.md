# Remediation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Remediation

## Scenario / Query
How to remediate risky users or unblock them after risk investigation in Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based policies configured for automatic remediation or manual user risk status update

## Symptoms
- Users are blocked due to user risk
- Risky users identified after risk investigation

## Error Codes
N/A

## Root Causes
1. User risk detected by Identity Protection
2. Risk-based policies blocking users automatically

## Remediation Steps
1. Set up risk-based policies to enable automatic remediation
2. Manually update the user's risk status

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky users. 3. Confirm that the user's risk level is 'None' or 'Low' after remediation. 4. If a risk-based policy was configured, verify the policy is enabled and set to 'Allow access' or 'Require password change' (not 'Block access') for the user's risk level. 5. Ask the user to attempt sign-in and confirm they are not blocked.

## Rollback
1. If automatic remediation via a risk-based policy caused issues, disable or modify the policy: navigate to Protection > Identity Protection > Risk policies > User risk policy, set 'User risk' to 'High' and 'Access' to 'Block access', then save. 2. If a user was manually unblocked but should remain blocked, navigate to Protection > Identity Protection > Risky users, select the user, and choose 'Confirm user compromised' to reset their risk level to 'High' and re-block access. 3. If a password reset was required but not completed, the user may need to reset their password via self-service password reset (SSPR) or an admin can reset it.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
