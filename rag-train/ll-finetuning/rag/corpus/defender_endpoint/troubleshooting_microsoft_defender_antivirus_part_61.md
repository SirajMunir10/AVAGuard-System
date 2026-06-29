# Troubleshooting: Microsoft Defender Antivirus (5101)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender Antivirus when Event ID 5101 indicates the antimalware platform is expired and protection is disabled?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The antimalware platform is expired
- Microsoft Defender Antivirus grace period has expired
- Protection against viruses, spyware, and other potentially unwanted software is disabled

## Error Codes
- `5101`

## Root Causes
1. The antimalware platform is expired

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational'. Verify that no new Event ID 5101 errors are present. 2. Run 'Get-MpComputerStatus' in PowerShell and confirm that 'AMProductVersion' and 'AMEngineVersion' are not empty and show a recent date. 3. Check that 'AntivirusEnabled' is True and 'RealTimeProtectionEnabled' is True in the output of 'Get-MpComputerStatus'. 4. Verify that the Microsoft Defender Antivirus service (WinDefend) is running by running 'Get-Service WinDefend' and confirming Status is 'Running'.

## Rollback
1. If the platform update caused issues, uninstall the latest update by running 'wusa /uninstall /kb:<KB number>' (replace <KB number> with the specific KB for the platform update). 2. Restart the device. 3. Re-run 'Get-MpComputerStatus' to confirm the platform version reverted to the previous state. 4. If protection remains disabled, manually re-enable real-time protection by running 'Set-MpPreference -DisableRealtimeMonitoring $false' in PowerShell. 5. If the issue persists, restore the device from a known good backup or system restore point.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
