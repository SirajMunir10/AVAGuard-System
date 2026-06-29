# Troubleshooting: Self-Service Password Reset (SSPR_0013)

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user receives SSPR_0013 error: 'You aren't a member of a group enabled for password reset' or 'UserNotProperlyConfigured = 14' with message 'We're sorry, you can't reset your password at this time because necessary information is missing from your account.' How to resolve?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Self-service password reset enabled for specific groups

## Symptoms
- User sees error SSPR_0013
- User sees error code UserNotProperlyConfigured = 14
- Message: 'We're sorry, you can't reset your password at this time because necessary information is missing from your account.'

## Error Codes
- `SSPR_0013`
- `UserNotProperlyConfigured = 14`

## Root Causes
1. User is not a member of a group enabled for password reset
2. Necessary security information is missing from the user's account

## Remediation Steps
1. Contact your admin and request to be added to the group enabled for password reset
2. Admin can reset the user's password for them
3. After user can access their account, they need to register the necessary information by following the steps in the 'Register for self-service password reset' article

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
