# Incident Response: Incident Response â€“ Privileged Role Activation

**Domain:** Entra ID
**Subdomain:** Incident Response â€“ Privileged Role Activation
**Incident Type:** Incident Response

## Scenario / Query
A security administrator notices that a user who should not have Global Administrator privileges has been assigned the role and has activated it multiple times in the last hour. How can the administrator investigate and revoke the unauthorized role assignment using Microsoft Entra ID audit logs and Privileged Identity Management (PIM)?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Microsoft Entra ID PIM enabled; audit logging enabled; Conditional Access policies configured for privileged roles

## Symptoms
- Unexpected Global Administrator role activation alerts in Microsoft Entra ID
- User with no prior privileged role history appears in PIM activation history
- Audit logs show role activation from an unfamiliar IP address or device

## Error Codes
N/A

## Root Causes
1. A user was assigned the Global Administrator role in PIM without proper approval or justification
2. An attacker compromised a user account and activated the role
3. Misconfigured PIM role settings allowed self-activation without approval

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as a Privileged Role Administrator.
2. Navigate to Identity > Governance > Privileged Identity Management > Azure AD roles.
3. Select the role (e.g., Global Administrator) and review the 'Active assignments' and 'Activation history' to identify the unauthorized user.
4. Remove the unauthorized role assignment by selecting the user and choosing 'Remove active assignment'.
5. Revoke any active role activations by selecting the user and choosing 'Deactivate'.
6. Investigate the user account for compromise: reset the user's password, revoke sessions, and require re-authentication.
7. Review and tighten PIM role settings: require approval for activation, set maximum activation duration, and enable justification.
8. Enable Azure AD Identity Protection to detect and respond to compromised identities.

## Validation
Confirm that the unauthorized user no longer appears in the active assignments list for the Global Administrator role and that no recent activation events are present in the audit log.

## Rollback
If the removal was in error, re-assign the role via PIM following the standard approval process. Ensure that the userâ€™s account is not compromised before re-assigning.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-investigate-activation>
