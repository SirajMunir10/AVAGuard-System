# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate programmatic listing of all backup policies in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- User programmatically got the list of all backup policies

## Error Codes
N/A

## Root Causes
1. User accessed ListAllBackupPolicies

## Remediation Steps
1. Review the audit log for ListAllBackupPolicies activity
2. Verify user permissions and access controls

## Validation
Search the unified audit log for the 'ListAllBackupPolicies' activity. Use the Search-UnifiedAuditLog cmdlet with StartDate and EndDate parameters covering the incident timeframe, and filter by Operations 'ListAllBackupPolicies'. Confirm that the audit records show the user's identity, client IP, and timestamp. Additionally, verify that the user's role assignments (e.g., via Get-RoleGroupMember) do not include any backup administrator roles beyond their required scope.

## Rollback
If the audit log review reveals unauthorized access, immediately revoke the user's permissions by removing them from any backup-related role groups using Remove-RoleGroupMember. If the user requires backup access for legitimate purposes, re-add them to a more restrictive role group (e.g., Backup Reader) using Add-RoleGroupMember. Finally, re-run the audit log search to confirm no further unauthorized ListAllBackupPolicies activity occurs.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
