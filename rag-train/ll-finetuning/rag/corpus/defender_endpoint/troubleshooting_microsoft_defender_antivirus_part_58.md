# Troubleshooting: Microsoft Defender Antivirus (5012)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when Microsoft Defender Antivirus scanning for viruses is disabled and Event ID 5012 is logged?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Scanning for viruses is disabled

## Error Codes
- `5012`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Verify that no new Event ID 5012 is logged after remediation. 2. Run the PowerShell command 'Get-MpComputerStatus | Select-Object AntivirusEnabled' and confirm the output is 'True'. 3. Run 'Get-MpPreference | Select-Object DisableRealtimeMonitoring' and confirm the value is 'False'. 4. Initiate a manual scan with 'Start-MpScan -ScanType QuickScan' and verify it completes without errors.

## Rollback
1. If the remediation fails, restore the previous registry or policy settings that disabled scanning. For example, if a Group Policy was applied, revert the policy to its original state. 2. If a registry key was modified, use 'reg add' to set 'HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\DisableAntiSpyware' back to '1' (or the original value). 3. Restart the 'WinDefend' service with 'Restart-Service WinDefend'. 4. Re-run 'Get-MpComputerStatus' to confirm the AntivirusEnabled property returns 'False' (original state).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
