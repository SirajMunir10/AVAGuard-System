# Optimization: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Optimization

## Scenario / Query
How to calculate the impact of userCertificate and proxyAddresses attribute weights on sync limits in Microsoft Entra Connect?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect sync

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. A synced user that doesn't have any attributes populated other than the mandatory Active Directory attributes and Mail might be able to sync up to 332 proxy addresses.
2. For a similar synced user that has a mailNickName attribute, plus 10 user certificates, the maximum number of proxy addresses decreases to 329.
3. If a similar synced user with 10 user certificates plus, for instance, 4 subscriptions assigned (with all service plans enabled), the maximum number of proxy addresses decreases to 311.
4. To achieve 312 proxy addresses, you would need to remove at least three user certificates (depending on the size of the certificate).

## Validation
1. Open PowerShell as Administrator on the Microsoft Entra Connect server. 2. Run `Get-ADSyncRule | Where-Object {$_.Name -like '*Out to AAD - User*'} | Select-Object Name, Precedence` to confirm the sync rules are in place. 3. Use `Get-ADSyncUser -Identity <testUserUPN> | Select-Object userPrincipalName, mail, mailNickName, proxyAddresses, userCertificate` to verify the user's attributes. 4. Check the sync statistics: `Get-ADSyncExportStatistics -ConnectorName 'contoso.onmicrosoft.com - AAD'` to ensure no export errors. 5. Review the provisioning logs in the Synchronization Service Manager (Start -> Synchronization Service) under the 'Export' tab for the specific user to confirm the number of proxy addresses synced.

## Rollback
1. If the remediation causes sync errors or unexpected attribute changes, restore the original userCertificate and proxyAddresses values from a backup or by re-importing the original Active Directory attributes. 2. To revert a specific user's attributes, use `Set-ADSyncUser -Identity <testUserUPN> -UserCertificate @() -ProxyAddresses @()` to clear the attributes, then re-apply the original values. 3. If the sync rule changes caused issues, re-import the default sync rules by running `Set-ADSyncScheduler -SyncCycleEnabled $false`, then `Import-Module ADSync`, and `Restore-ADSyncRule -Name 'Out to AAD - User'` to restore the default rule. 4. Force a full sync cycle: `Start-ADSyncSyncCycle -PolicyType Initial` to re-synchronize all objects. 5. Monitor the sync errors using `Get-ADSyncExportError` and verify no lingering issues.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
