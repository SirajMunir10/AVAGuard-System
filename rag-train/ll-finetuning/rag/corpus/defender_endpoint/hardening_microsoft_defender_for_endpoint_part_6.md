# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
What permissions are required to perform response actions on files in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 2
- **Configuration:** Role-based access control permissions for Alerts investigation, Live response basic, Live response advanced

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the permissions table for portable executable (PE) and non-PE files: Alerts investigation, Live response basic, Live response advanced.
2. Use roles with the fewest permissions to improve security.
3. Limit Global Administrator role to emergency scenarios when no existing role can be used.
4. For more information on roles, see 'Create and manage roles for role-based access control'.

## Validation
1. Verify that the user account has the required permissions by checking the assigned RBAC role in Microsoft Defender for Endpoint (security.microsoft.com > Permissions > Roles).
2. Confirm the role includes 'Alerts investigation' permission for basic response actions on files.
3. Confirm the role includes 'Live response basic' or 'Live response advanced' permission for live response actions on files.
4. Test by initiating a response action (e.g., 'Collect file' or 'Stop and quarantine') on a test file and ensure no permission error is returned.
5. Review audit logs in Microsoft 365 Defender for successful action execution.

## Rollback
1. If the remediation fails due to insufficient permissions, assign a role with the required permissions (e.g., 'Security Operator' or custom role with 'Alerts investigation' and 'Live response basic').
2. If the remediation causes unintended access, remove the assigned role or modify it to remove the 'Live response advanced' permission.
3. Revert to the original role configuration by reassigning the previous role or removing the custom role.
4. For emergency scenarios, temporarily assign the Global Administrator role and then remove it after the action is completed.
5. Document the change and monitor for any unauthorized actions in the audit log.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
