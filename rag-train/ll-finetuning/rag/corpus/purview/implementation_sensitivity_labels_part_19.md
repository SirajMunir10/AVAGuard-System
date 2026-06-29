# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure a sensitivity label to require multifactor authentication (MFA) for accessing a SharePoint site?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Authentication context configured to require MFA, applied to a SharePoint site with highly confidential items

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose an authentication context that is configured to require multifactor authentication (MFA).
2. Apply this label to a SharePoint site that contains highly confidential items.
3. When users from an untrusted network attempt to access a document in this site, they see the MFA prompt that they must complete before they can access the document.

## Validation
1. Verify that the authentication context is configured and requires MFA by running: Get-AzureADConditionalAccessPolicy | Where-Object {$_.DisplayName -eq 'MFA required for sensitive sites'}. 
2. Confirm the sensitivity label is published and applied to the SharePoint site by running: Get-Label -Identity 'Highly Confidential' | fl DisplayName, AuthenticationContextId. 
3. Test access from an untrusted network: Attempt to open a document in the labeled SharePoint site and confirm that an MFA prompt is displayed before access is granted.

## Rollback
1. Remove the authentication context from the sensitivity label by running: Set-Label -Identity 'Highly Confidential' -AuthenticationContextId $null. 
2. If needed, disable the conditional access policy that enforces MFA: Set-AzureADConditionalAccessPolicy -Id <PolicyId> -State 'disabled'. 
3. Revert the SharePoint site to a previous label or remove the label: Set-SPOSite -Identity <SiteURL> -SensitivityLabel <PreviousLabelId>.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
