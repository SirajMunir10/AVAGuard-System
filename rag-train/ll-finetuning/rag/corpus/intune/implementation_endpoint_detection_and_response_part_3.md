# Implementation: Endpoint Detection and Response

**Domain:** Intune
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Implementation

## Scenario / Query
How to configure and deploy Microsoft Defender for Endpoint onboarding policy via Intune Endpoint Security?

## Environment Context
- **Tenant Type:** Microsoft Intune with Microsoft Defender for Endpoint
- **Configuration:** Endpoint security > Endpoint detection and response policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select device groups that receive this profile.
2. Device groups: Recommended for immediate deployment.
3. User groups: Requires user sign-in before policy applies.
4. For assignment guidance, see Assign user and device profiles.
5. Review + create: Verify all settings and select Create.
6. Check policy deployment: Navigate to Endpoint security > Endpoint detection and response > Select your policy > Device status.
7. Verify device onboarding: After 15-30 minutes, devices should appear in the Microsoft Defender portal under Endpoints > Device inventory.
8. Avoid policy conflicts: Multiple policies managing the same settings can cause conflicts. See Manage policy conflicts for resolution guidance.

## Validation
1. Navigate to Endpoint security > Endpoint detection and response in Microsoft Intune. Select the created policy and click 'Device status'. Confirm that the policy shows 'Succeeded' for the target devices. 2. Wait 15-30 minutes, then open the Microsoft Defender portal (https://security.microsoft.com). Go to Endpoints > Device inventory. Verify that the target devices appear in the list with an 'Active' sensor state. 3. On a target device, open PowerShell as administrator and run: Get-MpComputerStatus | Select-Object AMRunningMode, AMProductVersion, OnboardingState. Confirm that OnboardingState is 'Onboarded' and AMRunningMode is 'Normal' or 'Active'.

## Rollback
1. In Microsoft Intune, navigate to Endpoint security > Endpoint detection and response. Select the policy you created and click 'Delete'. Confirm deletion to remove the policy assignment. 2. If devices were already onboarded, they will remain onboarded until the next policy refresh cycle (up to 8 hours). To force immediate offboarding, on each device run in PowerShell as administrator: Set-MpPreference -DisableRealtimeMonitoring $true; & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All; & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Unsubscribe. 3. In the Microsoft Defender portal, go to Endpoints > Device inventory and verify that the devices eventually show as 'Inactive' or disappear after offboarding.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
