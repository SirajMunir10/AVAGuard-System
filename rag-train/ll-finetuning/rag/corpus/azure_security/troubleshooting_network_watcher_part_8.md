# Troubleshooting: Network Watcher

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Troubleshooting

## Scenario / Query
How to check VM connectivity using Azure Network Watcher when connection status is Unreachable?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- ConnectionStatus : Unreachable
- ProbesSent : 100
- ProbesFailed : 100

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Windows: Check connectivity with Azure Network Watcher using PowerShell
2. For Linux: Check connectivity with Azure Network Watcher using Azure CLI 2.0

## Validation
Run the following Azure CLI command to verify VM connectivity after remediation: az network watcher test-connectivity --resource-group <ResourceGroupName> --source-resource <SourceVMResourceId> --dest-resource <DestinationVMResourceId> --protocol TCP --destination-port 80. Confirm that ConnectionStatus is 'Reachable' and ProbesFailed is 0. For PowerShell: Test-AzNetworkWatcherConnectivity -NetworkWatcherName <NWName> -ResourceGroupName <NWResourceGroup> -SourceId <SourceVMId> -DestinationId <DestinationVMId> -DestinationPort 80 -Protocol TCP. Verify output shows ConnectionStatus 'Reachable'.

## Rollback
If the remediation fails or causes issues, revert any changes made to the source or destination VM's network security groups, route tables, or firewall rules. For example, if a network security group rule was added to allow traffic, remove that rule using: az network nsg rule delete --resource-group <NSGResourceGroup> --nsg-name <NSGName> --name <RuleName>. If a route was added, delete it with: az network route-table route delete --resource-group <RouteTableRG> --route-table-name <RouteTableName> --name <RouteName>. For Windows firewall changes, run 'netsh advfirewall firewall delete rule name="<RuleName>"' on the VM. Re-run the connectivity test to confirm the original Unreachable state is restored.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-vm-connectivity>
