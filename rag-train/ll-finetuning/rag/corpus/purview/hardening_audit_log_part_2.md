# Hardening: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Hardening

## Scenario / Query
What permissions are required to access audit logs in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log access permissions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Users need to be a global admin or have audit read permissions to access audit logs.
2. Microsoft recommends that you use roles with the fewest permissions.
3. Minimizing the number of users with the Global Administrator role helps improve security for your organization.

## Validation
1. Confirm the user account is assigned the 'Audit Logs' role or 'View-Only Audit Logs' role in the Microsoft Purview compliance portal (Roles & scopes > Roles).
2. Run the following PowerShell command to verify the user's effective audit log access:
   Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -ResultSize 1
   If the command returns results, the user has audit log read permissions.
3. Alternatively, navigate to Microsoft Purview > Audit > Search and attempt to run a simple audit log search. A successful search confirms access.

## Rollback
1. Remove the 'Audit Logs' or 'View-Only Audit Logs' role assignment from the user in the Microsoft Purview compliance portal (Roles & scopes > Roles > select the role > remove member).
2. If the user was previously a Global Administrator, reassign the Global Administrator role via Azure AD > Roles and administrators > Global Administrator > Add assignments.
3. Verify the user can no longer access audit logs by running:
   Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -ResultSize 1
   This should now fail with an access denied error.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
