# Troubleshooting: Onboarding (Event ID 5006)

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
A Windows 10 device shows 'Onboarding state: Incomplete' in the Microsoft 365 Defender portal. The device has been enrolled for over 24 hours but still does not report sensor data. How do I troubleshoot and resolve this onboarding failure?

## Environment Context
- **Tenant Type:** Commercial
- **Configuration:** Windows 10 Enterprise, version 21H2, onboarded via Group Policy using the Microsoft Defender for Endpoint onboarding package

## Symptoms
- Device status shows 'Incomplete' in Microsoft 365 Defender portal
- No sensor data received from the device for more than 24 hours
- Event ID 5006 or 5007 may appear in the Microsoft-Windows-Windows Defender/Operational log

## Error Codes
- `Event ID 5006`
- `Event ID 5007`

## Root Causes
1. The Microsoft Defender for Endpoint service (Sense) is not running or is disabled
2. The onboarding script or Group Policy did not apply correctly
3. Antivirus exclusions are blocking the Defender for Endpoint sensor
4. The device is not connected to the internet or is behind a proxy that blocks required endpoints

## Remediation Steps
1. Verify the service 'Microsoft Defender for Endpoint' (Sense) is running. Open an elevated PowerShell and run: Get-Service -Name Sense
2. If the service is stopped, start it: Start-Service -Name Sense
3. Check the onboarding status by running: Get-MpComputerStatus | Select-Object OnboardingState, AntivirusEnabled, IsTamperProtected
4. If OnboardingState is 0, re-run the onboarding script from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding)
5. Ensure the device can reach the required URLs: *.endpoint.microsoft.com, *.security.microsoft.com, *.events.data.microsoft.com. Test connectivity using Test-NetConnection or Invoke-WebRequest
6. Review the Microsoft-Windows-Windows Defender/Operational log for Event ID 5006 or 5007 and follow the guidance in the event details

## Validation
After remediation, run Get-MpComputerStatus | Select-Object OnboardingState. A value of 1 indicates successful onboarding. Also confirm the device appears as 'Active' in the Microsoft 365 Defender portal within one hour.

## Rollback
If the device was onboarded via Group Policy, remove the policy assignment and delete the registry key HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status. Then restart the Sense service.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
