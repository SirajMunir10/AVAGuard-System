# Troubleshooting: Network Watcher

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Troubleshooting

## Scenario / Query
How to determine if a network security group is blocking connectivity based on connectivity check results?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- SourceSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.SecurityRuleAccessResult shows Deny
- DestinationSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.SecurityRuleAccessResult shows Deny

## Error Codes
N/A

## Root Causes
1. Network security group rule with action Deny is matched
2. Matched rule name can be found in SourceSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.EvaluatedSecurityGroups[].MatchedRule.RuleName

## Remediation Steps
1. Identify the network security group ID from SourceSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.EvaluatedSecurityGroups[].NetworkSecurityGroupId
2. Modify the identified network security group rule to allow the required traffic, or create a new rule with higher priority

## Validation
Run 'az network watcher test-connectivity --source-resource <vm-id> --destination-address <dest-ip> --destination-port <port> --protocol TCP' and inspect the output. Confirm that SourceSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.SecurityRuleAccessResult is 'Allow' and DestinationSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.SecurityRuleAccessResult is 'Allow'. Also verify that the MatchedRule.RuleName for the relevant NSG is the new or modified rule.

## Rollback
If the remediation fails or causes issues, revert the NSG rule change: either delete the newly created rule using 'az network nsg rule delete --nsg-name <nsg-name> --resource-group <rg> --name <rule-name>' or restore the original rule by setting its access back to 'Deny' with 'az network nsg rule update --nsg-name <nsg-name> --resource-group <rg> --name <rule-name> --access Deny'. Then re-run the connectivity check to confirm the original Deny state is restored.

## References
- <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-connectivity-overview>
