# Troubleshooting: Virtual Network

**Domain:** Azure
**Subdomain:** Virtual Network
**Incident Type:** Troubleshooting

## Scenario / Query
How to enable a secondary network adapter on an Azure VM to communicate outside its own subnet?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure VM with secondary network adapter configured

## Symptoms
- Azure VM can't connect to the second network adapter of an Azure VM in same virtual network
- Traffic flow on the secondary adapter is limited to the same subnet

## Error Codes
N/A

## Root Causes
1. By default, secondary network adapters aren't configured to have a default gateway

## Remediation Steps
1. On the VM that has the second network adapter configured, open a Command Prompt window as an administrator.
2. Run the following command to add the entry in routing table: Route add 0.0.0.0 mask 0.0.0.0 -p <Gateway IP>
3. For example, if the second IP address is 192.168.0.4, the gateway IP should be 192.168.0.1. You have to run the following command: Route add 0.0.0.0 mask 0.0.0.0 -p 192.168.0.1
4. Run route print. If the entry is added successfully, you'll see an entry that resembles the following.
5. Now, try to connect to secondary network adapter. If the connection is still unsuccessful, go to next step.
6. For both the primary and secondary network adapters, check the default Inbound port rules of Allow VNet Inbound and Allow Load Balancer allow inbound on both network adapters. You should also make sure that there are no matching blocking rules that have a lower-priority rule above them.
7. Run a connectivity check to the secondary network adapter.
8. Run a connectivity check across the environment to make sure that the process works end to end.

## Validation
Run route print. If the entry is added successfully, you'll see an entry that resembles the following.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-vm-connectivity>
