# Troubleshooting: Pass-through Authentication

**Domain:** Entra ID
**Subdomain:** Pass-through Authentication
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot an unexpected error during Pass-through Authentication agent operation?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Pass-through Authentication agent

## Symptoms
- An unexpected error occurred

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Collect agent logs from the server
2. Contact Microsoft Support with your issue

## Validation
1. On the server running the Pass-through Authentication agent, open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > AzureADConnect > AuthenticationAgent > Admin'. Verify that no new 'UnexpectedError' events (Event ID 2) appear after remediation.
2. Run the PowerShell command: Get-Service 'AzureADConnectAuthenticationAgent' | Format-List Status, StartType. Confirm the service status is 'Running' and start type is 'Automatic'.
3. From a domain-joined client, trigger a user sign-in and confirm no 'An unexpected error occurred' prompt appears.
4. Review the agent logs at 'C:\ProgramData\Microsoft\Azure AD Connect Authentication Agent\Trace\' for the latest .etl file. Use Get-WinEvent -Path <logfile.etl> -Oldest | Where-Object { $_.LevelDisplayName -eq 'Error' } to verify no new error entries.

## Rollback
1. If the agent service is not running, run: Start-Service 'AzureADConnectAuthenticationAgent'.
2. If the service fails to start, reinstall the agent using the Azure AD Connect wizard: On the Azure AD Connect server, run the wizard, select 'Change user sign-in', uncheck 'Pass-through authentication', complete the wizard, then re-run and re-enable it.
3. If the issue persists, restore the agent configuration from a backup of the 'C:\ProgramData\Microsoft\Azure AD Connect Authentication Agent\' folder (if available) and restart the service.
4. As a last resort, disable Pass-through Authentication via the Azure AD Connect wizard and switch to Password Hash Synchronization temporarily, then contact Microsoft Support as per the remediation steps.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
