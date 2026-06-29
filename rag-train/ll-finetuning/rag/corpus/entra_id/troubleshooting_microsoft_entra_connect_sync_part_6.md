# Troubleshooting: Microsoft Entra Connect Sync (Error Type 114)

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Connect Sync
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot deletion access violation and password access violation errors in Microsoft Entra Connect sync?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect sync configuration

## Symptoms
- This synchronization operation, Delete, isn't valid. Contact Technical Support (Error Type 114).
- Unable to process this update because one or more cloud-only users' credential update is included in the current request.
- Deleting a cloud-only object isn't supported. Contact Microsoft Customer Support.
- The password change request can't be executed because it contains changes to one or more cloud-only user objects, which aren't supported. Contact Microsoft Customer Support.

## Error Codes
- `Error Type 114`

## Root Causes
1. Microsoft Entra ID protects cloud-only objects from being updated through Microsoft Entra Connect.
2. Calls made directly to Microsoft Entra back-end to attempt to change cloud-only objects.

## Remediation Steps
N/A

## Validation
1. Open the Synchronization Service Manager on the Microsoft Entra Connect server. 2. Go to the 'Operations' tab and verify that no export errors of type 'delete-attribute' or 'delete-add' are present for cloud-only objects. 3. Run the command: `Get-ADSyncExportError -ErrorType 114` to confirm no active error type 114 entries. 4. Check the 'Connectors' tab, select the Microsoft Entra connector, and click 'Search Connector Space'. Filter by 'Object Type' = 'user' and 'DN' containing 'cloud-only' to ensure no cloud-only objects appear in the pending export. 5. Review the synchronization rules to confirm that no outbound sync rules are configured to export changes to cloud-only user objects.

## Rollback
1. If validation fails, restore the original Microsoft Entra Connect synchronization rules from backup using: `Import-ADSyncRule -Path <backup_file>.xml`. 2. Re-enable any disabled sync rules that were previously blocking cloud-only object exports: `Set-ADSyncRule -Identifier <rule_guid> -Enabled $true`. 3. Run a full synchronization cycle: `Start-ADSyncSyncCycle -PolicyType Initial`. 4. If errors persist, revert to the previous Microsoft Entra Connect build by running the installer and selecting 'Restore' from the maintenance options. 5. Contact Microsoft Support if rollback does not resolve the issue, as per the error message guidance.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
