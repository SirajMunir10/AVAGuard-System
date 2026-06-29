# Troubleshooting: Password Reset

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that Microsoft .NET Framework 4.8 or higher is enabled on the Sync Server for SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Sync Server with SSPR writeback enabled

## Symptoms
- SSPR writeback not functioning
- Password writeback failures

## Error Codes
N/A

## Root Causes
1. Microsoft .NET Framework 4.8 or higher not enabled on the Sync Server

## Remediation Steps
1. Query the registry using PowerShell to check if .NET is already installed
2. Download .NET framework if not installed

## Validation
On the sync server, open PowerShell as Administrator and run: Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full' -Name Release. Verify the Release value is 528040 or greater (indicating .NET Framework 4.8 or later). If the value is missing or less than 528040, .NET 4.8 or higher is not enabled.

## Rollback
If the .NET Framework installation causes issues, uninstall it via 'Control Panel > Programs and Features' or run the following PowerShell command as Administrator: Get-WmiObject -Class Win32_Product | Where-Object {$_.Name -like '*Microsoft .NET Framework 4.8*'} | ForEach-Object {$_.Uninstall()}. Then restart the sync server and verify SSPR writeback functionality returns to its previous state.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
