# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot IaaS VM backup failures related to DHCP configuration inside the guest VM?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** IaaS VM backup, DHCP settings inside guest VM

## Symptoms
- IaaS VM backup fails

## Error Codes
N/A

## Root Causes
1. DHCP is not enabled inside the guest VM

## Remediation Steps
1. Ensure DHCP is enabled inside the guest VM for IaaS VM backup to work
2. If a static private IP is needed, configure it through the Azure portal or PowerShell
3. Make sure the DHCP option inside the VM is enabled

## Validation
1. Connect to the guest VM via RDP or SSH. 2. Open a command prompt or terminal. 3. Run 'ipconfig /all' (Windows) or 'ip addr show' (Linux) to verify that the network interface is obtaining an IP address from DHCP. 4. Confirm that the DHCP Enabled field shows 'Yes' (Windows) or that the interface shows a dynamic address (Linux). 5. If a static private IP is required, verify in the Azure portal that the VM's network interface has a static private IP assignment and that the guest OS still has DHCP enabled (the static IP is assigned at the Azure level, not inside the VM). 6. Trigger a test backup from the Azure portal or using PowerShell (Start-AzBackupJob) and confirm the backup completes without errors.

## Rollback
1. If DHCP was disabled and enabling it causes network conflicts or loss of static IP, reconfigure the guest OS to use a static IP address that matches the Azure-assigned private IP. 2. In Windows, set a static IP via 'netsh interface ip set address' or the network adapter properties. 3. In Linux, edit the appropriate network configuration file (e.g., /etc/network/interfaces or /etc/sysconfig/network-scripts/ifcfg-eth0) to set a static address. 4. If the backup still fails after enabling DHCP, revert to the previous DHCP setting (disable DHCP) and contact Azure support for further troubleshooting.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
- <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-static-private-ip-arm-ps>
