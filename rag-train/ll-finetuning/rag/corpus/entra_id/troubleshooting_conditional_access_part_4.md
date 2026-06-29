# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How does Conditional Access validate multiple grant controls like MFA, Device State, and Terms of Use when multiple policies apply to a user?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Multiple policies applied to a user requiring MFA, Device State, and ToU

## Symptoms
- Unexpected sign-in failures or interruptions
- Multiple log entries for the same sign-in attempt

## Error Codes
N/A

## Root Causes
1. Conditional Access follows a specific validation order: MFA, Device State, then ToU. If a valid MFA claim is present, a single log shows success for all three. If not, interruptions occur in that order.

## Remediation Steps
1. Ensure the user has a valid MFA claim in the token before expecting Device State or ToU validation
2. If a valid MFA claim is present, a single log entry shows success for MFA, Device State, and ToU

## Validation
Check sign-in logs: if a valid MFA claim is present, expect a single log showing success for MFA, Device State, and ToU.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
