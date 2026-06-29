# Troubleshooting: Sensor Health

**Domain:** Defender for Endpoint
**Subdomain:** Sensor Health
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Defender for Endpoint sensor on a Windows Server 2019 machine shows as 'Inactive' in the Microsoft 365 Defender portal. How do I troubleshoot and restore sensor communication?

## Environment Context
- **Tenant Type:** commercial
- **Configuration:** Windows Server 2019, Microsoft Defender for Endpoint sensor version 10.8040.22439.1045, onboarded via Group Policy

## Symptoms
- Sensor status shows 'Inactive' in Microsoft 365 Defender portal
- No recent data from the device in the device inventory
- Event Viewer shows no new MpTelemetry events

## Error Codes
N/A

## Root Causes
1. The Microsoft Defender for Endpoint service (Sense) is not running
2. The sensor is blocked by a firewall or proxy preventing communication to the required endpoints
3. The sensor certificate has expired or is invalid

## Remediation Steps
1. Verify the Microsoft Defender for Endpoint service (Sense) is running: Open Services.msc, locate 'Microsoft Defender for Endpoint service', and ensure its status is 'Running' and startup type is 'Automatic'.
2. Check connectivity to the required service URLs: Use the Microsoft Defender for Endpoint connectivity test tool (MDEClientAnalyzer) to validate that the machine can reach *.endpoint.security.microsoft.com and *.events.data.microsoft.com.
3. If a proxy is configured, ensure the proxy settings are correctly applied via Group Policy or registry (HKLM\Software\Microsoft\Windows Advanced Threat Protection\Sense\ProxyServer).
4. If the sensor certificate is expired, run the command 'sensecert -r' from an elevated command prompt to renew the certificate, then restart the Sense service.
5. Re-run the onboarding script (WindowsDefenderATPOnboardingScript.cmd) from the Microsoft 365 Defender portal if the sensor remains inactive after the above steps.

## Validation
After remediation, verify the sensor status changes to 'Active' in the Microsoft 365 Defender portal within 30 minutes. Confirm that new alerts and device timeline events appear for the machine.

## Rollback
If the issue persists, restore the original proxy settings or Group Policy configuration before making further changes. Revert any registry changes by deleting the added keys.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-sensor-health>
