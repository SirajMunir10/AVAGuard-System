# Optimization: Cost Management

**Domain:** Azure
**Subdomain:** Cost Management
**Incident Type:** Optimization

## Scenario / Query
An Azure subscription shows a high number of unattached managed disks incurring storage costs. How can I identify and delete unattached disks to optimize costs?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure subscription with multiple managed disks; no automated lifecycle management in place

## Symptoms
- Monthly cost report shows significant storage charges from managed disks
- Azure Cost Management + Billing advisor recommendations list unattached disks
- Azure Advisor alerts for underutilized or idle resources

## Error Codes
N/A

## Root Causes
1. Managed disks remain provisioned after associated virtual machines are deleted
2. No policy or automation to delete orphaned disks

## Remediation Steps
1. Use Azure Cost Management + Billing to view cost by resource and identify unattached disks
2. Run the following Azure CLI command to list unattached disks: az disk list --query "[?managedBy==null].{Name:name, ResourceGroup:resourceGroup, DiskSizeGB:diskSizeGb}" --output table
3. Verify each disk is no longer needed by checking last attach time or contacting the owner
4. Delete unattached disks using: az disk delete --name <disk-name> --resource-group <resource-group> --yes
5. Optionally, set up an Azure Policy to audit or automatically delete unattached disks after a defined grace period

## Validation
After deletion, re-run the Azure CLI query to confirm no unattached disks remain. Check the next monthly cost report for reduced storage charges.

## Rollback
If a disk is deleted by mistake, restore it from the most recent snapshot (if snapshots were enabled) or recreate the disk from a backup.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-machines/disks-find-unattached-portal>
