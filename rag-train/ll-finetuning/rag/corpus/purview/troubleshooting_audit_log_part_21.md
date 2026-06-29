# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate programmatic listing of restore points in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled; Only Global Admins have access

## Symptoms
- User programmatically got all restore points

## Error Codes
N/A

## Root Causes
1. User accessed ListAllRestorePoints

## Remediation Steps
1. Review the audit log for ListAllRestorePoints activity
2. Verify user permissions and access controls; only Global Admins should have access

## Validation
Search the unified audit log for the past 90 days using Search-UnifiedAuditLog -Operations ListAllRestorePoints. Confirm that only Global Admin accounts appear in the UserIds field. If any non-Global Admin user is found, the remediation has not fully succeeded.

## Rollback
If the remediation fails or causes issues, restore the previous permission configuration by re-adding any users or groups that were removed from the Global Admin role using Add-RoleGroupMember -Identity 'Global Admins' -Member <UserPrincipalName>. Then verify the change with Get-RoleGroupMember -Identity 'Global Admins'.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
