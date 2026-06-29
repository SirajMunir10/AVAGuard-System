# Optimization: Data Collection

**Domain:** Sentinel
**Subdomain:** Data Collection
**Incident Type:** Optimization

## Scenario / Query
How can I reduce the volume of security events ingested into Microsoft Sentinel by filtering out informational and benign events from Windows Event Log sources, while still retaining critical security events?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Windows Security Events connector configured with 'All Events' ingestion

## Symptoms
- High daily ingestion cost for Sentinel
- Large number of low-severity events (e.g., Event ID 4688 with process name 'svchost.exe')
- Sentinel workspace approaching or exceeding budgeted data volume

## Error Codes
N/A

## Root Causes
1. Windows Security Events connector is set to stream 'All Events' instead of using a filtered event collection
2. No event filtering or exclusion rules applied in the connector configuration

## Remediation Steps
1. 1. In the Azure portal, navigate to your Sentinel workspace and select 'Data connectors'.
2. 2. Open the 'Windows Security Events via AMA' connector and click 'Open connector page'.
3. 3. Under 'Configuration', select 'Create data collection rule' or edit an existing rule.
4. 4. In the 'Collect events' step, choose 'Common Security Events' instead of 'All Events' to reduce noise.
5. 5. Optionally, create a custom XPath query to exclude specific event IDs (e.g., exclude Event ID 4688 for certain processes) as documented in 'Filter events using XPath queries'.
6. 6. Save the data collection rule and verify that ingestion volume decreases.

## Validation
Run the following KQL query in Sentinel to confirm reduction in low-severity event ingestion:
  SecurityEvent
  | where TimeGenerated > ago(24h)
  | summarize Count = count() by EventID
  | order by Count desc

## Rollback
Reconfigure the data collection rule to use 'All Events' or remove custom XPath filters to restore previous ingestion behavior.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/agents/data-collection-rule-edit#filter-events-using-xpath-queries>
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-windows-security-events?tabs=AMA#configure-the-data-connector>
