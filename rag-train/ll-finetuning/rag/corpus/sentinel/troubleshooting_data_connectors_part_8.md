# Troubleshooting: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Troubleshooting

## Scenario / Query
Why do queries on Defender Vulnerability Management (TVM) tables like DeviceTvmSoftwareInventory and DeviceTvmSoftwareVulnerabilities return no results in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Microsoft 365 Defender connector

## Symptoms
- TVM queries accepted by query editor but return no results

## Error Codes
N/A

## Root Causes
1. Microsoft Sentinel does not ingest TVM data into the workspace.

## Remediation Steps
1. Run TVM queries in Defender XDR Advanced Hunting where the data is available.
2. To use TVM data in Microsoft Sentinel, build a custom ingestion path.

## Validation
1. Open the Microsoft Sentinel workspace in the Azure portal. 2. Navigate to Logs and run a sample query: DeviceTvmSoftwareInventory | take 10. Confirm the query returns no results. 3. Open the Microsoft 365 Defender portal (security.microsoft.com). 4. Go to Advanced Hunting and run the same query: DeviceTvmSoftwareInventory | take 10. Confirm results are returned. 5. Verify that the Microsoft 365 Defender connector in Sentinel is enabled and shows no data ingestion errors by checking Sentinel > Data connectors > Microsoft 365 Defender > Status.

## Rollback
1. If the validation confirms TVM data is not in Sentinel, no rollback is needed as no changes were made to the environment. 2. If a custom ingestion path was attempted and caused issues, disable or remove the custom data collection rule or pipeline. 3. Revert any changes to the Microsoft 365 Defender connector configuration by resetting it to default settings via the connector page in Sentinel. 4. Confirm that no other data connectors or Sentinel features are impacted by reviewing the connector status and data ingestion logs.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
