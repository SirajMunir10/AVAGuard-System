# Governance: Role-Based Access Control

**Domain:** Intune
**Subdomain:** Role-Based Access Control
**Incident Type:** Governance

## Scenario / Query
An Intune administrator reports that a custom role they created for help desk staff is no longer granting the 'Read' permission for managed devices, even though the role assignment appears correct. What governance issue could cause this, and how should it be resolved?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Intune
- **Configuration:** Custom Intune role assigned to a security group containing help desk users; role definition includes 'Managed devices' > 'Read' permission.

## Symptoms
- Help desk users receive 'Access denied' when trying to view managed device properties in the Intune admin center.
- The custom role assignment still shows the correct security group and scope tags.
- No recent changes to the role definition were made by the administrator.

## Error Codes
N/A

## Root Causes
1. The custom role's 'Read' permission for 'Managed devices' was inadvertently removed by another administrator with the 'Intune Administrator' role, or the role definition was overwritten by a policy refresh that did not include the intended permissions.

## Remediation Steps
1. Sign in to the Microsoft Intune admin center as a user with the 'Intune Administrator' or 'Global Administrator' role.
2. Go to 'Tenant administration' > 'Roles' > 'All roles' and select the custom role.
3. Review the 'Permissions' tab to verify that 'Managed devices' > 'Read' is enabled.
4. If the permission is missing, edit the role and add the 'Read' permission under 'Managed devices'.
5. Save the role and confirm that the assignment to the security group is still active.
6. Instruct affected users to sign out and sign back in to refresh their permissions.

## Validation
Ask the help desk users to navigate to 'Devices' > 'All devices' in the Intune admin center and confirm they can see the device list and properties.

## Rollback
If the permission was intentionally removed for security reasons, document the change and communicate the new access level to the help desk team. Do not re-add the permission without proper governance approval.

## References
- <https://learn.microsoft.com/en-us/mem/intune/fundamentals/create-custom-role>
