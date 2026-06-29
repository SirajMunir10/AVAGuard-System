# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to apply a sensitivity label to a new SharePoint site (modern team site or communication site)?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured for groups and sites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Admins and end users can select sensitivity labels when they create modern team sites and communication sites.
2. Expand Advanced settings.
3. The dropdown box displays the label names for the selection.
4. The help icon displays all the label names with their tooltip, which can help users determine the correct label to apply.

## Validation
1. Navigate to the SharePoint admin center and create a new modern team site or communication site. 2. In the site creation wizard, expand 'Advanced settings'. 3. Verify that the 'Sensitivity' dropdown box displays the configured sensitivity labels. 4. Select a label and complete site creation. 5. After creation, go to the site's settings and confirm the applied sensitivity label is visible under 'Site information' or 'Sensitivity'. 6. Use PowerShell: `Get-SPOSite -Identity <SiteURL> | Select-Object SensitivityLabel` to confirm the label GUID is set.

## Rollback
1. If the sensitivity label is incorrectly applied, navigate to the site's settings and change the label to the correct one via the 'Sensitivity' dropdown. 2. If the label cannot be changed, use PowerShell: `Set-SPOSite -Identity <SiteURL> -SensitivityLabel <CorrectLabelGUID>` to update it. 3. If the site creation fails due to label issues, delete the site via SharePoint admin center or PowerShell: `Remove-SPOSite -Identity <SiteURL> -Confirm:$false` and recreate it without a label or with the correct label.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
