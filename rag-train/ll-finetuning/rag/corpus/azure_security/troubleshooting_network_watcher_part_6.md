# Troubleshooting: Network Watcher (UnexpectedVirtualNetworkGatewayConnection)

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot unexpected virtual network gateway connections found on the path in Azure Network Watcher connectivity checks?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Network Watcher connectivity check configuration

## Symptoms
- UnexpectedVirtualNetworkGatewayConnection error during connectivity check

## Error Codes
- `UnexpectedVirtualNetworkGatewayConnection`

## Root Causes
1. A virtual network gateway connection was found on the path that wasn't expected

## Remediation Steps
N/A

## Validation
Run the Azure Network Watcher connectivity check again using the same source and destination. Confirm that the check completes without the 'UnexpectedVirtualNetworkGatewayConnection' error. Use the Azure CLI command: az network watcher test-connectivity --source-resource <sourceVM> --dest-resource <destVM> --protocol TCP --dest-port <port>. Verify the output shows 'ProbesSucceeded': true and no unexpected gateway connections in the 'hops' array.

## Rollback
If the remediation fails or causes issues, restore the original virtual network gateway connections and routing configuration. Use the Azure CLI to re-add any removed gateway connections: az network vpn-connection create --resource-group <rg> --name <connectionName> --vnet-gateway1 <gateway1> --vnet-gateway2 <gateway2> --shared-key <key>. Also, revert any route table changes that may have been made to bypass the gateway. Then re-run the connectivity check to confirm the original error reappears.

## References
- <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-connectivity-overview>
