# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure an authentication context for a sensitivity label to enforce MFA or terms-of-use when accessing labeled SharePoint sites?

## Environment Context
- **Tenant Type:** Microsoft 365 with Microsoft Entra Conditional Access
- **Configuration:** Authentication context must be created and published for Conditional Access deployment

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose an existing authentication context that has been created and published for your organization's Conditional Access deployment.
2. Select an authentication context configured to require multifactor authentication (MFA) or terms-of-use (ToU) policies.
3. Apply the label to a SharePoint site containing highly confidential items.
4. Users from untrusted networks will see the MFA prompt or terms-of-use document before accessing documents.

## Validation
1. Verify the authentication context is assigned to the sensitivity label: Run `Get-Label -Identity "HighlyConfidential" | fl *authentication*` in Security & Compliance PowerShell. Confirm the 'AuthenticationContextId' field matches the GUID of the expected authentication context. 2. Confirm the label is published and applied to the target SharePoint site: Run `Get-SPOSite -Identity "https://contoso.sharepoint.com/sites/confidential" | fl SensitivityLabel` to ensure the label GUID is set. 3. Simulate access from an untrusted network: Use a browser in InPrivate/Incognito mode or a device not compliant with the Conditional Access policy. Navigate to the labeled SharePoint site and verify that an MFA prompt or terms-of-use acceptance page is displayed before document access is granted.

## Rollback
1. Remove the authentication context from the sensitivity label: Run `Set-Label -Identity "HighlyConfidential" -AuthenticationContextId $null` in Security & Compliance PowerShell. 2. If the label was applied to the SharePoint site, remove it: Run `Set-SPOSite -Identity "https://contoso.sharepoint.com/sites/confidential" -SensitivityLabel ""` (or set to a different label without authentication context). 3. Verify the site no longer enforces MFA/ToU: Access the site from an untrusted network and confirm that no additional authentication prompts appear beyond the standard sign-in.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
