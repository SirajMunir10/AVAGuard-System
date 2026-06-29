# Troubleshooting: Network Watcher

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify which network security group is applied to a specific NIC or subnet during connectivity troubleshooting?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Connectivity check results show unexpected Deny or Unstable status

## Error Codes
N/A

## Root Causes
1. Network security group applied to NIC or subnet may be blocking traffic

## Remediation Steps
1. Check SourceSecurityRuleAnalysis.Results[].NetworkSecurityGroupResult.EvaluatedSecurityGroups[].AppliedTo to find the resource ID of the NIC or subnet where the NSG is applied
2. Review the NSG rules associated with that AppliedTo resource

## Validation
Run the following Azure CLI command to verify the NSG applied to a specific NIC or subnet: az network watcher test-connectivity --source-resource <VM-ID> --destination-address <IP> --destination-port <port> --protocol <TCP|UDP> --query 'sourceSecurityRuleAnalysis.results[].networkSecurityGroupResult.evaluatedSecurityGroups[].{appliedTo:appliedTo, rules:rules}' -o json. Confirm that the 'appliedTo' field shows the expected NIC or subnet resource ID and that the NSG rules listed are not blocking the desired traffic.

## Rollback
If the remediation fails or causes issues, revert to the previous NSG configuration by restoring the original NSG rules. Use Azure CLI: az network nsg rule create --resource-group <RG> --nsg-name <NSG> --name <original-rule-name> --priority <original-priority> --direction <Inbound|Outbound> --access <Allow|Deny> --protocol <*> --source-address-prefixes <original-source> --source-port-ranges <original-source-port> --destination-address-prefixes <original-destination> --destination-port-ranges <original-destination-port>. Alternatively, if the NSG was removed from the NIC/subnet, reapply it: az network nic update --resource-group <RG> --name <NIC> --network-security-group <NSG> or az network vnet subnet update --resource-group <RG> --vnet-name <VNET> --name <subnet> --network-security-group <NSG>.

## References
- <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-connectivity-overview>
