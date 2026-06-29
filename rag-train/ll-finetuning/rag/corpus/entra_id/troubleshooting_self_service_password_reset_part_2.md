# Troubleshooting: Self-Service Password Reset (SSPR_0014)

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user receives SSPR_0014 error: 'Additional security info is needed to reset your password.' How to resolve?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Self-service password reset with required security info

## Symptoms
- User sees error SSPR_0014
- Message: 'Additional security info is needed to reset your password. To proceed, contact your admin and ask them to reset your password.'

## Error Codes
- `SSPR_0014`

## Root Causes
1. User has not registered sufficient security information for password reset

## Remediation Steps
1. Contact your admin and ask them to reset your password
2. After user can access their account, they can register additional security info at https://aka.ms/ssprsetup
3. Admin can add additional security info to the user's account by following the steps in 'Set and read authentication data for password reset'

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
