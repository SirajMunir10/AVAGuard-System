# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a machine that is not reporting sensor data to Microsoft Defender for Endpoint, showing the status 'Inactive' or 'Unhealthy'?

## Environment Context
- **Tenant Type:** Commercial (GCC/GCC High not applicable)
- **Configuration:** Microsoft Defender for Endpoint onboarding via Group Policy, machine running Windows 10 21H2

## Symptoms
- Machine status shows 'Inactive' or 'Unhealthy' in Microsoft 365 Defender portal
- No recent sensor data or alerts from the machine
- Machine appears in the device inventory but with stale last seen timestamp

## Error Codes
N/A

## Root Causes
1. Sensor service (Microsoft Defender for Endpoint service) is not running or has stopped
2. Onboarding script or configuration is missing or corrupted
3. Machine is not connected to the internet or cannot reach the required Microsoft Defender for Endpoint cloud service endpoints
4. Antivirus or security software is interfering with the sensor
5. The machine has been decommissioned or removed from the domain without proper offboarding

## Remediation Steps
1. Verify that the Microsoft Defender for Endpoint service (Sense) is running on the machine. Use Services.msc or run 'sc query sense' from an elevated command prompt.
2. If the service is not running, start it with 'net start sense' and set it to automatic startup.
3. Re-run the onboarding script from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding) to ensure the configuration is correct.
4. Check network connectivity: ensure the machine can reach the required URLs listed in 'Configure device proxy and internet connectivity settings' documentation.
5. Review the machine's event logs for Sense-related errors (Event ID 1, 2, 3 under Microsoft-Windows-Windows Defender/Operational).
6. If the machine was recently offboarded, re-onboard it using the correct onboarding package.

## Validation
After remediation, confirm the machine status changes to 'Active' or 'Healthy' in the Microsoft 365 Defender portal within one hour.

## Rollback
If re-onboarding does not resolve the issue, offboard the machine using the offboarding script from the same portal, then re-onboard again.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-sensor-status>
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet>
