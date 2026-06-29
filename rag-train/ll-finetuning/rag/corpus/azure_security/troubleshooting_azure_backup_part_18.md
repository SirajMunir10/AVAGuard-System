# Troubleshooting: Azure Backup (ExtensionSnapshotFailedNoSecureNetwork)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the ExtensionSnapshotFailedNoSecureNetwork error when taking Azure VM backup snapshots?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The snapshot operation failed because of failure to create a secure network communication channel

## Error Codes
- `ExtensionSnapshotFailedNoSecureNetwork`

## Root Causes
1. Failure to create a secure network communication channel

## Remediation Steps
1. Open the Registry Editor by running regedit.exe in an elevated mode
2. Identify all versions of the .NET Framework present in your system under the hierarchy of registry key HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft
3. For each .NET Framework present in the registry key, add the following key: SchUseStrongCrypto"=dword:00000001

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
