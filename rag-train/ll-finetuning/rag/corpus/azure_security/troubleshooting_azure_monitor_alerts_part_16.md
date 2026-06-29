# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
An alert processing rule is not working as expected; how do I troubleshoot why it didn't process a fired alert?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- A fired alert is visible in the portal, but the related alert processing rule did not work as expected

## Error Codes
N/A

## Root Causes
1. The alert processing rule may not be enabled
2. The alert may be a service health alert, which is not affected by alert processing rules
3. The alert processing rule scope or filter conditions may not match the fired alert

## Remediation Steps
1. Check the alert processing rule status field to verify that the related action role is enabled. By default, the portal only shows alert rules that are enabled, but you can change the filter to show all rules. If it isn't enabled, you can enable the alert processing rule by selecting it and clicking Enable.
2. Select the fired alert in the portal, and look at the History tab to see if the alert processing rule was processed.
3. Carefully examine the alert processing rule scope and filter conditions and compare them to the properties of the fired alert.

## Validation
1. In the Azure portal, navigate to Monitor > Alerts > Alert processing rules. Verify the rule is listed with Status = 'Enabled'. If not, change the filter from 'Enabled' to 'All' to confirm. 2. Select the fired alert in Monitor > Alerts, then click its History tab. Confirm that the alert processing rule appears in the history with a status indicating it was processed (e.g., 'Suppressed' or 'Action group modified'). 3. Compare the scope (resource group, resource type, resource) and filter conditions (severity, monitor condition, etc.) of the alert processing rule against the properties of the fired alert (e.g., resource ID, severity, signal type). Ensure they match.

## Rollback
1. If the alert processing rule was incorrectly enabled, select it and click Disable. 2. If the rule’s scope or filters were changed incorrectly, revert them to the previous values (e.g., restore original resource scope or filter conditions). 3. If the rule was deleted, recreate it using the original configuration (scope, filters, and action). 4. If no changes were made, no rollback is needed.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
