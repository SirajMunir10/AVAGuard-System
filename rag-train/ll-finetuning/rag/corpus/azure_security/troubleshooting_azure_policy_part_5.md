# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
A resource that you expect Azure Policy to act on isn't being acted on, and there's no entry in the Azure Activity log.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Resource not acted on by Azure Policy
- No entry in the Azure Activity log

## Error Codes
N/A

## Root Causes
1. Policy assignment configured with enforcementMode set to Disabled

## Remediation Steps
1. Wait the appropriate amount of time for an evaluation to finish and compliance results to become available in the Azure portal or the SDK.
2. To start a new evaluation scan with Azure PowerShell or the REST API, see On-demand evaluation scan.
3. Ensure that the assignment parameters and assignment scope are set correctly and that enforcementMode is Enabled.
4. Check the policy definition mode: The mode should be all for all resource types. The mode should be indexed if the policy definition checks for tags or location.
5. Ensure that the scope of the resource isn't excluded or exempt.
6. Verify that the resource payload matches the policy logic. This verification can be done by capturing an HTTP Archive (HAR) trace or reviewing the Azure Resource Manager template (ARM template) properties.
7. For other common issues and solutions, see Troubleshoot: Compliance not as expected.
8. If you still have an issue with your duplicated and customized built-in policy definition or custom definition, create a support ticket under Authoring a policy to route the issue correctly.

## Validation
1. Verify that the policy assignment's enforcementMode is set to Enabled: run `Get-AzPolicyAssignment -Name '<assignmentName>' | Select-Object -Property EnforcementMode` in Azure PowerShell. 2. Confirm the assignment scope includes the resource: run `Get-AzPolicyAssignment -Name '<assignmentName>' | Select-Object -Property Scope`. 3. Check the policy definition mode: run `Get-AzPolicyDefinition -Name '<definitionName>' | Select-Object -Property Mode`. 4. Ensure the resource is not excluded or exempt: review the assignment's exclusion scopes and any exemptions at the resource or resource group scope via the Azure portal or `Get-AzPolicyExemption`. 5. Trigger an on-demand evaluation scan: run `Start-AzPolicyComplianceScan -ResourceGroupName '<resourceGroupName>'` in Azure PowerShell. 6. After the scan completes, check the compliance state of the specific resource: run `Get-AzPolicyState -ResourceId '<resourceId>' -PolicyAssignmentName '<assignmentName>'`. 7. If still no Activity log entry, capture an HAR trace while performing an action on the resource and inspect the payload for policy evaluation details.

## Rollback
1. If enforcementMode was incorrectly set to Disabled, re-enable it: run `Set-AzPolicyAssignment -Name '<assignmentName>' -EnforcementMode Default` in Azure PowerShell. 2. If the assignment scope was incorrectly narrowed, update it to the original scope: run `Set-AzPolicyAssignment -Name '<assignmentName>' -Scope '<originalScope>'`. 3. If the policy definition mode was incorrectly changed, revert it by creating a new policy definition with the correct mode and updating the assignment: run `New-AzPolicyDefinition -Name '<definitionName>' -Policy '<policyRule>' -Mode '<correctMode>'` then `Set-AzPolicyAssignment -Name '<assignmentName>' -PolicyDefinitionId '<newDefinitionId>'`. 4. If exclusions or exemptions were incorrectly removed, reapply them: run `New-AzPolicyExemption -Name '<exemptionName>' -PolicyAssignment '<assignmentName>' -Scope '<resourceScope>' -ExemptionCategory Waiver`. 5. If the on-demand scan caused unexpected load, wait for the next scheduled evaluation cycle to restore normal behavior.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
