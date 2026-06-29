# Governance: Governance

**Domain:** Defender for Endpoint
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that some devices in the organization are not reporting to Microsoft Defender for Endpoint even though they have been onboarded. The administrator wants to verify the current onboarding status and ensure that all devices are properly configured to report to the service.

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Devices are onboarded via Group Policy or Microsoft Endpoint Manager; some devices may have stale or missing sensor data.

## Symptoms
- Devices appear as 'Inactive' or 'Not reporting' in the Microsoft 365 Defender portal
- Device inventory shows fewer devices than expected
- Security alerts are not generated for known threats on certain devices

## Error Codes
N/A

## Root Causes
1. Device has not checked in with the Defender for Endpoint service within the last 7 days
2. Onboarding script or configuration was removed or corrupted
3. Network connectivity issues preventing the device from reaching the required Defender for Endpoint endpoints
4. Device is running an unsupported operating system or missing required updates

## Remediation Steps
1. Verify that the device meets the minimum requirements for Microsoft Defender for Endpoint as documented in 'Minimum requirements for Microsoft Defender for Endpoint'.
2. Check the device's connectivity to the Defender for Endpoint service by reviewing the 'Client connectivity' section in the Microsoft 365 Defender portal.
3. Re-run the onboarding script or reapply the onboarding configuration via Group Policy or Microsoft Endpoint Manager.
4. Ensure that the device's time is synchronized with an NTP server and that the date and time are correct.
5. Review the device's event logs for errors related to the Microsoft Defender for Endpoint sensor (e.g., Event ID 1000, 1001, or 1002 from source 'Microsoft Defender for Endpoint').
6. If the device is still not reporting, run the 'MDEOnboardingTool.cmd' script again with administrative privileges.

## Validation
After remediation, confirm that the device appears as 'Active' in the Microsoft 365 Defender portal under Devices and that the last seen timestamp is within the last hour.

## Rollback
If the device was previously reporting and stops after remediation, restore the original onboarding configuration from backup or reapply the previous Group Policy Object.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
- <https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements>
