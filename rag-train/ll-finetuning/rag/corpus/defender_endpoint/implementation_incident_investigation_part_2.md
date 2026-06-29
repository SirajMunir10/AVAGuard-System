# Implementation: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites for using blast radius analysis in Microsoft Defender XDR incident investigation?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Microsoft Sentinel data lake onboarding, Exposure management (read) permission or higher

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Onboard to Microsoft Sentinel data lake. For more information, see Onboarding to Microsoft Sentinel data lake and graph.
2. Ensure you have Exposure management (read) permission or higher. For more information, see Manage permissions with Microsoft Defender unified role-based access control (RBAC).
3. Define critical assets to fully represent environmental risks. For more information, see Review and classify critical assets.

## Validation
1. Confirm Microsoft Sentinel data lake onboarding: In the Microsoft Defender portal, navigate to Settings > Microsoft Sentinel > Data lake. Verify that the status shows 'Onboarded' and that data ingestion is active. Alternatively, run the following PowerShell command with appropriate permissions: Get-MSSentinelDataLakeOnboardingStatus | Format-List. 2. Verify Exposure management permissions: In the Microsoft Defender portal, go to Permissions > Roles. Ensure the assigned role includes 'Exposure management (read)' or higher. Use the command: Get-MSSecurityRoleAssignment -RoleName 'Exposure management' | Where-Object {$_.Permissions -contains 'read'}. 3. Check critical asset classification: In the Microsoft Defender portal, navigate to Assets > Critical assets. Confirm that at least one asset is classified as 'Critical' and that the classification aligns with organizational risk. Use the command: Get-MSCriticalAsset | Where-Object {$_.Classification -eq 'Critical'}.

## Rollback
1. If Sentinel data lake onboarding causes issues, disable the data lake connection: In the Microsoft Defender portal, go to Settings > Microsoft Sentinel > Data lake, and select 'Disconnect'. Alternatively, run: Disconnect-MSSentinelDataLake. 2. If permission changes cause access issues, revert to the previous role assignment: In the Microsoft Defender portal, go to Permissions > Roles, edit the role to remove 'Exposure management (read)' or assign a lower permission level. Use: Set-MSSecurityRoleAssignment -RoleName 'PreviousRole' -Permissions @(). 3. If critical asset classification leads to false positives, reclassify assets to their original state: In the Microsoft Defender portal, navigate to Assets > Critical assets, select the asset, and change classification to 'Non-critical' or the previous value. Use: Set-MSCriticalAsset -AssetId '<AssetId>' -Classification 'Non-critical'.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
