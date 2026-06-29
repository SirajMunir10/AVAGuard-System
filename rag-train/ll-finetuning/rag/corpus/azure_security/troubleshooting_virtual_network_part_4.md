# Troubleshooting: Virtual Network

**Domain:** Azure
**Subdomain:** Virtual Network
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Azure VM connectivity issues when a VM cannot connect to another VM in the same virtual network?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Virtual Network, Network Security Groups

## Symptoms
- Azure VM cannot connect to another Azure VM in the same virtual network

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Download TCping to your source VM.
2. Open a Command Prompt window.
3. Navigate to the folder in which you downloaded TCping.
4. Ping the destination from the source VM by using the following command: tcping64.exe -t <destination VM address> 3389
5. If the ping test is successful, go to Step 3. Otherwise, go to the next step.
6. For each VM, check for default Inbound port rules of Allow VNet Inbound and Allow Load Balancer Inbound. Make sure to also check that there are no matching blocking rules that are listed below a lower-priority rule. Rules that have a lower number are matched first. For example, if you have a rule that has priority 1000 and 6500, the rule that has priority 1000 is matched first.
7. After that, try to ping the destination from the source VM again: tcping64.exe -t <destination VM address> 3389
8. To connect by using Remote Desktop, follow these steps: Sign in to the Azure portal. In the left menu, select Virtual Machines. Select the virtual machine in the list. On the page for the virtual machine, select Connect.
9. If the Remote Desktop or SSH connection is successful, go to next step.
10. Run a connectivity check on the source VM, and check the response.

## Validation
1. On the source VM, open Command Prompt and run: tcping64.exe -t <destination VM private IP> 3389. Verify that the output shows 'Port is open' or similar success. 2. In Azure portal, navigate to each VM's Network Security Group (NSG). Under 'Inbound security rules', confirm that a rule with priority lower than 6500 (e.g., 1000) allows 'VirtualNetwork' inbound (source 'VirtualNetwork', destination 'Any', service 'Custom' with port 3389, action 'Allow'). Also confirm no higher-priority (lower number) rule blocks the traffic. 3. From the source VM, attempt an RDP connection to the destination VM's private IP. Verify the connection succeeds. 4. In Azure portal, on the source VM's 'Connect' blade, run the 'Connectivity check' tool targeting the destination VM's private IP and port 3389. Verify the result is 'Reachable'.

## Rollback
1. If validation fails, revert any NSG rule changes: In Azure portal, for each VM's NSG, delete any newly added inbound rule or restore the previous rule priority/action. 2. If a blocking rule was accidentally removed, re-add it with the original priority and action. 3. If RDP/SSH connectivity is lost, use Azure Serial Console or Boot Diagnostics to access the VM and restore network configuration. 4. If the connectivity check still fails, verify that the destination VM's firewall (e.g., Windows Firewall) allows inbound RDP (port 3389) and that the VM is running.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-vm-connectivity>
