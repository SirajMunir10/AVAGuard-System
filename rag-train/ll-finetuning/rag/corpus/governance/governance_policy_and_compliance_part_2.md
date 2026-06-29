# Governance: Policy and Compliance

**Domain:** Governance
**Subdomain:** Policy and Compliance
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that several Azure subscriptions are not compliant with the organization's policy requiring all storage accounts to use HTTPS-only traffic. How can the administrator identify and remediate these non-compliant resources using Azure Policy?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure Policy initiative 'Audit Windows VMs with a pending reboot' is not relevant; the scenario uses the built-in policy 'Storage accounts should restrict network access' or 'Secure transfer to storage accounts should be enabled'.

## Symptoms
- Storage accounts allow HTTP traffic despite organizational policy requiring HTTPS-only
- Azure Policy compliance dashboard shows non-compliant resources under the 'Secure transfer to storage accounts should be enabled' policy

## Error Codes
N/A

## Root Causes
1. Storage account configuration does not have the 'Enable secure transfer' property set to true
2. Azure Policy assignment is in 'Audit' mode and not 'Deny' or 'DeployIfNotExists', so non-compliant resources are not automatically remediated

## Remediation Steps
1. Assign the built-in policy 'Secure transfer to storage accounts should be enabled' at the management group or subscription scope with effect 'Deny' or 'DeployIfNotExists'
2. Use Azure Policy remediation task to update existing non-compliant storage accounts by setting the 'supportsHttpsTrafficOnly' property to true
3. Alternatively, use Azure CLI: az storage account update --name <storage-account-name> --resource-group <rg> --https-only true

## Validation
Run Azure Policy compliance scan and confirm that the storage account now shows as 'Compliant' for the 'Secure transfer to storage accounts should be enabled' policy.

## Rollback
Set the storage account property 'supportsHttpsTrafficOnly' back to false using Azure CLI: az storage account update --name <storage-account-name> --resource-group <rg> --https-only false. Remove or change the policy assignment effect to 'Audit' or 'Disabled'.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects>
- <https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer>
