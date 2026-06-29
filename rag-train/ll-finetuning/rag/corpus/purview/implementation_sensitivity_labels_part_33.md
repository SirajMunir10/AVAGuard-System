# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
What happens when you disable sensitivity labels for containers in Microsoft 365?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels for containers enabled

## Symptoms
- Containers ignore the Sensitivity property and use the Classification property again.
- Any label settings from sites and groups previously applied to containers won't be enforced.
- Containers no longer display the labels.
- If containers have Microsoft Entra classification values applied, they revert to using the classifications again.
- Any new sites or groups created after enabling the feature won't display a label or have a classification.

## Error Codes
N/A

## Root Causes
1. Disabling sensitivity labels for containers switches the property used from Sensitivity to Classification.

## Remediation Steps
1. For containers that revert to using classifications, you can apply classification values.
2. For new containers, you can apply classification values.

## Validation
1. Verify that the 'Enable sensitivity labels for containers' setting is disabled in the Microsoft Purview compliance portal (Settings > Sensitivity labels > Containers).
2. For an existing container (e.g., a Microsoft 365 group or SharePoint site) that previously had a sensitivity label applied, confirm that the label is no longer displayed in the container's settings and that the 'Classification' property (if previously set) is now visible and used.
3. For a new container created after the setting was disabled, confirm that no sensitivity label is assigned and that no classification value is automatically applied.
4. Use PowerShell to check the 'Classification' property of a container: `Get-UnifiedGroup -Identity <GroupName> | fl Classification` (for groups) or `Get-SPOSite -Identity <SiteURL> | fl Classification` (for sites). Verify that the 'Classification' field contains a value if one was previously set, and that the 'Sensitivity' field is empty or not used.

## Rollback
1. Re-enable sensitivity labels for containers in the Microsoft Purview compliance portal: navigate to Settings > Sensitivity labels > Containers, and set 'Enable sensitivity labels for containers' to 'On'.
2. For existing containers that reverted to using classifications, reapply the appropriate sensitivity label using the Microsoft Purview compliance portal or PowerShell (e.g., `Set-UnifiedGroup -Identity <GroupName> -SensitivityLabelId <LabelId>`).
3. For new containers created while the feature was disabled, apply a sensitivity label manually via the container's settings or via PowerShell.
4. Verify that containers now display the sensitivity label and that the 'Sensitivity' property is used instead of 'Classification'.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
