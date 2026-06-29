# Troubleshooting: Azure Backup (Event Viewer error 517)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot basic Azure VM backup failures?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** VM Agent (WA Agent), Windows or Linux VM OS version, snapshot extension, internet connectivity, other backup services

## Symptoms
- Backup failures in Event log
- Azure Backup option greyed out on Azure VM

## Error Codes
- `Event Viewer error 517`

## Root Causes
1. VM Agent (WA Agent) not latest version
2. Windows or Linux VM OS version not supported
3. Another backup service running
4. Snapshot extension issues
5. VM lacks internet connectivity
6. Windows Azure Guest Agent service not running or missing

## Remediation Steps
1. Ensure that the VM Agent (WA Agent) is the latest version
2. Ensure that the Windows or Linux VM OS version is supported, refer to the IaaS VM Backup Support Matrix
3. Verify that another backup service isn't running
4. Uninstall extensions to force reload and then retry the backup
5. Verify that the VM has internet connectivity
6. From Services.msc, ensure the Windows Azure Guest Agent service is Running
7. If the Windows Azure Guest Agent service is missing, install it from Back up Azure VMs in a Recovery Services vault

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
