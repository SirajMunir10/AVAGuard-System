# Troubleshooting: Azure Backup (ExtensionSnapshotFailedCOM)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve ExtensionSnapshotFailedCOM, ExtensionInstallationFailedCOM, or ExtensionInstallationFailedMDTC errors during Azure VM backup?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Snapshot operation failed due to COM+ error
- Extension installation/operation failed due to a COM+ error
- Extension installation failed with the error 'COM+ was unable to talk to the Microsoft Distributed Transaction Coordinator'

## Error Codes
- `ExtensionSnapshotFailedCOM`
- `ExtensionInstallationFailedCOM`
- `ExtensionInstallationFailedMDTC`

## Root Causes
1. Issue with Windows service COM+ System application

## Remediation Steps
1. Try starting/restarting Windows service COM+ System Application (from an elevated command prompt - net start COMSysApp)
2. Ensure Distributed Transaction Coordinator service is running as Network Service account. If not, change it to run as Network Service account and restart COM+ System Application
3. If unable to restart the service, then reinstall Distributed Transaction Coordinator service by following the steps below: Stop the MSDTC service, Open a command prompt (cmd), Run the command msdtc -uninstall, Run the command msdtc -install, Start the MSDTC service
4. Stop the MSDTC service, Open a command prompt (cmd), Run the command msdtc -uninstall, Run the command msdtc -install, Start the MSDTC service
5. Start the Windows service COM+ System Application
6. After the COM+ System Application starts, trigger a backup job from the Azure portal

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
