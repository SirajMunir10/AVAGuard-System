# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot missing SMS alert notifications from Azure Monitor action groups?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- SMS notifications from Azure Monitor action groups are not received

## Error Codes
N/A

## Root Causes
1. Opted out of SMS delivery from a specific action group using the DISABLE action_group_short_name reply
2. Opted out of SMS delivery from all action groups using the STOP reply
3. Accidentally blocked notifications on the phone, such as blocking calls or SMS from specific phone numbers or short codes, or blocking push notifications from specific apps like the Azure mobile app

## Remediation Steps
1. Open your SMS history and check if you opted out of SMS delivery from this specific action group (using the DISABLE action_group_short_name reply) or from all action groups (using the STOP reply)
2. To subscribe again, either send the relevant SMS command (ENABLE action_group_short_name or START), or remove the SMS action from the action group, and then add it back again
3. To check if you accidentally blocked the notifications on your phone, search the documentation specific for your phone operating system and model, or test with a different phone and phone number

## Validation
1. Open the SMS history on the phone and verify that no 'DISABLE <action_group_short_name>' or 'STOP' replies were sent to the Azure Monitor SMS number. 2. If a previous opt-out is found, send an 'ENABLE <action_group_short_name>' or 'START' SMS to the same number and confirm receipt of a confirmation message. 3. Alternatively, in the Azure portal, navigate to the action group, remove the SMS action, save, then add the SMS action back and save. 4. Trigger a test alert from the action group and verify that the SMS is received on the target phone. 5. If still not received, test with a different phone number to rule out device-specific blocking.

## Rollback
1. If re-subscribing via SMS does not restore notifications, send a 'STOP' SMS to the same number to opt out of all action groups again, or send 'DISABLE <action_group_short_name>' to opt out of the specific group. 2. If the SMS action was removed and re-added in the portal, remove the SMS action again and save to revert to the previous configuration. 3. If testing with a different phone number succeeded, investigate the original phone's SMS blocking settings (e.g., check blocked numbers, short codes, or carrier-level blocks) and adjust accordingly.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
