# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to enable and configure sensitivity labels for containers such as Microsoft team sites, Microsoft 365 groups, SharePoint sites, Viva Engage communities, and Loop workspaces?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels for containers must be enabled and configured before users can apply them to containers.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable and configure sensitivity labels for containers.
2. After enabling, users can see and apply sensitivity labels to containers that support them, including Microsoft team sites, Microsoft 365 groups, SharePoint sites, Viva Engage communities, and Loop workspaces.

## Validation
1. Verify that the 'Enable support for sensitivity labels' setting is turned on in the Microsoft Purview compliance portal: navigate to Information Protection > Label policies > 'Sensitivity labels for containers' policy and confirm the policy is enabled. 2. Run the following PowerShell command to confirm the configuration: Connect to Exchange Online PowerShell and execute Get-OrganizationConfig | fl Name,EnableMIPLabels. Ensure EnableMIPLabels is True. 3. Create or edit a sensitivity label that includes container settings (e.g., 'Site and group settings') and publish it to a test group. 4. As a test user, create a new Microsoft 365 group or SharePoint site and verify the published sensitivity label appears in the label picker. 5. Confirm that applying the label enforces the configured container settings (e.g., privacy, external sharing).

## Rollback
1. Disable the 'Enable support for sensitivity labels' setting in the Microsoft Purview compliance portal: navigate to Information Protection > Label policies, select the 'Sensitivity labels for containers' policy, and set the toggle to Off. 2. Remove any published sensitivity labels that include container settings from all label policies. 3. Run the following PowerShell command to revert: Connect to Exchange Online PowerShell and execute Set-OrganizationConfig -EnableMIPLabels $false. 4. Verify that users can no longer see or apply sensitivity labels to containers by creating a test group or site and checking the label picker. 5. If any containers were labeled, remove the label assignment via the container's settings (e.g., SharePoint site settings > 'Sensitivity' dropdown > 'None').

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
