# Optimization: Cost Management + Billing

**Domain:** Azure
**Subdomain:** Cost Management + Billing
**Incident Type:** Optimization

## Scenario / Query
How can I identify and downsize underutilized virtual machines in my Azure subscription to reduce compute costs without affecting performance?

## Environment Context
- **Tenant Type:** Enterprise (EA or MCA)
- **Configuration:** Azure Advisor cost recommendations enabled; VMs with CPU utilization below 5% and network utilization below 2% for 7 days

## Symptoms
- Monthly Azure spending exceeds budget despite stable workloads
- Azure Advisor displays cost recommendations for right-sizing or shutting down VMs
- Multiple VMs show average CPU usage < 5% and network I/O < 2% over a 7-day period

## Error Codes
N/A

## Root Causes
1. Virtual machines provisioned with oversized SKUs relative to actual workload demand
2. No automated scaling or shutdown policies for development/test VMs during off-hours
3. Lack of regular review of Azure Advisor cost recommendations

## Remediation Steps
1. Review Azure Advisor cost recommendations for right-sizing or shutting down underutilized VMs
2. Resize the VM to a smaller SKU that matches its actual usage pattern (e.g., from Standard_D4s_v3 to Standard_D2s_v3)
3. Implement auto-shutdown schedules for non-production VMs using Azure Automation or DevTest Labs
4. Enable Azure Cost Management anomaly alerts to detect unexpected spending increases

## Validation
After resizing, monitor the VM's CPU and network metrics for 7 days to confirm performance remains acceptable. Verify the monthly cost reduction in Azure Cost Management + Billing.

## Rollback
If performance degrades, resize the VM back to its original SKU using the Azure portal, PowerShell (Update-AzVM), or CLI (az vm resize).

## References
- Azure Advisor cost recommendations documentation
- CIS Microsoft Azure Foundations Benchmark v2.0.0 - Control 5.1.1: 'Ensure that Azure Advisor recommendations are reviewed at regular intervals'
