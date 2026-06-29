# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I connect Microsoft Defender XDR to Microsoft Sentinel to synchronize incidents and alerts?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Microsoft Defender XDR license

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In Microsoft Sentinel, select Data connectors.
2. Select Microsoft Defender XDR from the gallery and Open connector page.
3. In the Configuration section, select Connect incidents and alerts to enable basic integration between Microsoft Defender XDR and Microsoft Sentinel, synchronizing incidents and their alerts between the two platforms.

## Validation
1. In Microsoft Sentinel, navigate to Data connectors and select Microsoft Defender XDR. Confirm the connector status shows 'Connected'. 2. In the connector page, under Configuration, verify 'Connect incidents and alerts' is toggled to 'Enabled'. 3. Use Log Analytics: run `Microsoft365DefenderIncident | take 10` to confirm incidents are flowing. 4. Check that alerts from Microsoft Defender XDR appear in Sentinel's Incidents blade.

## Rollback
1. In Microsoft Sentinel, go to Data connectors, select Microsoft Defender XDR, and open the connector page. 2. Under Configuration, toggle 'Connect incidents and alerts' to 'Disabled'. 3. Confirm the connector status changes to 'Disconnected'. 4. Optionally, delete the connector by selecting 'Delete' on the connector page.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
