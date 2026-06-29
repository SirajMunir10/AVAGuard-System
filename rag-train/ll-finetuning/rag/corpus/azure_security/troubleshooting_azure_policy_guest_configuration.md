# Troubleshooting: Azure Policy / Guest Configuration

**Domain:** Azure
**Subdomain:** Azure Policy / Guest Configuration
**Incident Type:** Troubleshooting

## Scenario / Query
Azure virtual machine user-assigned identities are replaced by system-assigned managed identities after assigning Guest Configuration policy initiatives

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Guest Configuration policy initiatives assigned to audit settings inside a machine

## Symptoms
- User-assigned managed identities that were assigned to the machine are no longer assigned
- Only a system-assigned managed identity is assigned

## Error Codes
N/A

## Root Causes
1. The policy definitions that were previously used in Guest Configuration deployIfNotExists definitions ensured that a system-assigned identity is assigned to the machine, but they also removed the user-assigned identity assignments

## Remediation Steps
1. Delete any existing policy assignments that are marked as [Deprecated]
2. Replace them with the updated prerequisite policy initiative and policy definitions that have the same name as the original

## Validation
1. Run 'az vm identity show --resource-group <vm-rg> --name <vm-name>' and verify that the 'type' field is 'UserAssigned' and the 'userAssignedIdentities' dictionary contains the expected user-assigned identity resource IDs.
2. Run 'az policy assignment list --resource-group <vm-rg> --query "[?contains(displayName, 'Deprecated')]"' and confirm no deprecated policy assignments exist.
3. Run 'az policy assignment list --resource-group <vm-rg> --query "[?contains(displayName, 'Guest Configuration')]"' and verify the assignments use the updated (non-deprecated) initiative/definition names as documented in the source.

## Rollback
1. If validation fails, re-assign the original deprecated policy initiative by running 'az policy assignment create --name <original-deprecated-assignment-name> --policy <deprecated-initiative-definition-id> --resource-group <vm-rg> --assign-identity'.
2. Remove the updated policy assignments with 'az policy assignment delete --name <updated-assignment-name> --resource-group <vm-rg>'.
3. Reapply the user-assigned identity to the VM using 'az vm identity assign --resource-group <vm-rg> --name <vm-name> --identities <user-assigned-identity-resource-id>'.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general (blog post: Important change released for Guest Configuration audit policies)>
