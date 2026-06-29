# Troubleshooting: Microsoft Entra Connect Sync (114)

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Connect Sync
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the DeletingCloudOnlyObjectNotAllowed (Error Type 114) error during Microsoft Entra Connect synchronization when migrating from hybrid to cloud-only?

## Environment Context
- **Tenant Type:** hybrid
- **Configuration:** DirSyncEnabled set to False

## Symptoms
- Microsoft Entra Connect returns error DeletingCloudOnlyObjectNotAllowed (Error Type 114)
- Error literal: 'This synchronization operation, Delete, isn't valid. Contact Technical Support.'
- Export error with ErrorCode 0x8023134a
- Synchronization fails for specific features, resulting in users not being deleted accordingly

## Error Codes
- `114`
- `0x8023134a`

## Root Causes
1. The call from Microsoft Entra Connect has no UPN, a new or unique GUID, or other required information
2. Microsoft Entra Connect is trying to export data, but it has DirSyncEnabled set to False
3. Microsoft Entra Connect is trying to delete a restored user or other object, usually because a user or other object reference has been moved out of sync scope or to Lost & Found container
4. The rule created by the customer to move users out of scope is based on the Admin attribute

## Remediation Steps
1. Identify the problem object reference

## Validation
1. Run the Microsoft Entra Connect Synchronization Service Manager and check the 'Export' tab for the object that previously failed. Confirm that the error code 0x8023134a no longer appears and the export status is 'Success'.
2. In the Synchronization Service Manager, verify that the object's 'Delete' operation is no longer blocked and that the object is either deleted or correctly moved out of scope.
3. Use the Microsoft Entra admin center to search for the affected user or object and confirm it is no longer present in the cloud (if deletion was intended) or that its status is correct.
4. Run a delta synchronization cycle and check the 'Export' logs to ensure no new instances of error 114 or 0x8023134a appear.
5. Validate that the DirSyncEnabled flag remains set to False (as expected for cloud-only migration) by running: Get-MsolCompanyInformation | Select-Object DirSyncEnabled.

## Rollback
1. If the deletion was unintended, restore the deleted object from the Microsoft Entra admin center's 'Deleted users' or 'Deleted groups' page within 30 days.
2. If the object was moved out of sync scope incorrectly, re-add the object to the synchronization scope by adjusting the filtering rules in Microsoft Entra Connect.
3. If the DirSyncEnabled flag was incorrectly changed, set it back to True using: Set-MsolDirSyncEnabled -EnableDirSync $true (requires Global Administrator credentials).
4. Re-run a full synchronization cycle to re-import and re-export the affected object.
5. Verify that the object reappears in the cloud and that no new errors are generated.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
