# Implementation: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Defender for Endpoint, some Windows 10 devices show an onboarding state of 'Inactive' or 'Unhealthy' in the Microsoft 365 Defender portal. What are the common causes and documented remediation steps?

## Environment Context
- **Tenant Type:** Enterprise, Microsoft 365 E5
- **Configuration:** Devices are joined to Azure AD and managed by Microsoft Intune; onboarding script was deployed via Group Policy.

## Symptoms
- Devices appear as 'Inactive' or 'Unhealthy' in the Devices list of Microsoft 365 Defender
- Sensor health shows 'No sensor data' or 'Communication impaired'
- Last seen timestamp is older than 7 days

## Error Codes
N/A

## Root Causes
1. The Microsoft Defender for Endpoint service (Sense) is not running or is disabled
2. The onboarding script was not applied successfully or the registry key is missing
3. Network connectivity to the required Microsoft Defender for Endpoint cloud service URLs is blocked
4. Antivirus or security software is interfering with the Defender for Endpoint sensor

## Remediation Steps
1. Verify that the Microsoft Defender for Endpoint service (Sense) is running. Open an elevated PowerShell prompt and run: Get-Service -Name Sense. If the service is not running, start it with Start-Service -Name Sense.
2. Confirm the onboarding script was applied by checking the registry key: HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status. The 'OnboardingState' value should be 1.
3. Ensure the device can reach the required URLs. Use the Microsoft Defender for Endpoint connectivity test tool or run: Test-NetConnection -ComputerName <your-workspace>.endpoint.security.microsoft.com -Port 443.
4. If a third-party antivirus is installed, ensure it is not blocking the Defender for Endpoint processes (MsSense.exe, SenseCE.exe, SenseIR.exe). Add exclusions for these executables in the third-party security software.
5. Re-run the onboarding script from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding) and deploy it again via Group Policy or Intune.

## Validation
After remediation, the device should appear as 'Active' and 'Healthy' in the Microsoft 365 Defender portal within one hour. You can also run Get-MachineStatus from the Microsoft Defender for Endpoint API to confirm.

## Rollback
If the device was previously healthy and the issue started after a change, restore the previous Group Policy or Intune configuration. Uninstall the onboarding script by deleting the registry key HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection and restarting the Sense service.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
