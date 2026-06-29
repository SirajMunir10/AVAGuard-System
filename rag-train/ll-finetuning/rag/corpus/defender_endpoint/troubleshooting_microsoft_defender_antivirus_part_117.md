# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
What are the unsupported registry edits for turning Microsoft Defender Antivirus back on?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender Antivirus

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Do not edit Windows Defender start values for wdboot, wdfilter, wdnisdrv, wdnissvc, and windefend in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services
2. Such edits are unsupported and might force you to reimage your system

## Validation
1. Open Registry Editor (regedit.exe) as Administrator. 2. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services. 3. Verify that the Start value for each of the following subkeys is set to its default (not 4): wdboot (default 0), wdfilter (default 0), wdnisdrv (default 0), wdnissvc (default 2), windefend (default 2). 4. Run 'Get-Service wdboot,wdfilter,wdnisdrv,wdnissvc,windefend' in PowerShell as Administrator and confirm all services are running (Status = Running). 5. Run 'Get-MpComputerStatus' in PowerShell and verify that 'AMServiceEnabled', 'AntivirusEnabled', and 'RealTimeProtectionEnabled' are all True.

## Rollback
1. If any service fails to start or the system becomes unstable, restore the original Start values in the registry: set wdboot to 0, wdfilter to 0, wdnisdrv to 0, wdnissvc to 2, windefend to 2. 2. Reboot the system. 3. If the system cannot boot, use Windows Recovery Environment (WinRE) to access the registry offline and revert the Start values. 4. If the system is still unbootable or severely compromised, reimage the system from a known good backup. 5. Contact Microsoft Support if reimaging is required.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus-when-migrating>
