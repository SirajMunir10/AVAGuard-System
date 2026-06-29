# Troubleshooting: Password Reset (ValidationError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve ValidationError during SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** SSPR writeback

## Symptoms
- Received an invalid response from the password-reset web service

## Error Codes
- `ValidationError`

## Root Causes
1. Invalid response from the password-reset web service

## Remediation Steps
1. Try disabling and then re-enabling password writeback

## Validation
1. In the Entra admin center, navigate to Protection > Password reset > Properties and confirm 'Password writeback' is set to 'Yes'. 2. On a test user, initiate a password reset via SSPR and verify the new password is accepted and synced back to on-premises without error. 3. Check the Entra ID audit logs for successful password reset events and no 'ValidationError' entries. 4. Run `Get-ADSyncGlobalSettings | Select-Object -Property *` on the Azure AD Connect server to confirm password writeback is enabled.

## Rollback
1. In the Entra admin center, go to Protection > Password reset > Properties and set 'Password writeback' to 'No', then save. 2. Wait 5 minutes, then set it back to 'Yes' and save. 3. If the issue persists, run `Set-ADSyncGlobalSettings -ParameterName PasswordWritebackEnabled -ParameterValue $false` on the Azure AD Connect server, then `Set-ADSyncGlobalSettings -ParameterName PasswordWritebackEnabled -ParameterValue $true` to re-enable. 4. Restart the Azure AD Connect service with `Restart-Service ADSync`.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
