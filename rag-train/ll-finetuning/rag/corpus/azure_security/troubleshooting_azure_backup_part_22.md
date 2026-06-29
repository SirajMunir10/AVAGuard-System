# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreInvalidTargetSubscription)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve cross-subscription restore failure due to target subscription not registered to Recovery Services Resource Provider?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as the target subscription specified for restore is not registered to the Azure Recovery Services Resource Provider

## Error Codes
- `UserErrorCrossSubscriptionRestoreInvalidTargetSubscription`

## Root Causes
1. The target subscription specified for restore is not registered to the Azure Recovery Services Resource Provider.

## Remediation Steps
1. Ensure the target subscription is registered to the Recovery Services Resource Provider before you attempt a cross subscription restore.
2. Creating a vault in the target Subscription should register the Subscription to Recovery Services Resource Provider.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
