# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
I didn't receive the expected SMS, voice call, or push notification for a fired alert in Azure Monitor.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- A fired alert is visible in the Azure portal, but the configured SMS, voice call, or push notification was not received.

## Error Codes
N/A

## Root Causes
1. Action was suppressed by an alert processing rule.
2. Phone number has typos in country code or phone number.
3. SMS or voice call rate limit exceeded (one notification every five minutes per phone number).
4. Accidentally unsubscribed from the action group via SMS reply (DISABLE or STOP).

## Remediation Steps
1. Click on the fired alert in the portal and look at the history tab for suppressed action groups. If unintentional, modify, disable, or delete the alert processing rule.
2. Check the SMS action for typos in the country code or phone number.
3. Voice call: check call history for a different call from Azure in the preceding five minutes. SMS: check SMS history for a message indicating rate limiting. If high-volume notifications are needed, consider using a different action such as Webhook, Logic app, Azure function, or Automation runbooks (none are rate limited).
4. If unsubscribed, send the relevant SMS command (ENABLE action_group_short_name or START) to subscribe again, or remove the SMS action from the action group and add it back.

## Validation
1. In the Azure portal, navigate to Monitor > Alerts and click the specific fired alert. Under the 'History' tab, verify that no action group is listed as 'Suppressed' due to an alert processing rule. 2. Confirm the SMS action's phone number in the action group is correct, including country code and no typos. 3. For SMS, check the phone's SMS history for a message from Azure indicating rate limiting (e.g., 'You have exceeded the rate limit'). For voice calls, check call history for a missed call from Azure within the last five minutes. 4. If the user previously replied with 'DISABLE' or 'STOP', verify that the action group's SMS subscription status is active by sending 'ENABLE <action_group_short_name>' or 'START' to the SMS number and receiving a confirmation.

## Rollback
1. If an alert processing rule was unintentionally suppressing actions, modify the rule to remove the suppression or delete the rule. 2. If the phone number had typos, correct the country code and phone number in the action group's SMS action. 3. If rate limited, wait at least five minutes before triggering another alert, or replace the SMS/voice action with a non-rate-limited action (e.g., webhook, logic app, Azure function, automation runbook). 4. If the user unsubscribed, send the appropriate SMS command ('ENABLE <action_group_short_name>' or 'START') to re-subscribe, or remove and re-add the SMS action in the action group.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
