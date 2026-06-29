# Troubleshooting: Azure Backup (VMRestorePointInternalError)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve VMRestorePointInternalError caused by antivirus restricting the backup extension?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Antivirus configured on the VM

## Symptoms
- Event Viewer Application logs display message: Faulting application name: IaaSBcdrExtension.exe

## Error Codes
- `VMRestorePointInternalError`

## Root Causes
1. Antivirus configured in the VM is restricting the execution of backup extension

## Remediation Steps
1. Exclude the following directories in the antivirus configuration: C:\Packages\Plugins\Microsoft.Azure.RecoveryServices.VMSnapshot, C:\Packages\Plugins\Microsoft.Azure.RecoveryServices.VMSnapshot, C:\WindowsAzure\Logs\Plugins\Microsoft.Azure.RecoveryServices.VMSnapshot, C:\WindowsAzure\Logs\Plugins\Microsoft.Azure.RecoveryServices.VMSnapshot
2. Retry the backup operation

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
