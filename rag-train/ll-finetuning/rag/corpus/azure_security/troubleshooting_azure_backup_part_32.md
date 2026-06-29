# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve restore failure when the cloud service has reached its limit on the number of input endpoints?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The cloud service has reached its limit on the number of input endpoints

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Retry the operation by specifying a different cloud service
2. Retry the operation by using an existing endpoint

## Validation
1. Verify that the new cloud service does not exceed the input endpoint limit by running: Get-AzureDeployment -ServiceName <NewCloudServiceName> | Select-Object -ExpandProperty InputEndpoints. 2. Confirm the restore operation succeeded by checking the job status in the Azure portal: navigate to Recovery Services vault > Backup Jobs and verify the restore job shows 'Completed'. 3. If using an existing endpoint, run: Get-AzureDeployment -ServiceName <ExistingCloudServiceName> | Select-Object -ExpandProperty InputEndpoints and ensure the endpoint count is below the limit (typically 25 per deployment).

## Rollback
1. If the restore operation fails after changing cloud service, revert to the original cloud service by re-running the restore operation with the original service name: Restore-AzureRmBackupItem -BackupItem <BackupItem> -RecoveryPoint <RecoveryPoint> -CloudServiceName <OriginalCloudServiceName>. 2. If using an existing endpoint caused issues, remove the added endpoint: Remove-AzureEndpoint -Name <EndpointName> -ServiceName <CloudServiceName> -VM <VMName>. 3. If the restore operation cannot be completed, contact Azure support to increase the input endpoint limit for the subscription.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
