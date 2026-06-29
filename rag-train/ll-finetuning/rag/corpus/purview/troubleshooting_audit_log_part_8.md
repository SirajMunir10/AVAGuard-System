# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify folder activities recorded in the Microsoft 365 audit log for SharePoint and OneDrive?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Need to track folder operations like copy, create, delete, modify, move, rename, restore in SharePoint or OneDrive

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the Folder activities table in the audit log documentation
2. Check for FolderCopied, FolderCreated, FolderDeleted, FolderDeletedFirstStageRecycleBin, FolderDeletedSecondStageRecycleBin, FolderModified, FolderMoved, FolderRenamed, FolderRestored activities

## Validation
Search the Microsoft 365 audit log for folder activities using the following PowerShell command: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations FolderCopied, FolderCreated, FolderDeleted, FolderDeletedFirstStageRecycleBin, FolderDeletedSecondStageRecycleBin, FolderModified, FolderMoved, FolderRenamed, FolderRestored -ResultSize 1000. Confirm that the output includes records with the expected folder operations and that the 'Item' field contains folder paths (e.g., 'Shared Documents/FolderName').

## Rollback
If the audit log search returns unexpected or missing results, verify that audit logging is enabled by running: Get-AdminAuditLogConfig | fl UnifiedAuditLogIngestionEnabled. If disabled, enable it with: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true. Then re-run the search with a broader date range (e.g., -StartDate (Get-Date).AddDays(-90)). If the issue persists, review the audit log schema at https://learn.microsoft.com/en-us/purview/audit-log-activities to ensure the correct operation names are used.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
