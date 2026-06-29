# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How to implement Microsoft Intune security baselines as a starting point for MDM security configurations?

## Environment Context
- **Tenant Type:** Microsoft Intune with Microsoft Entra ID
- **Configuration:** Windows 10 and later baseline template

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Intune baseline recommendations as a starting point
2. Customize the baseline to meet IT and security demands

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Verify that the 'Windows 10 and later' baseline is listed and its status shows 'Assigned' to the intended groups.
4. Select the baseline and review the assigned profile; confirm that the settings match the customized values required by your organization.
5. On a Windows 10/11 device that is a member of the assigned group, open Settings > Accounts > Access work or school > click 'Info' and then 'Sync' to force a sync.
6. On the same device, open a command prompt as administrator and run: 'dsregcmd /status'. Verify that the device is Azure AD joined and that the MDM URL points to your Intune tenant.
7. Run 'Get-MgDeviceManagementConfigurationPolicy -Filter "displayName eq 'Windows 10 Security Baseline'"' in Microsoft Graph PowerShell to confirm the policy is applied.
8. Check the device's Event Viewer under Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin for Event ID 814 (policy applied successfully).

## Rollback
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Select the 'Windows 10 and later' baseline profile that was deployed.
4. Click 'Properties' and then 'Assignments'.
5. Remove all assigned groups by selecting each group and clicking 'Remove'.
6. Click 'Save' to remove the baseline assignment from all devices.
7. Alternatively, to revert to a previous baseline version, select the baseline, click 'Versions', and choose the earlier version. Then click 'Assign' and reassign the groups.
8. On affected devices, force a sync by going to Settings > Accounts > Access work or school > select the account > click 'Sync'.
9. Verify that the device no longer shows the baseline settings by running 'Get-MgDeviceManagementConfigurationPolicy' in Microsoft Graph PowerShell and confirming the policy is no longer assigned.
10. If the baseline was the only configuration source, consider deploying a less restrictive custom policy to restore previous settings.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
