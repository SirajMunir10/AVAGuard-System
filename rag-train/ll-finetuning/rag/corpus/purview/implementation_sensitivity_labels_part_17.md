# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure sensitivity labels to control access to SharePoint sites from unmanaged devices?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** SharePoint site with sensitivity label applied

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the SharePoint feature that uses Microsoft Entra Conditional Access to block or limit access to SharePoint and OneDrive content from unmanaged devices.
2. Specify the option for this label setting, which is the equivalent of running a PowerShell command for a site as described in steps 3-5 from the Block or limit access to a specific SharePoint site or OneDrive section from the SharePoint instructions.

## Validation
1. Verify that the sensitivity label is published and applied to the target SharePoint site. 2. Sign in to the SharePoint site from an unmanaged device (e.g., a device not joined to Microsoft Entra ID or not compliant). 3. Confirm that access is blocked or limited according to the label setting (e.g., you see a message indicating access is restricted or you are redirected to a sign-in page that enforces conditional access). 4. Optionally, run the SharePoint Online PowerShell command: `Get-SPOSite -Identity <siteURL> | fl LockState, ConditionalAccessPolicy` and verify that `ConditionalAccessPolicy` is set to the expected value (e.g., `AllowLimitedAccess` or `BlockAccess`).

## Rollback
1. Remove or modify the sensitivity label setting that controls access from unmanaged devices. 2. If the label was applied to the site, remove the label from the site or change the label to one that does not enforce device restrictions. 3. Optionally, run the SharePoint Online PowerShell command: `Set-SPOSite -Identity <siteURL> -ConditionalAccessPolicy Off` to explicitly disable the conditional access policy for the site. 4. Verify that access from an unmanaged device is restored (e.g., you can access the site without restrictions).

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
- <https://learn.microsoft.com/en-us/sharepoint/control-access-from-unmanaged-devices>
