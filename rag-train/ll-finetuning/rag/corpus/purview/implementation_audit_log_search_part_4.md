# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
What roles are required to search the audit log in the Microsoft Purview portal?

## Environment Context
- **Tenant Type:** Microsoft 365 or Office 365 enterprise
- **Configuration:** Audit Logs or View-Only Audit Logs roles

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign the Audit Logs or View-Only Audit Logs roles in the Microsoft Purview portal
2. Assign the Audit Logs or View-Only Audit Logs roles in the Exchange admin center to access audit cmdlets
3. Create custom role groups with the ability to search the audit log by adding the View-Only Audit Logs or Audit Logs roles to a custom role group

## Validation
1. In the Microsoft Purview portal, navigate to Solutions > Audit. Confirm that the 'Search' button is active and that you can execute a search query (e.g., search for activities from the last 24 hours).
2. Run the Exchange Online PowerShell command: Get-ManagementRoleAssignment -Role "Audit Logs" | Format-List User, Role, RoleAssigneeType. Verify that the intended user or group appears in the output.
3. Run the Exchange Online PowerShell command: Get-ManagementRoleAssignment -Role "View-Only Audit Logs" | Format-List User, Role, RoleAssigneeType. Verify that the intended user or group appears in the output.
4. If a custom role group was created, run: Get-RoleGroupMember "<CustomRoleGroupName>" | Format-List Name, RecipientType. Confirm the user is listed.

## Rollback
1. In the Microsoft Purview portal, navigate to Roles & Scopes > Role groups, select the role group containing the 'Audit Logs' or 'View-Only Audit Logs' role, and remove the user from the group.
2. In the Exchange admin center, go to Roles > Admin roles, select the role group, and remove the user.
3. If a custom role group was created, delete the custom role group via the Exchange admin center or PowerShell: Remove-RoleGroup "<CustomRoleGroupName>" -Confirm:$false.
4. Run the Exchange Online PowerShell command: Get-ManagementRoleAssignment -Role "Audit Logs" | Where-Object {$_.User -eq "<UserPrincipalName>"} | Remove-ManagementRoleAssignment -Confirm:$false.
5. Run the Exchange Online PowerShell command: Get-ManagementRoleAssignment -Role "View-Only Audit Logs" | Where-Object {$_.User -eq "<UserPrincipalName>"} | Remove-ManagementRoleAssignment -Confirm:$false.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
