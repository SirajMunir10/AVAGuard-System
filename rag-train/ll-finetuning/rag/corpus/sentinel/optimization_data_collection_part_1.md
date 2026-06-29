# Optimization: Data Collection

**Domain:** Sentinel
**Subdomain:** Data Collection
**Incident Type:** Optimization

## Scenario / Query
A security operations team notices that Microsoft Sentinel ingestion costs are higher than expected. They want to identify which tables consume the most data and whether any tables are being billed unnecessarily. How can they use the built-in Sentinel Usage and Cost workbook to analyze ingestion by table and optimize their data collection?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with multiple data connectors enabled, including Windows Security Events via AMA, Office 365, and Azure Activity logs.

## Symptoms
- Monthly Azure bill shows higher than anticipated Log Analytics ingestion charges
- Sentinel Usage and Cost workbook displays unexpected data volumes in tables such as SecurityEvent, OfficeActivity, and AzureDiagnostics
- Security team suspects that some high-volume tables are not needed for detection use cases

## Error Codes
N/A

## Root Causes
1. Data collection rules may be sending verbose logs (e.g., all Windows Event IDs) instead of filtered events
2. Office 365 connector may be ingesting all workloads (Exchange, SharePoint, Teams) when only a subset is needed
3. Legacy diagnostic settings may be routing verbose Azure resource logs to the Sentinel workspace

## Remediation Steps
1. Open the Sentinel Usage and Cost workbook from the Microsoft Sentinel > Threat Management > Workbooks blade
2. Review the 'Data Ingestion by Table' chart to identify the top 5 tables by volume
3. For high-volume security event tables, modify the Data Collection Rule (DCR) to collect only required event IDs (e.g., 4624, 4625) using the XPath query filter documented in 'Filter Windows security events using XPath'
4. For Office 365, reconfigure the connector to disable unnecessary workloads (e.g., disable Teams if not monitored) via the connector settings
5. For Azure resource logs, review and update diagnostic settings to exclude verbose categories (e.g., 'AuditEvent' for Key Vault) and route only required categories to Sentinel
6. Consider setting a daily ingestion cap on the Log Analytics workspace to prevent cost overruns (note: this may cause data loss)

## Validation
After changes, monitor the Sentinel Usage and Cost workbook over the next 48 hours to confirm a reduction in ingestion volume for the targeted tables.

## Rollback
If ingestion drops too low and detections miss events, revert the DCR XPath filter to a broader set, re-enable disabled Office 365 workloads, or add back the excluded diagnostic categories.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/usage-and-cost-workbook>
- <https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-overview>
