# Optimization: Policy Compliance

**Domain:** Governance
**Subdomain:** Policy Compliance
**Incident Type:** Optimization

## Scenario / Query
An organization has deployed Azure Policy to enforce tagging on new resources, but many existing resources lack required tags. How can the organization remediate non-compliant resources without manual intervention, and what is the recommended approach to apply tags at scale?

## Environment Context
- **Tenant Type:** Enterprise (multiple subscriptions)
- **Configuration:** Azure Policy initiative 'Add a tag to resources' deployed with 'Deny' effect on new resources; existing resources not covered

## Symptoms
- Azure Policy compliance dashboard shows non-compliant resources due to missing tags
- Manual tagging is time-consuming and error-prone for thousands of resources
- No automated remediation task configured for the policy assignment

## Error Codes
N/A

## Root Causes
1. Azure Policy 'Deny' effect only prevents creation of non-compliant resources, it does not remediate existing resources
2. Remediation task not created or not associated with the 'DeployIfNotExists' policy definition

## Remediation Steps
1. 1. Identify the built-in policy definition 'Add a tag to resources' (ID: /providers/Microsoft.Authorization/policyDefinitions/...).
2. 2. Assign the policy with effect 'DeployIfNotExists' instead of 'Deny' to trigger remediation on existing resources.
3. 3. Create a managed identity in the policy assignment with contributor permissions on the target scope.
4. 4. Trigger a remediation task from the Azure portal (Policy > Compliance > select non-compliant resource > 'Create Remediation Task') or via PowerShell: Start-AzPolicyRemediation -Name 'remediation1' -PolicyAssignmentId '<assignmentId>'.
5. 5. Monitor remediation task progress in the Azure portal under 'Remediation tasks'.

## Validation
After remediation task completes, verify in Azure Policy compliance dashboard that the number of non-compliant resources for the tag policy has dropped to zero.

## Rollback
If remediation causes unintended changes, use Azure Policy's 'deny' effect on a new assignment to prevent further tagging, and manually revert tags using Azure Resource Graph or PowerShell: Update-AzTag -ResourceId '<resourceId>' -Tag @{key='value'} -Operation Delete.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources>
