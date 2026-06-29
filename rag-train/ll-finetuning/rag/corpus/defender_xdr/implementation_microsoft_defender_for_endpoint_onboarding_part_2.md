# Implementation: Microsoft Defender for Endpoint Onboarding

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint Onboarding
**Incident Type:** Implementation

## Scenario / Query
A security administrator is deploying Microsoft Defender for Endpoint in an environment with Windows 10 Enterprise devices managed by Microsoft Endpoint Configuration Manager. After configuring the onboarding policy, the devices do not appear in the Microsoft 365 Defender portal. What is the most likely cause and how should it be resolved?

## Environment Context
- **Tenant Type:** Enterprise (E5)
- **Configuration:** Devices are joined to Azure AD and enrolled in Microsoft Endpoint Configuration Manager (current branch). The onboarding policy was created using the Configuration Manager console and deployed to a device collection.

## Symptoms
- Devices do not appear in the Microsoft 365 Defender portal (https://security.microsoft.com) under Devices > Computers.
- The Microsoft Defender for Endpoint service (Sense) is not running on the devices.
- Event ID 500 (MDE Sense) or Event ID 1000 (Sense) is not present in the Windows Event log.

## Error Codes
N/A

## Root Causes
1. The onboarding package (WindowsDefenderATPOnboardingScript.cmd) was not correctly deployed or executed on the target devices.
2. The devices are not receiving the required Group Policy or Configuration Manager policy to enable the Sense service and set the onboarding registration token.
3. The Configuration Manager client on the devices is not reporting the policy correctly, or the devices are in a different site that does not have the policy deployed.

## Remediation Steps
1. Verify that the onboarding configuration package has been deployed to the correct device collection in Configuration Manager. In the Configuration Manager console, go to Assets and Compliance > Device Collections, right-click the target collection, select Deploy > Configuration Baseline, and ensure the onboarding baseline is assigned.
2. On a non-compliant device, open the Configuration Manager control panel applet (Configuration Manager Properties) and verify that the client is assigned to the correct site and that the policy has been downloaded. Use the 'Actions' tab to trigger 'Machine Policy Retrieval & Evaluation Cycle'.
3. Manually run the onboarding script (WindowsDefenderATPOnboardingScript.cmd) with administrative privileges on a test device to confirm it completes without error. The script is located in the onboarding package folder under \\<SiteServer>\SMS_<SiteCode>\osd\lib\<PackageID>.
4. If the script runs successfully but the device still does not appear, check the Microsoft Defender for Endpoint service status by running 'sc query sense' from an elevated command prompt. If the service is not running, start it with 'net start sense'.
5. Ensure that the device meets the minimum requirements: Windows 10 version 1709 or later, and that the Microsoft Defender Antivirus platform is up to date (version 1.1.1700 or later).
6. If the issue persists, review the Microsoft Defender for Endpoint deployment troubleshooting guide for additional steps.

## Validation
After remediation, run 'sc query sense' on a test device to confirm the service is running. Then, from the Microsoft 365 Defender portal, navigate to Devices > Computers and verify the device appears within 15 minutes. Optionally, use the 'Test connection' feature in the portal for that device.

## Rollback
To roll back the onboarding, deploy the offboarding package from the Microsoft 365 Defender portal (Settings > Endpoints > Offboarding) using the same Configuration Manager method. This will remove the registration token and stop the Sense service.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-endpoints-sccm?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-onboarding?view=o365-worldwide>
