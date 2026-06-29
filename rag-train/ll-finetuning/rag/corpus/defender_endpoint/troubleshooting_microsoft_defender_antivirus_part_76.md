# Troubleshooting: Microsoft Defender Antivirus (0x805011011)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender Antivirus error code 0x805011011 with message MP_ERROR_CODE_LUA_CANCELLED?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x805011011 displayed
- Message displayed: MP_ERROR_CODE_LUA_CANCELLED

## Error Codes
- `0x805011011`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for event ID 1006, 1007, 1008, 1009, or 1010 that may indicate the error was resolved.
4. Run the command: Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, AMProductVersion, AMEngineVersion
5. Confirm that AMServiceEnabled, AntivirusEnabled, and RealTimeProtectionEnabled are all True.
6. Run a quick scan: Start-MpScan -ScanType QuickScan
7. Verify no new instances of error 0x805011011 appear in the Defender operational log after the scan.

## Rollback
1. If the error persists or new issues arise, restore the previous state by reverting any configuration changes made during remediation.
2. If a system restore point was created before remediation, run: rstrui.exe and select the restore point.
3. If registry changes were made, restore the backed-up registry keys using: reg import <backup_file>.reg
4. Reinstall Microsoft Defender Antivirus if it was disabled: Enable-WindowsOptionalFeature -Online -FeatureName Windows-Defender-Default-Defender
5. Reset Defender settings to default: Set-MpPreference -Force
6. Reboot the device and verify the error returns by checking the Defender operational log for event ID 0x805011011.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
