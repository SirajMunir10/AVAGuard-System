# Troubleshooting: Azure Backup (UserErrorMarketPlaceVMNotSupported)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve UserErrorMarketPlaceVMNotSupported when restoring a VM from Azure Backup?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- VM creation failed due to Market Place purchase request being not present
- Partial failure: disks are restored but the VM is not restored

## Error Codes
- `UserErrorMarketPlaceVMNotSupported`

## Root Causes
1. Attempting to restore a VM with a specific Plan/Publisher setting that is no longer available in Azure Marketplace

## Remediation Steps
1. If the publisher does not have any Marketplace information, attach the restored disk(s) (that were created during partial failure) as data disks to an existing VM

## Validation
1. Verify that the restored disks are attached as data disks to the target VM: `az vm disk list --resource-group <TargetRG> --vm-name <TargetVMName> --query "[?contains(name, 'restored')].{Name:name, Lun:lun}" -o table`
2. Confirm the target VM is running and accessible: `az vm show --resource-group <TargetRG> --name <TargetVMName> --query "provisioningState" -o tsv` (should return 'Succeeded')
3. Check that the data disks appear in the OS (e.g., via disk management or `lsblk` on Linux) and are mountable.
4. Validate that the original VM's data is accessible from the attached disks (e.g., browse file system).

## Rollback
1. Detach the restored disks from the target VM: `az vm disk detach --resource-group <TargetRG> --vm-name <TargetVMName> --name <RestoredDiskName>`
2. Delete the restored disks if no longer needed: `az disk delete --resource-group <TargetRG> --name <RestoredDiskName> --yes`
3. If the target VM was created solely for this recovery, delete it: `az vm delete --resource-group <TargetRG> --name <TargetVMName> --yes`
4. Re-attempt the restore using a different approach (e.g., restore to a new VM with compatible Marketplace plan or use a custom image).

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
