# Troubleshooting: Password Reset (ADUserIncorrectPassword)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback failure due to incorrect current password during a change operation?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with SSPR writeback
- **Configuration:** Password writeback enabled

## Symptoms
- Password change operation fails
- Event indicating incorrect current password

## Error Codes
- `ADUserIncorrectPassword`

## Root Causes
1. User specified an incorrect current password when performing a password change operation

## Remediation Steps
1. Specify the correct current password and try again

## Validation
1. Confirm the user's current password is correct by performing a test authentication using the Microsoft Entra admin center or PowerShell (e.g., Connect-MgGraph -Scopes 'User.Read.All'; Get-MgUser -UserId <user-id> -Property UserPrincipalName, PasswordPolicies).
2. Initiate a password change operation with the correct current password via the SSPR portal (https://passwordreset.microsoftonline.com) or Microsoft Graph API (e.g., POST /users/{id}/changePassword with currentPassword and newPassword).
3. Verify the operation succeeds by checking the audit logs in Microsoft Entra admin center under 'Monitoring & health' > 'Audit logs' for a successful 'Change password (self-service)' event.
4. Confirm the password writeback succeeded by reviewing the Microsoft Entra Connect Health or on-premises AD event logs for a successful password writeback event (e.g., Event ID 31000 in the ADSync service).

## Rollback
1. If the password change operation fails again due to an incorrect current password, instruct the user to verify their current password by signing in to a known working application (e.g., Outlook Web Access) or contacting their helpdesk for password reset.
2. If the user cannot recall their current password, initiate a password reset (not change) via the SSPR portal or Microsoft Graph API (e.g., POST /users/{id}/resetPassword) to set a new password without requiring the current password.
3. After reset, ensure the new password is written back to on-premises AD by checking the Microsoft Entra Connect Health or ADSync event logs for a successful writeback event.
4. If writeback continues to fail, temporarily disable password writeback in Microsoft Entra admin center under 'Password reset' > 'On-premises integration' > 'Write back passwords' and re-enable after verifying connectivity and permissions.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
