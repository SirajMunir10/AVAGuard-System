# Troubleshooting: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify the operation type when a sensitivity label is removed from a file or site?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured in Microsoft Purview compliance portal

## Symptoms
- Sensitivity label removed from file or site
- Audit log shows label removal activity

## Error Codes
N/A

## Root Causes
1. Label removed via Office for the web, details pane in SharePoint document library, Files tab in Teams, or auto-labeling policy
2. Label removed via Microsoft 365 apps
3. Label removed from a SharePoint site, Teams site that isn't group-connected, or Loop workspace

## Remediation Steps
1. Check the audit log for the specific activity: FileSensitivityLabelRemoved for Office for the web, details pane, or auto-labeling policy
2. Check the audit log for the specific activity: SensitivityLabelRemoved for Microsoft 365 apps
3. Check the audit log for the specific activity: SiteSensitivityLabelRemoved for site-level removal

## Validation
1. Go to Microsoft Purview compliance portal > Audit > Search audit log. 2. Set the Date range to cover the incident time. 3. In the Activities filter, select 'FileSensitivityLabelRemoved' and run the search. Confirm that the audit log shows entries with this activity for the affected file or site. 4. Repeat the search with 'SensitivityLabelRemoved' and confirm entries for Microsoft 365 apps. 5. Repeat the search with 'SiteSensitivityLabelRemoved' and confirm entries for site-level removal.

## Rollback
1. If the label removal was unintended, reapply the sensitivity label to the file or site using the same method that was used to remove it (e.g., via Office for the web, SharePoint details pane, Teams Files tab, or Microsoft 365 apps). 2. For site-level removal, navigate to the SharePoint site or Teams site settings and reapply the label under Sensitivity settings. 3. Verify reapplication by checking the audit log for the corresponding label application activity (e.g., FileSensitivityLabelApplied, SensitivityLabelApplied, SiteSensitivityLabelApplied).

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
