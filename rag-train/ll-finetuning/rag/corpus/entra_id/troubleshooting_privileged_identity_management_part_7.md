# Troubleshooting: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Troubleshooting

## Scenario / Query
What happens when a time-bound role assignment expires in Privileged Identity Management?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** PIM role assignments with expiration

## Symptoms
- Role assignment has expired
- User cannot access privileged role

## Error Codes
N/A

## Root Causes
1. Time-bound owner or member assignment has reached its expiration date

## Remediation Steps
1. User can use Privileged Identity Management to request a renewal for the role assignment
2. Renewal request requires approval from a Global Administrator or Privileged Role Administrator

## Validation
1. Sign in to the Microsoft Entra admin center as a user whose role assignment has expired. 2. Navigate to Identity Governance > Privileged Identity Management > My roles. 3. Verify that the expired role assignment is listed under 'Expired assignments' or similar section. 4. Attempt to activate the role; confirm that the activation request is blocked and a renewal option is presented. 5. Submit a renewal request and verify that it appears in the approval queue of a Global Administrator or Privileged Role Administrator.

## Rollback
1. If the renewal request is denied or causes issues, the user must not be granted the role. 2. A Global Administrator or Privileged Role Administrator can review the request in PIM > Approve requests and deny it. 3. If the role was inadvertently extended, the administrator can go to PIM > Roles, select the role, find the assignment, and use 'Remove' or 'Edit' to set a new expiration or deactivate it. 4. To prevent future automatic renewals, ensure that no recurring or auto-renew settings are enabled on the assignment.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure#extend-and-renew-assignments>
