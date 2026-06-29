# Troubleshooting: Microsoft Defender for Endpoint (0x8007064a)

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a machine that is not reporting sensor data to Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Windows 10/11 devices onboarded via Group Policy, sensor status shows 'Inactive' in Microsoft 365 Defender portal

## Symptoms
- Device appears as 'Inactive' in Microsoft 365 Defender portal
- No recent sensor data or alerts from the device
- Microsoft Defender for Endpoint service (Sense) is not running or fails to start

## Error Codes
- `0x8007064a`
- `0x80070643`

## Root Causes
1. Microsoft Defender for Endpoint sensor service (Sense) is disabled or stopped
2. Onboarding script was not applied correctly or the machine is not connected to the internet
3. Antivirus exclusion or security software blocking the sensor

## Remediation Steps
1. Verify the Microsoft Defender for Endpoint sensor service (Sense) is running: Open Services.msc, locate 'Microsoft Defender for Endpoint service', ensure it is set to Automatic and started.
2. If the service fails to start, check the Event Viewer under 'Microsoft-Windows-Sense/Operational' for error codes such as 0x8007064a or 0x80070643.
3. Re-run the onboarding script from Microsoft 365 Defender portal (Settings > Endpoints > Onboarding) using the appropriate deployment method (e.g., Group Policy, Local Script).
4. Ensure the device has outbound connectivity to the required Microsoft Defender for Endpoint service URLs (see 'Configure device proxy and internet connectivity settings' documentation).
5. If a third-party antivirus is installed, add exclusions for C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\ and the Sense service executable.

## Validation
After remediation, confirm the device status changes to 'Active' in Microsoft 365 Defender portal and sensor data appears within 1 hour.

## Rollback
If the issue persists, remove the onboarding configuration via local script (WindowsDefenderATPOnboardingScript.cmd /uninstall) and re-onboard using a fresh script from the portal.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-sensor>
