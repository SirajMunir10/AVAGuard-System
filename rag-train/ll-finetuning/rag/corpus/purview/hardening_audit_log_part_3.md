# Hardening: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Hardening

## Scenario / Query
How to minimize the number of users with the Global Administrator role to improve security?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Purview roles and permissions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use roles with the fewest permissions.
2. Minimize the number of users with the Global Administrator role.

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a Global Administrator. 2. Navigate to Roles & scopes > Permissions > Roles. 3. Under 'Azure AD roles', select 'Global Administrator' and review the list of assigned users. 4. Confirm that the number of users assigned to the Global Administrator role is minimized according to your organization's security policy. 5. Optionally, run the following Azure AD PowerShell command to list Global Administrators: Get-AzureADDirectoryRole | Where-Object {$_.DisplayName -eq 'Global Administrator'} | Get-AzureADDirectoryRoleMember | Select-Object DisplayName, UserPrincipalName. 6. Verify that no unauthorized or excessive users hold the role.

## Rollback
1. Sign in to the Microsoft 365 admin center (https://admin.microsoft.com) as a Global Administrator. 2. Go to Users > Active users. 3. Select the user who was removed from the Global Administrator role. 4. Under the 'Roles' tab, click 'Manage roles'. 5. Select 'Global Administrator' and save the changes. 6. Alternatively, use Azure AD PowerShell: Add-AzureADDirectoryRoleMember -ObjectId <GlobalAdminRoleObjectId> -RefObjectId <UserObjectId>. 7. Verify the user is reassigned by checking the Global Administrator list again.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
