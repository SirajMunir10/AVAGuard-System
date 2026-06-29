# Implementation: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Defender for Endpoint using Group Policy, the devices show as 'Inactive' in the Microsoft 365 Defender portal. What is the most likely cause and how do I resolve it?

## Environment Context
- **Tenant Type:** Enterprise (E5)
- **Configuration:** Devices are Windows 10 21H2, joined to on-premises Active Directory, and the onboarding policy was applied via Group Policy using the .onboarding file from the portal.

## Symptoms
- Devices appear as 'Inactive' in the Microsoft 365 Defender portal for more than 7 days.
- No sensor data is received from the affected devices.
- The Microsoft Defender for Endpoint service (Sense) is not running on the devices.

## Error Codes
N/A

## Root Causes
1. The onboarding script or policy was not correctly applied, or the device cannot communicate with the Defender for Endpoint cloud service due to network restrictions.
2. The required Group Policy settings for telemetry and data collection are missing or misconfigured.

## Remediation Steps
1. Verify that the device has internet connectivity to the Defender for Endpoint service URLs (e.g., *.endpoint.microsoft.com).
2. Reapply the onboarding policy by downloading a fresh onboarding package from the Microsoft 365 Defender portal and deploying it via Group Policy.
3. Ensure the Group Policy setting 'Turn on Windows Defender Antivirus' is enabled and that the 'Configure local setting override for reporting to Microsoft MAPS' policy is set to 'Enabled' with 'Send detailed reports'.
4. Run the command 'Get-MpComputerStatus | select AntivirusEnabled, AMProductVersion' to confirm the device is properly configured.
5. Restart the 'Microsoft Defender Antivirus Network Inspection Service' and 'Microsoft Defender Antivirus Service' on the affected devices.

## Validation
After remediation, the device should appear as 'Active' in the Microsoft 365 Defender portal within 1 hour. Confirm by navigating to Devices > select the device and verify the 'Last seen' timestamp is current.

## Rollback
Remove the onboarding Group Policy Object (GPO) and delete the registry key 'HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\OnboardingState' to offboard the device.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
