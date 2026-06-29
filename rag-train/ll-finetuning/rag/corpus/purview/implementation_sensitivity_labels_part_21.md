# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure a sensitivity label with an authentication context requiring MFA for a SharePoint site containing highly confidential items?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured for containers (Teams, groups, sites)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose an authentication context that is configured to require multifactor authentication (MFA).
2. Apply this label to a SharePoint site that contains highly confidential items.
3. As a result, when users from an untrusted network attempt to access a document in this site, they see the MFA prompt that they must complete before they can access the document.

## Validation
1. Verify that the sensitivity label is published and applied to the SharePoint site: Run `Get-SPOSite -Identity <SiteURL> | Select-Object SensitivityLabel` in SharePoint Online Management Shell. 2. Confirm the authentication context is enforced: Use `Get-SPOSite -Identity <SiteURL> | Select-Object ConditionalAccessPolicy` and ensure it returns the expected authentication context GUID. 3. Simulate access from an untrusted network: Attempt to open a document in the site from a non-corporate network and confirm that an MFA prompt is displayed before access is granted.

## Rollback
1. Remove the sensitivity label from the SharePoint site: Run `Set-SPOSite -Identity <SiteURL> -SensitivityLabel <LabelId>` with an empty or different label ID. 2. If needed, delete or unpublish the sensitivity label: In the Microsoft Purview compliance portal, navigate to Information Protection > Labels, select the label, and choose 'Delete label' or 'Unpublish label'. 3. Clear the authentication context assignment: Run `Set-SPOSite -Identity <SiteURL> -ConditionalAccessPolicy Off` in SharePoint Online Management Shell.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
