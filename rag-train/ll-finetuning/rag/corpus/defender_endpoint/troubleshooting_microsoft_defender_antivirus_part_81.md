# Troubleshooting: Microsoft Defender Antivirus (0x80501106)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501106 (MP_ERROR_CODE_BAD_REGEXP) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501106 displayed
- Message displayed: MP_ERROR_CODE_BAD_REGEXP

## Error Codes
- `0x80501106`
- `MP_ERROR_CODE_BAD_REGEXP`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that no new events with ID 1006, 1007, or 1008 appear, and that the specific error 0x80501106 is no longer logged.
4. Run the following PowerShell command to check the current status of Microsoft Defender Antivirus:
   Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, LastQuickScanDateTime, LastFullScanDateTime
5. Confirm that AntivirusEnabled and RealTimeProtectionEnabled are both True.
6. Perform a quick scan using: Start-MpScan -ScanType QuickScan
7. After the scan completes, verify no error 0x80501106 is returned by checking the scan result with: Get-MpThreatDetection

## Rollback
1. If the remediation introduced new issues, restore the previous configuration by reverting any changes made to registry keys or Group Policy settings related to Microsoft Defender Antivirus.
2. If custom exclusions or scan settings were modified, reset them to the original values documented before the remediation.
3. Restart the Microsoft Defender Antivirus service using PowerShell:
   Restart-Service -Name WinDefend
4. Re-run a quick scan to confirm the original error 0x80501106 reappears, indicating the rollback was successful.
5. If the error persists after rollback, consult the official troubleshooting guide at https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus for further steps.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
