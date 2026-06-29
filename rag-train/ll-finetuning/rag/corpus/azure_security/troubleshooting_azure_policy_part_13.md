# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to duplicate a Guest Configuration policy definition from Azure portal without losing custom metadata?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure Policy, Guest Configuration

## Symptoms
- After duplicating a policy definition in the Guest Configuration category via the Azure portal, machines are NonCompliant
- No guest configuration assignment resource exists

## Error Codes
N/A

## Root Causes
1. The Duplicate definition activity in the Azure portal does not copy custom metadata required for guest configuration assignment resources

## Remediation Steps
1. Instead of using the portal, duplicate the policy definition using the Policy Insights API
2. Use the following PowerShell sample with Az.Resources 7.3.0 or higher:
3. # duplicates the built-in policy which audits Windows machines for pending reboots
4. $def = Get-AzPolicyDefinition -id "/providers/Microsoft.Authorization/policyDefinitions/4221adbc-5c0f-474f-88b7-037a99e6114c"
5. New-AzPolicyDefinition -name (new-guid).guid -DisplayName "$($def.DisplayName) (Copy)" -Description $def.Description -Metadata ($def.Metadata | convertto-json) -Parameter ($def.Parameter | convertto-json) -Policy ($def.PolicyRule | convertto-json -depth 15)

## Validation
1. Run the following PowerShell command to verify the new policy definition exists and includes the required metadata: Get-AzPolicyDefinition -Name '<NewPolicyDefinitionName>' | Select-Object Name, DisplayName, Description, Metadata. 2. Confirm that the metadata property is not empty and contains the 'guestConfiguration' category and any custom metadata. 3. Assign the new policy definition to a test scope and verify that guest configuration assignment resources are created for applicable machines. 4. Check compliance status of a test machine using: Get-AzPolicyState -PolicyAssignmentName '<AssignmentName>' -ResourceId '<ResourceId>' | Where-Object {$_.ComplianceState -eq 'NonCompliant'}.

## Rollback
1. Remove the duplicated policy definition created via the API using: Remove-AzPolicyDefinition -Name '<NewPolicyDefinitionName>' -Force. 2. If the original policy definition was accidentally modified or deleted, restore it from backup or recreate it using the original parameters and metadata. 3. Reassign the original policy definition to any scopes that were changed. 4. Verify that the original guest configuration assignments and compliance state are restored by checking: Get-AzGuestConfigurationAssignment -ResourceGroupName '<ResourceGroupName>' -VMName '<VMName>'.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
