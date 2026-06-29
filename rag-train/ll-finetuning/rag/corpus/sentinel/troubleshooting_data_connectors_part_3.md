# Troubleshooting: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Sentinel workspace shows no data ingestion from the Azure Activity connector, even though the connector is enabled and the subscription is correctly selected. What are the steps to diagnose and resolve this issue?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with multiple subscriptions)
- **Configuration:** Azure Activity data connector enabled in Microsoft Sentinel, diagnostics settings configured to stream Activity logs to Log Analytics workspace

## Symptoms
- Azure Activity connector shows 'Connected' but no data appears in the workspace
- No AzureActivity records in the Log Analytics workspace for the past 24 hours
- Diagnostic settings for the subscription appear to be present but not sending data

## Error Codes
N/A

## Root Causes
1. Diagnostic settings may be misconfigured or pointing to the wrong Log Analytics workspace
2. The subscription may have been moved or renamed after the connector was configured
3. The Azure Activity connector may require re-authentication or re-deployment of the policy

## Remediation Steps
1. 1. Verify that the subscription used in the connector is the same as the one with diagnostic settings configured. In the Azure portal, navigate to Monitor > Activity Log > Export Activity Logs and confirm the diagnostic setting is sending to the correct Log Analytics workspace.
2. 2. If the diagnostic setting is missing or incorrect, create a new diagnostic setting for the subscription: select 'Send to Log Analytics workspace' and choose the same workspace that Microsoft Sentinel is using.
3. 3. In Microsoft Sentinel, go to Data connectors > Azure Activity, click 'Open connector page', and then click 'Connect' to re-establish the connection. If prompted, select the appropriate subscription.
4. 4. Wait up to 30 minutes for data to appear, then run the following KQL query in the workspace: AzureActivity | take 10
5. 5. If data still does not appear, check the workspace's data ingestion status: in the Log Analytics workspace, go to 'Usage and estimated costs' and verify that data is being received from the AzureActivity table.

## Validation
After following the remediation steps, run the query 'AzureActivity | where TimeGenerated > ago(1h) | count' in the Microsoft Sentinel Logs blade. A non-zero count confirms data ingestion is restored.

## Rollback
If the diagnostic setting was modified, revert to the previous setting by deleting the new diagnostic setting and re-creating the original one. If the connector was reconnected, no rollback is needed as the connector state is idempotent.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/troubleshoot-azure-activity-log-data-connector>
