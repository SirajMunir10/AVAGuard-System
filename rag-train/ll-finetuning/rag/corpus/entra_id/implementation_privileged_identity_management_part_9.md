# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How do users activate eligible role assignments in Privileged Identity Management?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with PIM licensed
- **Configuration:** Role activation settings configured by administrators, including maximum activation duration and approval requirements

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Users who are eligible for a role must activate the role assignment before using the role.
2. To activate the role, users select specific activation duration within the maximum (configured by administrators), and the reason for the activation request.
3. If the role requires approval to activate, a notification appears in the upper right corner of the user's browser informing them the request is pending approval.
4. If an approval isn't required, the member can start using the role.

## Validation
1. Sign in to the Microsoft Entra admin center as a user with an eligible role assignment. 2. Navigate to Identity > Governance > Privileged Identity Management > My roles > Eligible assignments. 3. Select the eligible role and click Activate. 4. Verify that the activation duration field allows a value within the administrator-configured maximum. 5. Enter a reason for activation and submit. 6. If the role requires approval, confirm that a notification appears in the upper right corner indicating the request is pending approval. 7. If no approval is required, confirm that the role is activated immediately and the user can access the role's permissions.

## Rollback
1. If the activation request is pending approval, the user can cancel the request by navigating to PIM > My roles > Active requests and selecting Cancel. 2. If the role was activated without approval, the user can deactivate the role assignment manually by going to PIM > My roles > Active assignments, selecting the role, and choosing Deactivate. 3. Alternatively, the activation will automatically expire after the configured maximum duration. 4. If the activation caused unintended access, an administrator can remove the eligible assignment or deactivate the active assignment from the PIM admin view.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure#activate>
