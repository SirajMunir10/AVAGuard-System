# Troubleshooting: Azure Backup (UserErrorRequestDisallowedByPolicy)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Azure VM backup failure due to policy preventing snapshot operation with error UserErrorRequestDisallowedByPolicy?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure Policy governing tags with Deny effect

## Symptoms
- VM backup fails with error code UserErrorRequestDisallowedByPolicy
- Error message: An invalid policy is configured on the VM which is preventing Snapshot operation

## Error Codes
- `UserErrorRequestDisallowedByPolicy`

## Root Causes
1. An Azure Policy that governs tags within the environment is configured with a Deny effect, blocking the snapshot operation

## Remediation Steps
1. Consider changing the policy from a Deny effect to a Modify effect
2. Or create the resource group manually according to the naming schema required by Azure Backup

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
