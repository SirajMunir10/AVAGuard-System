# Troubleshooting: Azure Backup (ExtensionConfigParsingFailure)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve ExtensionConfigParsingFailure error in Azure VM backup due to changed permissions on the MachineKeys directory?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Failure in parsing the config for the backup extension

## Error Codes
- `ExtensionConfigParsingFailure`

## Root Causes
1. Changed permissions on the MachineKeys directory: %systemdrive%\programdata\microsoft\crypto\rsa\machinekeys

## Remediation Steps
1. Run the following command and verify that permissions on the MachineKeys directory are default ones: icacls %systemdrive%\programdata\microsoft\crypto\rsa\machinekeys
2. Default permissions are as follows: Everyone: (R,W) BUILTIN\Administrators: (F)
3. If permissions are different than defaults, fix permissions on the MachineKeys directory by using Explorer security properties and advanced security settings in the directory, reset permissions back to the default values.
4. Remove all user objects except the defaults from the directory and make sure the Everyone permission has special access as follows: List folder/read data, Read attributes, Read extended attributes, Create files/write data, Create folders/append data, Write attributes, Write extended attributes, Read permissions.
5. Delete all certificates where Issued To is the classic deployment model or Windows Azure CRP Certificate Generator: Open certificates on a local computer console. Under Personal > Certificates, delete all certificates where Issued To is the classic deployment model or Windows Azure CRP Certificate Generator.
6. Trigger a VM backup job.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
