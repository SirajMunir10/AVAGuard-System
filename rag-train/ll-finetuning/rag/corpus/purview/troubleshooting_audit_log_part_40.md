# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to track changes to document preview settings in SharePoint?

## Environment Context
- **Tenant Type:** SharePoint
- **Configuration:** Document preview

## Symptoms
- Document preview not working for users
- Preview mode enabled or disabled unexpectedly

## Error Codes
N/A

## Root Causes
1. Site administrator enabled or disabled document preview for a site

## Remediation Steps
1. Review audit log for PreviewModeEnabledSet activity
2. Identify the site administrator who made the change
3. Reconfigure document preview settings as needed

## Validation
1. Sign in to the Microsoft Purview compliance portal as a user with the Audit Log role. 2. Navigate to Solutions > Audit. 3. Under Search, set the Activities filter to 'PreviewModeEnabledSet'. 4. Set the Date range to cover the period when the issue occurred. 5. Click Search and confirm that at least one event with the activity 'PreviewModeEnabledSet' appears in the results. 6. Select an event and verify that the 'Item' field shows the SharePoint site URL and the 'User' field shows the site administrator who made the change. 7. Confirm that the current document preview setting for the affected site matches the intended configuration (e.g., using SharePoint Online Management Shell: `Get-SPOSite -Identity <SiteURL> | Select-Object -ExpandProperty DisablePreview` should return $false if preview is enabled).

## Rollback
1. If the audit log reveals that an unauthorized administrator disabled preview, run the following SharePoint Online Management Shell command to re-enable it: `Set-SPOSite -Identity <SiteURL> -DisablePreview $false`. 2. If the audit log reveals that an unauthorized administrator enabled preview and you need to disable it, run: `Set-SPOSite -Identity <SiteURL> -DisablePreview $true`. 3. After making the change, verify the setting by running: `Get-SPOSite -Identity <SiteURL> | Select-Object -ExpandProperty DisablePreview`. 4. If the change does not take effect immediately, wait up to 15 minutes for propagation and re-verify. 5. If the issue persists, review the audit log again for any subsequent 'PreviewModeEnabledSet' events that may have overwritten your change.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
