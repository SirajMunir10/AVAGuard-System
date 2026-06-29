# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
Compliance isn't as expected: A resource isn't in either the Compliant or Not-Compliant evaluation state expected for the resource.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Resource is not in the expected Compliant or Not-Compliant evaluation state
- Compliance for a policy assignment shows 0/0 resources

## Error Codes
N/A

## Root Causes
1. Resource is not in the correct scope for the policy assignment
2. Policy definition doesn't operate as intended
3. Assignment parameters or assignment scope are set incorrectly
4. Policy definition mode is incorrect (should be 'all' for all resource types, 'indexed' if checking tags or location)
5. Scope of the resource is excluded or exempt
6. No resources determined to be applicable within the assignment scope
7. Target value in policy definition is wrong
8. Current value in resource payload is wrong
9. RegEx string parameter is incorrect for Resource Provider mode definitions (e.g., Microsoft.Kubernetes.Data)

## Remediation Steps
1. Wait the appropriate amount of time for an evaluation to finish and compliance results to become available in the Azure portal or SDK
2. Start a new evaluation scan with Azure PowerShell or the REST API (see On-demand evaluation scan)
3. Ensure that the assignment parameters and assignment scope are set correctly
4. Check the policy definition mode: mode should be 'all' for all resource types; mode should be 'indexed' if the policy definition checks for tags or location
5. Ensure that the scope of the resource isn't excluded or exempt
6. Check both the policy definition and the assignment scope if compliance shows 0/0 resources
7. For a noncompliant resource expected to be compliant, determine the reasons for noncompliance
8. Compare the definition to the evaluated property value to identify why a resource was noncompliant
9. If the target value is wrong, revise the policy definition
10. If the current value is wrong, validate the resource payload through resources.azure.com
11. For a Resource Provider mode definition that supports a RegEx string parameter (e.g., Microsoft.Kubernetes.Data and built-in definition 'Container images should be deployed from trusted registries only'), validate that the RegEx string parameter is correct
12. If still having issues with duplicated and customized built-in policy definition or custom definition, create a support ticket under 'Authoring a policy' to route the issue correctly

## Validation
1. Verify the resource is within the assignment scope: Use Azure CLI: `az policy assignment list --query "[?displayName=='<assignmentName>'].{Scope:scope}" -o tsv`. 2. Check the policy definition mode: `az policy definition show --name <definitionName> --query mode`. 3. Confirm no exclusions or exemptions: `az policy exemption list --scope <resourceId> --query "[?policyAssignmentId=='<assignmentId>']"`. 4. For 0/0 resources, run an on-demand evaluation: `az policy state trigger-scan --resource-group <rgName>` and then check compliance: `az policy state list --resource <resourceId>`. 5. Compare expected vs actual property values: Use `az resource show --ids <resourceId> --query <propertyPath>` against the policy definition's condition.

## Rollback
1. If assignment scope was changed, revert to original scope: `az policy assignment update --name <assignmentName> --scope <originalScope>`. 2. If policy definition mode was changed, revert to original mode: `az policy definition update --name <definitionName> --mode <originalMode>`. 3. If an exemption was incorrectly removed, recreate it: `az policy exemption create --name <exemptionName> --policy-assignment <assignmentId> --scope <resourceId>`. 4. If parameters were modified, restore original parameters: `az policy assignment update --name <assignmentName> --params <originalParamsJson>`. 5. If the policy definition was revised, revert to previous version using source control or redeploy the original definition.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
