# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
Can a Microsoft Defender Antivirus scan run alongside other antivirus solutions, and what mode should Microsoft Defender Antivirus be in?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Microsoft Defender Antivirus compatibility

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. A Microsoft Defender Antivirus scan can run alongside other antivirus solutions, whether Microsoft Defender Antivirus is the active antivirus solution or not.
2. Microsoft Defender Antivirus can be in Passive mode. For more information, see Microsoft Defender Antivirus compatibility.

## Validation
1. Open PowerShell as Administrator and run: Get-MpComputerStatus | Select-Object AMRunningMode, AMServiceEnabled, AntivirusEnabled. Confirm AMRunningMode is 'Passive' and AMServiceEnabled is 'True' when a non-Microsoft antivirus is active. 2. Verify Microsoft Defender Antivirus can initiate a scan by running: Start-MpScan -ScanType QuickScan. Confirm no error is returned. 3. Check the Microsoft Defender Antivirus event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1001 indicating a scan completed successfully.

## Rollback
1. If Microsoft Defender Antivirus is in Passive mode and needs to return to Active mode, run: Set-MpPreference -DisableRealtimeMonitoring $false. 2. If the non-Microsoft antivirus solution was disabled, re-enable it according to its vendor documentation. 3. Restart the Microsoft Defender Antivirus service if needed: Restart-Service WinDefend. 4. Confirm the original state by running: Get-MpComputerStatus | Select-Object AMRunningMode, AMServiceEnabled, AntivirusEnabled.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
