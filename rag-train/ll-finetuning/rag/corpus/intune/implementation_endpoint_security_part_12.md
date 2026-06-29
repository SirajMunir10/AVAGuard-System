# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to assign built-in RBAC roles for endpoint security policy management in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Endpoint Security Manager, Help Desk Operator, Read Only Operator roles

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign the Endpoint Security Manager role for full management capabilities across all endpoint security policies.
2. Assign the Help Desk Operator role for limited operational tasks and read access.
3. Assign the Read Only Operator role for view-only access to policies and reports.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Tenant administration > Roles > All roles.
3. Select the 'Endpoint Security Manager' role and click 'Assignments'.
4. Verify that the intended users or groups are listed under 'Members'.
5. Repeat steps 3-4 for the 'Help Desk Operator' and 'Read Only Operator' roles.
6. As a test user assigned to each role, sign in to the Intune admin center and confirm:
   - Endpoint Security Manager: Can create, edit, and delete endpoint security policies under 'Endpoint security'.
   - Help Desk Operator: Can view policies and perform limited tasks (e.g., assign policies) but cannot create or delete policies.
   - Read Only Operator: Can view policies and reports under 'Endpoint security' but cannot make any changes.
7. Check that the correct scope groups (if any) are applied to each role assignment.

## Rollback
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Tenant administration > Roles > All roles.
3. Select the 'Endpoint Security Manager' role and click 'Assignments'.
4. Select the assignment that was created or modified, then click 'Delete' to remove the role assignment.
5. Repeat steps 3-4 for the 'Help Desk Operator' and 'Read Only Operator' roles if they were assigned.
6. If the original configuration used different roles or assignments, reapply those previous settings.
7. Verify that the affected users no longer have the unintended permissions by checking their access to 'Endpoint security' policies.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
