# Hardening: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Hardening

## Scenario / Query
How to modify published sensitivity labels configured for sites and groups without causing unintended access or configuration drift?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels applied to Microsoft 365 Groups, Teams, and SharePoint sites

## Symptoms
- Changes to site and group settings for a sensitivity label do not immediately apply to all containers
- External users who previously had access continue to have access after the External users access setting is cleared
- Privacy settings for group properties hiddenMembership and roleEnabled are not updated

## Error Codes
N/A

## Root Causes
1. Modifying published label settings after the label has been applied to teams, groups, or sites
2. Changes require at least 24 hours to replicate to all containers
3. External users access setting changes apply only to new users, not existing users
4. Privacy settings for hiddenMembership and roleEnabled are not updated by label changes

## Remediation Steps
1. As a best practice, do not change the site and group settings for a sensitivity label after the label has been applied to teams, groups, or sites
2. If changes are necessary, wait at least 24 hours for the changes to replicate to all containers that have the label applied
3. For External users access setting changes, note that the new setting applies to new users but not to existing users; existing guest users retain access even after the setting is cleared
4. Be aware that privacy settings for the group properties hiddenMembership and roleEnabled are not updated by label changes

## Validation
1. Verify that the sensitivity label's site and group settings have been updated by running: Get-SensitivityLabel -Identity '<LabelName>' | fl DisplayName, SiteAndGroupSettings. 2. Check that the label is still published and assigned to the correct containers: Get-SensitivityLabel -Identity '<LabelName>' | Select-Object -ExpandProperty PublishedPolicies. 3. For a specific Microsoft 365 Group, confirm the current label assignment: Get-UnifiedGroup -Identity '<GroupName>' | fl SensitivityLabel. 4. For a SharePoint site, verify the label: Get-SPOSite -Identity '<SiteURL>' | fl SensitivityLabel. 5. Wait at least 24 hours after the label change, then re-run steps 3-4 to confirm the new settings have replicated. 6. For external users access, check existing guest users in a group: Get-UnifiedGroupLinks -Identity '<GroupName>' -LinkType Members | Where-Object {$_.RecipientTypeDetails -eq 'Guest'}. If the setting was cleared, these users should still appear. 7. For privacy settings, verify the group's hiddenMembership and roleEnabled properties: Get-UnifiedGroup -Identity '<GroupName>' | fl HiddenMembership, RoleEnabled. These will not change after label modification.

## Rollback
1. If the label change causes unintended access or configuration drift, revert the label's site and group settings to the previous values using: Set-SensitivityLabel -Identity '<LabelName>' -SiteAndGroupSettings (Get-SensitivityLabel -Identity '<PreviousLabelName>').SiteAndGroupSettings. 2. Re-publish the label to ensure all containers receive the reverted settings: Publish-SensitivityLabel -Identity '<LabelName>'. 3. Wait at least 24 hours for the rollback to replicate. 4. For external users access, if the setting was cleared and you need to restore access for new users, re-enable the setting: Set-SensitivityLabel -Identity '<LabelName>' -ExternalUsersAccess $true. 5. For privacy settings, manually update the group properties if needed: Set-UnifiedGroup -Identity '<GroupName>' -HiddenMembership $true -RoleEnabled $true. Note that these are not controlled by the label. 6. Monitor the containers for the next 24-48 hours to ensure the rollback has taken effect.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
