# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve sync errors by soft-deleting a cloud account and restoring from Recycle Bin?

## Environment Context
- **Tenant Type:** hybrid
- **Configuration:** Microsoft Entra Connect sync

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run Start-ADSyncSyncCycle -PolicyType Delta which should successfully import the account deletion.
2. Start-ADSyncSyncCycle -PolicyType Delta Confirm that the deletion was successful.
3. Restore the user from the Recycle Bin.
4. Run Start-ADSyncSyncCycle -PolicyType Delta on the server to confirm the error doesn't occur again.
5. Start-ADSyncSyncCycle -PolicyType Delta

## Validation
1. Run 'Start-ADSyncSyncCycle -PolicyType Delta' on the Microsoft Entra Connect server and verify no sync errors appear in the Synchronization Service Manager. 2. Confirm the user object is restored in the Entra ID Recycle Bin (via Entra admin center > Identity > Users > Deleted users) and is no longer in soft-deleted state. 3. Run 'Start-ADSyncSyncCycle -PolicyType Delta' again and check that the previously failing sync error does not reoccur.

## Rollback
1. If the delta sync fails or errors persist, run 'Start-ADSyncSyncCycle -PolicyType Delta' again to re-import the deletion. 2. If the user restoration from Recycle Bin fails, re-soft-delete the user via Entra admin center or PowerShell (Remove-AzureADUser) and then restore again. 3. If sync errors continue, consult the Microsoft Entra Connect sync error troubleshooting guide at https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors for further steps.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
