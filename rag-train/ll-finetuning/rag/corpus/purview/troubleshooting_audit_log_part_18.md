# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate programmatic listing of all backup items in the tenant in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- User programmatically got list of all protection units in the organization backed up using Microsoft 365 Backup

## Error Codes
N/A

## Root Causes
1. User accessed ListAllBackupItemsInTenant

## Remediation Steps
1. Review the audit log for ListAllBackupItemsInTenant activity
2. Verify user permissions and access controls

## Validation
Search the Microsoft 365 Purview audit log for the 'ListAllBackupItemsInTenant' activity. Use the following PowerShell command to confirm the activity was logged: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations 'ListAllBackupItemsInTenant'. Verify that the output includes the user, timestamp, and client IP. Additionally, confirm that the user's role does not include permissions that allow listing all backup items (e.g., Global Administrator, Backup Administrator) by running Get-AzureADDirectoryRoleMember -ObjectId (Get-AzureADDirectoryRole | Where-Object {$_.DisplayName -eq 'Backup Administrator'}).ObjectId.

## Rollback
If the audit log review reveals unauthorized access, immediately revoke the user's permissions by removing them from any privileged roles using Remove-AzureADDirectoryRoleMember -ObjectId <RoleObjectId> -MemberId <UserObjectId>. If the user had custom permissions, remove the relevant role assignment via the Microsoft 365 admin center. Then, re-run the audit log search to confirm no further 'ListAllBackupItemsInTenant' activity from that user. If the remediation caused issues (e.g., legitimate user unable to perform duties), restore the user's permissions by adding them back to the required role using Add-AzureADDirectoryRoleMember -ObjectId <RoleObjectId> -RefObjectId <UserObjectId>.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
