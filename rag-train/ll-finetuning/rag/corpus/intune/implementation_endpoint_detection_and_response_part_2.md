# Implementation: Endpoint Detection and Response

**Domain:** Intune
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Implementation

## Scenario / Query
How to onboard Windows devices to Microsoft Defender for Endpoint using the custom setup manual policy creation in Intune?

## Environment Context
- **Tenant Type:** Intune-managed or ConfigMgr Tenant Attach
- **Configuration:** Service connection established between Intune and Microsoft Defender for Endpoint

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Microsoft Intune admin center, select Endpoint security > Endpoint detection and response > Summary tab > Create Policy.
2. Platform and profile: Platform: Windows; Profile: Endpoint detection and response; Select Create.
3. Basics: Enter a descriptive name and optional description, and then select Next.
4. Configuration settings: Configure these options based on your requirements: Defender for Endpoint client configuration package type: Auto from connector (recommended): Uses the automatic onboarding package from Microsoft Defender for Endpoint.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Endpoint detection and response and confirm the policy appears in the list with the assigned name and status 'Succeeded'.
2. On a targeted Windows device, open Windows Security > Device security > Security processor details and verify 'Microsoft Defender for Endpoint' shows as 'Active'.
3. Run the following PowerShell command as Administrator on a targeted device: Get-MpComputerStatus | Select-Object AMRunningMode, AMProductVersion, OnboardingState. Confirm 'AMRunningMode' is 'Normal' and 'OnboardingState' is 'Onboarded'.

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint security > Endpoint detection and response, select the created policy, and choose 'Delete' to remove the policy assignment.
2. On any affected Windows device, run the following PowerShell command as Administrator to offboard: & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
3. If the device was previously onboarded via another method, reapply the original onboarding configuration (e.g., re-run the original onboarding script or re-assign the previous policy).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
