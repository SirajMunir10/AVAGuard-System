# Implementation: Endpoint Detection and Response

**Domain:** Intune
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Implementation

## Scenario / Query
How to onboard Windows devices to Microsoft Defender for Endpoint using the quick setup preconfigured policy in Intune?

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
1. In the Microsoft Intune admin center, go to Endpoint security > Endpoint detection and response > EDR Onboarding Status tab.
2. Select Deploy preconfigured policy.
3. Configure the policy: Platform: Select Windows (for Intune-managed) or Windows (ConfigMgr) (for Tenant Attach); Profile: Select Endpoint detection and response; Name: Enter a descriptive name (for example, 'MDE EDR Onboarding - All Windows Devices').
4. Review and create: Verify settings and select Save. The policy immediately starts deploying to all Windows devices.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Endpoint detection and response. 2. On the EDR Onboarding Status tab, verify that the policy you created (e.g., 'MDE EDR Onboarding - All Windows Devices') appears in the list with a status of 'Active'. 3. Select the policy and review the 'Assigned' and 'Device status' sections to confirm that the intended Windows devices show a status of 'Onboarded' or 'Compliant'. 4. On a target Windows device, open Windows Security > Device security > Core isolation details and confirm that 'Microsoft Defender for Endpoint' is listed as a service. 5. Run the following PowerShell command as Administrator on a target device: Get-MpComputerStatus | Select-Object AMRunningMode, AMProductVersion, OnboardingState. Verify that AMRunningMode is 'Normal' and OnboardingState is 'Onboarded'.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Endpoint detection and response. 2. On the EDR Onboarding Status tab, locate the policy you deployed (e.g., 'MDE EDR Onboarding - All Windows Devices'). 3. Select the policy and choose 'Delete' to remove it. 4. Confirm the deletion when prompted. 5. On each affected Windows device, run the following PowerShell command as Administrator to offboard the device: & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All. 6. Restart the device to complete the offboarding process.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
