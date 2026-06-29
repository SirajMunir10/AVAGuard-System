# Troubleshooting: Policy Compliance

**Domain:** Governance
**Subdomain:** Policy Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
Why is a newly created Azure Policy initiative showing a non-compliant status for a resource group that should be compliant, and how do I resolve this?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure Policy initiative assigned at management group scope with enforcement mode enabled; resource group contains resources that match the policy rule but are reported as non-compliant.

## Symptoms
- Azure Policy compliance dashboard shows Non-compliant for a resource group that meets all policy conditions
- Policy evaluation timestamp is older than expected
- No recent policy evaluation results appear in the activity log for that resource group

## Error Codes
N/A

## Root Causes
1. Policy evaluation is not triggered automatically for existing resources after a policy assignment is created or updated; a manual compliance scan is required
2. The policy assignment may have been created before the resource group existed, and the evaluation cycle has not yet run

## Remediation Steps
1. Trigger an on-demand compliance scan using Azure PowerShell: Start-AzPolicyComplianceScan -ResourceGroupName '<ResourceGroupName>'
2. Alternatively, use Azure CLI: az policy state trigger-scan --resource-group '<ResourceGroupName>'
3. Wait for the scan to complete (typically within 10 minutes) and refresh the compliance dashboard in the Azure portal

## Validation
After the on-demand scan completes, the resource group should appear as Compliant in the Azure Policy compliance view.

## Rollback
No rollback required; the on-demand scan only triggers evaluation and does not change any policy assignments or resources.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data#on-demand-evaluation-scan>
