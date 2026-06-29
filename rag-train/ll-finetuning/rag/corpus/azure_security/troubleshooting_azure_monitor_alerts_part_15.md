# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot unexpected alert payload format in Azure Monitor action groups?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Alert action (webhook, function, logic app) receives payload in unexpected format
- Code that responds to alerts fails due to format mismatch

## Error Codes
N/A

## Root Causes
1. Action group action format specified as default legacy format instead of common schema format, or vice versa
2. Different actions in the same action group may have different formats
3. Format specified at the action level does not match what the receiver expects

## Remediation Steps
1. Check the format specified at the action level for each action in the action group
2. Verify the payload format (JSON) for activity log alerts, log search alerts (both Application Insights and log analytics), metric alerts, and the common alert schema
3. Use a webhook action to send the payload to your IP to see the result

## Validation
1. Navigate to the Azure portal, go to Monitor > Alerts > Action groups. Select the action group in question. For each action (webhook, function, logic app), check the 'Common alert schema' toggle under the action details. Confirm whether it is enabled or disabled as expected. 2. Use a test webhook action to send a sample alert payload to a request bin (e.g., https://webhook.site) or a custom endpoint that captures the payload. Trigger a test alert (e.g., a metric alert or log alert) and inspect the received JSON payload. Verify that the payload matches the expected format (common schema or legacy schema) based on the action's configuration. 3. For activity log alerts, log search alerts (Application Insights and Log Analytics), and metric alerts, review the respective alert rule's payload documentation at https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot to confirm the expected JSON structure matches what the receiver is coded to parse.

## Rollback
1. If the validation reveals an incorrect format, edit the action group: for each action that needs to change, toggle the 'Common alert schema' setting to the opposite state (enable if it was disabled, disable if it was enabled). 2. If the receiver code expects a specific schema, update the receiver code to handle the format that the action group is configured to send, rather than changing the action group. 3. After making changes, repeat the validation steps to confirm the payload format now matches expectations. If issues persist, revert the action group configuration to its previous state by toggling the 'Common alert schema' back, and update the receiver code to handle the original format.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
