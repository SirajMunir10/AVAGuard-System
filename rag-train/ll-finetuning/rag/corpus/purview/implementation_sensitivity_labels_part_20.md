# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure a sensitivity label to enforce terms-of-use (ToU) acceptance for accessing a SharePoint site?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Authentication context configured for terms-of-use (ToU) policies, applied to a SharePoint site with items requiring legal or compliance acceptance

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose an authentication context that is configured for terms-of-use (ToU) policies.
2. Apply this label to a SharePoint site that contains items that require a terms-of-use acceptance for legal or compliance reasons.
3. When users attempt to access a document in this site, they see a terms-of-use document that they must accept before they can access the original document.

## Validation
1. Verify that the sensitivity label is published and applied to the SharePoint site: Run Get-SPOSite -Identity <SiteURL> | Select-Object SensitivityLabel. 2. Confirm the authentication context is linked to the label: Run Get-Label -Identity <LabelName> | fl AuthenticationContext. 3. Test user access: As a test user, navigate to a document in the site and confirm the terms-of-use prompt appears before access is granted.

## Rollback
1. Remove the sensitivity label from the SharePoint site: Set-SPOSite -Identity <SiteURL> -SensitivityLabel "". 2. If needed, unassign the authentication context from the label: Set-Label -Identity <LabelName> -AuthenticationContext $null. 3. Publish the label changes: Run Start-SPOSiteContentJob -Identity <SiteURL> to propagate the removal.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
