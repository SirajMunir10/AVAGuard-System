# Troubleshooting: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a device that shows 'Not enough data to create a health status' in the Microsoft 365 Defender portal?

## Environment Context
- **Tenant Type:** Commercial
- **Configuration:** Device is running Windows 10, version 21H2, and has been onboarded via Group Policy. The sensor health tile in the portal shows 'Inactive' or 'Not enough data to create a health status'.

## Symptoms
- Device appears as 'Inactive' in the Microsoft 365 Defender portal
- Sensor health tile shows 'Not enough data to create a health status'
- No recent sensor data or alerts from the device

## Error Codes
N/A

## Root Causes
1. The Microsoft Defender for Endpoint sensor service (Sense) is not running
2. The device cannot communicate with the Defender for Endpoint cloud service due to network or proxy misconfiguration
3. The onboarding script or Group Policy has not been applied correctly, or the device is not properly registered in Azure AD

## Remediation Steps
1. 1. On the affected device, open an elevated PowerShell prompt and run 'Get-Service Sense' to verify the service status. If it is not running, run 'Start-Service Sense'.
2. 2. Check the Microsoft Defender for Endpoint connectivity by running 'Test-MdeConnection' (if available) or by reviewing the Microsoft Defender Antivirus client version and cloud-delivered protection status.
3. 3. Verify that the device can reach the required URLs: *.endpoint.microsoft.com, *.events.data.microsoft.com, and *.ecs.office.com. Use the Microsoft Defender for Endpoint connectivity tool or a network trace.
4. 4. Re-run the onboarding script from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding) or reapply the Group Policy that deploys the onboarding package.
5. 5. If the issue persists, review the Microsoft Defender for Endpoint sensor logs located at %ProgramData%\Microsoft\Windows Defender\Operational\Operational.evtx for error events (e.g., Event ID 500 or 501).
6. 6. Ensure the device is Azure AD joined or hybrid Azure AD joined. If not, re-register the device using dsregcmd /join.

## Validation
After remediation, verify that the device appears as 'Active' in the Microsoft 365 Defender portal and that the sensor health tile shows 'Healthy' or 'Active' within 30 minutes.

## Rollback
If the device was re-onboarded, remove the existing onboarding configuration by deleting the registry key HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status and then reapply the original onboarding method.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-onboarding?view=o365-worldwide>
