# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to disable sensitivity labels for Microsoft Teams, Microsoft 365 groups, and SharePoint sites?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels for containers enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the same instructions from Enable sensitivity label support in PowerShell.
2. In step 5, specify $setting["EnableMIPLabels"] = "False".
3. Run: $setting["EnableMIPLabels"] = "False"

## Validation
Run the following PowerShell commands to confirm that sensitivity labels are disabled for containers:

1. Connect to SharePoint Online PowerShell:
   Connect-SPOService -Url https://<tenant>-admin.sharepoint.com

2. Retrieve the current settings:
   $setting = Get-SPOTenant | Select-Object -ExpandProperty EnableMIPLabels

3. Verify that the value is False:
   if ($setting -eq $false) { Write-Host 'Sensitivity labels for containers are disabled.' } else { Write-Host 'Sensitivity labels are still enabled.' }

## Rollback
To re-enable sensitivity labels for containers, run the following PowerShell commands:

1. Connect to SharePoint Online PowerShell:
   Connect-SPOService -Url https://<tenant>-admin.sharepoint.com

2. Set the EnableMIPLabels property to True:
   Set-SPOTenant -EnableMIPLabels $true

3. Confirm the change:
   $setting = Get-SPOTenant | Select-Object -ExpandProperty EnableMIPLabels
   if ($setting -eq $true) { Write-Host 'Sensitivity labels for containers are re-enabled.' } else { Write-Host 'Re-enablement failed.' }

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
