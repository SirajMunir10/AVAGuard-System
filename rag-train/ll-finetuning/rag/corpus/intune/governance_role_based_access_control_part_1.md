# Governance: Role-Based Access Control

**Domain:** Intune
**Subdomain:** Role-Based Access Control
**Incident Type:** Governance

## Scenario / Query
An Intune administrator reports that custom role assignments created for helpdesk staff are not applying correctly, and some users are able to perform actions that should be restricted. How can this governance issue be investigated and resolved?

## Environment Context
- **Tenant Type:** Microsoft Intune standalone (Azure AD joined)
- **Configuration:** Custom Intune role with permissions for 'Managed devices' and 'Corporate device identifiers' assigned to a security group containing helpdesk users.

## Symptoms
- Helpdesk users can perform actions like remote wipe or retire on devices they should not have permission to manage.
- Role assignment appears in Intune admin center but changes are not enforced after 30 minutes.
- Audit logs show 'Permission not granted' errors for some actions, but other actions succeed unexpectedly.

## Error Codes
N/A

## Root Causes
1. Custom role permissions were not scoped to the correct Azure AD security group or device group.
2. Role assignment propagation delay (up to 30 minutes) caused interim inconsistent behavior.
3. Role definition had overlapping permissions from a built-in role also assigned to the same users.

## Remediation Steps
1. Review the custom role assignment in Microsoft Intune admin center > Tenant administration > Roles > All roles > select the custom role > Assignments > verify the 'Groups' and 'Scope (Groups)' settings match the intended device management scope.
2. Ensure the assigned security group contains only the intended helpdesk users and no nested groups that expand scope.
3. Remove any conflicting built-in role assignments (e.g., 'Helpdesk Operator') from the same users to avoid permission overlap.
4. Wait at least 30 minutes for role propagation to complete, then test with a non-privileged account.
5. Use the 'Audit logs' in Intune to verify permission changes and identify unauthorized actions.

## Validation
After remediation, confirm that helpdesk users can only perform actions defined in the custom role on devices within the scoped group. Use the 'Effective permissions' view in Intune for a test user.

## Rollback
Reassign the custom role to the original group if changes were incorrect, or revert to built-in role assignments by removing the custom role assignment.

## References
- <https://learn.microsoft.com/en-us/mem/intune/fundamentals/role-based-access-control>
