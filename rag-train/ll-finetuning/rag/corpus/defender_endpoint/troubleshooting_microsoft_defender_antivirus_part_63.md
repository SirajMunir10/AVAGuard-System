# Troubleshooting: Microsoft Defender Antivirus (0x805080211)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender Antivirus when it fails to quarantine a threat with error code 0x805080211?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Microsoft Defender Antivirus failed to quarantine a threat

## Error Codes
- `0x805080211`

## Root Causes
1. This error indicates that Microsoft Defender Antivirus failed to quarantine a threat.

## Remediation Steps
N/A

## Validation
1. Run 'Get-MpThreatDetection' in PowerShell to list recent threat detections and verify the threat with error 0x805080211 is no longer present. 2. Check the Microsoft Defender Antivirus event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1116 (detection) and Event ID 1117 (remediation) to confirm successful quarantine. 3. Execute 'Get-MpComputerStatus' to ensure real-time protection is enabled and signature versions are current.

## Rollback
1. If the threat remains unquarantined, run 'Start-MpScan -ScanType QuickScan' to trigger a new scan. 2. If the error persists, manually submit the file to Microsoft Defender for review using the 'Submit-MpSample' cmdlet. 3. As a last resort, restore the system from a known good backup or use System Restore to a point before the issue occurred.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
