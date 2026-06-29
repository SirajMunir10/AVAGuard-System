# Troubleshooting: Microsoft Defender Antivirus (0x8050800D)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot error code 0x8050800D with message ERR_MP_BAD_GLOBAL_STORAGE in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x8050800D displayed
- Message displayed: ERR_MP_BAD_GLOBAL_STORAGE ERR_MP_BAD_GLOBAL_STORAGE

## Error Codes
- `0x8050800D`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc) and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Look for Event ID 1006, 1007, 1008, or 1009 that indicate the error 0x8050800D is no longer occurring. 2. Run 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled, AntivirusEnabled' in PowerShell to confirm Microsoft Defender Antivirus is running and up to date. 3. Perform a quick scan by running 'Start-MpScan -ScanType QuickScan' and verify it completes without error. 4. Check for the error code by running 'Get-MpThreatDetection' and confirm no recent detections with error 0x8050800D.

## Rollback
1. If the remediation involved a system restore, run 'rstrui.exe' to revert to a previous restore point. 2. If registry changes were made, restore the original values from a backup or use 'reg delete' to remove added keys. 3. If the Microsoft Defender Antivirus service was restarted or reset, run 'Set-MpPreference -DisableRealtimeMonitoring $false' to re-enable real-time protection. 4. If the platform update was applied, roll back to the previous version using 'wusa /uninstall /kb:KBxxxxxxx' (replace with the specific KB number). 5. Reboot the system and verify the error returns by checking Event Viewer for the original error code.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
