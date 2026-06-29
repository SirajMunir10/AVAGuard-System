# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate programmatic access to backup policy details in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Programmatic access to backup policy details detected

## Error Codes
N/A

## Root Causes
1. User programmatically accessed details of a Microsoft 365 Backup policy

## Remediation Steps
1. Review the audit log for ViewBackupPolicyDetails activity
2. Verify user permissions and access controls

## Validation
Search the unified audit log for the 'ViewBackupPolicyDetails' activity using the Microsoft 365 Defender portal or the Search-UnifiedAuditLog cmdlet in Exchange Online PowerShell. Confirm that entries exist showing the user, timestamp, and details of the programmatic access. Example PowerShell command: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations ViewBackupPolicyDetails | Format-Table CreationDate, UserIds, Operations, AuditData

## Rollback
If the remediation causes issues, restore previous user permissions by removing any excessive access granted during the investigation. Use the Microsoft 365 admin center or Azure AD PowerShell to revert role assignments. For example, if a user was added to a privileged role, remove them using: Remove-MgRoleManagementDirectoryRoleAssignment -UnifiedRoleAssignmentId <id>. Additionally, ensure audit logging remains enabled and no other changes were made.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
