# Optimization: Data Collection

**Domain:** Sentinel
**Subdomain:** Data Collection
**Incident Type:** Optimization

## Scenario / Query
A Microsoft Sentinel workspace is ingesting more data than expected, causing high costs. How can I identify and reduce unnecessary data ingestion using built-in Sentinel optimization features?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Sentinel workspace with multiple data connectors and custom tables enabled

## Symptoms
- Monthly Azure bill for Log Analytics workspace exceeds budget
- Data ingestion rate higher than anticipated based on connected sources
- Sentinel Usage and Cost workbook shows unexpected spikes in specific tables

## Error Codes
N/A

## Root Causes
1. Unused or misconfigured data connectors sending excessive logs
2. Custom tables with verbose logging enabled unnecessarily
3. Lack of data retention and archiving policies for high-volume tables

## Remediation Steps
1. Review the Sentinel Usage and Cost workbook to identify top contributors to ingestion costs
2. Disable or reconfigure data connectors that are not needed or are sending excessive data
3. Set appropriate retention and archiving policies for tables with high ingestion volume
4. Use Basic Logs or Archive tier for tables where interactive analytics is not required

## Validation
After implementing changes, monitor the Usage and Cost workbook over a week to confirm reduced ingestion and cost.

## Rollback
Re-enable any disabled connectors and revert retention policies to previous values if cost reduction is insufficient or data gaps appear.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/optimize-costs>
