# Implementation: Onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Onboarding
**Incident Type:** Implementation

## Scenario / Query
A customer has deployed Microsoft Defender for Endpoint Plan 2 but cannot see any device inventory in the Microsoft 365 Defender portal. The onboarding script ran successfully on test devices, and the Microsoft Defender for Endpoint service is running. What is the most likely cause and how do you resolve it?

## Environment Context
- **Tenant Type:** Commercial (GCC not applicable)
- **Configuration:** Microsoft Defender for Endpoint Plan 2, devices running Windows 10 21H2, onboarding via local script

## Symptoms
- Devices appear as 'Inactive' or 'Not reporting' in the device inventory
- Onboarding script completes without error on the endpoint
- Microsoft Defender for Endpoint service (Sense) is running on the endpoint
- No devices appear in the Microsoft 365 Defender portal after 24 hours

## Error Codes
N/A

## Root Causes
1. The onboarding script was not executed with administrative privileges, or the device is not connected to the internet and cannot reach the Defender for Endpoint cloud service
2. The device is not properly configured to use the correct onboarding policy (e.g., group policy or local script mismatch)

## Remediation Steps
1. Verify that the onboarding script was run from an elevated command prompt (Run as Administrator).
2. Check that the device has outbound HTTPS connectivity to *.endpoint.microsoft.com and *.events.data.microsoft.com.
3. On the device, open an elevated PowerShell and run: Get-MpComputerStatus | Select-Object AMProductVersion, AMRunningMode, AMServiceEnabled, OnboardingState. Confirm OnboardingState is 1.
4. If OnboardingState is 0, re-run the onboarding script as Administrator and restart the device.
5. In the Microsoft 365 Defender portal, navigate to Settings > Endpoints > Onboarding and download a fresh onboarding package for the correct operating system.
6. If the issue persists, review the Microsoft Defender for Endpoint client analyzer results by running: MDEAnalyzer.cmd from the Microsoft Defender for Endpoint Client Analyzer tool.

## Validation
After remediation, the device should appear as 'Active' in the device inventory within 1-2 hours. Run Get-MpComputerStatus to confirm OnboardingState = 1 and AMRunningMode = 'Normal'.

## Rollback
To offboard a device, run the offboarding script from the same portal location (Settings > Endpoints > Offboarding). This will remove the device from the service.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
