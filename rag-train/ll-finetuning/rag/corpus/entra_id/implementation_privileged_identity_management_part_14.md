# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How to configure Privileged Identity Management for Microsoft Entra roles using Microsoft Graph APIs?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with PIM license
- **Configuration:** PIM for Microsoft Entra roles APIs

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use PIM for Microsoft Entra roles APIs
2. Use PIM for groups APIs

## Validation
1. Run the following Microsoft Graph API call to list all active role assignments for a specific role (e.g., Global Administrator) and confirm that the eligible assignments are present:
   GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleInstances?$filter=roleDefinitionId eq '<role-definition-id>'&$expand=principal
2. Verify that the PIM configuration for Microsoft Entra roles is enabled by calling:
   GET https://graph.microsoft.com/v1.0/policies/roleManagementPolicyAssignments?$filter=scopeId eq '/' and scopeType eq 'DirectoryRole' and roleDefinitionId eq '<role-definition-id>'
3. Confirm that the PIM activation settings (e.g., maximum duration, approval required) are correctly applied by reviewing the policy rules:
   GET https://graph.microsoft.com/v1.0/policies/roleManagementPolicies('<policy-id>')/rules
4. Validate that eligible users can activate the role by simulating an activation request (if possible) or by checking the activation audit logs in the Entra admin center under 'Privileged Identity Management' > 'Microsoft Entra roles' > 'Activation history'.

## Rollback
1. If the PIM configuration for Microsoft Entra roles is incorrect, remove the custom role management policy by calling:
   DELETE https://graph.microsoft.com/v1.0/policies/roleManagementPolicies('<policy-id>')
2. To revert to default PIM settings, delete any custom role assignment schedules:
   DELETE https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleInstances('<schedule-instance-id>')
3. If PIM for groups was misconfigured, remove the group's PIM policy:
   DELETE https://graph.microsoft.com/v1.0/groups('<group-id>')/appRoleAssignments
   (Note: This step is for PIM for groups; refer to the same source documentation for group-specific rollback.)
4. Restore previous role assignments by re-adding permanent assignments using:
   POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments
   with the original principal and role definition IDs.
5. Finally, verify that the rollback is complete by re-running the validation steps and ensuring that the PIM configuration matches the pre-change state.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
