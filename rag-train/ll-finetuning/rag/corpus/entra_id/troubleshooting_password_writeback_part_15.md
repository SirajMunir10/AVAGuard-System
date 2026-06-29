# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle UnknownError during password management operations?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- UnknownError event indicating an unknown error occurred during a password management operation

## Error Codes
N/A

## Root Causes
1. Unknown error; look at the exception text in the event for more details

## Remediation Steps
1. Look at the exception text in the event for more details
2. Try disabling and then re-enabling password writeback
3. If this doesn't help, include a copy of your event log along with the tracking ID specified when you open a support request

## Validation
1. Check the Microsoft Entra Connect event log for any new UnknownError events. Run: Get-WinEvent -LogName 'Application' | Where-Object { $_.ProviderName -eq 'Password Reset Writeback' -and $_.Id -eq 31001 -and $_.LevelDisplayName -eq 'Error' } | Format-List TimeCreated, Message. 2. Perform a test password reset for a hybrid user and verify success. 3. Confirm password writeback is enabled in Microsoft Entra Connect: Open the Microsoft Entra Connect wizard, select 'View current configuration', and verify 'Password writeback' is set to 'Enabled'.

## Rollback
1. If disabling and re-enabling password writeback caused issues, re-enable it: Open Microsoft Entra Connect, select 'Customize synchronization options', navigate to 'Optional features', check 'Password writeback', and complete the wizard. 2. If the issue persists, collect the event log and tracking ID: Export the Application event log filtered by provider 'Password Reset Writeback' using: Get-WinEvent -LogName 'Application' | Where-Object { $_.ProviderName -eq 'Password Reset Writeback' } | Export-Csv -Path 'PasswordWritebackLogs.csv'. 3. Open a support request with Microsoft, providing the exported logs and tracking ID from the UnknownError event.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
