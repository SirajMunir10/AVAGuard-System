# Implementation: Endpoint Detection and Response

**Domain:** Intune
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Implementation

## Scenario / Query
How to configure Microsoft Defender for Endpoint integration and onboarding using Intune EDR policies?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint detection and response policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Endpoint detection and response policy type to configure Microsoft Defender for Endpoint integration and onboarding.
2. Platform support: Windows, macOS, Linux.
3. Available profiles: Endpoint detection and response (For onboarding and configuration).
4. Use case: Enable advanced threat detection and response capabilities.
5. Requirements: Microsoft Defender for Endpoint licensing and tenant connection.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Endpoint detection and response. Verify that a policy of type 'Endpoint detection and response' exists with the intended profile (e.g., 'Endpoint detection and response (Windows)'). 2. Select the policy and confirm the 'Configuration settings' include the correct Microsoft Defender for Endpoint onboarding connection (e.g., 'Microsoft Defender for Endpoint connection' is enabled and points to the correct tenant). 3. Under 'Assignments', ensure the policy is assigned to the correct groups (e.g., 'All devices' or a test group). 4. On a target device, open the Microsoft Defender for Endpoint client and verify the device appears as 'Active' in the Microsoft 365 Defender portal (security.microsoft.com) under Assets > Devices. 5. Run the following PowerShell command as Administrator on a Windows device to confirm the onboarding state: Get-MpComputerStatus | Select-Object AMRunningMode, AMProductVersion, OnboardingState. The 'OnboardingState' should be 'Onboarded' and 'AMRunningMode' should be 'Active'.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Endpoint detection and response. Select the policy you created and choose 'Delete' to remove the policy. 2. If the policy was assigned, remove all group assignments from the policy before deletion. 3. On affected devices, run the following PowerShell command as Administrator to offboard the device from Microsoft Defender for Endpoint: & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All. 4. Alternatively, deploy a new Endpoint detection and response policy with the 'Offboard' profile (if available) to revert the onboarding. 5. Verify the device no longer appears in the Microsoft 365 Defender portal under Assets > Devices, or its status shows 'Inactive'. 6. Confirm the device's local Defender status by running: Get-MpComputerStatus | Select-Object OnboardingState. The 'OnboardingState' should be 'Not onboarded'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
