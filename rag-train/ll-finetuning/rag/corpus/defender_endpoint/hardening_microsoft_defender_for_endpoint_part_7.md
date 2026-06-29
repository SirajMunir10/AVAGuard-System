# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
What RBAC permissions are required to collect files in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** RBAC permissions for file collection

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Microsoft Defender Unified role-based access control (RBAC): Add file collection permission in Microsoft Defender Unified (RBAC)
2. For Microsoft Defender for Endpoint role-based access control (RBAC): Portable Executable files (.exe, .sys, .dll, and others): Security Administrator or Advanced live response or Alerts
3. For Microsoft Defender for Endpoint role-based access control (RBAC): Non-Portable Executable file (.txt, .docx, and others): Security Administrator or Advanced live response
4. Tenants with role-based access (RBAC) permissions enabled

## Validation
1. Confirm that the user or group assigned to collect files has the required RBAC permissions:
   - For Microsoft Defender Unified RBAC: Verify that the user is assigned a role that includes the 'File collection' permission under 'Security operations'.
   - For Microsoft Defender for Endpoint RBAC: Verify that the user is assigned the 'Security Administrator' role or has the 'Advanced live response' permission enabled. For Portable Executable files (.exe, .sys, .dll, etc.), also ensure the 'Alerts' permission is included.
2. Test file collection by initiating a live response session and attempting to collect a sample file (e.g., a .exe or .txt file). Use the command: `collect file <file_path>` in the live response console.
3. Check the action center in Microsoft Defender for Endpoint to confirm the file collection request was successful and the file is available for download.
4. Review audit logs in the Microsoft 365 Defender portal to verify that the file collection action was performed by the authorized user.

## Rollback
1. If the file collection permission was incorrectly assigned, remove the 'File collection' permission from the user or group in Microsoft Defender Unified RBAC settings.
2. For Microsoft Defender for Endpoint RBAC, remove the user from the 'Security Administrator' role or disable the 'Advanced live response' permission.
3. If the user was assigned a custom role with excessive permissions, modify the role to remove the file collection permission and reassign a more restrictive role.
4. Verify that the user can no longer initiate file collection by attempting to collect a file in a live response session; the action should be denied.
5. Monitor audit logs to ensure no unauthorized file collection attempts occur after the rollback.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
