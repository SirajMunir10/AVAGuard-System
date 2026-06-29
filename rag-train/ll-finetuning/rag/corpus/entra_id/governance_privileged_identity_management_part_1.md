# Governance: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Governance

## Scenario / Query
A security auditor reports that a user was assigned the Global Administrator role in Entra ID without any approval or justification, and the assignment was not time-bound. How can this be investigated and prevented using Microsoft Entra Privileged Identity Management (PIM)?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** PIM not enabled for Global Administrator role; direct permanent assignments allowed

## Symptoms
- User has a permanent Global Administrator role assignment
- No approval workflow was triggered for the role assignment
- Role assignment audit log shows 'Add member to role' activity without justification

## Error Codes
N/A

## Root Causes
1. Privileged Identity Management (PIM) was not configured to require approval for Global Administrator role activation
2. Role assignment was made directly via Azure AD portal or PowerShell bypassing PIM governance controls

## Remediation Steps
1. Enable PIM for the Global Administrator role in the Microsoft Entra admin center
2. Configure role settings to require approval for activation and set maximum activation duration (e.g., 8 hours)
3. Remove the permanent assignment and convert it to an eligible assignment in PIM
4. Enable justification requirement for role activation in PIM settings

## Validation
Verify in Microsoft Entra admin center > Identity Governance > Privileged Identity Management > Azure AD roles > Settings that Global Administrator requires approval and has a maximum activation duration set. Confirm the user's assignment is now 'Eligible' not 'Active'.

## Rollback
If PIM configuration causes disruption, temporarily disable the approval requirement for Global Administrator role in PIM settings, but this reduces security posture.

## References
- Microsoft Learn: 'Assign Azure AD roles in Privileged Identity Management' - https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user
- CIS Microsoft Azure Foundations Benchmark v2.0.0 - Control 1.3: 'Ensure that there are no permanent Global Administrator role assignments'
