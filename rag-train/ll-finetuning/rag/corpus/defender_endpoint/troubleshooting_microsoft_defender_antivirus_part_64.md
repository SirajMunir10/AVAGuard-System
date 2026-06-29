# Troubleshooting: Microsoft Defender Antivirus (0x80508022)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508022 indicating a reboot is required to complete threat removal in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508022 with message ERR_MP_REBOOT_REQUIRED

## Error Codes
- `0x80508022`

## Root Causes
1. A reboot is required to complete threat removal

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for Event ID 1006 (detection) or 1007 (action failed) with error code 0x80508022.
4. Run 'Get-MpThreatDetection' in PowerShell as Administrator and confirm no threats with 'Resources' containing 'RebootRequired' or 'PendingReboot'.
5. Run 'Get-MpComputerStatus' and verify 'AntivirusEnabled' is True and 'RealTimeProtectionEnabled' is True.
6. Check for pending reboot: 'Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\PendingFileRenameOperations' should be empty or not exist.

## Rollback
1. If validation fails or issues arise, restart the device to complete the pending reboot.
2. After reboot, run 'Start-MpScan -ScanType QuickScan' to verify threat removal.
3. If error persists, run 'Update-MpSignature' to ensure latest definitions.
4. As a last resort, run 'MpCmdRun -RemoveDefinitions -All' and then 'Update-MpSignature' to reset definitions.
5. If still failing, run 'MpCmdRun -Restore -ListAll' to list quarantined items and restore if needed, then re-run full scan.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
