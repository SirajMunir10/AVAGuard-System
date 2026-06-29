# Troubleshooting: Onboarding (Event ID 2005 - Sense failed to start)

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
After deploying Microsoft Defender for Endpoint via Microsoft Endpoint Configuration Manager, some Windows 10 devices show an onboarding state of 'Pending' for more than 24 hours. How do I troubleshoot this issue?

## Environment Context
- **Tenant Type:** Commercial
- **Configuration:** Devices are onboarded using Group Policy with the onboarding package downloaded from the Microsoft 365 Defender portal.

## Symptoms
- Devices appear as 'Pending' in the Microsoft 365 Defender portal for more than 24 hours.
- Event ID 2005 (MDE Sense) shows 'Sense failed to start' in the Windows Event Log.
- The Microsoft Defender for Endpoint service (Sense) is not running on affected devices.

## Error Codes
- `Event ID 2005 - Sense failed to start`

## Root Causes
1. The onboarding package is not correctly applied or is expired.
2. The device is not connected to the internet or cannot reach the required Microsoft URLs (e.g., *.endpoint.microsoft.com).
3. Antivirus or security software is blocking the Sense service.

## Remediation Steps
1. Verify that the onboarding package (.zip) is current and re-download it from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding).
2. Ensure the device can access the required endpoints listed in 'Configure device proxy and internet connectivity settings' documentation.
3. Check that the Sense service startup type is set to 'Automatic' and start it manually using `net start sense`.
4. Review the Windows Event Log under 'Microsoft-Windows-Sense/Operational' for additional error events.

## Validation
After remediation, confirm the device appears as 'Active' in the Microsoft 365 Defender portal within one hour.

## Rollback
If the issue persists, remove the onboarding package via Group Policy and re-apply a fresh onboarding package.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
