# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How to configure Privileged Identity Management (PIM) role assignments with eligibility and activation requirements?

## Environment Context
- **Tenant Type:** Entra ID tenant with PIM licensed
- **Configuration:** PIM role settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define role assignments as eligible requiring activation (e.g., MFA check, business justification, approval).
2. Set role assignments as active (permanent or time-bound) without activation steps.
3. Configure just-in-time (JIT) access to grant temporary permissions only when needed.
4. Apply principle of least privilege by minimizing Global Administrators and using specific administrator roles.

## Validation
1. Sign in to the Microsoft Entra admin center as a user with Privileged Role Administrator or Global Administrator. 2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Roles. 3. Select a role (e.g., User Administrator) and review the 'Eligible assignments' tab to confirm users appear with status 'Eligible'. 4. For an eligible user, perform a test activation: have the user sign in and activate the role, verifying that MFA is prompted, business justification is required, and approval workflow (if configured) is triggered. 5. Check the 'Active assignments' tab to confirm that time-bound active assignments (if any) are listed with correct start and end dates. 6. Review role settings: under the role's 'Settings' page, confirm that 'Require multifactor authentication on activation', 'Require justification on activation', and 'Require approval to activate' are set as intended. 7. Verify that Global Administrator count is minimized by reviewing Global Administrator role assignments and ensuring only essential users are assigned.

## Rollback
1. Sign in to the Microsoft Entra admin center as a user with Privileged Role Administrator or Global Administrator. 2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Roles. 3. Select the role that was modified. 4. Under 'Eligible assignments', remove any user that was incorrectly added by selecting the user and choosing 'Remove'. 5. Under 'Active assignments', remove any time-bound or permanent active assignment that was incorrectly set. 6. To revert role settings: go to the role's 'Settings' page, click 'Edit', and restore previous values (e.g., disable MFA requirement, justification requirement, or approval requirement). 7. If Global Administrator assignments were changed, reassign the original users as needed via 'Active assignments' or 'Eligible assignments'. 8. Confirm changes by reviewing the role's audit history to ensure original state is restored.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
