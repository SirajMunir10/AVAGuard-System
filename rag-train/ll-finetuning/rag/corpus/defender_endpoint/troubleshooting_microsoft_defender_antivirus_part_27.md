# Troubleshooting: Microsoft Defender Antivirus (1119)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 1119: The antimalware platform encountered a critical error when trying to take action on malware or other potentially unwanted software.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1119 is logged with message: The antimalware platform encountered a critical error when trying to take action on malware or other potentially unwanted software.

## Error Codes
- `1119`

## Root Causes
1. Microsoft Defender Antivirus encountered a critical error when taking action on malware or other potentially unwanted software.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. 2. Verify that no new Event ID 1119 errors appear after remediation. 3. Run 'Get-MpComputerStatus' in PowerShell and confirm that 'AMServiceEnabled' is True and 'AntivirusEnabled' is True. 4. Perform a quick scan using 'Start-MpScan -ScanType QuickScan' and check for successful completion without errors.

## Rollback
1. If remediation involved modifying registry keys, restore the previous values from a backup or revert to default by deleting the custom key and restarting the Microsoft Defender Antivirus service. 2. If a service was restarted or disabled, set the service startup type back to its original state (e.g., 'Set-Service WinDefend -StartupType Automatic') and start the service. 3. If a policy change was applied via Group Policy, remove or revert the policy setting and run 'gpupdate /force' to reapply the original configuration. 4. Reboot the device if necessary to restore previous operational state.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
