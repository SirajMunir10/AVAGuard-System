# Optimization: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Microsoft Sentinel costs by identifying and disabling unused or low-value data connectors that are ingesting data without producing useful security insights?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with multiple data connectors enabled

## Symptoms
- High data ingestion costs without corresponding security value
- Data connectors showing zero or minimal alerts/incidents over 30 days
- Connectors ingesting data from sources that are no longer in use

## Error Codes
N/A

## Root Causes
1. Connectors enabled for legacy or decommissioned systems
2. No regular review of connector usage and value
3. Lack of cost monitoring tied to connector activity

## Remediation Steps
1. Review the 'Data connectors' blade in Microsoft Sentinel to identify connectors with zero or low alert generation over the past 30 days
2. Use the 'Usage and cost' workbook to analyze ingestion volume per connector
3. Disable or remove connectors that are not providing security value by selecting the connector and clicking 'Disconnect'
4. Document the change and update the connector management policy to include quarterly reviews

## Validation
Verify that the disabled connector no longer appears in the 'Data connectors' list as 'Connected' and that ingestion logs show no new data from that source.

## Rollback
Re-enable the connector by selecting it in the 'Data connectors' blade and clicking 'Connect' with the appropriate configuration.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/optimize-costs-data-connectors>
