# Implementation: Microsoft Defender for Endpoint onboarding (0x87D1041E)

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
A customer is deploying Microsoft Defender for Endpoint in an enterprise environment. After running the onboarding script on several Windows 10 devices, the devices appear in the Microsoft 365 Defender portal as 'Inactive' and show error code 0x87D1041E in the Microsoft Defender for Endpoint troubleshooting report. What is the most likely cause and how should the administrator resolve this?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Devices are joined to Azure AD and enrolled in Microsoft Intune. The onboarding package was downloaded from the Microsoft 365 Defender portal and deployed via Group Policy.

## Symptoms
- Devices appear as 'Inactive' in the Microsoft 365 Defender portal
- Error code 0x87D1041E appears in the Microsoft Defender for Endpoint troubleshooting report
- The Microsoft Defender for Endpoint service (Sense) is not running on affected devices

## Error Codes
- `0x87D1041E`

## Root Causes
1. The device is not properly connected to the Microsoft Defender for Endpoint cloud service, often due to network proxy or firewall settings blocking required endpoints, or because the onboarding script was not executed with administrative privileges.

## Remediation Steps
1. Verify that the device meets all prerequisites listed in 'Minimum requirements for Microsoft Defender for Endpoint'.
2. Ensure the onboarding script was run from an elevated command prompt (Run as administrator).
3. Check that the device can reach the required service URLs listed in 'Configure device proxy and internet connectivity settings'.
4. If a proxy is configured, set the required Microsoft Defender for Endpoint URLs in the proxy bypass list or configure the 'TelemetryProxyServer' registry key as documented.
5. Re-run the onboarding script after resolving connectivity issues, then restart the device.

## Validation
After remediation, run the 'Get-MpComputerStatus' PowerShell cmdlet and confirm that 'AMRunningMode' is set to 'Normal' and 'AntivirusEnabled' is True. In the Microsoft 365 Defender portal, the device should show as 'Active' within a few minutes.

## Rollback
To uninstall the Microsoft Defender for Endpoint sensor, run the 'WindowsDefenderATPOnboardingScript.cmd' with the 'â€“Offboard' parameter from an elevated command prompt, then restart the device.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
- <https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements>
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet>
