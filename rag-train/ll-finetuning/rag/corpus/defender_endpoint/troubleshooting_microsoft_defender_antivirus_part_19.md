# Troubleshooting: Microsoft Defender Antivirus (1010)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 1010: The antimalware platform couldn't restore an item from quarantine in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The antimalware platform couldn't restore an item from quarantine.

## Error Codes
- `1010`

## Root Causes
1. Microsoft Defender Antivirus encountered an error trying to restore an item from quarantine.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. 2. Look for Event ID 1010 entries after the remediation attempt. 3. Verify that no new Event ID 1010 errors appear. 4. Optionally, run `Get-MpThreatDetection | Where-Object {$_.Resources -like '*quarantine*'}` in PowerShell to confirm no pending restore failures.

## Rollback
1. If the remediation introduced issues, restore the system to a previous state using System Restore: `rstrui.exe`. 2. Alternatively, re-register Microsoft Defender Antivirus by running `Uninstall-WindowsFeature -Name Windows-Defender` and then `Install-WindowsFeature -Name Windows-Defender` in an elevated PowerShell session. 3. Reboot the device after re-registration.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
