# Implementation: Microsoft Defender for Endpoint Onboarding

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint Onboarding
**Incident Type:** Implementation

## Scenario / Query
A security administrator is deploying Microsoft Defender for Endpoint in a hybrid environment. After configuring Group Policy to deploy the onboarding package, some Windows 10 devices appear as 'Inactive' in the Microsoft 365 Defender portal. What is the most likely cause and how should the administrator resolve this issue?

## Environment Context
- **Tenant Type:** Enterprise hybrid (on-premises AD + Azure AD)
- **Configuration:** Group Policy Objects for MDE onboarding, Windows 10 devices, Defender for Endpoint Plan 2

## Symptoms
- Devices show as 'Inactive' in Microsoft 365 Defender portal
- Devices do not appear in the device inventory
- No sensor data is received from affected endpoints

## Error Codes
N/A

## Root Causes
1. The onboarding script was not applied correctly via Group Policy, or the device is not connected to the organizational network to receive the policy
2. The Microsoft Defender for Endpoint sensor service (Sense) is not running or failed to start
3. The device is not properly registered in Azure AD or the onboarding package does not match the device's tenant

## Remediation Steps
1. Verify that the Group Policy object containing the onboarding script is linked to the correct organizational unit containing the affected devices
2. On an affected device, run 'gpupdate /force' from an elevated command prompt and then restart the device
3. Check the service status of 'Microsoft Defender for Endpoint' (Sense) on the device; if stopped, set startup type to Automatic and start the service
4. Re-download the onboarding package from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding) and redeploy it to the affected devices
5. Ensure the device has connectivity to the required Microsoft URLs (e.g., *.endpoint.microsoft.com, *.events.data.microsoft.com) as listed in the official documentation

## Validation
After remediation, the device should appear as 'Active' in the Microsoft 365 Defender portal within one hour. Run a test detection (e.g., run the provided detection test script) to confirm sensor health.

## Rollback
Remove the onboarding script from the Group Policy object and uninstall the Microsoft Defender for Endpoint sensor via Programs and Features or by running the uninstall script from the onboarding package.

## References
- Microsoft Learn - 'Troubleshoot Microsoft Defender for Endpoint onboarding issues' (https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding)
