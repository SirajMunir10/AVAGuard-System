# Governance: Role-Based Access Control (AuthorizationFailed)

**Domain:** Governance
**Subdomain:** Role-Based Access Control
**Incident Type:** Governance

## Scenario / Query
A user reports they cannot assign the 'Security Reader' role to a new team member in the Azure portal, receiving an access denied error. How should the organization enforce least privilege for role assignments while still allowing delegated administration?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure RBAC with custom roles; Privileged Identity Management (PIM) not enabled

## Symptoms
- User receives 'Authorization failed' when attempting to assign a role via Azure portal
- Audit logs show 'Microsoft.Authorization/roleAssignments/write' operation denied
- Helpdesk tickets increase as only Global Administrators can assign roles

## Error Codes
- `AuthorizationFailed`

## Root Causes
1. User lacks Microsoft.Authorization/roleAssignments/write permission on the target scope
2. No custom role with delegated role assignment capability has been created
3. PIM not configured to allow just-in-time role activation

## Remediation Steps
1. Create a custom RBAC role that includes 'Microsoft.Authorization/roleAssignments/write' permission scoped to the appropriate management group, subscription, or resource group
2. Assign the custom role to the user or group that needs to delegate roles
3. Enable Azure AD Privileged Identity Management (PIM) to provide time-bound role activation and approval workflows
4. Configure PIM role settings to require approval for role assignments and set maximum activation duration
5. Review and audit role assignments regularly using Azure AD access reviews

## Validation
Verify that the user can now assign the Security Reader role to another user within the assigned scope. Confirm that PIM activation requests require approval and are logged.

## Rollback
Remove the custom role assignment from the user. Disable PIM role settings if no longer needed. Revert to default RBAC permissions.

## References
- <https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles-powershell>
- <https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure>
