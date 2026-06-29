# Troubleshooting: Hybrid Identity (LargeObject)

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix the LargeObject or ExceededAllowedLength error in Microsoft Entra Connect sync?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect sync

## Symptoms
- LargeObject error
- ExceededAllowedLength error

## Error Codes
- `LargeObject`
- `ExceededAllowedLength`

## Root Causes
1. User properties contain attribute values that are too large or exceed allowed length

## Remediation Steps
1. Review the user properties and remove attribute values that might no longer be required. Examples include revoked or expired certificates and outdated or unnecessary addresses, such as SMTP, X.400, X.500, MSMail, and CcMail.

## Validation
1. Run the Microsoft Entra Connect Synchronization Service Manager on the server. Go to the 'Connectors' tab, select the Active Directory Connector, and click 'Search Connector Space'. Search for the object that previously caused the error. Verify that the object's attributes (e.g., proxyAddresses, certificateUserIds, or other multi-valued attributes) no longer contain values exceeding size limits (e.g., proxyAddresses entries > 256 characters, or total attribute size > 15 KB).
2. Run the following PowerShell command to check for pending export errors: `Get-ADSyncExportError -ConnectorName "<ConnectorName>"`. Confirm no 'LargeObject' or 'ExceededAllowedLength' errors are returned.
3. Initiate a full synchronization cycle: Start-ADSyncSyncCycle -PolicyType Delta. After completion, check the Synchronization Service Manager for any new errors under the 'Export' tab.

## Rollback
1. If the remediation fails or causes issues, restore the removed attribute values from a backup of the on-premises Active Directory user object. Use Active Directory Administrative Center or PowerShell to re-add the original values (e.g., `Set-ADUser -Identity <User> -Add @{proxyAddresses='SMTP:user@contoso.com'}`).
2. Run a delta synchronization: `Start-ADSyncSyncCycle -PolicyType Delta`.
3. Monitor the Synchronization Service Manager for recurrence of the 'LargeObject' or 'ExceededAllowedLength' error. If the error persists, consider splitting the attribute values across multiple objects or using a different attribute, as documented in the troubleshooting guide.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
