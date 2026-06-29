# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure external sharing and Conditional Access settings for sensitivity labels applied to SharePoint sites?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels with scope including groups and sites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the Define protection settings for groups and sites page, select the options you want to configure: External sharing and Conditional Access settings.
2. Configure the Control external sharing from labeled SharePoint sites setting.
3. Configure the Use Microsoft Entra Conditional Access to protect labeled SharePoint sites setting.

## Validation
1. Navigate to Microsoft Purview compliance portal > Information protection > Sensitivity labels. 2. Select the label configured for groups and sites, then click 'Edit label'. 3. On the 'Define protection settings for groups and sites' page, verify that 'External sharing' and 'Conditional Access' settings are configured as intended. 4. For external sharing, confirm the 'Control external sharing from labeled SharePoint sites' setting matches the desired policy (e.g., 'Anyone with a link can share' or 'Only people in your organization'). 5. For Conditional Access, confirm the 'Use Microsoft Entra Conditional Access to protect labeled SharePoint sites' setting is enabled and linked to the correct Conditional Access policy. 6. Apply the label to a test SharePoint site and verify that external sharing options are restricted per the label configuration. 7. Attempt to access the site from a non-compliant device or location to confirm Conditional Access policies are enforced.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Information protection > Sensitivity labels. 2. Select the label configured for groups and sites, then click 'Edit label'. 3. On the 'Define protection settings for groups and sites' page, revert the 'Control external sharing from labeled SharePoint sites' setting to its previous state (e.g., 'Anyone with a link can share' if previously set to 'Only people in your organization'). 4. Disable the 'Use Microsoft Entra Conditional Access to protect labeled SharePoint sites' setting if it was enabled. 5. Save the label changes and reapply the label to any test sites used during validation. 6. Verify that external sharing and Conditional Access behaviors return to the original state by testing with a non-compliant device or external user.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
