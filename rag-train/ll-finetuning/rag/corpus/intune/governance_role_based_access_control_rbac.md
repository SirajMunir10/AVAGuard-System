# Governance: Role-Based Access Control (RBAC)

**Domain:** Intune
**Subdomain:** Role-Based Access Control (RBAC)
**Incident Type:** Governance

## Scenario / Query
An Intune administrator discovers that a custom role assigned to helpdesk staff allows them to delete managed devices, which violates the principle of least privilege. How should the role be corrected to remove the delete permission while preserving other necessary actions?

## Environment Context
- **Tenant Type:** Microsoft Intune standalone (Azure AD joined)
- **Configuration:** Custom Intune role with permissions: 'Managed devices / Delete' set to 'Yes'; 'Managed devices / Read' set to 'Yes'; 'Managed devices / Retire' set to 'Yes'

## Symptoms
- Helpdesk staff can delete corporate-owned devices from Intune without approval
- Audit logs show 'Delete Managed Device' actions performed by non-admin helpdesk users
- Devices removed from management without a corresponding retire or wipe action

## Error Codes
N/A

## Root Causes
1. Custom Intune role was created with the 'Delete' permission on Managed Devices, which is not required for typical helpdesk operations
2. No separation of duties between device management and device deletion

## Remediation Steps
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com)
2. Navigate to Tenant administration > Roles > All roles
3. Select the custom role assigned to the helpdesk group
4. Click Properties, then Permissions
5. Under the 'Managed devices' category, set 'Delete' to 'No'
6. Click Review + create, then Update to save the role
7. Verify that the change takes effect immediately (no user sign-out required)

## Validation
As a test, sign in as a helpdesk user and attempt to delete a managed device from the Intune console. The 'Delete' option should be grayed out or absent. Confirm via audit logs that no new delete actions appear.

## Rollback
Re-edit the same custom role and set 'Managed devices / Delete' back to 'Yes' to restore the previous permission.

## References
- <https://learn.microsoft.com/en-us/mem/intune/fundamentals/create-custom-role>
