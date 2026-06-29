# Troubleshooting: Microsoft Defender Antivirus (5001)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when Microsoft Defender Antivirus real-time protection is disabled with Event ID 5001?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Real-time protection is disabled

## Error Codes
- `5001`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Verify that no Event ID 5001 (Real-time protection disabled) appears after remediation. 2. Open Windows Security app > Virus & threat protection > Virus & threat protection settings. Confirm 'Real-time protection' is toggled On. 3. Run 'Get-MpPreference | Select-Object DisableRealtimeMonitoring' in PowerShell as Administrator. Confirm the output is 'False'. 4. Run 'Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled' in PowerShell as Administrator. Confirm the output is 'True'.

## Rollback
1. If real-time protection remains disabled or issues arise, open PowerShell as Administrator and run 'Set-MpPreference -DisableRealtimeMonitoring $true' to revert to disabled state. 2. If the remediation involved modifying Group Policy, restore the original policy settings by reversing any changes made to 'Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Real-time Protection > Turn off real-time protection'. 3. If registry keys were modified, open Registry Editor and navigate to 'HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection'. Delete or set 'DisableRealtimeMonitoring' to 1. 4. Restart the Microsoft Defender Antivirus service by running 'net stop WinDefend' followed by 'net start WinDefend' in an elevated command prompt.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
