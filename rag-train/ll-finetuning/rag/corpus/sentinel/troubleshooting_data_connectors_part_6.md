# Troubleshooting: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Sentinel customer has enabled the Azure Activity connector, but no Activity logs appear in the Sentinel Logs workspace under the AzureActivity table. The connector status shows 'Connected'. What are the most common causes and how do you resolve this?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with multiple subscriptions)
- **Configuration:** Azure Activity data connector enabled in Sentinel; diagnostic settings may or may not be configured on the subscription

## Symptoms
- AzureActivity table in Log Analytics workspace is empty or missing expected entries
- Connector status in Sentinel shows 'Connected' but no data ingestion
- No errors or warnings visible in the connector blade

## Error Codes
N/A

## Root Causes
1. Diagnostic settings not configured on the subscription to stream Activity logs to the Log Analytics workspace used by Sentinel
2. The user or service principal used to configure the connector lacks required permissions (e.g., Reader role on the subscription)
3. Data collection rule or workspace key mismatch

## Remediation Steps
1. Verify that diagnostic settings are enabled on the subscription: In Azure portal, navigate to Monitor > Activity log > Export Activity Logs, and ensure a diagnostic setting streams to the correct Log Analytics workspace.
2. Confirm the Sentinel connectorâ€™s identity has at least Reader permissions on the subscription(s) being monitored. If using a managed identity, assign the Reader role at the subscription scope.
3. If diagnostic settings are already configured, check the workspaceâ€™s data ingestion logs for throttling or filtering. Use the following KQL query: `AzureActivity | where TimeGenerated > ago(1h) | summarize count()` to confirm data presence.
4. Re-run the connector health check from the Sentinel Data Connectors blade and review any warnings.

## Validation
After remediation, run the query `AzureActivity | take 10` in the Sentinel Logs workspace. If rows appear, the connector is working.

## Rollback
If diagnostic settings were misconfigured, remove the incorrect diagnostic setting and re-create it with the correct workspace ID.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/troubleshoot-azure-activity-log-data-connector>
