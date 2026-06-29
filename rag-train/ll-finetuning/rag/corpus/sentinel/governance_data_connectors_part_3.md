# Governance: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Governance

## Scenario / Query
A Microsoft Sentinel workspace is ingesting security events from multiple regions, but the organization has not configured diagnostic settings to send Azure Activity logs to Sentinel. How can an administrator verify that Activity log data is missing, and what is the documented method to enable the Azure Activity log connector?

## Environment Context
- **Tenant Type:** Enterprise (multi-region)
- **Configuration:** Sentinel workspace in East US; no Activity log connector deployed

## Symptoms
- No Azure Activity log entries appear in the Sentinel Logs workspace under the 'AzureActivity' table.
- The Sentinel Data Connectors blade shows the Azure Activity connector status as 'Not connected' or 'Disconnected'.

## Error Codes
N/A

## Root Causes
1. The Azure Activity log connector has not been deployed or configured in the Sentinel workspace.
2. Diagnostic settings for the subscription(s) are not sending Activity logs to the Sentinel Log Analytics workspace.

## Remediation Steps
1. In the Azure portal, navigate to Microsoft Sentinel > Data connectors > Azure Activity.
2. Select the connector and click 'Open connector page'.
3. Follow the documented steps under the 'Instructions' tab to configure diagnostic settings for the subscription(s) to stream Activity logs to the Log Analytics workspace used by Sentinel.
4. Alternatively, use the Azure Policy 'Deploy Diagnostic Settings for Activity Log to Log Analytics workspace' initiative to enforce the configuration at scale.

## Validation
After configuration, run the following KQL query in Sentinel Logs: 'AzureActivity | take 10'. If results appear, the connector is working.

## Rollback
Remove the diagnostic setting for the subscription(s) that sends Activity logs to the Sentinel workspace, or disable the Azure Activity connector in the Data connectors blade.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-activity>
