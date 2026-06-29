# Troubleshooting: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Troubleshooting

## Scenario / Query
How do I find support for a Microsoft Sentinel data connector that has no listed contacts?

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
1. Identify the data connector as community-supported on the data connector page in Microsoft Sentinel.
2. File an issue in the Microsoft Sentinel GitHub community for questions or issues.

## Validation
1. Navigate to the Microsoft Sentinel workspace in the Azure portal. 2. Go to the 'Data connectors' page. 3. Locate the specific data connector in the list. 4. Confirm that the connector's details page shows it is labeled as 'Community-supported' and that no support contacts are listed. 5. Verify that the connector is connected and ingesting data as expected by checking the 'Data received' graph or running a sample query (e.g., `YourConnectorName_CL | take 10`).

## Rollback
1. If the connector is not functioning after remediation, revert to the previous working state by disconnecting and reconnecting the data connector using the connector page in the Azure portal. 2. If the GitHub issue filed causes unintended changes, close the issue and remove any associated configuration changes. 3. Restore any custom data collection rules or policies that were modified by reapplying the previous version from backup or source control.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources>
