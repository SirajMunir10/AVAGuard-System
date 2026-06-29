# Troubleshooting: Virtual Network

**Domain:** Azure
**Subdomain:** Virtual Network
**Incident Type:** Troubleshooting

## Scenario / Query
An Azure VM deployed by using Resource Manager cannot connect to another Azure VM in the same virtual network.

## Environment Context
- **Tenant Type:** Azure Resource Manager
- **Configuration:** Virtual network configuration

## Symptoms
- Azure VM cannot connect to another Azure VM in same virtual network
- Azure VM cannot connect to the second network adapter of an Azure VM in same virtual network
- Azure VM cannot connect to the internet

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use netstat -an to list the ports that the VM is listening to
2. Use Test-NetConnection module in PowerShell to display diagnostic information for a connection such as ping test and tcp test
3. Utilize tcping or other TCP-based testing tools, as ICMP traffic is deprioritized by many networking devices. Using TCP tests provides more consistent and reliable results, especially in Azure environments.

## Validation
1. From the source VM, run 'Test-NetConnection -ComputerName <target_VM_private_IP> -Port 3389' (or another port known to be open) to verify TCP connectivity. 2. On the target VM, run 'netstat -an | findstr LISTEN' to confirm the expected ports are listening. 3. Use tcping from the source VM: 'tcping <target_VM_private_IP> <port>' and verify successful replies. 4. Confirm the source VM can reach the internet by running 'Test-NetConnection -ComputerName microsoft.com -Port 80'.

## Rollback
1. If connectivity fails after remediation, revert any temporary firewall rule changes made during testing. 2. Restore any modified Network Security Group (NSG) rules to their previous state using Azure Portal, CLI, or PowerShell. 3. If a custom route was added, remove it via 'Remove-AzRouteTable -ResourceGroupName <rg> -Name <route_table_name>'. 4. Re-enable any disabled network interfaces or subnets that were changed for testing.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-vm-connectivity>
