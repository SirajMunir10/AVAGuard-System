# Implementation: Policy Assignment

**Domain:** Governance
**Subdomain:** Policy Assignment
**Incident Type:** Implementation

## Scenario / Query
After assigning an Azure Policy initiative to a management group, the policy assignment is not visible in the Azure portal for any subscriptions within that management group. What is the likely cause and how do you resolve it?

## Environment Context
- **Tenant Type:** Enterprise (multiple management groups)
- **Configuration:** Azure Policy initiative assigned at management group scope; subscription-level readers cannot see the assignment.

## Symptoms
- Policy assignment does not appear in the Azure portal under Policy > Assignments for subscriptions in the management group
- No error message is displayed in the portal
- Policy evaluation results show 'Not started' or 'No data' for the assigned initiative

## Error Codes
N/A

## Root Causes
1. The policy assignment was created with the 'Not Scopes' property that excludes the subscriptions, or the assignment scope was incorrectly set to a child management group instead of the parent.
2. The user viewing the assignment does not have the 'Microsoft.Authorization/policyAssignments/read' permission at the assignment scope.

## Remediation Steps
1. 1. Verify the assignment scope: Use Azure PowerShell `Get-AzPolicyAssignment -Scope '/providers/Microsoft.Management/managementGroups/<MGName>'` to confirm the assignment exists at the intended management group.
2. 2. Check the `NotScopes` property: Run `(Get-AzPolicyAssignment -Name <AssignmentName>).Properties.notScopes` to see if subscriptions are excluded.
3. 3. Ensure the user has at least Reader role at the management group scope: `Get-AzRoleAssignment -Scope '/providers/Microsoft.Management/managementGroups/<MGName>' -SignInName <user@domain.com>`.
4. 4. If the assignment is missing, re-create it using the Azure portal or `New-AzPolicyAssignment` with the correct scope.

## Validation
After remediation, run `Get-AzPolicyAssignment -Scope '/providers/Microsoft.Management/managementGroups/<MGName>' | Format-List` to confirm the assignment is present and visible to users with appropriate permissions.

## Rollback
Remove the policy assignment using `Remove-AzPolicyAssignment -Name <AssignmentName> -Scope '/providers/Microsoft.Management/managementGroups/<MGName>'`.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure>
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data>
