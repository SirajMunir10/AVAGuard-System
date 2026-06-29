# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when Azure VM backup takes more than 12 hours or restore takes more than 6 hours?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Backup takes more than 12 hours
- Restore takes more than 6 hours

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review best practices
2. Review performance considerations

## Validation
1. Check the backup job duration in the Azure portal: Go to Recovery Services vault > Backup items > Azure Virtual Machine > select the VM > View details. Confirm that the backup duration is now within expected limits (e.g., less than 12 hours).
2. Run the following Azure CLI command to list recent backup jobs and verify their duration: az backup job list --resource-group <ResourceGroupName> --vault-name <VaultName> --output table. Look for jobs with status 'Completed' and note the 'Duration' column.
3. For restore, initiate a test restore of a file or folder from the VM backup and measure the time taken. Confirm it completes in under 6 hours.
4. Review the 'Backup Performance' report in the Azure portal (under Monitoring > Backup Reports) to ensure backup throughput and restore times are within recommended thresholds.

## Rollback
1. If backup duration remains high, revert any recent changes to the VM configuration (e.g., disk size, number of disks, or backup policy settings) that may have been modified during troubleshooting.
2. Restore the original backup policy settings: In Recovery Services vault > Backup policies, select the policy applied to the VM and click 'Edit'. Reset any changed parameters (e.g., backup frequency, retention range) to their previous values.
3. If a backup extension was updated or reinstalled, reinstall the previous version of the Azure Backup extension for Windows or Linux using the appropriate method (e.g., for Windows: az vm extension set --vm-name <VMName> --resource-group <ResourceGroupName> --name VMSnapshot --publisher Microsoft.Azure.RecoveryServices --version <PreviousVersion>).
4. If performance was degraded due to network throttling or storage account limits, remove any applied throttling rules or revert storage account replication settings (e.g., change from geo-redundant storage to locally redundant storage if that was changed).

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
