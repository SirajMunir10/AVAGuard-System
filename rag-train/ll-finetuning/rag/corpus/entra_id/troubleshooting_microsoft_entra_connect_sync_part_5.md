# Troubleshooting: Microsoft Entra Connect Sync (InvalidSoftMatch)

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Connect Sync
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the InvalidSoftMatch sync error when a synced object was accidentally deleted from on-premises Active Directory and a new object was created for the same entity without deleting the account in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with sourceAnchor attribute based on objectGUID

## Symptoms
- A synced object was accidentally deleted from on-premises Active Directory and a new object was created in Active Directory for the same entity (such as user) without deleting the account in Microsoft Entra ID.
- The new account fails to sync with the existing Microsoft Entra object.
- Microsoft Entra Connect was uninstalled and reinstalled. During the reinstallation, a different attribute was chosen as the sourceAnchor attribute.
- All the previously synced objects stop syncing with the InvalidSoftMatch error.

## Error Codes
- `InvalidSoftMatch`

## Root Causes
1. Two objects with different sourceAnchor (immutableId) attributes that have the same value for the proxyAddresses or userPrincipalName attributes, which are used during the soft-match process on Microsoft Entra ID.

## Remediation Steps
N/A

## Validation
1. Run the Microsoft Entra Connect Synchronization Service Manager and check the 'Connectors' tab for the on-premises Active Directory connector. Verify that the 'Run Profile' for 'Delta Import' and 'Delta Synchronization' completes without errors. 2. In the Synchronization Service Manager, go to the 'Search Connector Space' and search for the affected user object. Confirm that the 'immutableId' (sourceAnchor) matches the original value from the on-premises objectGUID. 3. Use the Microsoft Entra admin center to navigate to 'Identity > Users > All users', locate the affected user, and verify that the 'On-premises immutable ID' field matches the expected value. 4. Run the following PowerShell command on the Microsoft Entra Connect server to check for sync errors: `Get-ADSyncCSObject -ConnectorName "<ConnectorName>" -DistinguishedName "<DistinguishedName>" | Select-Object -ExpandProperty Error`. Ensure no InvalidSoftMatch errors are returned.

## Rollback
1. If the remediation fails, restore the original on-premises Active Directory user object using Active Directory Recycle Bin or authoritative restore. 2. Re-run Microsoft Entra Connect configuration wizard and set the sourceAnchor attribute back to the original attribute (e.g., objectGUID) if it was changed. 3. In the Synchronization Service Manager, perform a 'Full Import' and 'Full Synchronization' on the on-premises Active Directory connector to re-evaluate all objects. 4. Use the Microsoft Entra admin center to delete the orphaned cloud user object (if it was created) and allow the restored on-premises object to soft-match correctly. 5. Run `Start-ADSyncSyncCycle -PolicyType Delta` to force a delta sync cycle and monitor for errors.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
