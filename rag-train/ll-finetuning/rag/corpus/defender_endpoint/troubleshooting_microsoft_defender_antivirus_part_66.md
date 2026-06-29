# Troubleshooting: Microsoft Defender Antivirus (0x80508026)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508026 indicating that removal inside a container type is not supported?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508026
- Message: ERR_MP_REMOVE_NOT_SUPPORTED ERR_MP_REMOVE_NOT_SUPPORTED

## Error Codes
- `0x80508026`

## Root Causes
1. This error indicates that removal inside the container type might not be supported.

## Remediation Steps
1. Microsoft Defender Antivirus isn't able to remediate threats detected inside the archive. Consider manually removing the detected resources.

## Validation
1. Run the following PowerShell command to verify that the threat is no longer detected: Get-MpThreatDetection | Where-Object {$_.ThreatID -eq <ThreatID>}. If no detection is returned, the threat has been removed. 2. Check the Microsoft Defender Antivirus event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1006 (detection) and 1007 (remediation) to confirm no new detections of the same threat. 3. Manually inspect the archive file location to ensure the detected resource has been deleted or quarantined.

## Rollback
1. If the manual removal caused unintended data loss, restore the archive file from a known good backup. 2. If the threat persists or reoccurs, re-run a full scan using: Start-MpScan -ScanType FullScan. 3. If the error 0x80508026 continues, verify that the archive is not protected by system permissions or encryption; if so, temporarily disable real-time protection (Set-MpPreference -DisableRealtimeMonitoring $true) to allow manual deletion, then re-enable it (Set-MpPreference -DisableRealtimeMonitoring $false).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
