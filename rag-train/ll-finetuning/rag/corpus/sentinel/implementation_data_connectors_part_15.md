# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I collect raw advanced hunting events from Defender components into Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Microsoft Defender XDR

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In Microsoft Sentinel, select Data connectors.
2. Select Microsoft Defender XDR from the gallery and Open connector page.
3. In the Configuration section, select Connect events to enable the collection of raw advanced hunting events from Defender components.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Content management', select 'Data connectors'. 3. Locate and select 'Microsoft Defender XDR' from the list. 4. On the connector page, verify that the status shows 'Connected'. 5. In the 'Configuration' section, confirm that the toggle for 'Connect events' is enabled. 6. Use the following KQL query in the Sentinel Logs workspace to verify raw advanced hunting events are being ingested: `MicrosoftThreatProtection_* | take 10`. 7. Check the 'Data connectors' page for the 'Microsoft Defender XDR' connector to see if data ingestion is active (e.g., last data received timestamp).

## Rollback
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Content management', select 'Data connectors'. 3. Locate and select 'Microsoft Defender XDR' from the list. 4. On the connector page, in the 'Configuration' section, disable the 'Connect events' toggle to stop the collection of raw advanced hunting events. 5. If the connector was previously disconnected, you may also select 'Disconnect' to fully remove the data connection. 6. Verify the change by checking that the connector status shows 'Disconnected' and that no new MicrosoftThreatProtection_* events appear in the Logs workspace.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
