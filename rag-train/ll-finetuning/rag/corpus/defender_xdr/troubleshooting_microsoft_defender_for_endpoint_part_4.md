# Troubleshooting: Microsoft Defender for Endpoint (Event ID 2010 (Sensor initialization failure))

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that a device is not appearing in the Microsoft Defender for Endpoint device inventory. How do I troubleshoot sensor onboarding and connectivity issues?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Devices are onboarded via Group Policy; Microsoft Defender for Endpoint is enabled.

## Symptoms
- Device does not appear in the Microsoft 365 Defender portal under Device inventory.
- Microsoft Defender for Endpoint service is not running or is in a stopped state on the device.
- Event ID 2010 or 2011 is logged in the Microsoft-Windows-Windows Defender/Operational event log.

## Error Codes
- `Event ID 2010 (Sensor initialization failure)`
- `Event ID 2011 (Sensor connectivity failure)`

## Root Causes
1. The Microsoft Defender for Endpoint sensor service (Sense) is not started or is disabled.
2. The device is not properly onboarded (missing or invalid onboarding script/package).
3. Network connectivity issues prevent the sensor from reaching the required cloud service endpoints.

## Remediation Steps
1. Verify that the Microsoft Defender for Endpoint sensor service (Sense) is running. Open an elevated PowerShell prompt and run: Get-Service -Name Sense. If the service is not running, start it with Start-Service -Name Sense.
2. Confirm the device is onboarded by checking the registry key HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status. If the value is not 1, re-run the onboarding script from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding).
3. Ensure the device can reach the required Microsoft Defender for Endpoint service URLs. Use the Microsoft Defender for Endpoint connectivity test tool (MDATPAnalyzer.cmd) available from Microsoft.
4. Review the Microsoft-Windows-Windows Defender/Operational event log for Event IDs 2010 or 2011. For Event ID 2010, re-run the onboarding script. For Event ID 2011, check network proxy/firewall settings to allow traffic to *.endpoint.microsoft.com and *.events.data.microsoft.com.

## Validation
After remediation, the device should appear in the Microsoft 365 Defender portal under Device inventory within a few minutes. Confirm by running Get-MpComputerStatus | Select-Object AMRunningMode, AMProductVersion, OnboardingState from an elevated PowerShell prompt; OnboardingState should be 'Onboarded'.

## Rollback
If the device was previously working and the issue started after a change, restore the previous network proxy/firewall configuration or re-apply the original onboarding package. If the sensor service was disabled, re-enable it via Group Policy or local services console.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-sensor>
