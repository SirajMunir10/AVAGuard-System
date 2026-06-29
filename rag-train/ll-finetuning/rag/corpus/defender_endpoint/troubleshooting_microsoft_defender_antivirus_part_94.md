# Troubleshooting: Microsoft Defender Antivirus (0x80508014)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508014 with message ERR_MP_RESTORE_FAILED in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508014
- Message displayed: ERR_MP_RESTORE_FAILED ERR_MP_RESTORE_FAILED

## Error Codes
- `0x80508014`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Windows Logs > System.
3. Filter for Event ID 1006, 1008, or 1015 from source 'Microsoft-Windows-Windows Defender'.
4. Confirm no events with error code 0x80508014 appear after remediation.
5. Run 'Get-MpThreatDetection' in PowerShell as Administrator and verify no detections with error code 0x80508014.
6. Run 'Get-MpComputerStatus' and confirm AMEngineVersion and AMProductVersion are up to date.
7. Perform a manual scan: 'Start-MpScan -ScanType QuickScan' and verify it completes without error.

## Rollback
1. If remediation involved updating definitions, revert to previous definition version using 'Update-MpSignature -Rollback' in PowerShell as Administrator.
2. If remediation involved modifying registry keys, restore from backup or revert changes using 'reg delete' or 'reg add' with original values.
3. If remediation involved reinstalling or repairing Microsoft Defender Antivirus, reinstall using 'DISM /Online /Enable-Feature /FeatureName:Windows-Defender /All' or restore from system restore point.
4. Restart the device to ensure all changes are reverted.
5. Re-run validation steps to confirm rollback success.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
