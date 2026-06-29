# Troubleshooting: Microsoft Defender Antivirus (0x80508024)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508024 indicating a full system scan is required in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508024
- Message: ERR_MP_FULL_SCAN_REQUIRED

## Error Codes
- `0x80508024`

## Root Causes
1. This error indicates that a full system scan might be required.

## Remediation Steps
1. Run a full system scan.

## Validation
Run the following PowerShell command to verify that the full scan completed successfully and the error is resolved: Get-MpThreatDetection | Where-Object {$_.InitialDetectionTime -gt (Get-Date).AddHours(-1)}. Also check the Protection History in Windows Security for any remaining threats or error entries. Confirm no active error 0x80508024 appears in the Event Viewer under Microsoft-Windows-Windows Defender/Operational.

## Rollback
If the full scan fails or causes performance issues, stop the scan by running: Stop-MpScan. Then restart the Microsoft Defender Antivirus service: Restart-Service WinDefend. If the error persists, restore the previous scan schedule or configuration using Set-MpPreference -ScanScheduleDay <previous_value> and Set-MpPreference -ScanParameters 1 (for quick scan).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
