# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
What are the limitations when assigning a DLP policy to an administrative unit for SharePoint?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview and Entra ID
- **Configuration:** Administrative units with SharePoint sites added.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The option to further edit the scope to include or exclude specific sites is not available.
2. The policy applies to all sites that are part of the administrative unit.

## Validation
1. Confirm that the DLP policy is assigned to the administrative unit by running: Get-DlpCompliancePolicy -Identity "<PolicyName>" | Format-List Name, Mode, ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation, AdminUnits. 2. Verify that the policy applies to all SharePoint sites within the administrative unit by checking that the SharePointLocation property lists all site URLs in the unit. 3. Attempt to edit the policy scope to include or exclude specific sites via the Purview compliance portal or PowerShell; confirm that the option to further edit scope is not available and that any attempt returns an error or is grayed out.

## Rollback
1. Remove the administrative unit assignment from the DLP policy by running: Set-DlpCompliancePolicy -Identity "<PolicyName>" -AdminUnits @{Remove="<AdminUnitId>"}. 2. If the policy was created solely for this administrative unit, delete the policy with: Remove-DlpCompliancePolicy -Identity "<PolicyName>". 3. Recreate the policy with explicit site inclusion/exclusion if needed, using: New-DlpCompliancePolicy -Name "<PolicyName>" -SharePointLocation @("https://contoso.sharepoint.com/sites/site1","https://contoso.sharepoint.com/sites/site2").

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
