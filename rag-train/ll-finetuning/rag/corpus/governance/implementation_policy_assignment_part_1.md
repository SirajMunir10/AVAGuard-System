# Implementation: Policy Assignment

**Domain:** Governance
**Subdomain:** Policy Assignment
**Incident Type:** Implementation

## Scenario / Query
An administrator assigned an Azure Policy initiative to a management group, but the policy does not take effect on existing resources in child subscriptions. What configuration step was missed?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure Policy assigned at management group scope with 'enforce' effect; existing resources not evaluated

## Symptoms
- Newly assigned policy initiative shows compliance state 'Not Started' for existing resources
- Policy evaluation results do not appear in Azure Policy Compliance view for child subscriptions
- No remediation tasks are created automatically

## Error Codes
N/A

## Root Causes
1. Policy assignment was created without triggering an on-demand evaluation scan for existing resources
2. The default policy assignment does not automatically evaluate existing resources; a separate compliance scan must be initiated

## Remediation Steps
1. Trigger an on-demand compliance evaluation scan using Azure PowerShell: Start-AzPolicyComplianceScan -ResourceGroupName '<ResourceGroupName>' -AsJob
2. Alternatively, use the Azure CLI: az policy state trigger-scan --resource-group '<ResourceGroupName>'
3. After the scan completes, verify compliance results in the Azure portal under Policy > Compliance

## Validation
Run 'Get-AzPolicyState -PolicyAssignmentName <AssignmentName>' and confirm that compliance data appears for existing resources.

## Rollback
Remove the policy assignment using 'Remove-AzPolicyAssignment -Name <AssignmentName>' if the scan does not resolve the issue.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data>
