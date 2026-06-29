# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify admin activities related to Microsoft Places Directory in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Need to track creation, deletion, or update of places in Microsoft Places Directory

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search the audit log for the operation 'CreatedPlace' to find when an admin created a place
2. Search the audit log for the operation 'DeletedPlace' to find when an admin deleted a place
3. Search the audit log for the operation 'UpdatedPlace' to find when an admin updated a place

## Validation
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline. 2. Run the following command to search for 'CreatedPlace' operations: Search-UnifiedAuditLog -Operations 'CreatedPlace' -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) | Format-Table CreationDate, UserIds, Operations, AuditData. 3. Run the following command to search for 'DeletedPlace' operations: Search-UnifiedAuditLog -Operations 'DeletedPlace' -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) | Format-Table CreationDate, UserIds, Operations, AuditData. 4. Run the following command to search for 'UpdatedPlace' operations: Search-UnifiedAuditLog -Operations 'UpdatedPlace' -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) | Format-Table CreationDate, UserIds, Operations, AuditData. 5. Verify that the output includes entries for the expected admin activities, confirming that the audit log is capturing these events.

## Rollback
1. If the audit log search returns no results or unexpected results, verify that audit logging is enabled in the Microsoft 365 Purview compliance portal by navigating to Audit > Audit log and checking the status. 2. If audit logging is disabled, enable it by clicking 'Start recording user and admin activity' and wait up to 24 hours for historical data to populate. 3. Re-run the validation commands after enabling audit logging to confirm the operations are now captured. 4. If the issue persists, review the Microsoft 365 service health dashboard for any known issues with audit log ingestion or search.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
