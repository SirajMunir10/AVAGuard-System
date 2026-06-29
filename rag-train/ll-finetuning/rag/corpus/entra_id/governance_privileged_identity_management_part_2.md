# Governance: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Governance

## Scenario / Query
A security auditor reports that several users have permanent, active Entra ID Global Administrator role assignments instead of using just-in-time activation via Privileged Identity Management (PIM). How can an administrator identify and remediate these standing privileged role assignments?

## Environment Context
- **Tenant Type:** production
- **Configuration:** Entra ID PIM is enabled but not enforced for all privileged roles

## Symptoms
- Users appear in the Global Administrator role with an 'Active' assignment type in the Entra admin center
- No activation request records exist in the PIM audit history for those assignments
- The PIM role settings allow permanent active assignments instead of requiring activation

## Error Codes
N/A

## Root Causes
1. Administrators assigned roles directly via the Azure AD Roles and Administrators blade instead of through PIM
2. PIM role settings for Global Administrator allow 'Active' (permanent) assignments rather than requiring 'Eligible' assignments with activation

## Remediation Steps
1. Sign in to the Entra admin center as a Privileged Role Administrator.
2. Navigate to Identity > Roles & admins > Roles & administrators.
3. Select the Global Administrator role and review the list of permanently active members.
4. For each user with an 'Active' assignment, remove the direct assignment.
5. Go to Identity > Identity Governance > Privileged Identity Management > Azure AD roles.
6. Select the Global Administrator role and choose 'Add assignments'.
7. Set the assignment type to 'Eligible' and configure the activation duration and approval requirements as needed.
8. Optionally, update the role settings to disallow permanent active assignments by setting 'Allow permanent eligible assignment' and 'Allow permanent active assignment' to false.

## Validation
Confirm that no users have an 'Active' assignment for Global Administrator in the Entra admin center and that all privileged users appear only as 'Eligible' in PIM.

## Rollback
If issues arise, re-add the user as a permanent active Global Administrator via the Roles & administrators blade and then adjust PIM settings to allow permanent assignments.

## References
- Microsoft Learn: 'Assign Azure AD roles in Privileged Identity Management'
- CIS Microsoft Azure Foundations Benchmark v2.0.0, Control 1.3 â€“ 'Ensure that there are no permanent active Global Administrator role assignments'
