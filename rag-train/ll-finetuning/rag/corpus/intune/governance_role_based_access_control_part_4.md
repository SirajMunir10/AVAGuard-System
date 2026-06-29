# Governance: Role-Based Access Control

**Domain:** Intune
**Subdomain:** Role-Based Access Control
**Incident Type:** Governance

## Scenario / Query
An Intune administrator reports that a custom role they created for help desk staff is granting unintended permissions. How can the organization audit and remediate custom Intune role assignments to ensure least privilege?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Intune
- **Configuration:** Custom Intune roles created via Microsoft Intune admin center or Microsoft Graph

## Symptoms
- Help desk users can perform actions beyond their assigned scope (e.g., delete devices, modify compliance policies).
- Audit logs show unexpected role assignment changes.
- Custom role definition includes permissions that were not intended by the administrator.

## Error Codes
N/A

## Root Causes
1. Custom Intune role was created with overly broad permissions (e.g., 'All' scope instead of specific scope tags).
2. Role assignment was not reviewed after creation.
3. No periodic access review process for Intune roles.

## Remediation Steps
1. Sign in to the Microsoft Intune admin center as a user with the Intune Administrator role.
2. Go to Tenant administration > Roles > All roles and select the custom role in question.
3. Review the permissions assigned to the role and remove any unnecessary permissions. Documented guidance: 'You can remove permissions from a custom role by editing the role.'
4. Use scope tags to restrict the role's administrative scope to specific groups or devices.
5. Assign the role only to the required users or groups.
6. Enable audit logging and review the Audit log for role assignment changes.
7. Implement a periodic access review process using Microsoft Entra ID Governance (e.g., access reviews for Intune roles).

## Validation
Verify that the help desk users can no longer perform unintended actions by testing the role with a test user. Confirm that audit logs show the updated role permissions.

## Rollback
If the remediation causes unintended loss of access, re-add the removed permissions to the custom role or reassign the previous role version (if backed up).

## References
- <https://learn.microsoft.com/en-us/mem/intune/fundamentals/create-custom-role>
- <https://learn.microsoft.com/en-us/mem/intune/fundamentals/role-based-access-control>
