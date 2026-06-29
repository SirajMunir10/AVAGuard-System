# Troubleshooting: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a device that shows 'Inactive' or 'Unhealthy' status in Microsoft Defender for Endpoint after onboarding?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Devices running Windows 10/11, onboarded via Group Policy or Microsoft Intune

## Symptoms
- Device status shows 'Inactive' or 'Unhealthy' in Microsoft 365 Defender portal
- No sensor data received from the device for more than 7 days
- Device not appearing in the Devices list

## Error Codes
N/A

## Root Causes
1. Microsoft Defender for Endpoint sensor service (Sense) is not running
2. Communication blocked by firewall or proxy preventing sensor from reaching cloud service URLs
3. Onboarding script or configuration not applied correctly
4. Device is turned off or disconnected from network for an extended period

## Remediation Steps
1. Verify that the Microsoft Defender for Endpoint sensor service (Sense) is running: Open an elevated PowerShell prompt and run 'Get-Service -Name Sense'
2. If the service is not running, start it with 'Start-Service -Name Sense'
3. Check connectivity to required Microsoft Defender for Endpoint service URLs: Use 'Test-NetConnection' or review firewall/proxy logs against the list at 'Configure device proxy and Internet connectivity settings'
4. Re-run the onboarding script or reapply the onboarding policy from Microsoft Intune or Group Policy
5. Ensure the device has been restarted after initial onboarding

## Validation
After remediation, verify the device status changes to 'Active' in the Microsoft 365 Defender portal within a few hours. Confirm the Sense service is running and that the device can reach the required endpoints.

## Rollback
If the device becomes unhealthy after changes, revert any firewall or proxy changes and reapply the original onboarding configuration.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
