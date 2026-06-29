# Troubleshooting: Password Reset (ConfigurationError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve ConfigurationError during SSPR writeback onboarding?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** SSPR writeback

## Symptoms
- Error saving tenant-specific information in a configuration file in your on-premises environment
- Error reading the configuration file when the service was started

## Error Codes
- `ConfigurationError`

## Root Causes
1. Error saving the configuration file
2. Error reading the configuration file

## Remediation Steps
1. Try disabling and then re-enabling password writeback to force a rewrite of the configuration file

## Validation
1. Sign in to the Entra admin center as a Global Administrator. 2. Navigate to Protection > Password reset > On-premises integration. 3. Set the 'Write back passwords to your on-premises directory' toggle to No and save. 4. Wait 5 minutes. 5. Set the toggle back to Yes and save. 6. Wait 10 minutes. 7. On the Entra Connect server, open PowerShell as Administrator and run: `Get-ADSyncGlobalConfiguration | Select-Object -ExpandProperty PasswordWritebackConfiguration`. 8. Verify the output shows a valid configuration (e.g., `Enabled : True` and no error messages). 9. Trigger a test SSPR for a user and confirm the password is written back successfully.

## Rollback
1. If the remediation fails, sign in to the Entra admin center as a Global Administrator. 2. Navigate to Protection > Password reset > On-premises integration. 3. Set the 'Write back passwords to your on-premises directory' toggle to the original state (if known) or leave it as No. 4. On the Entra Connect server, open PowerShell as Administrator and run: `Set-ADSyncGlobalConfiguration -PasswordWritebackEnabled $false`. 5. Restart the Microsoft Azure AD Sync service: `Restart-Service -Name 'ADSync'`. 6. If the issue persists, restore the original configuration file from backup (if available) or re-run the Entra Connect wizard to repair the installation.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
