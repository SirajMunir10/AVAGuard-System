# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to monitor legacy workflow enablement in SharePoint?

## Environment Context
- **Tenant Type:** SharePoint
- **Configuration:** SharePoint 2013 Workflow Task content type

## Symptoms
- Legacy workflows not functioning
- Workflow options appearing or disappearing

## Error Codes
N/A

## Root Causes
1. Site administrator or owner added the SharePoint 2013 Workflow Task content type to the site, or global administrator enabled workflows for the entire organization

## Remediation Steps
1. Check audit log for LegacyWorkflowEnabledSet activity
2. Identify who enabled the legacy workflow
3. Verify workflow settings and content type availability

## Validation
Search the Purview audit log for LegacyWorkflowEnabledSet activity within the relevant time range. Use the command: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations LegacyWorkflowEnabledSet. Confirm that no entries appear, or if entries exist, verify that the SharePoint 2013 Workflow Task content type is not present on the site by checking Site Settings > Site Content Types > Add from existing site content types. Ensure the content type is not listed.

## Rollback
If legacy workflows are still not functioning or options are missing, remove the SharePoint 2013 Workflow Task content type from the site. Navigate to Site Settings > Site Content Types, select the content type, and click Delete this content type. If the issue persists, disable legacy workflows at the tenant level using the SharePoint Online Management Shell: Set-SPOTenant -LegacyWorkflowsEnabled $false. Re-run the audit log search to confirm no further LegacyWorkflowEnabledSet activities occur.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
