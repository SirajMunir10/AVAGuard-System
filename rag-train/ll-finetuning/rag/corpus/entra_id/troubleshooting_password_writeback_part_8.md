# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot password writeback connectivity issues for Microsoft Entra Connect?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Problems with password writeback for Microsoft Entra Connect

## Error Codes
N/A

## Root Causes
1. Network connectivity issues
2. TLS 1.2 not enabled
3. Outdated Microsoft .NET version
4. Microsoft Entra Connect Sync service not running
5. Password writeback feature misconfigured
6. Outdated Microsoft Entra Connect release

## Remediation Steps
1. Confirm network connectivity
2. Check TLS 1.2
3. Update Microsoft .NET 4.8
4. Restart the Microsoft Entra Connect Sync service
5. Disable and re-enable the password writeback feature
6. Install the latest Microsoft Entra Connect release

## Validation
1. Run 'Test-NetConnection -ComputerName passwordwriteback.azure.com -Port 443' to confirm network connectivity. 2. Verify TLS 1.2 is enabled by checking registry: Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client' -Name 'Enabled' (value should be 1). 3. Confirm .NET version is 4.8 or later: Get-ItemPropertyValue -Path 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full' -Name 'Release' (should be >= 528040). 4. Check Microsoft Entra Connect Sync service status: Get-Service -Name 'ADSync' | Select-Object Status (should be 'Running'). 5. Verify password writeback is enabled in Entra Connect: Open Synchronization Service Manager, go to Connectors, select the Entra ID connector, and check 'Enable Password Writeback' is checked. 6. Confirm latest Entra Connect version: (Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Azure AD Connect' -Name 'Version').Version.

## Rollback
1. If network changes were made, revert firewall rules or proxy settings to original state. 2. If TLS 1.2 was enabled, disable it by setting registry 'Enabled' to 0 (caution: may affect other services). 3. If .NET was updated, uninstall the update via 'Programs and Features' or roll back using system restore. 4. If service was restarted, no rollback needed; if service was stopped, start it: Start-Service -Name 'ADSync'. 5. If password writeback was disabled and re-enabled, re-disable it in Synchronization Service Manager if issues persist. 6. If Entra Connect was updated, restore previous version from backup or reinstall older release.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
