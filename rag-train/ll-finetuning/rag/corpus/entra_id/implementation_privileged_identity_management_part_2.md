# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How to assign an eligible role assignment using Microsoft Graph API in PIM?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** PIM role eligibility schedule request

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a unifiedRoleEligibilityScheduleRequest with action 'adminAssign'
2. Set principalId to the user's object ID
3. Set roleDefinitionId to the role's template ID
4. Set directoryScopeId to '/' for tenant-wide scope
5. Provide justification in the 'justification' field
6. Set scheduleInfo with startDateTime and expiration type and endDateTime

## Validation
1. Run the following Microsoft Graph API query to confirm the eligible role assignment was created: GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleRequests?$filter=principalId eq '{user-object-id}' and roleDefinitionId eq '{role-template-id}' and action eq 'adminAssign'. 2. Verify the response contains a request with status 'Granted' and the scheduleInfo matches the intended startDateTime and expiration. 3. Check that the principalId, roleDefinitionId, and directoryScopeId are correct. 4. Optionally, run: GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleInstances?$filter=principalId eq '{user-object-id}' and roleDefinitionId eq '{role-template-id}' to confirm the assignment is active in the schedule.

## Rollback
1. Retrieve the ID of the eligibility schedule request to remove: GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleRequests?$filter=principalId eq '{user-object-id}' and roleDefinitionId eq '{role-template-id}' and action eq 'adminAssign'. 2. Use the request ID to cancel the request if it is still in a cancellable state (e.g., status 'Granted' cannot be cancelled; instead, create a new request to remove the assignment). 3. To remove the eligible assignment, create a new unifiedRoleEligibilityScheduleRequest with action 'adminRemove', principalId, roleDefinitionId, directoryScopeId, and justification. 4. Verify removal by repeating the validation GET request and ensuring no active schedule instances remain.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role>
