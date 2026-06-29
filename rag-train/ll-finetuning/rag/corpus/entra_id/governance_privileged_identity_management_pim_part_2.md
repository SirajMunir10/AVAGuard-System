# Governance: Privileged Identity Management (PIM)

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management (PIM)
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that a user was unexpectedly assigned the Global Administrator role in Entra ID without any approval or activation request. How can the administrator investigate and remediate this governance violation?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Privileged Identity Management (PIM) is enabled and configured to require approval for role activations. Audit logs are sent to Azure Monitor.

## Symptoms
- User has Global Administrator role assigned directly (not through PIM activation).
- No PIM approval request or activation record exists for the user.
- The role assignment appears in the Entra ID Roles and Administrators blade.

## Error Codes
N/A

## Root Causes
1. A privileged user assigned the role outside of PIM using the Entra ID portal or PowerShell.
2. PIM configuration does not prevent direct role assignments (PIM is not set to require activation for the role).

## Remediation Steps
1. 1. Remove the direct role assignment: In the Entra ID portal, go to Roles and Administrators, select the Global Administrator role, remove the user.
2. 2. Review PIM settings for the Global Administrator role: In PIM, ensure 'Require approval to activate' is enabled and 'Assignment type' is set to 'Eligible' (not Active).
3. 3. Investigate who made the assignment: Use the Entra ID audit logs (under Monitoring > Audit logs) to find the 'Add member to role' activity and identify the actor.
4. 4. If the assignment was made via automation (e.g., PowerShell), review and restrict use of the `Add-MgRoleManagementDirectoryRoleAssignment` cmdlet to authorized personnel only.

## Validation
Confirm the user no longer has the Global Administrator role by checking the Roles and Administrators blade and verifying the role is not listed for the user. Run a PIM audit to confirm no other direct assignments exist.

## Rollback
If the removal was accidental, re-add the user as an eligible member in PIM and require activation with approval.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-security-workflow>
