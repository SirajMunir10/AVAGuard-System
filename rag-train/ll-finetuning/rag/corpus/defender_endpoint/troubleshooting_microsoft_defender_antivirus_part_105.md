# Troubleshooting: Microsoft Defender Antivirus (0x80508018)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508018 (ERR_MP_SCAN_ABORTED) when a Microsoft Defender Antivirus scan fails to complete?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508018 displayed
- Message displayed: ERR_MP_SCAN_ABORTED ERR_MP_SCAN_ABORTED
- Scan fails to complete

## Error Codes
- `0x80508018`

## Root Causes
1. This error is internal. It might have triggered when a scan fails to complete.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'.
3. Look for Event ID 1006, 1007, 1008, 1009, 1010, or 1011 that correspond to scan failures or detections.
4. Run a manual quick scan: 'Start > Settings > Update & Security > Windows Security > Virus & threat protection > Quick scan'.
5. Verify the scan completes without error 0x80508018.
6. Run a manual full scan: 'Start > Settings > Update & Security > Windows Security > Virus & threat protection > Scan options > Full scan'.
7. Confirm the full scan completes successfully.
8. Check the Microsoft Defender Antivirus client version: Open PowerShell as Admin and run 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled'.
9. Ensure AMServiceEnabled is True and versions are current.

## Rollback
1. If the scan still fails, restore any modified Group Policy settings: Run 'gpupdate /force' to reapply domain policies.
2. If a registry change was made, restore the previous value from a backup or export.
3. Reinstall Microsoft Defender Antivirus: In PowerShell (Admin), run 'Uninstall-WindowsFeature -Name Windows-Defender' then 'Install-WindowsFeature -Name Windows-Defender'.
4. Reset Microsoft Defender Antivirus settings: In PowerShell (Admin), run 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Set-MpPreference -DisableBehaviorMonitoring $false'.
5. Restart the Microsoft Defender Antivirus service: In PowerShell (Admin), run 'Restart-Service -Name WinDefend'.
6. If the issue persists, perform a system restore to a point before the error occurred: 'rstrui.exe' and select a restore point.
7. As a last resort, contact Microsoft Support with the error code and Event Viewer logs.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
