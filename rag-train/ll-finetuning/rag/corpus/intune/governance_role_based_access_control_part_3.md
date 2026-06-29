# Governance: Role-Based Access Control

**Domain:** Intune
**Subdomain:** Role-Based Access Control
**Incident Type:** Governance

## Scenario / Query
An Intune administrator reports that custom role assignments are not being enforced for device configuration profiles, and some users are unexpectedly able to modify policies they should not have access to.

## Environment Context
- **Tenant Type:** Microsoft Intune standalone (Azure AD tenant)
- **Configuration:** Custom Intune role created with 'Device configurations' permissions set to 'View reports' only, but assigned users can still edit profiles.

## Symptoms
- Users assigned a custom Intune role with 'View reports' permission for Device configurations can still edit and delete configuration profiles.
- Role assignment scope (e.g., specific security group) is ignored and all profiles are visible.
- Audit logs show 'Update device configuration' actions by users who should only have read access.

## Error Codes
N/A

## Root Causes
1. The custom role was created using the 'Intune Role Administrator' built-in role as a baseline, which includes broader permissions not overridden by the custom role.
2. Role assignments were not scoped to the correct Azure AD security group, or the scope group membership was misconfigured.
3. The custom role's permissions were not saved correctly after editing; the role may still inherit permissions from the built-in role.

## Remediation Steps
1. 1. Sign in to the Microsoft Intune admin center as a Global Administrator or Intune Service Administrator.
2. 2. Navigate to Tenant administration > Roles > All roles and select the custom role in question.
3. 3. Review the permissions assigned to the role. Ensure that only the intended permissions (e.g., 'View reports') are selected under each category.
4. 4. If the role was created from a built-in role, create a new custom role from scratch rather than modifying a copy of a built-in role to avoid inherited permissions.
5. 5. Verify the scope (groups) assigned to the role. Ensure the correct Azure AD security group is selected under 'Assignments' > 'Scope (Groups)'.
6. 6. Confirm that the users are members of the assigned scope group. Use Azure AD group membership reports to validate.
7. 7. After corrections, test by signing in as a user with the custom role and attempting to edit a device configuration profile. The action should be blocked.
8. 8. Review audit logs in Intune > Tenant administration > Audit logs to confirm that unauthorized modification attempts are now denied.

## Validation
After remediation, sign in as a user assigned the custom role and attempt to edit or delete a device configuration profile. The system should display an 'Access denied' or 'Insufficient permissions' message. Additionally, run the following Microsoft Graph PowerShell command (if available) to confirm the role permissions: Get-MgDeviceManagementRoleDefinition -RoleDefinitionId <role-id> | Select-Object -ExpandProperty RolePermissions

## Rollback
If the custom role was deleted during remediation, recreate it using the original settings documented in your change management records. Reassign the same scope groups and users.

## References
- <https://learn.microsoft.com/en-us/mem/intune/fundamentals/create-custom-role>
- <https://learn.microsoft.com/en-us/mem/intune/fundamentals/role-based-access-control>
