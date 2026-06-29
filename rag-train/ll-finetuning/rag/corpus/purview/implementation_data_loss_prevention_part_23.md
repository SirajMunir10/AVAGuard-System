# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I assign a DLP policy for SharePoint to an administrative unit so that it only applies to sites within that unit?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview and Entra ID
- **Configuration:** Administrative units must be created in Entra ID with SharePoint sites added.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create an Entra ID administrative unit for the desired department (e.g., engineering).
2. Add the relevant SharePoint site to that administrative unit.
3. Assign a DLP policy for the SharePoint location to the administrative unit.
4. Note: The option to further edit the scope to include or exclude specific sites is not available; the policy applies to all sites in the administrative unit.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the assigned DLP policy and verify that under 'Locations', 'SharePoint sites' is set to 'Specific administrative units' and the correct administrative unit (e.g., engineering) is listed. 3. Use PowerShell: Connect to Exchange Online via 'Connect-IPPSSession', then run 'Get-DlpCompliancePolicy -Identity "<PolicyName>" | Format-List Name, ExchangeLocation, SharePointLocation, OneDriveLocation, SharePointAdminUnit'. Confirm that 'SharePointAdminUnit' contains the correct administrative unit ID. 4. As a test, upload a file containing sensitive info (e.g., credit card number) to a SharePoint site within the administrative unit and verify that a policy tip or block action occurs. 5. Upload the same file to a SharePoint site outside the administrative unit and confirm no policy action is triggered.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the assigned DLP policy. 2. Under 'Locations', change 'SharePoint sites' from 'Specific administrative units' to 'All sites' or 'None' to remove the scope restriction. 3. Alternatively, delete the policy entirely by selecting it and clicking 'Delete policy'. 4. Use PowerShell: Connect to Exchange Online via 'Connect-IPPSSession', then run 'Set-DlpCompliancePolicy -Identity "<PolicyName>" -RemoveSharePointLocation "<AdminUnitName>"' to remove the administrative unit scope. 5. If the administrative unit itself is problematic, delete it via Entra ID > Administrative units > select the unit > Delete, after removing all SharePoint sites from it.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
