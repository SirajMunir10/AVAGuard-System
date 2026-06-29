# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to reduce CPU utilization caused by scanning obfuscated scripts in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender Antivirus script scanning

## Symptoms
- Higher CPU utilization by Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
1. Obfuscated scripts require more CPU utilization to check if the script contains malicious payloads

## Remediation Steps
1. Use script obfuscation only when necessary
2. As a workaround: Add Antivirus exclusions (process+path)

## Validation
1. Open Windows Security app > Virus & threat protection > Manage settings > Confirm 'Real-time protection' is On.
2. Run PowerShell as Admin: Get-MpPreference | Select-Object -Property ExclusionPath, ExclusionProcess
   Verify that the added exclusion paths/processes are listed.
3. Monitor CPU usage via Task Manager > Processes > Look for 'Antimalware Service Executable' (MsMpEng.exe) CPU usage. It should be lower than before the exclusion.
4. Optionally, run a quick scan: Start-MpScan -ScanType QuickScan and confirm no performance degradation.

## Rollback
1. Remove each added exclusion:
   Remove-MpPreference -ExclusionPath '<path>' (for each path)
   Remove-MpPreference -ExclusionProcess '<process.exe>' (for each process)
2. Verify removal: Get-MpPreference | Select-Object ExclusionPath, ExclusionProcess
3. Restart the Microsoft Defender Antivirus service: Restart-Service -Name WinDefend
4. Re-enable script obfuscation if it was disabled as part of the workaround.
5. Confirm CPU usage returns to baseline (may increase again if obfuscated scripts are present).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
