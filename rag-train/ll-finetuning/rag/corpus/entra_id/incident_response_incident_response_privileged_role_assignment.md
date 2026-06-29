# Incident Response: Incident Response - Privileged Role Assignment

**Domain:** Entra ID
**Subdomain:** Incident Response - Privileged Role Assignment
**Incident Type:** Incident Response

## Scenario / Query
An administrator suspects that a user was assigned a highly privileged Entra ID role (e.g., Global Administrator) outside of the approved Privileged Identity Management (PIM) activation process. How can the security team investigate the assignment and ensure that only eligible, time-bound role activations are used?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** PIM is enabled for Global Administrator role; audit logs are sent to Azure Monitor; Conditional Access policies require MFA for privileged role activation.

## Symptoms
- A user appears with a permanent Global Administrator role assignment in the Entra ID portal.
- No corresponding PIM activation request is found in the PIM audit history.
- The userâ€™s role assignment timestamp does not match any known PIM activation window.

## Error Codes
N/A

## Root Causes
1. A privileged user with the Privileged Role Administrator role assigned the Global Administrator role directly via the Entra ID portal, bypassing PIM.
2. Lack of alerting or monitoring for direct role assignments outside of PIM.

## Remediation Steps
1. 1. Sign in to the Entra admin center as a Privileged Role Administrator.
2. 2. Navigate to Identity > Roles & admins > Roles & admins, select Global Administrator, and remove the direct assignment.
3. 3. Ensure the user is added as an eligible member in PIM for the Global Administrator role with appropriate approval and MFA requirements.
4. 4. Review the Entra ID audit logs (under Identity > Monitoring & health > Audit logs) for the operation 'Add member to role' to identify who performed the direct assignment.
5. 5. If needed, revoke the Privileged Role Administrator role from the user who made the unauthorized assignment.
6. 6. Configure an alert in Microsoft Sentinel or Azure Monitor to detect any direct role assignment that does not originate from PIM.

## Validation
Confirm that the user no longer has a permanent Global Administrator assignment and can only activate the role through PIM with MFA and approval. Verify that an audit log entry shows the removal of the direct assignment.

## Rollback
If the direct assignment was legitimate (e.g., emergency break-glass account), re-add the user as a permanent Global Administrator and document the exception. Ensure the assignment is flagged in the incident report.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-perform-security-review>
