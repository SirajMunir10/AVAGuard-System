# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure a sensitivity label with an authentication context requiring terms-of-use acceptance for a SharePoint site?

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
1. Choose an authentication context that is configured for terms-of-use (ToU) policies.
2. Apply this label to a SharePoint site that contains items that require a terms-of-use acceptance for legal or compliance reasons.
3. As a result, when users attempt to access a document in this site, they see a terms-of-use document that they must accept before they can access the original document.

## Validation
1. Verify that the authentication context is configured with a terms-of-use policy: Run `Get-AzureADIdentityProtectionPolicy` or check in the Azure AD portal under 'Security > Conditional Access > Authentication context' to confirm the context is linked to a ToU policy.
2. Confirm the sensitivity label is published and applied to the target SharePoint site: Use `Get-Label | Where-Object {$_.DisplayName -eq '<LabelName>'}` in the Security & Compliance PowerShell to ensure the label exists and has the 'AuthenticationContext' setting.
3. Test access to a document in the labeled SharePoint site: As a user, navigate to the site and open a document. Verify that a terms-of-use acceptance prompt appears before the document is accessible.

## Rollback
1. Remove the sensitivity label from the SharePoint site: Use `Set-SPOSite -Identity '<SiteURL>' -SensitivityLabel ''` in SharePoint Online PowerShell to clear the label.
2. If the label itself needs to be removed or disabled: Use `Remove-Label -Identity '<LabelName>'` in Security & Compliance PowerShell, or set its status to 'Disabled' with `Set-Label -Identity '<LabelName>' -Enabled $false`.
3. Optionally, delete or disable the associated authentication context in Azure AD: Navigate to 'Azure AD > Security > Conditional Access > Authentication context' and remove or deactivate the context.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
