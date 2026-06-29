# Hardening: Incident Management

**Domain:** Sentinel
**Subdomain:** Incident Management
**Incident Type:** Hardening

## Scenario / Query
How to ensure only authorized users can delete incident comments in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel Contributor role

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Only users with the Microsoft Sentinel Contributor role have permission to delete comments.
2. Even the comment's author must have this role in order to delete it.

## Validation
1. Sign in to the Azure portal (https://portal.azure.com) as a user who is NOT assigned the Microsoft Sentinel Contributor role (e.g., a Reader).
2. Navigate to Microsoft Sentinel > select your workspace > Incidents.
3. Open an incident that contains a comment you authored.
4. Attempt to delete that comment. Confirm that the delete option is not available or returns an access denied error.
5. Sign in as a user who IS assigned the Microsoft Sentinel Contributor role.
6. Open the same incident and attempt to delete the same comment. Confirm that the delete action succeeds.
7. Repeat steps 5-6 for a comment authored by another user to verify that the Contributor role can delete any comment.

## Rollback
1. If the validation fails (e.g., a non-Contributor user can delete comments), immediately investigate and reassign the correct Azure RBAC roles:
   - Remove any custom role assignments that inadvertently grant delete permissions on Microsoft Sentinel resources.
   - Ensure only the Microsoft Sentinel Contributor role (or a custom role with the Microsoft.SecurityInsights/incidents/comments/delete action) is assigned to authorized users.
2. If the validation shows that a Contributor user cannot delete comments, verify the user's role assignment is active and not blocked by a deny assignment or Azure Policy. Reapply the Microsoft Sentinel Contributor role if necessary.
3. If the issue persists, review the Microsoft Sentinel workspace's diagnostic settings and audit logs to identify any configuration changes or policy conflicts that may have altered default permissions. Restore any changed settings to their original state as documented in the source reference.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
