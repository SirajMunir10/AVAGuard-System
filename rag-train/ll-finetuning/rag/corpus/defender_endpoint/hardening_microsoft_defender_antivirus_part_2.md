# Hardening: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Hardening

## Scenario / Query
How to enable limited periodic scanning for Microsoft Defender Antivirus when it is set to turn off automatically?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender Antivirus, non-Microsoft antivirus

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Limited periodic scanning is available to end-users when Microsoft Defender Antivirus is set to turn off automatically
2. This feature allows Microsoft Defender Antivirus to scan files periodically alongside a non-Microsoft antivirus, using a limited number of detections

## Validation
1. Verify that limited periodic scanning is enabled by checking the registry: reg query "HKLM\SOFTWARE\Microsoft\Windows Defender" /v AllowLimitedPeriodicScanning. Expected value: 1 (DWORD).
2. Confirm that Microsoft Defender Antivirus is not the primary antivirus by checking the Windows Security Center: Get-MpComputerStatus | Select-Object AMRunningMode. Expected output: 'Passive Mode' or 'Limited Periodic Scanning'.
3. Ensure that a non-Microsoft antivirus is installed and active: Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct | Select-Object displayName, productState.

## Rollback
1. Disable limited periodic scanning by setting the registry value to 0: reg add "HKLM\SOFTWARE\Microsoft\Windows Defender" /v AllowLimitedPeriodicScanning /t REG_DWORD /d 0 /f.
2. Restart the Microsoft Defender Antivirus service to apply changes: net stop WinDefend && net start WinDefend.
3. If the non-Microsoft antivirus is removed, re-enable Microsoft Defender Antivirus as the primary antivirus: Set-MpPreference -DisableRealtimeMonitoring $false.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus-when-migrating>
