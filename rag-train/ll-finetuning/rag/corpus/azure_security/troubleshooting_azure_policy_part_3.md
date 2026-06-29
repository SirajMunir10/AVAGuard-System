# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
Evaluation details aren't up to date: A resource is in the Not Started state, or the compliance details aren't current.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Resource is in the Not Started state
- Compliance details aren't current

## Error Codes
N/A

## Root Causes
1. New policy or initiative assignment takes about five minutes to be applied
2. New or updated resources within scope of an existing assignment become available in about 15 minutes
3. Standard compliance scan occurs every 24 hours

## Remediation Steps
1. Wait an appropriate amount of time for an evaluation to finish and compliance results to become available in the Azure portal or the SDK
2. To start a new evaluation scan with Azure PowerShell or the REST API, see On-demand evaluation scan

## Validation
1. Wait 5 minutes after a new policy or initiative assignment, or 15 minutes after creating/updating a resource in scope of an existing assignment. 2. Run the Azure PowerShell command: Start-AzPolicyComplianceScan -ResourceGroupName '<ResourceGroupName>' -AsJob. 3. Verify compliance state in Azure portal: navigate to Policy > Compliance, select the assignment, and confirm the resource shows a non-'Not Started' state and current timestamp. 4. Alternatively, use REST API: POST https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyStates/latest/triggerEvaluation?api-version=2019-10-01.

## Rollback
1. If the on-demand scan fails or causes unexpected results, wait for the next standard 24-hour compliance scan to reset states. 2. Remove any temporary policy assignments created for testing: use Azure PowerShell Remove-AzPolicyAssignment -Name '<AssignmentName>' or Azure portal. 3. If a resource was modified to trigger evaluation, revert the resource to its previous configuration using Azure Resource Manager templates or previous deployment history.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
