# Troubleshooting: Onboarding (Event ID 2005: Sense sensor disconnected from the cloud)

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
A Windows 10 device shows 'Onboarding state: Inactive' in Microsoft 365 Defender. How do I troubleshoot and resolve this using the Microsoft Defender for Endpoint Client Analyzer?

## Environment Context
- **Tenant Type:** commercial
- **Configuration:** Device is running Windows 10 21H2, onboarded via Group Policy, Microsoft Defender Antivirus is active, but the sensor status shows 'Inactive'.

## Symptoms
- Device appears in Microsoft 365 Defender with onboarding state 'Inactive'
- No sensor data (alerts, telemetry) received from the device for more than 7 days
- Event ID 2005 (Sensor disconnected) may appear in the Microsoft-Windows-Sense/Operational log

## Error Codes
- `Event ID 2005: Sense sensor disconnected from the cloud`

## Root Causes
1. Network connectivity issues blocking the sensor from reaching the required Defender for Endpoint service URLs
2. Corrupted sensor installation or missing prerequisites
3. Group Policy or registry misconfiguration causing the sensor to fail to start

## Remediation Steps
1. Download and run the Microsoft Defender for Endpoint Client Analyzer tool (MDEClientAnalyzer.cmd) from the official Microsoft site on the affected device.
2. The tool will generate a .zip archive with logs; review the 'MDEClientAnalyzerResult.htm' report for connectivity and configuration issues.
3. Ensure the device can reach all required URLs listed in 'Configure device proxy and internet connectivity settings' (e.g., *.endpoint.microsoft.com, *.events.data.microsoft.com).
4. If connectivity is blocked, update proxy or firewall rules to allow the required endpoints.
5. If the analyzer reports a corrupted sensor, run 'MpCmdRun.exe -RemoveDefinitions -All' and then re-run the onboarding script from Microsoft 365 Defender.
6. Restart the Microsoft Defender Advanced Threat Protection service (Sense) via PowerShell: 'Restart-Service Sense'.
7. Verify the onboarding state changes to 'Active' within one hour.

## Validation
After remediation, check the device status in Microsoft 365 Defender under Devices. The onboarding state should change from 'Inactive' to 'Active' within 60 minutes. Also confirm that the device is sending telemetry by checking the 'Last seen' timestamp.

## Rollback
If the issue persists, re-onboard the device by removing the existing onboarding configuration (delete the 'OnboardingInfo' registry key under HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status) and reapply the onboarding package via Group Policy.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
- <https://learn.microsoft.com/en-us/defender-endpoint/overview-client-analyzer>
