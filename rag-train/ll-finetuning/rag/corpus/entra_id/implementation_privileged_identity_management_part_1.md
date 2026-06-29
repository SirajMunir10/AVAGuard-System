# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How to activate a role using Microsoft Graph API in Privileged Identity Management (PIM)?

## Environment Context
- **Tenant Type:** Entra ID tenant with PIM enabled
- **Configuration:** User must have eligible role assignments via PIM

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Send a GET request to https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleRequests/filterByCurrentUser(on='principal') to get all eligible roles that you can activate.
2. Note: When a user gets their role eligibility via group membership, this Microsoft Graph request doesn't return their eligibility.

## Validation
1. Send a GET request to https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleRequests/filterByCurrentUser(on='principal') and confirm the response includes the eligible role assignments expected for the user.
2. If the user's eligibility is via group membership, verify the group membership is correctly assigned in Entra ID and that the role is activated through the group's PIM configuration.
3. Check the PIM audit log in the Entra admin center for successful activation events.

## Rollback
1. If activation fails or causes issues, deactivate the role immediately by sending a POST request to https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleRequests with the action 'AdminRemove' and the appropriate roleDefinitionId and principalId.
2. Alternatively, use the Entra admin center to manually deactivate the role under Privileged Identity Management > My roles > Active roles.
3. Review the PIM audit log to confirm the role has been deactivated.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role>
