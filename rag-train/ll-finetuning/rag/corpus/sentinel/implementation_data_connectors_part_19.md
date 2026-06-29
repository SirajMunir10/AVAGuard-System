# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I connect Microsoft 365 Defender to Microsoft Sentinel and query advanced hunting tables in Log Analytics?

## Environment Context
- **Tenant Type:** Azure tenant with Microsoft Sentinel workspace
- **Configuration:** Microsoft 365 Defender connector enabled in Sentinel

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Apply Changes
2. To run a query in the advanced hunting tables in Log Analytics, enter the table name in the query window

## Validation
1. In the Microsoft Sentinel workspace, navigate to Data connectors and confirm the Microsoft 365 Defender connector shows a status of 'Connected' and the 'Data received' graph shows recent activity.
2. Open the Logs blade in the Sentinel workspace and run a sample query against an advanced hunting table, e.g.:
   EmailEvents
   | take 10
   Ensure results are returned without errors.
3. Verify that the 'Microsoft 365 Defender' data connector is listed under 'Data connectors' with a green check mark and the 'Last data received' timestamp is within the last hour.

## Rollback
1. In the Microsoft Sentinel workspace, navigate to Data connectors, select the Microsoft 365 Defender connector, and click 'Disconnect' or 'Remove connector' to disable the integration.
2. Confirm the connector status changes to 'Disconnected' and no data is being ingested from Microsoft 365 Defender.
3. If the connector was previously configured with a specific data collection rule or permissions, revert those changes by removing any custom role assignments or policies added for the connector.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
