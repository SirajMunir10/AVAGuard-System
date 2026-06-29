# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How do eligible role users request activation of a role that requires approval in PIM?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with PIM enabled
- **Configuration:** Role activation requires approval

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Request activation of a role that requires approval
2. View the status of your request to activate
3. Complete your task in Microsoft Entra ID if activation was approved

## Validation
1. Sign in to the Microsoft Entra admin center as a user with an eligible role assignment. 2. Browse to Identity Governance > Privileged Identity Management > My roles. 3. Select the eligible role that requires approval and click Activate. 4. Complete the activation form, provide a reason, and submit the request. 5. Confirm that the request status shows 'Pending approval' or similar. 6. Have an approver approve the request. 7. Verify that the user can now access the role (e.g., by checking the 'Active assignments' tab under My roles or by attempting to perform a task that requires the role).

## Rollback
1. If the activation request is still pending, the user can cancel it from the 'My roles' page by selecting the request and clicking Cancel. 2. If the activation was approved and the role is active, the user can deactivate the role manually by going to My roles, selecting the active assignment, and clicking Deactivate. 3. Alternatively, an administrator can remove the active assignment via Privileged Identity Management > Approve requests or by directly modifying the user's role assignment in Microsoft Entra ID.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
