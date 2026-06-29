# Optimization: Data Collection

**Domain:** Sentinel
**Subdomain:** Data Collection
**Incident Type:** Optimization

## Scenario / Query
A Microsoft Sentinel workspace is ingesting more data than expected, causing high costs. The customer wants to identify which tables or data connectors are responsible for the excess ingestion and then reduce unnecessary data collection.

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Sentinel workspace with multiple data connectors (e.g., Windows Security Events via AMA, Office 365, Azure Activity) and a pay-as-you-go pricing tier.

## Symptoms
- Monthly Azure bill shows higher-than-expected Sentinel data ingestion charges.
- Sentinel Usage and Cost workbook shows a sudden increase in daily GB ingested.
- Certain tables (e.g., SecurityEvent, CommonSecurityLog) show unusually high row counts.

## Error Codes
N/A

## Root Causes
1. Verbose logging enabled on security events (e.g., EventID 4688 with command line) without filtering.
2. Unused or misconfigured data connectors sending duplicate or irrelevant logs.
3. Lack of data collection rules (DCR) to filter out unnecessary events.

## Remediation Steps
1. 1. Open the Sentinel Usage and Cost workbook to identify top tables and connectors by data volume.
2. 2. For Windows Security Events via AMA, review the Data Collection Rule (DCR) and reduce the event collection level from 'All Events' to 'Common Events' or create a custom XPath filter to exclude verbose events (e.g., filter out EventID 4688 with specific conditions).
3. 3. Disable or reconfigure any data connector that is sending logs not required for security monitoring.
4. 4. Implement log retention policies: set shorter retention for high-volume, low-value tables (e.g., 30 days) and use long-term retention (Archived Logs) for compliance data.
5. 5. Monitor ingestion using the Sentinel Cost Management workbook and set budget alerts.

## Validation
After applying changes, verify in the Usage and Cost workbook that daily ingestion has decreased to the expected level and that no critical security events are missing.

## Rollback
Re-enable any disabled data connectors and revert DCR changes to the previous configuration. Restore retention policies to original values.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/billing?tabs=simplified>
- <https://learn.microsoft.com/en-us/azure/sentinel/usage-and-cost-workbook>
