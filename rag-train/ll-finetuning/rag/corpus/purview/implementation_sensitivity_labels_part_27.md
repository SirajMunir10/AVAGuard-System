# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to apply sensitivity labels to Microsoft 365 groups, Teams, SharePoint sites, Loop workspaces, and Viva Engage communities?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured in Microsoft Purview compliance portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Apply the sensitivity label or labels to the following containers: Microsoft 365 group in Microsoft Entra ID, Microsoft Teams team site, Microsoft 365 group in Outlook on the web, SharePoint site, Loop workspaces, Viva Engage communities.
2. Use PowerShell if you need to apply a sensitivity label to multiple sites.

## Validation
1. Verify that the sensitivity label is published and enabled for containers: In Microsoft Purview compliance portal, navigate to Solutions > Information protection > Label policies, select the policy that includes the label, and confirm the label is assigned to 'Groups & sites' with status 'Enabled'. 2. For a specific Microsoft 365 group, run: Get-UnifiedGroup -Identity <GroupName> | fl SensitivityLabel. 3. For a SharePoint site, run: Get-SPOSite -Identity <SiteURL> | fl SensitivityLabel. 4. For a Teams team, run: Get-Team -DisplayName <TeamName> | fl SensitivityLabel. 5. For a Loop workspace, confirm the label appears in the workspace settings under 'Sensitivity'. 6. For a Viva Engage community, confirm the label appears in community settings. 7. If using PowerShell to apply labels to multiple sites, run: Get-SPOSite -Template 'GROUP#0' | Set-SPOSite -SensitivityLabel <LabelGUID> and then verify with Get-SPOSite.

## Rollback
1. Remove the sensitivity label from a container: For a Microsoft 365 group, run: Set-UnifiedGroup -Identity <GroupName> -SensitivityLabel $null. 2. For a SharePoint site, run: Set-SPOSite -Identity <SiteURL> -SensitivityLabel $null. 3. For a Teams team, run: Set-Team -DisplayName <TeamName> -SensitivityLabel $null. 4. For a Loop workspace, remove the label via workspace settings. 5. For a Viva Engage community, remove the label via community settings. 6. If labels were applied to multiple sites via PowerShell, run: Get-SPOSite -Template 'GROUP#0' | Set-SPOSite -SensitivityLabel $null. 7. If the label policy itself caused issues, edit the label policy in Purview to remove the label from the policy or disable it for containers.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
