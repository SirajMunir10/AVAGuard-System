# Implementation: Mailbox Migration (MapiExceptionShutoffQuotaExceeded)

**Domain:** Exchange Online
**Subdomain:** Mailbox Migration
**Incident Type:** Implementation

## Scenario / Query
A tenant administrator is performing a remote move migration of on-premises mailboxes to Exchange Online. The migration batch fails with the error 'MapiExceptionShutoffQuotaExceeded: Unable to open message store' for certain users. What is the root cause and how should it be remediated?

## Environment Context
- **Tenant Type:** Enterprise Hybrid
- **Configuration:** On-premises Exchange 2016 with hybrid configured; migration using New-MigrationBatch with RemoteMove endpoint

## Symptoms
- Migration batch shows status 'Failed' for specific users
- Error in migration report: 'MapiExceptionShutoffQuotaExceeded: Unable to open message store'
- Affected users cannot be migrated until the issue is resolved

## Error Codes
- `MapiExceptionShutoffQuotaExceeded`

## Root Causes
1. The on-premises mailbox has exceeded its 'ProhibitSendReceiveQuota' or 'RecoverableItemsQuota', preventing the migration process from opening the mailbox

## Remediation Steps
1. Increase the on-premises mailbox quota to accommodate the migration: Set-Mailbox -Identity <User> -ProhibitSendReceiveQuota <higher value> -RecoverableItemsQuota <higher value>
2. Alternatively, temporarily disable the quota check on the on-premises server by setting the registry key 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MSExchangeIS\ParametersSystem\Disable Quota Check' to 1 (only for migration duration)
3. After increasing quotas, resume the migration batch: Resume-MigrationBatch -Identity <BatchName>

## Validation
Run Get-MigrationUser -Identity <User> | fl Status, Error to confirm the user now shows 'Synced' or 'Completed' status

## Rollback
If quotas were increased, reduce them back to original values after migration completes. If registry key was used, set it back to 0 and restart the Information Store service.

## References
- <https://learn.microsoft.com/en-us/exchange/troubleshoot/migration/mapiexceptionshutoffquotaexceeded-error>
