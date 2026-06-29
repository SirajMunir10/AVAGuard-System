# Troubleshooting: Virtual Network

**Domain:** Azure
**Subdomain:** Virtual Network
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve VM connectivity issues identified in the Hops section of a connectivity check response?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Connectivity check response shows issues in the Hops section

## Error Codes
N/A

## Root Causes
1. NetworkSecurityRule blocking traffic
2. UserDefinedRoute blocking traffic
3. CPU usage
4. Memory usage
5. Guest firewall blocking traffic
6. DNS resolution failure
7. Socket error (port already in use)

## Remediation Steps
1. For NetworkSecurityRule: Delete the NSG rule or modify the rule as described here.
2. For UserDefinedRoute: If you don't require this route, delete the UDR. If you can't delete the route, update the route by using the appropriate address prefix and next hop. You can also adjust the Network Virtual Appliance to forward traffic appropriately. For more information, see: Virtual network traffic routing and Route network traffic with a route table using PowerShell.
3. For CPU Usage: Follow these recommendations that describe in Generic performance troubleshooting for Azure Virtual Machine running Linux or Windows.
4. For Memory Usage: Follow the recommendations that are described in Generic performance troubleshooting for Azure Virtual Machine running Linux or Windows.
5. For Guest Firewall: Follow these steps: Turn Windows Firewall on or off.
6. For DNS Resolution: Follow these steps: Azure DNS troubleshooting guide and Name resolution for resources in Azure virtual networks.
7. For Socket Error: The specified port is already in use by another application. Try to use a different port.

## Validation
1. Run the connectivity check again using Azure Network Watcher: `az network watcher test-connectivity --resource-group <rg> --source-resource <vm-id> --dest-resource <target-vm-id> --protocol TCP --destination-port <port>`. 2. Verify that the Hops section now shows no blocking rules or routes. 3. Confirm the VM can reach the target resource (e.g., using `Test-NetConnection` or `ssh`).

## Rollback
1. If an NSG rule was deleted, recreate it using: `az network nsg rule create --resource-group <rg> --nsg-name <nsg> --name <rule-name> --priority <priority> --direction Inbound --access Allow --protocol Tcp --source-address-prefixes <prefix> --source-port-ranges * --destination-address-prefixes <prefix> --destination-port-ranges <port>`. 2. If a UDR was deleted, recreate it using: `az network route-table route create --resource-group <rg> --route-table-name <rt> --name <route-name> --address-prefix <prefix> --next-hop-type VirtualAppliance --next-hop-ip-address <ip>`. 3. For CPU/memory changes, revert any configuration changes (e.g., stop unnecessary processes, restore VM size). 4. For guest firewall, re-enable the firewall rule that was disabled. 5. For DNS, revert DNS server settings to previous values. 6. For socket error, stop the conflicting application or change the port back.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-vm-connectivity>
