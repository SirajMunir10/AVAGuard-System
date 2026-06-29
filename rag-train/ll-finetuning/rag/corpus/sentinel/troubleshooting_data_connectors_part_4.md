# Troubleshooting: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Sentinel customer has enabled the Azure Activity connector, but no Activity logs appear in the Log Analytics workspace after 24 hours. What are the most common causes and how do you resolve them?

## Environment Context
- **Tenant Type:** Azure AD tenant with Azure subscription
- **Configuration:** Azure Activity data connector enabled in Sentinel; Log Analytics workspace in same region as subscription; diagnostic settings may be missing or misconfigured

## Symptoms
- Azure Activity connector shows 'Connected' but no data ingested
- No AzureActivity table in Log Analytics workspace
- Usage and estimated costs show zero ingestion for Azure Activity

## Error Codes
N/A

## Root Causes
1. Diagnostic settings not configured on the Azure subscription to stream Activity logs to the Log Analytics workspace
2. Insufficient permissions to create or modify diagnostic settings (requires Owner or Contributor on the subscription)
3. Log Analytics workspace is in a different region than the subscription (not supported for Activity logs)
4. Data collection rule or connector was not fully deployed after initial enablement

## Remediation Steps
1. Verify that diagnostic settings exist on the Azure subscription: navigate to Monitor > Activity log > Export Activity Logs, and ensure a diagnostic setting sends 'Administrative', 'Security', 'ServiceHealth', 'Alert', 'Recommendation', 'Policy', and 'Autoscale' categories to the Sentinel workspace.
2. If missing, create a new diagnostic setting with the required categories and select 'Send to Log Analytics workspace'.
3. Confirm the workspace is in the same region as the subscription (Activity logs cannot be sent cross-region).
4. Ensure the user configuring the connector has at least Contributor permissions on the subscription.
5. After configuring diagnostic settings, wait up to 30 minutes for data to appear in the AzureActivity table.

## Validation
Run the following KQL query in Sentinel: `AzureActivity | take 10`. If results appear, ingestion is working. Also check the connector health blade for any error messages.

## Rollback
To disable the connector, remove the diagnostic setting from the subscription. In Sentinel, disable the Azure Activity data connector.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/troubleshoot-activity-log-connector>
