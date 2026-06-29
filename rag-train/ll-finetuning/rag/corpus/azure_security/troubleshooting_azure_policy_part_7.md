# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle ARM template functions in Azure Policy definitions that are processed by Resource Manager instead of the policy engine?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Functions like parameter() or resourceGroup() are processed at deployment time instead of being dynamic in the policy definition

## Error Codes
N/A

## Root Causes
1. Resource Manager processes ARM template functions as part of a deployment, not as part of a policy definition

## Remediation Steps
1. Escape the entire string with [ such that the property looks like [[resourceGroup().tags.myTag]
2. The escape character causes Resource Manager to treat the value as a string when it processes the template
3. Azure Policy then places the function into the policy definition, allowing it to be dynamic as expected

## Validation
1. Deploy the corrected policy definition using Azure CLI: `az policy definition create --name <policyName> --rules <path-to-corrected-rules.json>`
2. Verify the policy definition contains the escaped function by running: `az policy definition show --name <policyName> --query "policyRule.then.details"`
3. Confirm the output shows `[[resourceGroup().tags.myTag]` (double bracket) instead of `[resourceGroup().tags.myTag]`.
4. Assign the policy to a test scope and trigger a compliance scan: `az policy state trigger-scan --resource-group <testRG>`
5. Check that the policy evaluates the dynamic function correctly by reviewing compliance results: `az policy state list --resource-group <testRG> --filter "(policyDefinitionName eq '<policyName>')"`

## Rollback
1. Delete the corrected policy definition: `az policy definition delete --name <policyName>`
2. Re-deploy the original policy definition (without the escape character) using: `az policy definition create --name <policyName> --rules <path-to-original-rules.json>`
3. Re-assign the policy to the same scope: `az policy assignment create --name <assignmentName> --policy <policyName> --resource-group <testRG>`
4. Trigger a new compliance scan: `az policy state trigger-scan --resource-group <testRG>`
5. Confirm the original behavior (function processed at deployment time) is restored by reviewing the policy definition: `az policy definition show --name <policyName> --query "policyRule.then.details"`

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
