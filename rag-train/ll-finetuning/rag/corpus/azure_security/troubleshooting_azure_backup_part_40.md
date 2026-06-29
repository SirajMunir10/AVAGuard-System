# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreInvalidTenant)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve cross-subscription restore failure due to tenant ID mismatch?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as the tenant IDs for source and target subscriptions don't match

## Error Codes
- `UserErrorCrossSubscriptionRestoreInvalidTenant`

## Root Causes
1. The tenant IDs for source and target subscriptions don't match.

## Remediation Steps
1. Ensure that the source and target subscriptions belong to the same tenant.

## Validation
1. Verify that both source and target subscriptions are in the same Azure AD tenant by running: Get-AzSubscription -SubscriptionId '<source-subscription-id>' | Select-Object TenantId and Get-AzSubscription -SubscriptionId '<target-subscription-id>' | Select-Object TenantId. 2. Confirm the TenantId values match. 3. Retry the cross-subscription restore operation and check that it completes without the UserErrorCrossSubscriptionRestoreInvalidTenant error.

## Rollback
1. If the restore operation fails or causes issues, cancel any in-progress restore jobs via the Azure portal or using Stop-AzRecoveryServicesBackupJob. 2. Revert any subscription changes made to align tenants (e.g., move the target subscription back to its original tenant using Azure support if needed). 3. Re-assess the restore plan and consider using a different target subscription within the same tenant as the source.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
