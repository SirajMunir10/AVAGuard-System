# Optimization: Sensor Health and Configuration

**Domain:** Defender for Endpoint
**Subdomain:** Sensor Health and Configuration
**Incident Type:** Optimization

## Scenario / Query
A customer reports that Microsoft Defender for Endpoint is not receiving telemetry from a subset of Windows 10 devices. The devices show as 'Inactive' in the Microsoft 365 Defender portal. What is the recommended approach to verify and restore sensor communication?

## Environment Context
- **Tenant Type:** Enterprise (E5)
- **Configuration:** Devices are onboarded via Group Policy; Microsoft Defender Antivirus is active; no third-party antivirus is installed.

## Symptoms
- Devices appear as 'Inactive' in the Microsoft 365 Defender portal
- No recent sensor data or alerts from affected machines
- Microsoft Defender for Endpoint sensor service (Sense) is not running on some devices

## Error Codes
N/A

## Root Causes
1. Sensor service (Sense) is stopped or disabled
2. Onboarding script or configuration has become corrupted or was removed
3. Device is not connected to the internet or proxy settings block sensor communication

## Remediation Steps
1. Verify the Microsoft Defender for Endpoint sensor service (Sense) is running: Open Services.msc, locate 'Microsoft Defender for Endpoint service', and ensure it is set to Automatic and started.
2. Run the onboarding script again on the affected device using the official onboarding package from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding).
3. Ensure the device can reach the required URLs and IPs for Defender for Endpoint as documented in 'Configure device proxy and internet connectivity settings'.
4. If the sensor remains inactive, run the Microsoft Defender for Endpoint Client Analyzer tool to diagnose connectivity and configuration issues.

## Validation
After remediation, confirm in the Microsoft 365 Defender portal that the device status changes from 'Inactive' to 'Active' and that recent sensor data appears.

## Rollback
If the onboarding script was reapplied, no rollback is needed; the original configuration is restored. If proxy settings were changed, revert to previous proxy configuration.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-sensor-health>
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet>
