# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify eDiscovery activities recorded in the Microsoft Purview audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Need to track eDiscovery case creation and management
- Need to monitor search actions for eDiscovery cases
- Need to audit hold creation and removal for eDiscovery cases
- Need to review set activities in eDiscovery cases

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search the audit log for eDiscovery activities as documented in 'Search the audit log'
2. Ensure administrators or eDiscovery managers (or any user assigned eDiscovery permissions) perform the following tasks: Creating and managing eDiscovery cases, Creating and editing searches for eDiscovery cases, Performing search actions (generating statistics, creating a sample, exporting from search), Creating, editing, and removing holds for eDiscovery cases, Creating review sets and performing review activities in eDiscovery cases

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search. 2. Set Activities filter to 'eDiscovery activities' and specify a date range covering the incident period. 3. Run the search and verify that entries appear for: 'CaseCreated', 'CaseDeleted', 'SearchCreated', 'SearchEdited', 'SearchExportPreviewResults', 'HoldCreated', 'HoldDeleted', 'ReviewSetCreated', 'ReviewSetAddedToReviewSet'. 4. Confirm each entry shows the correct user, timestamp, and item details.

## Rollback
1. If audit log search returns no expected eDiscovery activities, verify audit logging is enabled: Run `Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled` in Exchange Online PowerShell. 2. If disabled, enable with `Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true`. 3. If enabled but activities missing, confirm the user performing the eDiscovery actions has the 'eDiscovery Manager' role or equivalent permissions assigned in Microsoft Purview compliance portal > Roles > eDiscovery Manager. 4. If permissions are missing, add the user to the appropriate role group. 5. Re-run the audit log search after 24 hours to allow activity ingestion.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
