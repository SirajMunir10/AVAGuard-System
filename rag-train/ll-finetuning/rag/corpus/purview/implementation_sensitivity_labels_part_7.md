# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure privacy and external user access settings for sensitivity labels applied to Microsoft 365 groups, Teams, and SharePoint sites?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels with scope including groups and sites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the Define protection settings for groups and sites page, select the options you want to configure: Privacy and external user access settings.
2. Configure Privacy: Keep the default of Public if you want anyone in your organization to access the container where this label is applied. Select Private if you want access to be restricted to only approved members in your organization. Select None when you want to protect content in the container by using the sensitivity label, but still let users configure the privacy setting themselves.
3. Configure External user access: Control whether the owner can add guests to the container, similar to Manage guest access in Microsoft 365 groups.

## Validation
1. Verify that the sensitivity label is published and applied to a test Microsoft 365 group, Teams team, or SharePoint site. 2. For a group or team with the label set to Private, confirm that non-members cannot access the container and that the privacy setting shows 'Private' in the Microsoft 365 admin center or via Get-UnifiedGroup -Identity <GroupName> | fl AccessType. 3. For a label with External user access set to Block, attempt to add a guest user to the container and verify the operation is denied. 4. For a label with External user access set to Allow, confirm that the owner can successfully add a guest. 5. Use the Microsoft Purview compliance portal to review the label's configuration under 'Define protection settings for groups and sites' and ensure the selected privacy and external user access options match the intended settings.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Sensitivity labels and edit the label in question. 2. On the 'Define protection settings for groups and sites' page, revert the Privacy setting to its original value (e.g., change from Private to Public or None) and the External user access setting to its original state (e.g., change from Block to Allow or vice versa). 3. Save the label configuration and wait for replication (up to 24 hours). 4. If the label was applied to containers, remove the label from affected groups, teams, or sites by clearing the sensitivity label assignment in the respective admin center or via PowerShell (e.g., Set-UnifiedGroup -Identity <GroupName> -SensitivityLabelIdentity $null). 5. Reapply any previous custom privacy or guest access settings that were overridden by the label.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
