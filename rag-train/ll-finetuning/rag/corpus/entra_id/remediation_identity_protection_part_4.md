# Remediation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Remediation

## Scenario / Query
How to dismiss risk for a sign-in or user in Identity Protection after confirming no compromise?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Security Operator role required

## Symptoms
- Risky sign-in or user flagged in Identity Protection

## Error Codes
N/A

## Root Causes
1. Admin investigation confirms no actual risk of compromise

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Security Operator.
2. Browse to Protection > Identity Protection > Risky sign-ins or Risky users.
3. Select the risky activity.
4. Select Dismiss risky sign-in(s) or Dismiss user risk.

## Validation
Risk state changes from 'At risk' to 'Dismissed'; risk detail changes to 'Admin dismissed risk for sign-in' or 'Admin dismissed all risk for user'.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
