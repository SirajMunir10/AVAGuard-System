# Governance: Management Groups and RBAC

**Domain:** Governance
**Subdomain:** Management Groups and RBAC
**Incident Type:** Governance

## Scenario / Query
How do I detect and remediate a scenario where a subscription is not covered by any Azure Policy assignment at the management group hierarchy, leading to a governance gap?

## Environment Context
- **Tenant Type:** Enterprise (multiple management groups)
- **Configuration:** Management group hierarchy with root management group containing multiple child management groups and subscriptions

## Symptoms
- Azure Policy compliance dashboard shows 'Not started' or 'Not covered' for a subscription
- Azure Resource Graph query returns no policy assignments for a specific subscription
- Security Center or Defender for Cloud shows 'Policy coverage gap' alert for the subscription

## Error Codes
N/A

## Root Causes
1. Subscription is not placed under any management group that has an Azure Policy assignment
2. Policy assignment was removed or excluded from the management group hierarchy that includes the subscription

## Remediation Steps
1. Identify the subscription's management group path using Azure Resource Graph or Azure CLI: `az account management-group list --query "[?name=='<subscription-id>'].{Name:name, DisplayName:displayName, Parent:parent.id}"`
2. Assign the required Azure Policy initiative (e.g., Azure Security Benchmark) at the appropriate management group scope using Azure Portal or CLI: `az policy assignment create --name 'SecurityBenchmark' --policy-set-definition '/providers/Microsoft.Authorization/policySetDefinitions/1f3afdf9-d0c9-4c3d-847f-89da613e70a8' --scope '/providers/Microsoft.Management/managementGroups/<management-group-id>'`
3. Verify assignment propagation using Azure Resource Graph: `policyResources | where type =~ 'Microsoft.Authorization/policyAssignments' | where properties.scope contains '<subscription-id>'`

## Validation
Run Azure Resource Graph query to confirm the subscription now shows policy assignments and compliance data in Azure Policy dashboard.

## Rollback
Remove the policy assignment from the management group using Azure CLI: `az policy assignment delete --name 'SecurityBenchmark' --scope '/providers/Microsoft.Management/managementGroups/<management-group-id>'`

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/overview>
- <https://learn.microsoft.com/en-us/azure/governance/policy/overview>
