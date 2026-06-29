# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate programmatic listing of backup items in a workload in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- User programmatically got list of all protection units in workload (SharePoint, OneDrive, or Exchange) backed up using Microsoft 365 Backup

## Error Codes
N/A

## Root Causes
1. User accessed ListAllBackupItemsInWorkload

## Remediation Steps
1. Review the audit log for ListAllBackupItemsInWorkload activity
2. Verify user permissions and access controls

## Validation
Search the Microsoft 365 Purview audit log for the 'ListAllBackupItemsInWorkload' activity. Use the following PowerShell command to retrieve audit records: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations 'ListAllBackupItemsInWorkload' -ResultSize 1000. Verify that the output includes the user who performed the action, the workload (SharePoint, OneDrive, or Exchange), and the timestamp. Confirm that the audit records match the expected scope and that no unauthorized access is present.

## Rollback
If the audit log review reveals unauthorized access or misconfigured permissions, immediately revoke the user's access to the Microsoft 365 Backup service by removing the user from the appropriate role group (e.g., Backup Administrator) in the Microsoft 365 Defender portal or via the Exchange admin center. Additionally, disable any service principal or application that was used for programmatic access. To prevent recurrence, review and update Conditional Access policies to restrict backup API access. Document the changes and monitor the audit log for any further 'ListAllBackupItemsInWorkload' activity.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
