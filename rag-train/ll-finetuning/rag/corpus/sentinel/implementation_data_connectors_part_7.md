# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I add data connectors to Microsoft Sentinel using solutions from the Content Hub?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Microsoft Sentinel Data connectors page.
2. To add more data connectors, install the solution associated with the data connector from the Content Hub.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace and select 'Data connectors' under Configuration.
2. Verify that the newly installed solution's data connector appears in the list with a green check mark and a status of 'Connected'.
3. Confirm that data ingestion is occurring by checking the 'Received data' graph for the connector over the last 24 hours.
4. Optionally, run a sample query in Log Analytics (e.g., for the connector's table) to ensure logs are flowing.

## Rollback
1. In the Azure portal, go to Microsoft Sentinel > Content hub.
2. Find the solution you installed and select 'Manage' or 'Uninstall' to remove it.
3. Confirm removal when prompted.
4. Return to the Data connectors page to verify the connector is no longer listed.
5. If the connector was previously configured, delete its data connector resource from the Data connectors page by selecting it and choosing 'Delete'.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources>
