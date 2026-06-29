# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to apply a sensitivity label to multiple SharePoint or OneDrive sites using PowerShell?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** SharePoint Online Management Shell version 16.0.19418.12000 or later

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open a PowerShell session with the Run as Administrator option.
2. If you don't know your label GUID: Connect to Security & Compliance PowerShell and get the list of sensitivity labels and their GUIDs using: Get-Label |ft Name, Guid
3. Connect to SharePoint Online PowerShell and store your label GUID as a variable. For example: $Id = [GUID]("e48058ea-98e8-4940-8db0-ba1310fd955e")
4. Create a new variable that identifies multiple sites that have an identifying string in common in their URL. For example: $sites = Get-SPOSite -IncludePersonalSite $true -Limit all -Filter "Url -like 'documents"
5. Run the following command to apply the label to these sites: $sites | ForEach-Object {Set-SPOTenant $_.url -SensitivityLabel $Id}
6. Use the Set-SPOSite cmdlet when you need to apply a different label to specific sites by repeating the following command for each of these sites: Set-SPOSite -Identity <URL> -SensitivityLabel "<labelguid>"

## Validation
1. Run the following command in SharePoint Online PowerShell to verify the sensitivity label was applied: Get-SPOSite -Identity <siteURL> | Select-Object -Property Url, SensitivityLabel. 2. Confirm the output shows the expected label GUID for each site. 3. Optionally, use Get-SPOSite -Filter "Url -like 'documents'" | Select-Object Url, SensitivityLabel to check all targeted sites.

## Rollback
1. To remove the sensitivity label from a site, run: Set-SPOSite -Identity <siteURL> -SensitivityLabel "". 2. To revert to a previous label, run: Set-SPOSite -Identity <siteURL> -SensitivityLabel "<previousLabelGUID>". 3. For bulk rollback, use: $sites | ForEach-Object { Set-SPOSite -Identity $_.Url -SensitivityLabel "" }.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
