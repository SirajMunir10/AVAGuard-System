# Hardening: Data Collection and Retention

**Domain:** Sentinel
**Subdomain:** Data Collection and Retention
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that Microsoft Sentinel is ingesting large volumes of data from a non-critical source, causing the workspace to approach its daily ingestion limit and potentially lose critical security events. How can the administrator configure a daily cap or set an expiration on data retention to prevent data loss while ensuring compliance with organizational retention policies?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with Microsoft Sentinel enabled)
- **Configuration:** Log Analytics workspace with Microsoft Sentinel enabled; daily ingestion cap not set; default retention period of 30 days applied to all tables.

## Symptoms
- Microsoft Sentinel workspace shows 'Daily cap reached' warning in Azure Monitor
- Security events from critical sources (e.g., Windows Event Logs, Azure AD Sign-in logs) are missing from recent queries
- Billing reports indicate unexpected cost spikes

## Error Codes
N/A

## Root Causes
1. No daily ingestion cap configured on the Log Analytics workspace
2. Retention period set to default (30 days) for all tables, including high-volume non-critical tables

## Remediation Steps
1. 1. In the Azure portal, navigate to your Log Analytics workspace, select 'Usage and estimated costs', then 'Daily cap'. Set a daily cap value (e.g., 100 GB) and enable 'Set daily cap'.
2. 2. Configure retention for individual tables: In the workspace, go to 'Tables', select a high-volume table (e.g., 'ContainerLog'), and set its retention period to a shorter value (e.g., 7 days) while keeping critical tables (e.g., 'SecurityEvent', 'SigninLogs') at the required retention (e.g., 90 days).
3. 3. Create an Azure Monitor alert rule to notify when the daily cap is reached or when ingestion approaches the cap (e.g., 80% threshold).

## Validation
Verify that the daily cap is set by running the Azure CLI command: `az monitor log-analytics workspace show --resource-group <rg> --workspace-name <ws> --query dailyQuotaGb`. Confirm retention settings per table using: `az monitor log-analytics workspace table show --resource-group <rg> --workspace-name <ws> --table-name <table> --query retentionInDays`.

## Rollback
To remove the daily cap, set the daily cap value to 0 (unlimited) in the Azure portal or via CLI: `az monitor log-analytics workspace update --resource-group <rg> --workspace-name <ws> --daily-quota-gb 0`. To revert retention for a table, set its retention back to the default (30 days) or the previous value.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/logs/daily-cap>
- <https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive>
