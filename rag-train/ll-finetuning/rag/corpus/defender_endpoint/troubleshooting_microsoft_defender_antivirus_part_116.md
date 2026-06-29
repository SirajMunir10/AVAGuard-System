# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and resolve Microsoft Defender Antivirus being turned off due to the DisableAntiSpyware policy during migration?

## Environment Context
- **Tenant Type:** Windows 10 Workstations
- **Configuration:** DisableAntiSpyware GPO applied via GPEdit.exe, LGPO.exe, or registry modification in task sequence

## Symptoms
- Microsoft Defender Antivirus is turned off
- Registry key HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender has DisableAntiSpyware (dword) set to 1 (hex)

## Error Codes
N/A

## Root Causes
1. DisableAntiSpyware policy set to 1 via GPO or local registry modification

## Remediation Steps
1. Check registry at HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender for DisableAntiSpyware (dword) value
2. If value is 1, configure a Trusted Image Identifier for Microsoft Defender Antivirus

## Validation
1. Open Registry Editor (regedit.exe) as Administrator. 2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender. 3. Verify that the DisableAntiSpyware DWORD value is either absent or set to 0. 4. Run the following PowerShell command to confirm Microsoft Defender Antivirus is active: Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled. 5. Check that AntivirusEnabled and RealTimeProtectionEnabled both return True.

## Rollback
1. Open Registry Editor (regedit.exe) as Administrator. 2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender. 3. Set the DisableAntiSpyware DWORD value back to 1 (hex). 4. If a Trusted Image Identifier was configured, remove it by deleting the corresponding registry value under the same path. 5. Restart the Microsoft Defender Antivirus service (WinDefend) or reboot the device to reapply the policy.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus-when-migrating>
