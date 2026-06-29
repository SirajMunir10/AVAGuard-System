# Implementation: Microsoft Defender for Endpoint onboarding

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
During the initial onboarding of Microsoft Defender for Endpoint, a security administrator runs the Microsoft 365 Defender portal onboarding script on a Windows 10 device but the device does not appear in the Devices list after 30 minutes. What are the likely causes and how should this be resolved?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Defender for Endpoint onboarding using local script (Group Policy not yet deployed)

## Symptoms
- Onboarding script runs without error on the endpoint
- Device does not appear in Microsoft 365 Defender > Assets > Devices after 30 minutes
- No error message is displayed during script execution

## Error Codes
N/A

## Root Causes
1. The device may not have internet connectivity to the required Microsoft Defender for Endpoint service URLs
2. The Microsoft Defender Antivirus service (WinDefend) may not be running or is disabled
3. The onboarding script was not executed with administrative privileges
4. The device is already onboarded to another Defender for Endpoint tenant and the script is for a different tenant

## Remediation Steps
1. Verify the device can reach the required service URLs listed in Microsoft documentation: https://learn.microsoft.com/en-us/defender-endpoint/configure-network-connections
2. Ensure the Microsoft Defender Antivirus service (WinDefend) is running and set to automatic start
3. Re-run the onboarding script from an elevated command prompt (Run as Administrator)
4. If the device was previously onboarded to another tenant, offboard it using the offboarding script from the original tenant, then re-onboard with the correct script
5. Check the Microsoft-Windows-Sense/Operational event log for errors (Event ID 1 or 2 indicate connectivity issues)

## Validation
After applying remediation, the device should appear in the Devices list within 30 minutes. Run the command 'Get-MpComputerStatus | select AMRunningMode' to confirm the device is in 'Normal' mode.

## Rollback
If onboarding fails repeatedly, offboard the device by running the offboarding script from the same tenant portal, then restart the device and attempt onboarding again.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-network-connections>
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
