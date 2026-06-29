# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure a sensitivity label to block or limit access to SharePoint sites from unmanaged devices using Microsoft Entra Conditional Access?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Entra Conditional Access configured and in use

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the option 'Use Microsoft Entra Conditional Access to protect labeled SharePoint sites'.
2. Choose the setting 'Determine whether users can access SharePoint sites from unmanaged devices'.
3. The option specified is the equivalent of running a PowerShell command for a site, as described in steps 3-5 from the 'Block or limit access to a specific SharePoint site or OneDrive' section from the SharePoint instructions.

## Validation
1. Verify that the sensitivity label is published and applied to a SharePoint site. 2. Sign in as a user from an unmanaged device (a device not joined or compliant with Microsoft Entra ID). 3. Attempt to access the labeled SharePoint site. 4. Confirm that access is blocked or limited (e.g., you receive a conditional access block page or are prompted for additional authentication). 5. Alternatively, run the SharePoint Online PowerShell command: `Get-SPOSite -Identity <SiteURL> | fl LockState, ConditionalAccessPolicy` and confirm that `ConditionalAccessPolicy` is set to `BlockAccess` or `AllowLimitedAccess` as configured.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Information Protection > Sensitivity labels. 2. Edit the sensitivity label that was configured. 3. Under 'Protect labeled SharePoint sites', clear the option 'Use Microsoft Entra Conditional Access to protect labeled SharePoint sites' or change the setting to 'Allow full access from unmanaged devices'. 4. Alternatively, run the SharePoint Online PowerShell command: `Set-SPOSite -Identity <SiteURL> -ConditionalAccessPolicy Off` to remove the conditional access policy from the specific site. 5. Publish the updated label if necessary and wait for replication.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
