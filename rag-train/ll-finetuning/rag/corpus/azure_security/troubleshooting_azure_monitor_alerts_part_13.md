# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
Why did I receive a notification for an alert (such as an email or SMS) more than once, or why was the alert's action (such as webhook or Azure function) triggered multiple times?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Received notification for an alert (such as an email or SMS) more than once
- Alert's action (such as webhook or Azure function) was triggered multiple times

## Error Codes
N/A

## Root Causes
1. Multiple similar alerts are fired at around the same time, e.g., an activity log alert rule configured to fire both when an event starts and finishes (succeeded or failed) by not filtering on the event status field
2. In Log search alerts when dimensions are defined, all dimension combinations are checked, which can result in similar alerts
3. An action (such as an email address) appears in multiple triggered action groups, and each action group is processed independently

## Remediation Steps
1. Examine the alert details, such as its timestamp and either the alert ID or its correlation ID, to check if actions or notifications came from different alerts
2. Check the list of fired alerts in the portal
3. If multiple similar alerts are the cause, adapt the alert rule logic or otherwise configure the alert source
4. Check the alert history tab to see which action groups were triggered, including action groups defined in the alert rule and action groups added by alert processing rules

## Validation
1. In the Azure portal, navigate to Monitor > Alerts. 2. Review the list of fired alerts for the time period in question. 3. For each alert, examine the timestamp, alert ID, and correlation ID to determine if multiple distinct alerts fired. 4. Select a specific alert and go to its History tab to see which action groups were triggered (both those defined in the alert rule and those added by alert processing rules). 5. If using a log search alert with dimensions, verify whether multiple dimension combinations produced separate alerts. 6. Check if the same email address or webhook endpoint appears in more than one action group that was triggered.

## Rollback
1. If the issue is caused by an activity log alert rule that fires on both start and finish events, modify the rule to filter on a specific event status (e.g., only 'Succeeded' or 'Failed'). 2. If the issue is due to log search alert dimensions, adjust the dimension configuration or aggregation to reduce duplicate alerts. 3. If the same action appears in multiple action groups, remove the duplicate action from one of the action groups or consolidate the action groups. 4. If alert processing rules are adding duplicate action groups, update or disable those processing rules. 5. After making changes, monitor the alert history to confirm that duplicate notifications no longer occur.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
