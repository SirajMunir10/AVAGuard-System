# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a Microsoft Defender for Endpoint sensor that is not reporting data, showing a 'No sensor data' status in the Microsoft 365 Defender portal?

## Environment Context
- **Tenant Type:** Enterprise (E5)
- **Configuration:** Microsoft Defender for Endpoint Plan 2, Windows 10/11 devices onboarded via Group Policy

## Symptoms
- Device shows 'No sensor data' in Microsoft 365 Defender portal
- Device status is 'Inactive' for more than 7 days
- Event logs on the device show no recent Microsoft Defender for Endpoint telemetry

## Error Codes
N/A

## Root Causes
1. Sensor service (Microsoft Defender for Endpoint service) is stopped or disabled
2. Device is not connected to the internet or proxy/firewall blocks required endpoints
3. Onboarding script or Group Policy has expired or was not applied correctly
4. Device is running an unsupported or outdated Windows version

## Remediation Steps
1. Verify the Microsoft Defender for Endpoint service (Sense) is running: Open Services.msc, locate 'Microsoft Defender for Endpoint service', ensure status is 'Running' and startup type is 'Automatic'.
2. Check network connectivity to the required service URLs: Use the Microsoft Defender for Endpoint URL validation tool or run 'Test-NetConnection' to endpoints listed in 'Microsoft Defender for Endpoint service URLs' documentation.
3. Re-run the onboarding script or reapply the Group Policy: Download the latest onboarding package from Microsoft 365 Defender > Settings > Endpoints > Onboarding, and deploy it to the affected device.
4. Ensure the device meets minimum requirements: Windows 10 version 1709 or later, or Windows Server 2016/2019 with appropriate updates.
5. Review the Microsoft Defender for Endpoint event logs: Open Event Viewer > Applications and Services Logs > Microsoft > Windows > Sense > Operational for errors or warnings.

## Validation
After remediation, the device should show 'Active' status in the Microsoft 365 Defender portal within 1 hour. Run 'Get-MpComputerStatus' in PowerShell to confirm the AMProductVersion and AMServiceEnabled are correct.

## Rollback
If the issue persists, consider uninstalling the sensor via Programs and Features, then re-onboard the device using the latest onboarding package.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-sensor-states>
