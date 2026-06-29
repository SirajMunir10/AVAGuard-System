# Troubleshooting: Onboarding (Event ID 1006)

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
A Windows 10 device shows 'Pending' status in Microsoft Defender for Endpoint after running the onboarding script. How do I troubleshoot and resolve this?

## Environment Context
- **Tenant Type:** commercial
- **Configuration:** Windows 10 Enterprise, onboarded via Local Group Policy using the downloaded onboarding package

## Symptoms
- Device appears as 'Pending' in Microsoft 365 Defender portal for more than one hour
- Event ID 1006 or 1007 may appear in Microsoft-Windows-Windows Defender/Operational log
- The Microsoft Defender for Endpoint service (Sense) is not running or shows 'Stopped'

## Error Codes
- `Event ID 1006`
- `Event ID 1007`

## Root Causes
1. Onboarding script was not executed with administrative privileges
2. Antivirus or security software is blocking the Sense service
3. Network connectivity to the Defender for Endpoint cloud service is blocked
4. The device is not properly licensed or the required service URL is not in the allow list

## Remediation Steps
1. Run the onboarding script again from an elevated command prompt (Run as Administrator)
2. Verify that the Microsoft Defender for Endpoint service (Sense) is set to Automatic and started; if not, start it manually
3. Check Windows Event Log for Microsoft-Windows-Windows Defender/Operational for error events 1006 or 1007 and follow the guidance in the event details
4. Ensure the device can reach the required URLs: *.endpoint.microsoft.com, *.security.microsoft.com, and *.events.data.microsoft.com
5. If a third-party antivirus is installed, temporarily disable it and re-run the onboarding script
6. Confirm the device has an appropriate Microsoft 365 E5 or Defender for Endpoint license assigned

## Validation
After remediation, the device should change from 'Pending' to 'Active' in the Microsoft 365 Defender portal within one hour. You can also run 'Get-MpComputerStatus' in PowerShell and verify that 'AMProductVersion' and 'AMEngineVersion' are populated.

## Rollback
Remove the onboarding configuration by running the downloaded 'WindowsDefenderATPOnboardingScript.cmd' with the /uninstall switch, or delete the related Group Policy settings.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
