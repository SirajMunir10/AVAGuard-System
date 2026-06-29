# Troubleshooting: Microsoft Defender for Endpoint (0x80070643)

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a Microsoft Defender for Endpoint sensor that is not reporting data and shows as inactive in the Microsoft 365 Defender portal?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD joined)
- **Configuration:** Microsoft Defender for Endpoint sensor with version 10.8040.22439.1000 on Windows Server 2019

## Symptoms
- Device shows as 'Inactive' in Microsoft 365 Defender portal
- No recent sensor data or alerts from the device
- Microsoft Defender for Endpoint service (Sense) is not running or fails to start

## Error Codes
- `0x80070643`
- `0x80004005`

## Root Causes
1. Sensor service (Sense) is stopped or disabled
2. Corrupted sensor installation or missing prerequisites
3. Connectivity issues to Microsoft Defender for Endpoint cloud services (e.g., blocked URLs)

## Remediation Steps
1. Verify the Microsoft Defender for Endpoint service (Sense) is running: Open Services.msc, locate 'Microsoft Defender for Endpoint service', and ensure its status is 'Running' and startup type is 'Automatic'.
2. If the service is not running, attempt to start it manually. If it fails, check the System and Application event logs for errors related to Sense.
3. Run the Microsoft Defender for Endpoint client analyzer tool (MDEClientAnalyzer.cmd) to collect diagnostic logs and identify configuration or connectivity issues.
4. Ensure the device can reach the required Microsoft Defender for Endpoint service URLs. Use the Microsoft Defender for Endpoint connectivity test (via the client analyzer) or manually verify access to *.endpoint.microsoft.com and *.events.data.microsoft.com.
5. If the sensor installation is corrupted, uninstall and reinstall the Microsoft Defender for Endpoint sensor using the latest onboarding package from the Microsoft 365 Defender portal.
6. After reinstallation, run the 'WindowsDefenderATPOnboardingScript.cmd' (or equivalent) to re-onboard the device.

## Validation
After remediation, confirm the device status changes to 'Active' in the Microsoft 365 Defender portal under Devices > Inventory within 1 hour. Verify the Sense service is running and event logs show successful data uploads.

## Rollback
If reinstallation is performed, the previous sensor state cannot be restored. Ensure a backup of any custom sensor configuration (e.g., proxy settings) is saved before uninstalling.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-sensor>
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet>
