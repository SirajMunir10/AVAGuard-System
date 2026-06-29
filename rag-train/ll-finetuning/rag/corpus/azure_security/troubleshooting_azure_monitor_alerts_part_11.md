# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
A fired alert is visible in the Azure portal but its configured action (webhook, Azure function, or logic app) did not trigger. How do I troubleshoot this?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure Monitor alerts with action groups

## Symptoms
- Fired alert visible in portal
- Configured action did not trigger

## Error Codes
N/A

## Root Causes
1. Action suppressed by an alert processing rule
2. Webhook source IP address blocked by firewall
3. Webhook endpoint not working correctly
4. Incorrect format for calling Slack or Microsoft Teams
5. Webhook became unresponsive or returned errors

## Remediation Steps
1. Click on the fired alert in the portal and look at the history tab for suppressed action groups. If unintentional, modify, disable, or delete the alert processing rule.
2. Add the IP addresses that the webhook is called from to your allow list.
3. Verify that the webhook endpoint you configured is correct and that the endpoint is working correctly. Check your webhook logs or instrument its code to investigate (e.g., log the incoming payload).
4. Follow instructions to configure a logic app action instead for Slack or Microsoft Teams.
5. After retries attempted to call the webhook fail, no action group calls the endpoint for 15 minutes.

## Validation
1. In the Azure portal, navigate to Monitor > Alerts, select the fired alert, and review the History tab to confirm no action groups were suppressed. 2. Verify that the webhook endpoint is reachable by running a test from a machine with the same source IP as Azure Monitor (see https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot for IP ranges). 3. Check the webhook endpoint logs to confirm it received the payload and returned a 200 OK. 4. For Slack/Teams, confirm the logic app action is configured per Microsoft guidance. 5. Wait at least 15 minutes after the last retry and verify no further failures.

## Rollback
1. If an alert processing rule was modified or deleted, restore the original rule configuration from backup or recreate it. 2. If firewall allow list was changed, remove the added IP addresses. 3. If webhook endpoint was changed, revert to the original URL. 4. If logic app action was added for Slack/Teams, remove it and revert to the original webhook configuration. 5. If no changes were made, no rollback is needed.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
