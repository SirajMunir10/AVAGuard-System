# Troubleshooting: Password Reset Writeback (ReportServiceHealthError)

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot ReportServiceHealthError event in SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback configuration

## Symptoms
- Error when sending heartbeat data to password-reset web service

## Error Codes
- `ReportServiceHealthError`

## Root Causes
1. Error when sending health information back to the cloud web service

## Remediation Steps
N/A

## Validation
1. On the Entra Connect server, open Event Viewer and navigate to Applications and Services Logs > Microsoft > AzureADConnect > PasswordResetService > Operations. Verify no new ReportServiceHealthError events appear after remediation. 2. Run the PowerShell command: Get-ADSyncGlobalSettings | Where-Object {$_.Name -like '*PasswordReset*'} to confirm SSPR writeback settings are correct. 3. Trigger a test SSPR writeback by resetting a user's password from the Entra admin center and confirm the password is written back to on-premises AD.

## Rollback
1. If the issue persists, restore the original Entra Connect configuration by running the Entra Connect wizard and selecting 'Customize synchronization options' to re-apply previous settings. 2. Revert any changes made to the service account permissions for the AD DS connector account by resetting its permissions to the default using the 'Set-ADSyncPasswordResetConfiguration' cmdlet with the -ResetPermissions parameter. 3. If a hotfix or update was applied, uninstall it via Programs and Features and reinstall the previous version of Entra Connect from a backup.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
