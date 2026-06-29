# Troubleshooting: Outlook Connectivity

**Domain:** Exchange Online
**Subdomain:** Outlook Connectivity
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose and fix common Outlook connectivity issues using automated tools or manual steps?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Outlook client configuration

## Symptoms
- Outlook connection problems

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Support and Recovery Assistant for Microsoft 365 to diagnose and fix common Outlook connectivity issues.
2. If the automated tool cannot fix the issue, refer to the next section for manual troubleshooting.

## Validation
1. Run the Microsoft Support and Recovery Assistant (SaRA) from https://aka.ms/SaRA and select 'Outlook for Windows' > 'I'm having problems with Outlook connecting to Exchange' to confirm the tool reports no issues. 2. Open Outlook and verify it connects to Exchange Online by checking the connection status (Ctrl+Right-click the Outlook icon in the notification area, select 'Connection Status' and confirm all columns show 'Connected' or 'OK'). 3. Send a test email to yourself and confirm delivery within a few minutes.

## Rollback
1. If SaRA made changes, run SaRA again and select 'Undo changes' if prompted. 2. Manually revert any configuration changes made during troubleshooting: a. Reset Outlook profiles via Control Panel > Mail > Show Profiles > select profile > Properties > Email Accounts > Repair or Remove/Add account. b. Clear cached credentials in Windows Credential Manager under 'Windows Credentials' for entries containing 'MicrosoftOffice' or 'Outlook'. c. Re-enable any disabled add-ins by going to File > Options > Add-ins > Manage COM Add-ins > check all previously disabled items. d. Restore any modified registry keys from backup if available (e.g., HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\RPC).

## References
- <https://learn.microsoft.com/en-us/exchange/troubleshoot/outlook-connectivity/outlook-connection-issues>
