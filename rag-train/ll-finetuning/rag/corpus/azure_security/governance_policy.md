# Governance: Policy

**Domain:** Azure
**Subdomain:** Policy
**Incident Type:** Governance

## Scenario / Query
A user reports that a newly created Azure subscription is not covered by any Azure Policy assignments, even though the management group hierarchy has a policy initiative assigned at the root. What configuration step is missing to enforce governance on new subscriptions?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure Policy assignment at root management group scope with 'enforcementMode' set to 'Default' (not 'DoNotEnforce')

## Symptoms
- New subscriptions do not show any policy compliance data in Azure Policy dashboard
- Azure Policy compliance report shows 'Not started' or 'No data' for the new subscription
- Audit logs show no policy evaluation events for the new subscription

## Error Codes
N/A

## Root Causes
1. The policy assignment at the root management group does not have 'enforcementMode' set to 'Default' (it may be set to 'DoNotEnforce')
2. The new subscription was not placed under the correct management group that inherits the policy assignment
3. The policy assignment scope does not include the management group containing the new subscription

## Remediation Steps
1. Verify that the policy assignment at the root management group has 'enforcementMode' set to 'Default' (not 'DoNotEnforce') using Azure Policy > Assignments > select assignment > Edit > Enforcement
2. Ensure the new subscription is moved under the correct management group that inherits the policy assignment using Azure portal > Management groups > select subscription > Move
3. If the subscription was recently created, wait up to 30 minutes for policy evaluation to trigger, or manually trigger evaluation using: Start-AzPolicyComplianceScan -ResourceGroupName '<rg>' (PowerShell) as documented in 'Trigger on-demand evaluation'

## Validation
After remediation, run 'Get-AzPolicyState -SubscriptionId '<subscriptionId>' -Top 1' (PowerShell) to confirm policy states are returned, or check Azure Policy > Compliance for the subscription.

## Rollback
To revert, set 'enforcementMode' back to 'DoNotEnforce' on the policy assignment, or move the subscription to a management group without the policy assignment.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure#enforcement-mode>
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data#on-demand-evaluation>
