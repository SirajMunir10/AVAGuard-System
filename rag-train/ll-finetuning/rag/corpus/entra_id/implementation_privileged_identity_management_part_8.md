# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How do I configure PIM role assignments to grant secure access to resources in my organization?

## Environment Context
- **Tenant Type:** Entra ID tenant with PIM licensed
- **Configuration:** PIM role assignments

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign roles to members
2. Activate assignments
3. Approve or deny requests
4. Extend and renew assignments

## Validation
1. Sign in to the Microsoft Entra admin center as a user with the Privileged Role Administrator role.
2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Assignments.
3. Verify that each intended member appears under 'Eligible assignments' or 'Active assignments' with the correct role, scope, and expiration settings.
4. For each assignment, confirm that the activation settings (e.g., approval required, justification, MFA) are configured as expected by reviewing the role settings.
5. As a test user with an eligible assignment, attempt to activate the role and confirm that the activation process follows the configured policies (e.g., MFA challenge, approval workflow).
6. Check the PIM audit history to ensure no unexpected assignment changes occurred during the configuration.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Privileged Role Administrator.
2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Assignments.
3. For each role assignment that was added or modified, select the assignment and choose 'Remove' to delete the assignment, or edit the assignment settings to revert to the previous configuration.
4. If role settings were changed (e.g., activation duration, approvers), navigate to the role's settings page and restore the original values.
5. Verify that any test users who activated roles have their activations expired or deactivated manually via the 'Active assignments' tab.
6. Review the PIM audit log to confirm that all rollback actions were completed successfully and that no residual assignments remain.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
