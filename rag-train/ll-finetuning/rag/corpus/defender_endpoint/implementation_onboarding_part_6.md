# Implementation: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Implementation

## Scenario / Query
A customer reports that after running the Microsoft Defender for Endpoint onboarding script on a Windows 10 device, the device does not appear in the Microsoft 365 Defender portal under Devices. The script completed without errors, but the device remains absent for over 24 hours.

## Environment Context
- **Tenant Type:** Commercial (GCC not specified)
- **Configuration:** Windows 10, version 21H2; onboarded via local script; no proxy configured

## Symptoms
- Onboarding script runs successfully with no error messages
- Device does not appear in Microsoft 365 Defender portal > Devices list after 24 hours
- No events from the device visible in Advanced Hunting

## Error Codes
N/A

## Root Causes
1. The Microsoft Defender for Endpoint sensor service (Sense) is not running or is in a stopped state after onboarding
2. The device is not able to reach the required Microsoft Defender for Endpoint cloud service URLs due to network restrictions or firewall rules

## Remediation Steps
1. Verify that the Microsoft Defender for Endpoint sensor service (Sense) is running: Open an elevated PowerShell prompt and run 'Get-Service Sense'. If the service is not running, start it with 'Start-Service Sense'.
2. Check that the device can connect to the required service URLs. Use the Microsoft Defender for Endpoint connectivity validation tool: download and run MDECA.exe from the Microsoft 365 Defender portal (Settings > Endpoints > Advanced features > Connectivity validation).
3. If connectivity fails, ensure the following URLs are allowed in the firewall/proxy: *.endpoint.microsoft.com, *.events.data.microsoft.com, *.dm.microsoft.com, and *.dc.services.visualstudio.com. Refer to 'Configure device proxy and internet connectivity settings' documentation.
4. If the service is running and connectivity is verified, wait up to 2 hours for the device to appear. If it still does not appear, re-run the onboarding script from the portal.

## Validation
After remediation, run 'Get-Service Sense' to confirm the service is running, then use the connectivity validation tool to confirm all required endpoints are reachable. The device should appear in the Microsoft 365 Defender portal within 2 hours.

## Rollback
To roll back onboarding, uninstall the Microsoft Defender for Endpoint sensor: run 'MDEUninstall.cmd' from the installation directory (typically C:\Program Files\Windows Defender Advanced Threat Protection\Tools\). Then remove the device from the onboarding policy in the portal.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet>
