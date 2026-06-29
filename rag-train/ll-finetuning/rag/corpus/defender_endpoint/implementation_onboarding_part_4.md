# Implementation: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Implementation

## Scenario / Query
After configuring a Group Policy to deploy the Microsoft Defender for Endpoint onboarding package to Windows 10 devices, the devices appear as 'Inactive' in the Microsoft 365 Defender portal. The onboarding script ran successfully with no errors, and the device can reach the required URLs. What is the most likely cause and how do I resolve it?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD joined)
- **Configuration:** Group Policy deployed onboarding package (WindowsDefenderATPOnboardingScript.cmd) to Windows 10 20H2 devices. Devices are internet-connected and can reach *.endpoint.microsoft.com and *.events.data.microsoft.com.

## Symptoms
- Devices show as 'Inactive' in Microsoft 365 Defender portal > Device inventory
- Onboarding script completes without error on the device
- Device connectivity to required Microsoft Defender for Endpoint URLs is confirmed

## Error Codes
N/A

## Root Causes
1. The onboarding script was executed but the device was not restarted after the Group Policy update, or the Sense service (Microsoft Defender for Endpoint sensor) failed to start due to a missing prerequisite (e.g., KB4052623 or a servicing stack update on an older build).

## Remediation Steps
1. 1. On the affected device, open an elevated PowerShell prompt and run `Get-Service Sense` to verify the service status. If it is not running, run `Start-Service Sense`.
2. 2. Ensure the device has the required update: For Windows 10, version 1809 or later, no additional update is needed. For earlier versions, install the update described in 'Update for Windows 10 (KB4052623)'.
3. 3. Restart the device to complete the onboarding process.
4. 4. In the Microsoft 365 Defender portal, navigate to Settings > Endpoints > Onboarding and verify that the correct onboarding package (e.g., 'Windows 10 and Windows 11 (via Group Policy)') was used.

## Validation
After restart and service start, run `Get-MpComputerStatus | select OnboardingState` in PowerShell. Expected output: 'OnboardingState : Onboarded'. Then verify the device appears as 'Active' in the Microsoft 365 Defender portal within 30 minutes.

## Rollback
To roll back onboarding, run the offboarding script from the same portal page: Settings > Endpoints > Offboarding. Then delete the Group Policy object that deployed the onboarding script.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding#device-is-inactive-after-onboarding>
