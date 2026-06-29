# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure sensitivity labels to protect containers such as Microsoft Teams sites, Microsoft 365 groups, SharePoint sites, Viva Engage communities, and Loop workspaces?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured for container-level protection

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the following label settings: Privacy (public or private), External user access, External sharing from SharePoint sites, Access from unmanaged devices, Authentication contexts, Prevent discovery of private teams for users who have this capability, Shared channels control for team invitations, Default sharing link for a SharePoint site (PowerShell-only configuration), Site sharing settings (PowerShell-only configuration), Default label for channel meetings.
2. Configure Microsoft Entra Conditional Access for settings related to unmanaged devices and authentication contexts.
3. Ensure sensitivity labels for Office files in SharePoint and OneDrive are enabled so users can label documents in SharePoint sites or team sites.

## Validation
1. Verify that the sensitivity label is published and applied to a container (e.g., a Microsoft 365 group or SharePoint site).
2. Run the following PowerShell command to confirm the label is applied to a specific group:
   Get-UnifiedGroup -Identity <GroupName> | fl SensitivityLabel
3. For SharePoint sites, use:
   Get-SPOSite -Identity <SiteURL> | fl SensitivityLabel
4. Check that the container’s privacy setting matches the label configuration:
   Get-UnifiedGroup -Identity <GroupName> | fl AccessType
5. Validate external sharing settings on the SharePoint site:
   Get-SPOSite -Identity <SiteURL> | fl SharingCapability
6. Confirm that Conditional Access policies for unmanaged devices and authentication contexts are enforced by signing in from an unmanaged device and verifying access is blocked or restricted.
7. Ensure sensitivity labels for Office files in SharePoint and OneDrive are enabled:
   Get-SPOTenant | fl EnableAIPIntegration

## Rollback
1. Remove the sensitivity label from the container:
   Set-UnifiedGroup -Identity <GroupName> -SensitivityLabel <LabelGUID> -RemoveSensitivityLabel
2. For SharePoint sites:
   Set-SPOSite -Identity <SiteURL> -SensitivityLabel <LabelGUID> -RemoveSensitivityLabel
3. Reset the container’s privacy setting to the original value:
   Set-UnifiedGroup -Identity <GroupName> -AccessType Private (or Public)
4. Restore external sharing settings on the SharePoint site:
   Set-SPOSite -Identity <SiteURL> -SharingCapability ExternalUserAndGuestSharing (or original value)
5. Disable or modify the associated Conditional Access policy in Microsoft Entra admin center to remove restrictions for unmanaged devices or authentication contexts.
6. If needed, disable sensitivity labels for Office files in SharePoint and OneDrive:
   Set-SPOTenant -EnableAIPIntegration $false

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
