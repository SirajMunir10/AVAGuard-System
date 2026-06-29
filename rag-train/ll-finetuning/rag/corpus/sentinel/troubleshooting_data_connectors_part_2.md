# Troubleshooting: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Troubleshooting

## Scenario / Query
Why are no security events appearing in Microsoft Sentinel after configuring the Windows Security Events via AMA connector, and how do I resolve this?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Windows Security Events via AMA connector configured on a Windows Server 2019, Azure Monitor Agent installed, Data Collection Rule (DCR) linked to the Log Analytics workspace used by Sentinel.

## Symptoms
- No SecurityEvent table data in the Sentinel Logs workspace for over 2 hours after connector setup.
- Connector health page shows 'Data collection is healthy' but no events ingested.
- Azure Monitor Agent (AMA) is running on the source server.

## Error Codes
N/A

## Root Causes
1. The Data Collection Rule (DCR) does not include the necessary XPath query to collect security events (e.g., Event ID 4624, 4625).
2. The DCR may be missing the 'Security' event log stream definition for Windows Security Events.

## Remediation Steps
1. 1. Navigate to the Data Collection Rule in the Azure portal.
2. 2. Under 'Resources', verify the target virtual machine is listed.
3. 3. Under 'Collect and deliver', select 'Add data source'.
4. 4. Choose 'Windows Event Log' as the data source type.
5. 5. In the 'Minimum log level' dropdown, select 'Security' and specify the desired event IDs (e.g., 4624, 4625) or use the default 'All Security Events' option.
6. 6. Ensure the 'Destination' is set to the Log Analytics workspace used by Sentinel.
7. 7. Save the DCR and wait up to 10 minutes for data to appear.
8. 8. Verify ingestion by running the following KQL query in Sentinel: `SecurityEvent | take 10`.

## Validation
Run `SecurityEvent | where TimeGenerated > ago(1h) | count` in Sentinel Logs. A non-zero count confirms successful data ingestion.

## Rollback
Remove the Windows Event Log data source from the DCR or set the minimum log level to 'None' to stop collection.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/troubleshoot-windows-security-events-connector>
