# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify SystemSync activities in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Need to track data export creation
- Need to track data export deletion
- Need to track Lake Data copy downloads
- Need to track Lake Data copy generation

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search for DataShareCreated activity in audit log when user created data export
2. Search for DataShareDeleted activity in audit log when user deleted data export
3. Search for DownloadCopyOfLakeData activity in audit log when copy of Lake Data is downloaded
4. Search for GenerateCopyOfLakeData activity in audit log when copy of Lake Data is generated

## Validation
1. Run the following Search-UnifiedAuditLog command to confirm DataShareCreated activities are logged: Search-UnifiedAuditLog -Operations DataShareCreated -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) | Format-Table CreationTime, UserIds, Operations, ResultStatus -Auto. 2. Run the following command to confirm DataShareDeleted activities are logged: Search-UnifiedAuditLog -Operations DataShareDeleted -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) | Format-Table CreationTime, UserIds, Operations, ResultStatus -Auto. 3. Run the following command to confirm DownloadCopyOfLakeData activities are logged: Search-UnifiedAuditLog -Operations DownloadCopyOfLakeData -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) | Format-Table CreationTime, UserIds, Operations, ResultStatus -Auto. 4. Run the following command to confirm GenerateCopyOfLakeData activities are logged: Search-UnifiedAuditLog -Operations GenerateCopyOfLakeData -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) | Format-Table CreationTime, UserIds, Operations, ResultStatus -Auto. 5. Verify that each command returns at least one record with ResultStatus 'Succeeded' for the expected user actions.

## Rollback
1. If audit logging is not capturing the expected activities, verify that the Unified Audit Log is enabled by running: Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled. 2. If UnifiedAuditLogIngestionEnabled is False, enable it by running: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true. 3. If the issue persists, check that the user performing the actions has the appropriate license (e.g., E5 or A5) by reviewing the user's license assignment in the Microsoft 365 admin center. 4. If the problem continues, ensure that the audit log retention policy is configured to retain logs for the required period by running: Get-AdminAuditLogConfig | Format-List AuditLogRetentionPeriod. 5. If no records appear for the specific operations, confirm that the operations are supported in the tenant's region and service plan by reviewing the documentation at https://learn.microsoft.com/en-us/purview/audit-log-activities.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
