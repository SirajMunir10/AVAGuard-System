# Troubleshooting: Network Watcher

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret connectivity check results when a hop shows an issue?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Source port status is Unstable, NoConnection, or Timeout
- Destination port status is Unstable, NoConnection, or Timeout

## Error Codes
N/A

## Root Causes
1. Network security group rules may be blocking traffic
2. Network security group rule evaluation shows Deny action

## Remediation Steps
1. Review SourceSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.EvaluatedSecurityGroups[].MatchedRule.Action to determine if traffic is allowed or denied
2. Check SourceSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.RulesEvaluationResult[] for matched source, destination, protocol, and port values
3. Review DestinationSecurityRuleAnalysis similarly for destination-side rules

## Validation
Run the connectivity check again and verify that the SourceSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.EvaluatedSecurityGroups[].MatchedRule.Action is 'Allow' and that the DestinationSecurityRuleAnalysis shows 'Allow' for the matched rule. Confirm that the source port status and destination port status are 'Reachable' or 'Stable'.

## Rollback
If the remediation fails, revert the NSG rule changes by restoring the previous rule configuration. Use the Azure portal, PowerShell (Set-AzNetworkSecurityRuleConfig), or CLI (az network nsg rule update) to reapply the original rules that were in place before the modification.

## References
- <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-connectivity-overview>
