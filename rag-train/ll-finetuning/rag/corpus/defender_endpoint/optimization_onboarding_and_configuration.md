# Optimization: Onboarding and Configuration

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding and Configuration
**Incident Type:** Optimization

## Scenario / Query
How can I verify that my Microsoft Defender for Endpoint deployment is fully optimized and that all required sensors are reporting correctly?

## Environment Context
- **Tenant Type:** Enterprise Microsoft 365 E5
- **Configuration:** Microsoft Defender for Endpoint Plan 2, onboarding via Group Policy

## Symptoms
- Some devices show as 'Inactive' or 'Not reporting' in the Microsoft 365 Defender portal
- The Device Health report indicates a lower-than-expected number of active sensors
- Security operations team notices gaps in alert coverage for certain endpoints

## Error Codes
N/A

## Root Causes
1. Devices are not properly onboarded or the onboarding script/package has not been applied
2. The Microsoft Defender for Endpoint sensor service (Sense) is not running or is disabled
3. Network connectivity issues prevent the sensor from communicating with the cloud service
4. Outdated or incompatible operating system versions that are not supported by Defender for Endpoint

## Remediation Steps
1. Run the 'Device Health' report in the Microsoft 365 Defender portal to identify devices with issues
2. On each affected device, verify that the 'Microsoft Defender for Endpoint Sensor' service (Sense) is running and set to automatic start
3. Re-apply the onboarding package using Group Policy or a supported deployment tool (e.g., Microsoft Configuration Manager)
4. Ensure that the device meets the minimum OS requirements and has the latest cumulative updates installed
5. Check network connectivity to the required endpoints: *.endpoint.microsoft.com, *.events.data.microsoft.com, and *.blob.core.windows.net
6. Use the 'MDEHealthTool.ps1' script from Microsoft to diagnose common onboarding and sensor issues

## Validation
After remediation, confirm that the device appears as 'Active' in the Microsoft 365 Defender portal and that the 'Device Health' report shows all expected sensors reporting within the last 7 days.

## Rollback
If re-onboarding causes issues, remove the onboarding package via Group Policy (delete the registry key under HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status) and re-run the original onboarding script.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
- <https://learn.microsoft.com/en-us/defender-endpoint/device-health>
