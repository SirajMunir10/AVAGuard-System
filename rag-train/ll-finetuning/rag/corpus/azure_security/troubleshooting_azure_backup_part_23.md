# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreInvalidTargetSubscription)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve UserErrorCrossSubscriptionRestoreInvalidTargetSubscription when performing a cross-subscription restore in Azure Backup?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as the target subscription specified for restore is not registered to the Azure Recovery Services Resource Provider

## Error Codes
- `UserErrorCrossSubscriptionRestoreInvalidTargetSubscription`

## Root Causes
1. Target subscription specified for restore is not registered to the Azure Recovery Services Resource Provider

## Remediation Steps
1. Ensure that the target subscription is registered to the Recovery Services Resource Provider before you attempt a cross subscription restore.
2. Creating a vault in the target Subscription should typically register the Subscription to Recovery Services vault Provider.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
