# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure external user access for containers using sensitivity labels in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured for containers (Teams, Groups, Sites)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Control whether the owner can add guests to the container, similar to Manage guest access in Microsoft 365 groups.
2. If you selected External sharing and Conditional Access settings, now configure the following settings:
3. Control external sharing from labeled SharePoint sites: Select this option to then select either external sharing for anyone, new and existing guests, existing guests, or only people in your organization.
4. Use Microsoft Entra Conditional Access to protect labeled SharePoint sites: Select this option only if your organization has configured and is using Microsoft Entra Conditional Access.
5. Then, select one of the following settings:
6. Determine whether users can access SharePoint sites from unmanaged devices: This option uses the SharePoint feature that uses Microsoft Entra Conditional Access to block or limit access to SharePoint and OneDrive content from unmanaged devices.
7. The option you specify for this label setting is the equivalent of running a PowerShell command for a site, as described in steps 3-5 from the Block or limit access to a specific SharePoint site or OneDrive section from the SharePoint instructions.

## Validation
1. Verify that the sensitivity label is published and applied to a test container (e.g., Microsoft 365 group, team, or SharePoint site).
2. For the labeled container, confirm the external sharing setting: navigate to SharePoint Admin Center > Active sites > select the site > Settings > External sharing, and ensure it matches the label's configured option (e.g., 'New and existing guests').
3. If Conditional Access was configured, sign in as an external guest user and attempt to access the container; verify that access is granted or blocked as expected.
4. Run the following PowerShell command to check the external sharing status for a specific site: Get-SPOSite -Identity <siteURL> | Select-Object SharingCapability. Confirm the value aligns with the label's setting.
5. If 'Determine whether users can access SharePoint sites from unmanaged devices' was set, test access from an unmanaged device and confirm the expected block or limited access.

## Rollback
1. Remove or reassign the sensitivity label from the affected container(s) by editing the label settings in the Microsoft Purview compliance portal > Information protection > Labels, and uncheck the container-related settings.
2. If external sharing was changed, revert to the original sharing setting via SharePoint Admin Center > Active sites > select the site > Settings > External sharing, and choose the previous option.
3. If Conditional Access policies were applied, disable or remove the specific policy in the Microsoft Entra admin center > Protection > Conditional Access.
4. For unmanaged device access control, reset the site's device access policy by running: Set-SPOSite -Identity <siteURL> -ConditionalAccessPolicy Off.
5. Wait for replication (up to 24 hours) and then re-test external user access to confirm the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
