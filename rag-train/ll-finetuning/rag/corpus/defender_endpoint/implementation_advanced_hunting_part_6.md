# Implementation: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Implementation

## Scenario / Query
How to extend data retention beyond 30 days for advanced hunting using streaming APIs?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Streaming API enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. See the following resources: Microsoft Defender XDR Streaming API
2. See the following resources: Microsoft Defender for Endpoint Raw Data Streaming API

## Validation
1. Verify that the streaming API is configured: Run the PowerShell command `Get-MpPreference | Select-Object -ExpandProperty CloudBlockLevel` to confirm Defender for Endpoint is active. 2. Check the streaming API export status: Use the Microsoft 365 Defender portal, navigate to Settings > Microsoft 365 Defender > Streaming API, and confirm that at least one export rule is enabled and set to export to Azure Event Hubs or Azure Storage. 3. Validate data is flowing: In the Azure portal, navigate to the configured Event Hubs namespace or Storage account, and verify that recent data (e.g., within the last hour) is present in the corresponding container or event hub. 4. Confirm retention duration: For Azure Storage, check the 'Change feed' or 'Blob properties' to ensure data is retained beyond 30 days (e.g., set a lifecycle management policy for 365 days). For Event Hubs, verify the 'Message retention' setting is greater than 30 days (e.g., 7 days maximum; for longer retention, use Azure Storage export).

## Rollback
1. Disable the streaming API export rule: In the Microsoft 365 Defender portal, go to Settings > Microsoft 365 Defender > Streaming API, select the rule, and click 'Delete' or 'Disable'. 2. Remove any custom retention policies: In Azure Storage, delete any lifecycle management rules that were added to retain data beyond 30 days. 3. Reset Event Hubs retention: If Event Hubs message retention was increased, revert it to the default (1 day) or the previous value via the Azure portal or PowerShell: `Set-AzureRmEventHub -ResourceGroupName <ResourceGroup> -Namespace <Namespace> -EventHubName <EventHub> -MessageRetentionInDays <OriginalValue>`. 4. Verify no data is being exported: Run a test query in Advanced Hunting to confirm that data is no longer being streamed to external storage.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
