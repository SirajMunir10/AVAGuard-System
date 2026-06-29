# Optimization: Cost Management + Billing

**Domain:** Azure
**Subdomain:** Cost Management + Billing
**Incident Type:** Optimization

## Scenario / Query
A customer notices that their Azure subscription costs have increased significantly, and they want to identify underutilized virtual machines that can be resized or shut down to optimize spending.

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure subscription with multiple VMs running; no Azure Advisor recommendations previously reviewed

## Symptoms
- Monthly cost spike of 20% or more compared to previous months
- Multiple VMs with average CPU utilization below 5% over the last 30 days
- Azure Advisor cost recommendations showing 'Resize or shut down underutilized virtual machines'

## Error Codes
N/A

## Root Causes
1. Virtual machines provisioned with larger SKUs than required for the workload
2. No automated shutdown schedule for non-production VMs during off-hours
3. Lack of regular review of Azure Advisor cost optimization recommendations

## Remediation Steps
1. Review Azure Advisor cost recommendations in the Azure portal under 'Advisor > Cost'
2. For each underutilized VM (CPU <= 5% and network <= 7 MB/s for 7 days), resize to a smaller SKU or shut down if not needed
3. Implement auto-shutdown schedules for development/test VMs using Azure Automation or DevTest Labs schedules
4. Enable Azure Cost Management budgets and alerts to monitor future cost anomalies

## Validation
After resizing or shutting down underutilized VMs, verify the monthly cost reduction in Cost Management + Billing and confirm that Azure Advisor no longer flags those VMs as underutilized.

## Rollback
If performance degrades after resizing, revert to the original VM size using Azure PowerShell: Update-AzVM -ResourceGroupName <rg> -VM <vm> -Size <originalSKU>. If a VM was shut down, restart it via the Azure portal or Start-AzVM.

## References
- <https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations>
