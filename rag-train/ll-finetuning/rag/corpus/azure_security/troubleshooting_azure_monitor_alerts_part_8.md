# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot email notifications not being sent from an action group in Azure Monitor?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Email notifications from an action group are not being sent

## Error Codes
N/A

## Root Causes
1. Accidentally unsubscribed from the action group
2. Exceeded service limits: email is rate limited to no more than 100 emails every hour to each email address

## Remediation Steps
1. Edit the action group in the portal and check the Status column
2. Search your email for the unsubscribe confirmation
3. To subscribe again, either use the link in the unsubscribe confirmation email you received, or remove the email address from the action group, and then add it back again
4. If rate limited, consider using a different action such as Webhook, Logic app, Azure function, or Automation runbooks (none of these actions are rate limited)

## Validation
1. In the Azure portal, navigate to Monitor > Alerts > Action groups, select the action group in question, and verify the 'Status' column shows 'Enabled' for the email action. 2. Check the email inbox for any unsubscribe confirmation messages from Azure Monitor. 3. If the email address was removed and re-added, confirm the action group now includes the correct email address and the status is 'Enabled'. 4. If rate limiting was suspected, verify that fewer than 100 emails have been sent to that address in the past hour by reviewing the action group's notification history or using Azure Monitor logs.

## Rollback
1. If the email address was removed and re-added but notifications still fail, re-add the original email address exactly as it was before. 2. If the action group was edited to change the email address, revert to the previous email address. 3. If a different action type (e.g., webhook, logic app) was configured as a workaround for rate limiting, remove that action and re-enable the original email action. 4. If the email address was accidentally unsubscribed and the unsubscribe link was used to resubscribe, but notifications still fail, remove the email address from the action group and add it back again.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
