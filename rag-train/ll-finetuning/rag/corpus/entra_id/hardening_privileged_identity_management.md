# Hardening: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Hardening

## Scenario / Query
How to enforce just-in-time (JIT) access and least privilege in Privileged Identity Management?

## Environment Context
- **Tenant Type:** Entra ID tenant with PIM licensed
- **Configuration:** PIM role settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use time-bound eligible role assignments to limit activation windows.
2. Require activation actions such as MFA, business justification, or approval.
3. Avoid permanent active assignments; use time-bound active assignments when necessary.
4. Minimize Global Administrator assignments and use specific administrator roles.

## Validation
1. Verify that all privileged role assignments are eligible, not permanently active, by running: Get-AzureADMSPrivilegedRoleAssignment -ProviderId 'aadRoles' -Filter 'assignmentState eq ''Active'' and isPermanent eq true'. Ensure no results are returned. 2. Confirm that at least one role requires approval for activation: Get-AzureADMSPrivilegedRoleSetting -ProviderId 'aadRoles' | Where-Object {$_.ApprovalRequired -eq $true}. 3. Check that MFA is enforced on activation: Get-AzureADMSPrivilegedRoleSetting -ProviderId 'aadRoles' | Select-Object RoleDefinitionId, MfaOnActivation. 4. Validate that Global Administrator assignments are minimized: Get-AzureADDirectoryRole -Filter 'roleTemplateId eq ''62e90394-69f5-4237-9190-012177145e10''' | Get-AzureADDirectoryRoleMember | Measure-Object. Ensure count is less than 5.

## Rollback
1. If a permanent active assignment was mistakenly removed, re-add it: Add-AzureADDirectoryRoleMember -ObjectId <roleObjectId> -RefObjectId <userObjectId>. 2. If activation approval was incorrectly enabled, disable it: Set-AzureADMSPrivilegedRoleSetting -ProviderId 'aadRoles' -RoleDefinitionId <roleId> -ApprovalRequired $false. 3. If MFA requirement was incorrectly enforced, disable it: Set-AzureADMSPrivilegedRoleSetting -ProviderId 'aadRoles' -RoleDefinitionId <roleId> -MfaOnActivation $false. 4. If a Global Administrator was incorrectly removed, restore the assignment: Add-AzureADDirectoryRoleMember -ObjectId (Get-AzureADDirectoryRole -Filter 'roleTemplateId eq ''62e90394-69f5-4237-9190-012177145e10''').ObjectId -RefObjectId <userObjectId>.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
