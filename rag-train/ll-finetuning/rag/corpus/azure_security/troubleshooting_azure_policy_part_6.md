# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot a resource creation or update that is denied by Azure Policy?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Creation or update of a resource is denied
- Error message includes policy definition and policy assignment IDs

## Error Codes
N/A

## Root Causes
1. A policy assignment to the scope of the new or updated resource meets the criteria of a policy definition with a Deny effect

## Remediation Steps
1. Use the error information in the message to get more details to understand the resource restrictions
2. Adjust the resource properties in your request to match allowed values
3. If the error information in the message is missed, check the Activity log for the policy definition and policy assignment IDs

## Validation
1. Review the error message from the denied resource creation or update. Note the policy definition ID and policy assignment ID. 2. Run the following Azure CLI command to get details about the policy assignment: az policy assignment show --id '<policyAssignmentId>'. 3. Run the following Azure CLI command to get details about the policy definition: az policy definition show --id '<policyDefinitionId>'. 4. Verify that the resource properties in your request now comply with the policy definition's allowed values. 5. Attempt the resource creation or update again and confirm it succeeds without a denial error.

## Rollback
1. If the remediation fails or causes issues, revert the resource properties to their original values before the attempted change. 2. If the resource was created and needs to be removed, delete the resource using: az resource delete --ids '<resourceId>'. 3. If the policy assignment itself is problematic, contact your Azure Policy administrator to review and potentially modify or disable the policy assignment using: az policy assignment update --id '<policyAssignmentId>' --parameters '<newParameters>' or az policy assignment delete --id '<policyAssignmentId>'.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
