# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve restore failure when the specified cloud service is using a reserved IP that doesn't match the configuration of the VM being restored?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The specified cloud service is using a reserved IP that doesn't match the configuration of the virtual machine being restored

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Specify a different cloud service that isn't using a reserved IP
2. Choose another recovery point to restore from

## Validation
1. Verify that the new cloud service selected for the restore does not have a reserved IP assigned: In Azure portal, navigate to the cloud service, select 'IP addresses' under Settings, and confirm the 'Reserved IP' field is empty or set to 'None'. 2. Confirm the VM configuration (e.g., size, network, storage) matches the chosen recovery point: In the restore wizard, review the selected recovery point details and ensure the target cloud service is listed as 'Not using reserved IP'. 3. Initiate a test restore from the chosen recovery point to the new cloud service and monitor the job status in Azure Backup center; verify the job completes with status 'Succeeded'.

## Rollback
1. If the restore fails or causes issues, cancel the ongoing restore job from Azure Backup center by selecting the job and clicking 'Cancel'. 2. Revert to the original cloud service by re-assigning any previously removed reserved IP: In the cloud service's 'IP addresses' blade, set the 'Reserved IP' back to the original reserved IP address. 3. If a different recovery point was used, return to the original recovery point by initiating a new restore job from the backup vault, selecting the original recovery point, and specifying the original cloud service (now with its reserved IP restored). 4. Monitor the new restore job to ensure it completes successfully.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
