# Troubleshooting: Azure Backup (ExtensionVCRedistInstallationFailure)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the ExtensionVCRedistInstallationFailure error during Azure VM backup snapshot operation?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Windows VM with Azure Backup extension

## Symptoms
- Snapshot operation fails with error code ExtensionVCRedistInstallationFailure
- Error message: The snapshot operation failed because of failure to install Visual C++ Redistributable for Visual Studio 2015

## Error Codes
- `ExtensionVCRedistInstallationFailure`
- `Error 1401`

## Root Causes
1. Failure to install Visual C++ Redistributable for Visual Studio 2015
2. Registry key value for Msiserver service not set correctly
3. Insufficient permissions to update registry key HKEY_LOCAL_MACHINE\SOFTWARE\Classes
4. Antivirus products blocking installation

## Remediation Steps
1. Navigate to C:\Packages\Plugins\Microsoft.Azure.RecoveryServices.VMSnapshot\agentVersion and install vcredist2013_x64
2. Set the Start value in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Msiserver to 3 and not 4
3. If issues persist, restart the installation service by running MSIEXEC /UNREGISTER followed by MSIEXEC /REGISTER from an elevated command prompt
4. Ensure the administrator or user account has sufficient permissions to update the registry key HKEY_LOCAL_MACHINE\SOFTWARE\Classes
5. Provide sufficient permissions and restart the Windows Azure Guest Agent
6. If antivirus products are in place, ensure they have the right exclusion rules to allow the installation

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
