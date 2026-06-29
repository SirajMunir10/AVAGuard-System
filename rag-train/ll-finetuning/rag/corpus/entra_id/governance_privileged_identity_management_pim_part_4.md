# Governance: Privileged Identity Management (PIM)

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management (PIM)
**Incident Type:** Governance

## Scenario / Query
A security auditor reports that several users have permanent, active Entra ID role assignments that bypass the approval and activation requirements of Privileged Identity Management (PIM). How can an administrator identify and remediate these standing privileged role assignments to enforce just-in-time access?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** PIM is enabled for Entra ID roles, but some roles were assigned directly via the Azure AD portal or PowerShell before PIM was configured, leaving permanent active assignments.

## Symptoms
- Users listed in PIM with 'Active' assignments that do not require activation
- Audit log entries showing role activation bypassed for certain users
- PIM reports showing a mix of eligible and active assignments for the same role

## Error Codes
N/A

## Root Causes
1. Roles were assigned directly through the Entra ID blade or via the Azure AD PowerShell module (Add-AzureADDirectoryRoleMember) instead of through PIM
2. PIM was enabled after some role assignments were already made, and those assignments were not converted to eligible assignments

## Remediation Steps
1. 1. Sign in to the Entra admin center as a Privileged Role Administrator.
2. 2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles.
3. 3. Select the role with permanent active assignments, go to Assignments, and identify users with 'Active' type.
4. 4. For each user, select 'Remove assignment' to revoke the permanent active assignment.
5. 5. Reassign the role as an 'Eligible' assignment through PIM, requiring activation with approval if configured.
6. 6. Alternatively, use the Microsoft Graph PowerShell SDK cmdlet Remove-MgRoleManagementDirectoryRoleAssignment to remove direct assignments.

## Validation
Run the PIM 'Eligible assignments' report for each role to confirm no permanent active assignments remain. Use the Microsoft Graph API to list role assignments and verify that all assignments are of type 'Eligible'.

## Rollback
If a user loses access due to removal, re-add the user as an eligible assignment in PIM and ensure they can activate the role.

## References
- Microsoft Learn: 'Remove Azure AD role assignments in Privileged Identity Management' â€“ https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-remove-role-assignments
