# Optimization: Cost Management + Billing

**Domain:** Azure
**Subdomain:** Cost Management + Billing
**Incident Type:** Optimization

## Scenario / Query
An Azure subscription shows a high number of unattached managed disks incurring storage costs. How can I identify and delete unattached disks to optimize costs?

## Environment Context
- **Tenant Type:** Enterprise (EA or MCA)
- **Configuration:** Subscription with multiple VMs and managed disks

## Symptoms
- Monthly cost report shows significant storage charges from managed disks
- Azure Advisor cost recommendations list unattached disks
- Azure Cost Management + Billing shows unused resources

## Error Codes
N/A

## Root Causes
1. Virtual machines were deleted without deleting their attached managed disks
2. Disks were created for future use but never attached
3. Lack of lifecycle management or governance for orphaned resources

## Remediation Steps
1. Identify unattached disks using Azure CLI: az disk list --query "[?managedBy==null].{Name:name, ResourceGroup:resourceGroup, Size:diskSizeGb}" --output table
2. Review the list and confirm disks are not needed (e.g., no pending snapshots or backup dependencies)
3. Delete unattached disks using Azure CLI: az disk delete --name <disk-name> --resource-group <rg-name> --yes
4. Alternatively, use Azure PowerShell: Remove-AzDisk -ResourceGroupName <rg-name> -DiskName <disk-name> -Force
5. Enable Azure Policy to audit or automatically delete unattached disks (built-in policy: 'Audit unattached managed disks')

## Validation
Run the query again to confirm no unattached disks remain: az disk list --query "[?managedBy==null]" --output table | Measure-Object -Line

## Rollback
Deleted disks cannot be recovered unless a snapshot or backup exists. Before deletion, ensure a backup or export of the disk is taken if data retention is required.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-machines/delete-unattached-disks>
- <https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations#unattached-managed-disks>
