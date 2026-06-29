# Troubleshooting: Microsoft Defender for Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to confirm onboarding of newly built devices when the SENSE service does not start automatically after the onboarding package is deployed?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Onboarding package deployed to newly built devices; Windows 10 version 1809 or later, Windows Server 2019 or later, Azure Stack HCI OS version 23H2 and later

## Symptoms
- Sensor doesn't start because the Out-of-box experience (OOBE) or first user logon hasn't been completed
- Device is turned off or restarted before the end user performs a first logon
- SENSE service won't start automatically even though onboarding package was deployed

## Error Codes
N/A

## Root Causes
1. Onboarding package is deployed to newly built devices but not completed
2. OOBE or first user logon hasn't been completed
3. Device is turned off or restarted before the end user performs a first logon

## Remediation Steps
1. Ensure that the device has completed OOBE and the first user logon has occurred
2. For Windows 10 version 1809 or later, Windows Server 2019 or later, and Azure Stack HCI OS version 23H2 and later, user logon after OOBE is no longer required for SENSE service to start

## Validation
1. Confirm the device has completed OOBE by checking the registry key: HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\UserInit. If the value is not empty, OOBE is complete. 2. Verify the SENSE service status by running: Get-Service -Name Sense. The status should be 'Running'. 3. Check the Microsoft Defender for Endpoint onboarding status by running: Get-MpComputerStatus | Select-Object -Property AMProductVersion, AMServiceEnabled, AntivirusEnabled, OnboardingState. The OnboardingState should be 'Onboarded'. 4. Review the Microsoft Defender for Endpoint machine timeline in the portal to confirm the device is listed and active.

## Rollback
1. If the SENSE service fails to start, ensure OOBE and first user logon have occurred. For Windows 10 version 1809 or later, Windows Server 2019 or later, and Azure Stack HCI OS version 23H2 and later, user logon after OOBE is no longer required. 2. Redeploy the onboarding package using the same method as initially used (e.g., Group Policy, Microsoft Configuration Manager, or local script). 3. After redeployment, restart the SENSE service manually: Start-Service -Name Sense. 4. If the service still does not start, verify the device meets the minimum requirements and that no other security software is interfering. 5. As a last resort, uninstall the onboarding package by running the uninstall script provided in the onboarding package, then re-deploy.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
