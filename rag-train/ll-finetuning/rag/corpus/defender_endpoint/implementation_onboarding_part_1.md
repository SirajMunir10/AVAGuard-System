# Implementation: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Implementation

## Scenario / Query
A customer is deploying Microsoft Defender for Endpoint Plan 2 in a new tenant. After running the onboarding script on Windows 10 devices, the devices show as 'Inactive' in the Microsoft 365 Defender portal. The customer has verified that the devices meet all prerequisites (Windows 10 version 1709 or later, KB5005565 installed, and Microsoft Defender Antivirus is active). What is the most likely cause and how should the customer resolve the issue?

## Environment Context
- **Tenant Type:** Commercial (GCC not applicable)
- **Configuration:** Devices are joined to Azure AD only (no on-premises AD). The customer used the Local Script (for up to 10 machines) onboarding method from the Microsoft 365 Defender portal.

## Symptoms
- Devices appear as 'Inactive' in the Devices list in Microsoft 365 Defender
- Onboarding script ran successfully with no errors on the client
- Microsoft Defender Antivirus is running and up to date
- Devices are able to reach *.endpoint.microsoft.com and *.events.data.microsoft.com

## Error Codes
N/A

## Root Causes
1. The onboarding script was executed without administrative privileges (not 'Run as administrator')
2. The device is not properly connected to the internet or is behind a proxy that blocks the required endpoints
3. The device is not enrolled in Microsoft Defender for Endpoint because the required service 'Sense' is not started or is disabled

## Remediation Steps
1. Re-run the onboarding script with administrative privileges (right-click PowerShell or Command Prompt and select 'Run as administrator')
2. Verify that the Windows Security Center service (SecurityHealthService) is running and set to automatic start
3. Ensure the Microsoft Defender for Endpoint service (Sense) is running; if not, start it manually and set its startup type to Automatic
4. Check the device connectivity to the required service URLs: https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet#enable-access-to-microsoft-defender-for-endpoint-service-urls-in-the-proxy-server
5. If the device uses a proxy, configure the 'DisableEnterpriseAuthProxy' registry key as documented: https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet#configure-the-proxy-settings-manually-using-a-registry-key

## Validation
After remediation, run the following command as administrator: 'sc query Sense' and confirm the service state is 'RUNNING'. Then in the Microsoft 365 Defender portal, refresh the Devices list and confirm the device status changes to 'Active' within one hour.

## Rollback
To remove a device from Defender for Endpoint, run the offboarding script from the portal (Settings > Endpoints > Offboarding). This will stop the Sense service and remove the machine from the service.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-script>
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet>
