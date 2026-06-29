# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve restore failure when the Backup service doesn't have authorization to access resources in your subscription?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The Backup service doesn't have authorization to access resources in your subscription

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. First restore disks by using the steps in Restore backed-up disks
2. Then use the PowerShell steps in Create a VM from restored disks

## Validation
1. Verify that the restored disks are present in the target resource group by running: Get-AzDisk -ResourceGroupName <TargetResourceGroup> | Where-Object {$_.Name -like '*Restore*'}. 2. Confirm that the managed disk IDs are correct and the disk state is 'Attached' or 'Unattached' as expected. 3. Attempt to create a VM from the restored disks using: New-AzVM -ResourceGroupName <TargetResourceGroup> -Location <Location> -VM <VMConfig> -Disks <DiskConfig>. 4. Check that the VM provisioning state is 'Succeeded' and the VM is running: Get-AzVM -ResourceGroupName <TargetResourceGroup> -Name <VMName> -Status.

## Rollback
1. If the VM creation fails, delete the partially created VM: Remove-AzVM -ResourceGroupName <TargetResourceGroup> -Name <VMName> -Force. 2. Delete the restored disks that were created during the restore process: Get-AzDisk -ResourceGroupName <TargetResourceGroup> | Where-Object {$_.Name -like '*Restore*'} | Remove-AzDisk -Force. 3. Re-initiate the restore operation from the backup vault using the original restore point, ensuring the Backup service has the required permissions (e.g., assign 'Backup Contributor' role to the Backup service principal). 4. Monitor the restore job status in the Azure portal or via: Get-AzRecoveryServicesBackupJob -VaultId <VaultID>.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
