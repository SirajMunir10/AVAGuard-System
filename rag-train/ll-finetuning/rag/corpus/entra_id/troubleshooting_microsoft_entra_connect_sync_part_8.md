# Troubleshooting: Microsoft Entra Connect Sync (LargeObject)

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Connect Sync
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve LargeObject or ExceededAllowedLength sync errors when an attribute exceeds the allowed size, length, or count limit set by Microsoft Entra schema?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect synchronization

## Symptoms
- Synchronization operation results in a LargeObject or ExceededAllowedLength sync error
- Export error thrown when Microsoft Entra Connect tries to sync an object that exceeds the object size limit

## Error Codes
- `LargeObject`
- `ExceededAllowedLength`

## Root Causes
1. An attribute exceeds the allowed size limit, length limit, or count limit set by Microsoft Entra schema
2. Typically occurs for attributes: userCertificate, userSMIMECertificate, thumbnailPhoto, proxyAddresses
3. Microsoft Entra ID has a hard-coded limit of 15 certificates in the userCertificate attribute
4. Up to 100 attributes for Directory extensions with a maximum of 250 characters for each directory extension
5. All attributes contribute to the object's final size; some attributes have different weight multipliers due to additional processing overhead (e.g., indexed values)
6. Different cloud services, service plans, and licenses assigned to the account consume more attributes and contribute to the overall object size

## Remediation Steps
N/A

## Validation
1. Run the Microsoft Entra Connect Synchronization Service Manager and check the 'Export' tab for any remaining LargeObject or ExceededAllowedLength errors. 2. Use the PowerShell cmdlet `Get-ADSyncExportError -ObjectId <objectId>` to confirm no errors for the previously failing object. 3. Verify the attribute values (e.g., userCertificate, proxyAddresses) are within the allowed limits using `Get-MsolUser -UserPrincipalName <UPN> | Select-Object -ExpandProperty userCertificate | Measure-Object` to count certificates. 4. Confirm the object syncs successfully by triggering a delta sync: `Start-ADSyncSyncCycle -PolicyType Delta`.

## Rollback
1. Restore the original attribute values from backup or re-add the removed entries (e.g., certificates or proxy addresses) using `Set-MsolUser -UserPrincipalName <UPN> -UserCertificate @(originalCertificates)` or `Set-ADSyncAttribute -ObjectId <objectId> -AttributeName <attribute> -Value <originalValue>`. 2. If a directory extension was removed, re-create it via `New-MsolServicePrincipal -ServicePrincipalName <extensionName>`. 3. Re-run a full sync cycle: `Start-ADSyncSyncCycle -PolicyType Initial` to re-evaluate the object. 4. Monitor the export errors again in the Synchronization Service Manager to confirm the original error reappears.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
