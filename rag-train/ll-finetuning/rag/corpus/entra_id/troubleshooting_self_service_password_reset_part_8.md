# Troubleshooting: Self-Service Password Reset

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports the error 'Your administrator has not enabled you to use this feature' when attempting to reset their password. How do I resolve this?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Self-service password reset enabled configuration

## Symptoms
- User sees error: 'Your administrator has not enabled you to use this feature.'

## Error Codes
N/A

## Root Causes
1. The directory isn't enabled for password reset.

## Remediation Steps
1. In the Microsoft Entra admin center, change the Self-service password reset enabled configuration to Selected or All.
2. Select Save.

## Validation
1. Sign in to the Microsoft Entra admin center as a Global Administrator. 2. Browse to Protection > Password reset > Properties. 3. Confirm that the 'Self-service password reset enabled' setting is set to 'Selected' or 'All'. 4. If set to 'Selected', verify the affected user is included in the selected group. 5. Ask the user to navigate to https://passwordreset.microsoftonline.com and attempt to reset their password. 6. Confirm the user no longer sees the error 'Your administrator has not enabled you to use this feature.'

## Rollback
1. Sign in to the Microsoft Entra admin center as a Global Administrator. 2. Browse to Protection > Password reset > Properties. 3. Change the 'Self-service password reset enabled' setting back to 'None'. 4. Select 'Save'. 5. Inform the user that the change has been reverted and they will again see the error when attempting password reset.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
