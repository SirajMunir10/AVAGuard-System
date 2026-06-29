# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Sentinel, I configured the Azure Activity connector to ingest subscription-level logs. However, after 24 hours, no Activity logs appear in the Log Analytics workspace. The connector shows as 'Connected' but no data is flowing. What could be wrong and how do I fix it?

## Environment Context
- **Tenant Type:** Enterprise (single tenant, multiple subscriptions)
- **Configuration:** Azure Activity log connector enabled on a Log Analytics workspace in the same region as the subscription; diagnostic settings may not be properly configured.

## Symptoms
- Azure Activity connector shows status 'Connected' in Sentinel Data connectors blade
- No records of type 'AzureActivity' appear in the Log Analytics workspace for over 24 hours
- Diagnostic settings blade for the subscription shows no diagnostic setting sending Activity logs to the Sentinel workspace

## Error Codes
N/A

## Root Causes
1. The Azure Activity log connector requires a diagnostic setting on the subscription to export Activity logs to the Log Analytics workspace. If the diagnostic setting is missing or misconfigured, no data flows even though the connector appears connected.
2. The connector in Sentinel only creates the data collection rule and permissions; it does not automatically create the diagnostic setting in older deployments or when the connector is re-enabled after a workspace move.

## Remediation Steps
1. Navigate to Monitor > Activity log > Export Activity Logs in the Azure portal.
2. Click 'Add diagnostic setting' and provide a name (e.g., 'Sentinel-Activity').
3. Under 'Category details', select 'Administrative', 'Security', 'ServiceHealth', 'Alert', 'Recommendation', 'Policy', and 'Autoscale' as needed.
4. Under 'Destination details', select 'Send to Log Analytics workspace' and choose the same workspace where Sentinel is enabled.
5. Click 'Save'. Activity logs should begin flowing within 15 minutes.
6. Alternatively, use the following Azure PowerShell command (documented by Microsoft):
   Set-AzDiagnosticSetting -Name 'Sentinel-Activity' -ResourceId '/subscriptions/<subscription-id>' -WorkspaceId '<workspace-resource-id>' -Category 'Administrative', 'Security', 'ServiceHealth', 'Alert', 'Recommendation', 'Policy', 'Autoscale' -Enabled $true

## Validation
Run the following KQL query in the Sentinel workspace:
  AzureActivity
  | where TimeGenerated > ago(1h)
  | count
If the count is greater than 0, data is flowing. Also verify the diagnostic setting exists under Monitor > Activity log > Export Activity Logs.

## Rollback
Delete the diagnostic setting created for the subscription under Monitor > Activity log > Export Activity Logs. The Sentinel connector will remain but no data will be ingested.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-activity>
