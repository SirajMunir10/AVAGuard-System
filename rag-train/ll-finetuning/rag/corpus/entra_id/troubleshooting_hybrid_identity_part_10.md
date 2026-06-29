# Troubleshooting: Hybrid Identity (InvalidHardMatch)

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to clear an InvalidHardMatch error for general hard match issues?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with hybrid identity
- **Configuration:** Microsoft Entra Connect synchronization

## Symptoms
- InvalidHardMatch error during synchronization

## Error Codes
- `InvalidHardMatch`

## Root Causes
N/A

## Remediation Steps
1. Enable hard match again as described in Hard-match vs Soft-match

## Validation
1. On the Microsoft Entra Connect server, open PowerShell as Administrator and run: `Get-ADSyncScheduler | Format-List *`. Confirm the scheduler is enabled. 2. Run `Start-ADSyncSyncCycle -PolicyType Delta` to trigger a delta sync. 3. After the sync completes, run `Get-ADSyncExportError` to verify no InvalidHardMatch errors remain. 4. In the Microsoft Entra admin center, navigate to 'Identity > Hybrid management > Microsoft Entra Connect > Connect Sync' and check the 'Synchronization Service Manager' for any new errors.

## Rollback
1. On the Microsoft Entra Connect server, open PowerShell as Administrator and run: `Set-ADSyncScheduler -HardMatchEnabled $false` to disable hard matching again. 2. Run `Start-ADSyncSyncCycle -PolicyType Delta` to apply the change. 3. Confirm the InvalidHardMatch error returns by checking `Get-ADSyncExportError` or the Synchronization Service Manager. 4. If needed, restore any previously modified user attributes (e.g., UserPrincipalName, SourceAnchor) to their original values using the Microsoft Entra admin center or on-premises Active Directory.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
