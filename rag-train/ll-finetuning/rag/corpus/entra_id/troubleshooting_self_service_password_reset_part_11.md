# Troubleshooting: Self-Service Password Reset (TenantSSPRFlagDisabled = 9)

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user sees error 'We're sorry, you can't reset your password at this time because your administrator has disabled password reset for your organization.' What is the cause and how to resolve?

## Environment Context
- **Tenant Type:** Microsoft Entra
- **Configuration:** SSPR feature enabled/disabled

## Symptoms
- User cannot reset password
- Error message: 'We're sorry, you can't reset your password at this time because your administrator has disabled password reset for your organization.'

## Error Codes
- `TenantSSPRFlagDisabled = 9`
- `SSPR_0009: We've detected that password reset hasn't been enabled by your administrator.`

## Root Causes
1. The SSPR feature is disabled for the tenant.

## Remediation Steps
1. Contact your admin and ask them to enable this feature.

## Validation
1. Sign in to the Microsoft Entra admin center as a Global Administrator. 2. Browse to Identity > Users > Password reset. 3. Verify that 'Self-service password reset enabled' is set to 'Selected' or 'All' (not 'None'). 4. If set to 'Selected', confirm the user's group is included. 5. As a test user, navigate to https://passwordreset.microsoftonline.com and attempt a password reset; confirm no SSPR-disabled error appears.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Global Administrator. 2. Browse to Identity > Users > Password reset. 3. Set 'Self-service password reset enabled' back to 'None'. 4. Confirm the change by navigating to https://passwordreset.microsoftonline.com as a test user and verifying the original error message reappears.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
