# Hardening: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Hardening

## Scenario / Query
What roles are required to change a sensitivity label applied to a site in SharePoint or Teams?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels applied to containers

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For a group-connected site: The user must be a Microsoft 365 group Owner.
2. For a site that is not group-connected: The user must be a SharePoint site admin.

## Validation
1. For a group-connected site: Confirm the user is listed as an Owner of the Microsoft 365 group by running: Get-UnifiedGroup -Identity '<GroupName>' | Select-Object -ExpandProperty Owners. 2. For a site not group-connected: Confirm the user is a SharePoint site admin by running: Get-SPOSite -Identity '<SiteURL>' | Select-Object -ExpandProperty Owner. 3. Attempt to change the sensitivity label on the site via the SharePoint admin center or PowerShell (Set-SPOSite -Identity '<SiteURL>' -SensitivityLabel '<LabelGUID>') and verify no permission error is returned.

## Rollback
1. If the user lacks required permissions, add the user as a Microsoft 365 group Owner (Add-UnifiedGroupLinks -Identity '<GroupName>' -LinkType Owners -Links '<UserPrincipalName>') or as a SharePoint site admin (Set-SPOUser -Site '<SiteURL>' -LoginName '<UserPrincipalName>' -IsSiteAdmin $true). 2. If the label change fails due to other issues, revert the label to its previous value using Set-SPOSite -Identity '<SiteURL>' -SensitivityLabel '<PreviousLabelGUID>'. 3. If the site becomes inaccessible, restore the previous sensitivity label via the Microsoft Purview compliance portal or PowerShell.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
