# Governance: Privileged Identity Management (PIM)

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management (PIM)
**Incident Type:** Governance

## Scenario / Query
A user with a permanent eligible assignment to the Global Administrator role in Entra ID PIM has not activated the role for 90 days. How should the administrator enforce periodic activation and review to reduce standing privileged access?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** PIM role settings for Global Administrator â€“ activation duration set to 8 hours, no approval required, no justification required, no MFA on activation, no notification, no access reviews configured.

## Symptoms
- Eligible Global Administrator assignment is permanent (not time-bound).
- No access review schedule exists for the Global Administrator role.
- Role activation does not require approval or justification.
- No alerts or notifications are sent when the role is activated.

## Error Codes
N/A

## Root Causes
1. PIM role settings do not enforce time-bound eligible assignments.
2. Access reviews are not configured to periodically review and remove stale assignments.
3. Activation requirements (MFA, justification, approval) are not enforced.

## Remediation Steps
1. 1. In the Entra admin center, go to Identity Governance > Privileged Identity Management > Azure AD roles > Settings > Global Administrator.
2. 2. Set 'Eligible assignment duration' to a maximum of 365 days (or shorter) and require justification for assignment.
3. 3. Enable 'Require Azure AD Multi-Factor Authentication on activation'.
4. 4. Enable 'Require justification on activation' and optionally 'Require approval to activate'.
5. 5. Under 'Notifications', enable email notifications to security administrators on role activation.
6. 6. Create an access review for the Global Administrator role: Identity Governance > Access Reviews > New access review, select 'Azure AD roles', scope to Global Administrator, set frequency to quarterly, and require reviewer to provide justification.
7. 7. Ensure the access review is set to auto-apply results and remove denied users after review.

## Validation
Verify that the Global Administrator role settings now require MFA and justification for activation, and that an access review is scheduled and active. Confirm that no user has a permanent eligible assignment exceeding the configured duration.

## Rollback
Revert PIM role settings to previous values and delete the access review if needed. Note that removing access reviews may leave stale assignments.

## References
- Microsoft Learn: 'Create an access review of Azure AD roles in Privileged Identity Management' â€“ https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-create-azure-ad-roles-and-feature-roles-review
- CIS Microsoft Azure Foundations Benchmark v2.0.0 â€“ Control 1.4: 'Ensure that 'Require Multi-Factor Authentication to activate' is set to 'Yes' for all privileged roles'
