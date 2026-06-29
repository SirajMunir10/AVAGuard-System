# Troubleshooting: Network Watcher

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Troubleshooting

## Scenario / Query
How to check VM connectivity using Azure Network Watcher with PowerShell or Azure CLI when the connection status is Unreachable?

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
1. Check connectivity with Azure Network Watcher using PowerShell for Windows
2. Check connectivity with Azure Network Watcher using Azure CLI 2.0 for Linux
3. In the Hops section of the connectivity check response, check the listed issues

## Validation
Run the following Azure CLI command to verify connectivity after remediation: az network watcher test-connectivity --resource-group <rg> --source-resource <vm1> --dest-resource <vm2> --protocol Tcp --destination-port 80. Confirm that 'ConnectionStatus' is 'Reachable' and 'ProbesFailed' is 0. Alternatively, use PowerShell: Test-AzNetworkWatcherConnectivity -NetworkWatcher $nw -SourceResourceId $vm1.Id -DestinationResourceId $vm2.Id -DestinationPort 80 -Protocol Tcp; verify that 'ConnectionStatus' equals 'Reachable'.

## Rollback
If the remediation fails or causes issues, revert any changes made to network security groups, routes, or firewall rules. For example, if a network security group rule was added to allow traffic, remove that rule using: az network nsg rule delete --resource-group <rg> --nsg-name <nsg> --name <rule>. If a route was added, delete it with: az network route-table route delete --resource-group <rg> --route-table-name <rt> --name <route>. Then re-run the connectivity test to confirm the original 'Unreachable' state is restored.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-vm-connectivity>
