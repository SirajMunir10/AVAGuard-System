# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve restore failure when the resource group quota has been reached?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The resource group quota has been reached

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Delete some resource groups from the Azure portal
2. Contact Azure Support to increase the limits

## Validation
1. Open the Azure portal and navigate to the resource group that was targeted for the restore. 2. In the left menu, select 'Overview' and verify the resource group exists and is not in a 'Deleting' state. 3. Run the following Azure CLI command to confirm the resource group quota is no longer exceeded: az group list --query "[?location=='<your-region>'].{Name:name, Quota:properties.quota}" --output table. 4. Attempt a test restore of a small VM to the same resource group and confirm the restore completes without quota errors.

## Rollback
1. If the restore still fails due to quota, re-create any deleted resource groups using the Azure portal or CLI: az group create --name <deleted-group-name> --location <region>. 2. If you contacted Azure Support to increase limits and the increase is not yet applied, revert to the original quota by submitting a support request to decrease the limit back to the previous value. 3. As a last resort, restore the VM to a different resource group that has available quota.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
