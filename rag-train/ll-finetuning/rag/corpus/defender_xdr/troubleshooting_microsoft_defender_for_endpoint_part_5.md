# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a sensor health issue where Microsoft Defender for Endpoint machines show as 'Inactive' or 'Misconfigured' in the Microsoft 365 Defender portal?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Machines onboarded via Microsoft Endpoint Manager; sensor data not updating for more than 7 days

## Symptoms
- Machine status shows 'Inactive' in the Microsoft 365 Defender portal
- Machine status shows 'Misconfigured' in the Microsoft 365 Defender portal
- No sensor data received for more than 7 days
- Alerts not generated for the affected machine

## Error Codes
N/A

## Root Causes
1. Machine has not communicated with the Defender for Endpoint cloud service for more than 7 days
2. Sensor service (Microsoft Defender Antivirus or Microsoft Defender for Endpoint sensor) stopped or is not running
3. Firewall or proxy blocking communication to required Defender for Endpoint URLs
4. Machine is uninstalled or the onboarding script was removed

## Remediation Steps
1. Verify that the machine is powered on and connected to the network
2. Check the status of the Microsoft Defender for Endpoint sensor service (Sense) by running 'sc query sense' in an elevated command prompt
3. If the service is not running, start it with 'net start sense'
4. Ensure the machine can reach the Defender for Endpoint cloud service endpoints. Refer to the Microsoft documentation for the list of required URLs and IP ranges
5. Re-run the onboarding script from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding) if the machine was recently reinstalled or the sensor data is missing
6. If the machine remains inactive, offboard and re-onboard the device using the official offboarding script

## Validation
After remediation, the machine status in the Microsoft 365 Defender portal should change to 'Active' within a few hours. You can also run 'sense -t' from an elevated command prompt to test connectivity.

## Rollback
If re-onboarding was performed, use the offboarding script from the same portal to remove the machine from Defender for Endpoint, then re-onboard if needed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-sensor-health>
