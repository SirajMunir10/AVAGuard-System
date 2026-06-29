# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
Why does a Conditional Access policy show a failure for Terms of Use (ToU) in the sign-in logs even though the user accepted it in a previous sign-in?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Multiple grant controls applied to a user, including MFA and ToU

## Symptoms
- Sign-in logs show a failure for ToU
- User reports having accepted ToU previously

## Error Codes
N/A

## Root Causes
1. Conditional Access validates MFA claim first, then ToU. If a valid MFA claim is not in the token, an interrupt occurs for MFA and a failure for ToU is logged, even if ToU was accepted previously.

## Remediation Steps
1. Complete multifactor authentication to generate a valid MFA claim in the token
2. After MFA completion, a second log entry appears validating the ToU

## Validation
After completing MFA, check sign-in logs for a second entry showing success for both MFA and ToU.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
