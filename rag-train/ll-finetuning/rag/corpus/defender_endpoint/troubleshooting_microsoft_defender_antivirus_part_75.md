# Troubleshooting: Microsoft Defender Antivirus (0x80501003)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501003 (ERROR_MP_ACTIVE_THREATS) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501003 displayed
- Message displayed: ERROR_MP_ACTIVE_THREATS

## Error Codes
- `0x80501003`
- `ERROR_MP_ACTIVE_THREATS`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to Virus & threat protection. 2. Verify that no active threats are listed under 'Current threats'. 3. Run 'Get-MpThreatDetection' in PowerShell as Administrator and confirm no active detections are returned. 4. Run 'Start-MpScan -ScanType QuickScan' and ensure the scan completes without error 0x80501003. 5. Check the Microsoft Defender Antivirus operational event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1006 or 1116 indicating no active threats.

## Rollback
1. If validation fails, restore the previous state by re-running any remediation steps that were applied (e.g., if a registry key was modified, revert it to its original value). 2. If a system restore point was created, perform a system restore to the point before changes were made. 3. If the issue persists, contact Microsoft Support for further assistance as the error is internal and not clearly defined.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
