# Optimization: Cost Management

**Domain:** Sentinel
**Subdomain:** Cost Management
**Incident Type:** Optimization

## Scenario / Query
A customer notices that their Microsoft Sentinel bill has increased unexpectedly. They have many analytics rules that run frequent queries on large volumes of historical data. How can they optimize their Sentinel costs by adjusting data retention and analytics rule schedules?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Sentinel workspace with Pay-as-you-go pricing tier, multiple analytics rules running every 5 minutes on 90-day retention data

## Symptoms
- Monthly Azure bill shows higher-than-expected charges for Log Analytics data ingestion and retention
- Sentinel Cost Management workbook displays high ingestion volume from SecurityEvent and CommonSecurityLog tables

## Error Codes
N/A

## Root Causes
1. Analytics rules are scheduled too frequently (every 5 minutes) for large data sets
2. Data retention period is set longer than necessary for security use cases
3. Inefficient KQL queries that scan entire tables instead of using time filters

## Remediation Steps
1. Review and adjust analytics rule run frequency: for rules that do not require near-real-time detection, increase the run interval to 1 hour or more
2. Set appropriate data retention periods: use the 'Retention' setting in Log Analytics workspace to reduce retention for tables that do not need long-term storage (e.g., set SecurityEvent to 30 days if not required for compliance)
3. Optimize KQL queries: add time range filters (e.g., 'where TimeGenerated > ago(1h)') to reduce the amount of data scanned per query
4. Use the 'Sentinel Cost Management' workbook to identify high-cost tables and rules, then apply the above changes

## Validation
After implementing changes, monitor the Cost Management workbook for a full billing cycle to confirm cost reduction.

## Rollback
Revert any changed analytics rule schedules to their original frequency and restore previous retention settings via the Log Analytics workspace 'Retention' blade.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/billing-cost-management>
