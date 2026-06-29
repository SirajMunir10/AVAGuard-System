# Troubleshooting: Microsoft Defender Antivirus (0x80508020)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot error code 0x80508020 (ERR_MP_BAD_CONFIGURATION) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508020
- Message: ERR_MP_BAD_CONFIGURATION

## Error Codes
- `0x80508020`

## Root Causes
1. Engine configuration error
2. Input data that doesn't allow the engine to function properly

## Remediation Steps
N/A

## Validation
1. Open an elevated PowerShell prompt and run: Get-MpComputerStatus | Select-Object AMServiceEnabled, AMServiceVersion, AntivirusEnabled, AntispywareEnabled, NISEnabled, NISVersion. Verify that all protection services are enabled and versions are current.
2. Run: Get-MpPreference. Check that all policy settings are valid (e.g., DisableRealtimeMonitoring is False, DisableBehaviorMonitoring is False).
3. Run: Get-MpThreatDetection. Confirm no new detections or errors related to engine configuration.
4. Run: Start-MpScan -ScanType QuickScan. Verify the scan completes without error 0x80508020.
5. Review the Microsoft Defender Antivirus operational event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1000 (engine start) and no error events matching 0x80508020.

## Rollback
1. If the issue persists after remediation, restore the previous Microsoft Defender Antivirus policy settings by running: Set-MpPreference -DisableRealtimeMonitoring $true (if previously disabled) or revert any modified Group Policy objects (GPO) to their original state.
2. If engine files were manually replaced or updated, restore the original engine files from a backup or by running: Start-MpWDOScan (Windows Defender Offline Scan) to reinitialize the engine.
3. If registry changes were made (e.g., under HKLM\SOFTWARE\Policies\Microsoft\Windows Defender), delete or revert the added/modified keys using reg delete or reg add commands.
4. Reboot the device to ensure all changes are reverted: Restart-Computer -Force.
5. After reboot, verify the error code returns by running: Get-MpComputerStatus and checking for any error flags. If the error persists, contact Microsoft Support with the error code and system logs.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
