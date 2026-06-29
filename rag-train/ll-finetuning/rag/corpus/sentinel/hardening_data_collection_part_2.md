# Hardening: Data Collection

**Domain:** Sentinel
**Subdomain:** Data Collection
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that Microsoft Sentinel is ingesting logs from a non-critical virtual machine that is not covered by any analytics rule. How can the administrator stop ingestion from this specific VM to reduce cost and attack surface, while ensuring that critical VMs continue to send logs?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with multiple Azure VMs connected via the Azure Monitor Agent (AMA). Some VMs are non-critical and not monitored by any Sentinel analytics rule.

## Symptoms
- High data ingestion costs in Microsoft Sentinel
- Logs from non-critical VMs appear in the workspace
- No analytics rules or detections are associated with those VMs

## Error Codes
N/A

## Root Causes
1. All VMs in the resource group are sending logs to the same Data Collection Rule (DCR) without filtering
2. No mechanism to exclude specific VMs from data collection

## Remediation Steps
1. Identify the Data Collection Rule (DCR) that is sending logs from the non-critical VM to the Sentinel workspace.
2. Edit the DCR in the Azure portal or using PowerShell to remove the non-critical VM from the 'Resources' list, or create a separate DCR that excludes that VM.
3. Alternatively, use Azure Policy to assign a DCR only to critical VMs, preventing non-critical VMs from being associated with the Sentinel workspace.
4. Verify that the non-critical VM no longer appears in the Sentinel Logs ingestion table.

## Validation
Run the following KQL query in Sentinel to confirm the VM is no longer sending data: `Heartbeat | where Computer == "<NonCriticalVMName>" | where TimeGenerated > ago(1h)`. If no results appear, ingestion has been stopped.

## Rollback
Re-add the non-critical VM to the original DCR's 'Resources' list, or reassign the DCR to the VM via Azure Policy.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-assignments>
