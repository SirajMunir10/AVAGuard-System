# Implementation: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Implementation

## Scenario / Query
How to enable controlled folder access using Microsoft Intune admin center?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint Security Attack surface reduction policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create an endpoint security policy using Microsoft Intune Endpoint Security Attack surface reduction policy.
2. Set Policy type to Attack surface reduction.
3. Set Platform to Windows 10, Windows 11, and Windows Server.
4. Set Profile to Attack Surface Reduction Rules.
5. Set Configuration settings: Enable Controlled Folder Access to Audit mode to assess impact before switching to Enabled.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Attack surface reduction and confirm the policy exists with the name and description you created. 2. Select the policy, then select 'Properties' and verify that 'Configuration settings' shows 'Controlled Folder Access' set to 'Audit mode'. 3. On a Windows 10/11 or Windows Server device that is targeted by the policy, open Event Viewer, navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational, and confirm event ID 1123 appears when an application attempts to modify a protected folder. 4. Run the PowerShell command 'Get-MpPreference | Select-Object EnableControlledFolderAccess' on a targeted device and confirm the output is 'AuditMode'.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Attack surface reduction and select the policy you created. 2. Select 'Properties', then select 'Edit' next to 'Configuration settings'. 3. Change 'Controlled Folder Access' from 'Audit mode' to 'Not configured' and select 'Review + save'. 4. Alternatively, delete the entire policy by selecting the policy, then selecting 'Delete' and confirming. 5. On a targeted device, run the PowerShell command 'Set-MpPreference -EnableControlledFolderAccess Disabled' to immediately disable controlled folder access if needed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
