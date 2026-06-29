# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure a sensitivity label to enforce access conditions on SharePoint sites using authentication contexts?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Entra Conditional Access deployment with authentication contexts

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose an existing authentication context that has been created and published for your organization's Conditional Access deployment.
2. Apply the label to a SharePoint site that contains highly confidential items.
3. Configure the authentication context to require multifactor authentication (MFA) or terms-of-use (ToU) policies as needed.

## Validation
1. Verify that the authentication context is assigned to the sensitivity label by running: Get-SensitivityLabel -Identity 'YourLabelName' | Select-Object -ExpandProperty Settings. 2. Confirm the label is published to the SharePoint site by checking site permissions or using: Get-SPOSite -Identity 'https://yourtenant.sharepoint.com/sites/yoursite' | Select-Object -ExpandProperty SensitivityLabel. 3. Test access by attempting to open the site from a session that does not meet the authentication context requirements (e.g., without MFA) and confirm access is blocked. 4. Review Conditional Access logs in Entra ID to ensure the authentication context policy is enforced.

## Rollback
1. Remove the authentication context assignment from the sensitivity label by running: Set-SensitivityLabel -Identity 'YourLabelName' -RemoveSettings @('AuthenticationContextId'). 2. If the label was applied to the site, remove it by running: Set-SPOSite -Identity 'https://yourtenant.sharepoint.com/sites/yoursite' -SensitivityLabel '' (or set to a different label without authentication context). 3. Verify the site is accessible without the authentication context requirement by testing access from a non-compliant session. 4. If needed, disable or delete the authentication context in Entra ID via Conditional Access > Authentication contexts.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
