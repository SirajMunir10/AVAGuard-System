# Troubleshooting: Virtual Network

**Domain:** Azure
**Subdomain:** Virtual Network
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot an Azure VM that cannot connect to the internet by checking and resetting the NIC state via Resource Explorer?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Azure VM can't connect to the internet

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Log in to the Resource Explorer portal.
2. In the left pane, select Subscriptions.
3. In the left pane, select the resource group that the affected network adapter or VM belongs to.
4. Go to the Microsoft Network.
5. Select the Network Interfaces option.
6. Select the affected network interface.
7. Select the Read/Write option at the top of the portal.
8. Select the Edit option. Note: After you select the Edit option, the 'Get' option changes to a Put option.
9. Select the affected network interface, and then select the Put option. Note: After you make this selection, the ProvisioningState is displayed as Updating. The same result is shown on the regular Azure Resource Manager portal. If the operation is completed successfully, the ProvisioningState value changes to Succeeded, as shown.
10. Refresh your portal. The network adapter should be in a success state.

## Validation
1. In the Azure portal, navigate to the affected VM and select 'Networking'. Verify that the public IP address is assigned and the effective security rules allow outbound traffic. 2. From the VM, run 'Test-NetConnection google.com -Port 80' (Windows) or 'curl -I http://google.com' (Linux) to confirm internet connectivity. 3. In Resource Explorer, navigate to the NIC's Microsoft.Network/networkInterfaces resource and confirm 'properties.provisioningState' is 'Succeeded'.

## Rollback
1. In Resource Explorer, navigate to the affected NIC and select 'Edit'. 2. Revert any changes made during remediation (e.g., restore original properties). 3. Select 'Put' to apply the original configuration. 4. Verify the NIC's provisioning state returns to 'Succeeded'. 5. Re-test VM internet connectivity using the same commands as in validation.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-vm-connectivity>
