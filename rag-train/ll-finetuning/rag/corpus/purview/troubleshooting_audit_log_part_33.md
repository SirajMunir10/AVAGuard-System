# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to monitor completion of migration jobs in SharePoint?

## Environment Context
- **Tenant Type:** SharePoint
- **Configuration:** Migration jobs

## Symptoms
- Migration job status shows as completed but data may not be fully accessible

## Error Codes
N/A

## Root Causes
1. A migration job completed

## Remediation Steps
1. Check audit log for MigrationJobCompleted activity
2. Verify the migration job details in the SharePoint admin center
3. Ensure all migrated content is accessible and permissions are correctly applied

## Validation
1. Run the following command in the SharePoint Online Management Shell to check the migration job status: Get-SPOMigrationJob -TargetSiteUrl <SiteURL> | Where-Object {$_.JobState -eq 'Completed'}. 2. Search the Purview audit log for 'MigrationJobCompleted' activity using the Search-UnifiedAuditLog cmdlet: Search-UnifiedAuditLog -StartDate <StartDate> -EndDate <EndDate> -Operations 'MigrationJobCompleted'. 3. Verify that the migration job details in the SharePoint admin center show 'Completed' status and that the job ID matches the audit log entry. 4. Test access to migrated content by navigating to the target site and confirming that files and permissions are correctly applied.

## Rollback
1. If the migration job completed but data is not accessible, initiate a full re-scan of the migration job using: Set-SPOMigrationJob -TargetSiteUrl <SiteURL> -JobId <JobID> -Rescan. 2. If content is missing or permissions are incorrect, restore the previous version of the site from a backup or use the SharePoint admin center to revert to the pre-migration state. 3. If the audit log shows incomplete migration, cancel the current job and restart the migration using: Stop-SPOMigrationJob -TargetSiteUrl <SiteURL> -JobId <JobID> followed by Start-SPOMigrationJob -TargetSiteUrl <SiteURL> -SourcePath <SourcePath>.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
