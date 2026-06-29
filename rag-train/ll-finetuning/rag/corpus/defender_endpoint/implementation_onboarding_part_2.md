# Implementation: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Defender for Endpoint via Group Policy, some Windows 10 devices show as 'Inactive' in the Microsoft 365 Defender portal. What are the most common causes and how do I resolve this?

## Environment Context
- **Tenant Type:** Enterprise (E5)
- **Configuration:** Group Policy-based onboarding using the WindowsDefenderATP.onboarding script

## Symptoms
- Devices appear as 'Inactive' in the Microsoft 365 Defender portal
- Device not reporting sensor data
- Last seen timestamp is more than 7 days old

## Error Codes
N/A

## Root Causes
1. Onboarding script not applied correctly or expired
2. Connectivity issues â€“ device cannot reach the required Defender for Endpoint cloud service URLs
3. Antivirus or firewall blocking the Microsoft Defender for Endpoint sensor
4. Device is not properly licensed or the required service is disabled

## Remediation Steps
1. Verify the onboarding script is correctly applied and not expired. Re-download the latest onboarding package from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding).
2. Ensure the device can reach the required service URLs: *.endpoint.microsoft.com, *.security.microsoft.com, *.events.data.microsoft.com, and ctldl.windowsupdate.com.
3. Check that Microsoft Defender Antivirus is active and not disabled by group policy or third-party antivirus.
4. Run the Microsoft Defender for Endpoint client analyzer tool (MDEClientAnalyzer.cmd) to identify connectivity or configuration issues.
5. Restart the Microsoft Defender for Endpoint service (Sense) from an elevated command prompt: 'net stop sense && net start sense'.

## Validation
After applying remediation, confirm the device status changes to 'Active' in the Microsoft 365 Defender portal within a few hours.

## Rollback
Remove the onboarding policy from the device by deleting the registry key HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\OnboardingState and restarting the Sense service.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
