# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure sensitivity labels to enforce authentication contexts for SharePoint site access?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** SharePoint site with sensitivity label applied and existing authentication context

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select an existing authentication context that has been created and published for your organization's Conditional Access deployment.
2. If users don't meet the configured conditions or if they use apps that don't support authentication contexts, they are denied access.

## Validation
1. Verify that the sensitivity label is published and applied to the SharePoint site. Run: Get-SPOSite -Identity <SiteURL> | Select-Object SensitivityLabel. 2. Confirm the authentication context is enforced by attempting to access the site from a non-compliant device or app; access should be denied. 3. Check the Conditional Access policy logs in Azure AD for sign-in events related to the site to ensure the authentication context is being evaluated.

## Rollback
1. Remove the authentication context assignment from the sensitivity label by editing the label in the Microsoft Purview compliance portal and clearing the 'Use authentication context' setting. 2. If the label was applied to the site, remove the label from the site using: Set-SPOSite -Identity <SiteURL> -SensitivityLabel <LabelGuid> -RemoveLabel. 3. Verify that users can access the site without the authentication context requirement.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
