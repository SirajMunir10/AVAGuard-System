# Hardening: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Hardening

## Scenario / Query
How to minimize security risks when managing Microsoft Purview audit log roles?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Role-based access control

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use roles with the fewest permissions
2. Minimize the number of users with the Global Administrator role to improve security for your organization

## Validation
1. Confirm that only the minimum required roles (e.g., Audit Logs Administrator, Audit Logs Viewer) are assigned to users by running: Get-AzureADDirectoryRole | Where-Object {$_.DisplayName -like '*Audit*'} | ForEach-Object {Get-AzureADDirectoryRoleMember -ObjectId $_.ObjectId}. 2. Verify that no user holds both Global Administrator and any audit-specific role by running: Get-AzureADDirectoryRole | Where-Object {$_.DisplayName -eq 'Global Administrator'} | ForEach-Object {Get-AzureADDirectoryRoleMember -ObjectId $_.ObjectId}. 3. Check the audit log for role assignment changes using: Search-UnifiedAuditLog -Operations 'Add member to role', 'Remove member from role' -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date).

## Rollback
1. If a user was incorrectly removed from a required role, re-add them using: Add-AzureADDirectoryRoleMember -ObjectId '<RoleObjectId>' -RefObjectId '<UserObjectId>'. 2. If a user was incorrectly assigned a high-privilege role, remove them using: Remove-AzureADDirectoryRoleMember -ObjectId '<RoleObjectId>' -MemberId '<UserObjectId>'. 3. Restore any Global Administrator assignments that were changed by re-adding the user to the Global Administrator role: Add-AzureADDirectoryRoleMember -ObjectId (Get-AzureADDirectoryRole | Where-Object {$_.DisplayName -eq 'Global Administrator'}).ObjectId -RefObjectId '<UserObjectId>'.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
