# Implementation: Microsoft Defender for Endpoint onboarding

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
A customer is deploying Microsoft Defender for Endpoint in their environment. After running the onboarding script on a Windows 10 device, the device shows 'Inactive' in the Microsoft 365 Defender portal instead of 'Active'. The device is not reporting telemetry. What is the most likely cause and how should it be resolved?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Devices are joined to Azure AD and managed by Microsoft Endpoint Manager. The onboarding script was downloaded from the Microsoft 365 Defender portal.

## Symptoms
- Device appears as 'Inactive' in the Microsoft 365 Defender portal after running the onboarding script.
- No telemetry data is received from the device.
- The Microsoft Defender for Endpoint service (Sense) is not running on the device.

## Error Codes
N/A

## Root Causes
1. The onboarding script was not executed with administrative privileges.
2. The device is not connected to the internet or is blocked by a firewall/proxy that prevents communication with the Defender for Endpoint cloud service.
3. The device was previously onboarded to a different tenant and the old onboarding data conflicts with the new tenant.

## Remediation Steps
1. Run the onboarding script again from an elevated command prompt (Run as Administrator).
2. Verify that the device can reach the required URLs: *.endpoint.microsoft.com, *.events.data.microsoft.com, and *.blob.core.windows.net. For a complete list, see 'Configure device proxy and internet connectivity settings' in Microsoft documentation.
3. If the device was previously onboarded to another tenant, use the 'MicrosoftDefenderATPOnboardingScript.cmd' with the '-Offboard' parameter to remove the old configuration, then re-onboard.
4. After successful onboarding, run 'sense.bat' from the installation directory to start the service, or reboot the device.

## Validation
In the Microsoft 365 Defender portal, navigate to Devices. The device should show 'Active' within a few minutes. Confirm by running 'Get-MpComputerStatus' in PowerShell; the 'AMProductVersion' and 'AMServiceEnabled' fields should indicate Defender is active.

## Rollback
To offboard a device, run the offboarding script downloaded from the Microsoft 365 Defender portal (Settings > Endpoints > Offboarding) with administrative privileges. This removes the device from the tenant and stops data collection.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/onboard-windows-client>
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet>
