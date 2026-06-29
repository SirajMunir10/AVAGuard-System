# Troubleshooting: Password Reset

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to check if TLS 1.2 is enabled on the Entra Connect Sync Server for SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Entra Connect Sync Server

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run PowerShell Script to check TLS 1.2 on Entra Connect Server. Make sure to run the script in Admin Mode.
2. Check that the output from the check script looks like the following image (the path, name and value columns) to be enabled correctly.
3. If it doesn't, run the PowerShell Script to enable TLS 1.2 on Entra Connect Server.
4. Then reboot the server, and run script to check TLS 1.2 again.

## Validation
Run the following PowerShell script in an elevated (Admin) PowerShell session on the Entra Connect Sync Server to verify TLS 1.2 is enabled:

```powershell
# Check TLS 1.2 registry settings
$tls12Path = 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client'
$tls12ServerPath = 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server'

Write-Host 'Checking TLS 1.2 Client settings...'
Get-ItemProperty -Path $tls12Path -Name 'Enabled' -ErrorAction SilentlyContinue
Get-ItemProperty -Path $tls12Path -Name 'DisabledByDefault' -ErrorAction SilentlyContinue

Write-Host 'Checking TLS 1.2 Server settings...'
Get-ItemProperty -Path $tls12ServerPath -Name 'Enabled' -ErrorAction SilentlyContinue
Get-ItemProperty -Path $tls12ServerPath -Name 'DisabledByDefault' -ErrorAction SilentlyContinue
```

Confirm that the output shows:
- `Enabled` = 1 (DWORD)
- `DisabledByDefault` = 0 (DWORD)

for both Client and Server paths. If these values are not present or incorrect, TLS 1.2 is not properly enabled.

## Rollback
If the remediation (enabling TLS 1.2) causes issues, revert the registry changes by running the following PowerShell script in an elevated session:

```powershell
# Rollback TLS 1.2 registry settings to default (disabled)
$tls12ClientPath = 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client'
$tls12ServerPath = 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server'

# Remove the TLS 1.2 keys entirely (or set to default disabled values)
Remove-Item -Path $tls12ClientPath -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path $tls12ServerPath -Recurse -Force -ErrorAction SilentlyContinue

Write-Host 'TLS 1.2 registry settings have been removed. Reboot the server to apply changes.'
```

After running the rollback script, reboot the Entra Connect Sync Server. Then re-run the validation script to confirm TLS 1.2 is no longer enabled.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
