# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
Why does an email notification from an Azure Monitor alert have unexpected content or formatting?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Email notification from an action group has slightly different formatting or content than expected
- Email notification contains a note: 'To ensure timely delivery, this email was processed through a secondary notification provider. You may notice minor differences in formatting or content compared to standard notifications. This is expected behavior and does not indicate an issue with your alert rules or action groups. https://aka.ms/armemail'

## Error Codes
N/A

## Root Causes
1. An outage triggered the use of the fallback email provider in Action Groups
2. The secondary email provider has different email templates, causing degraded email experience and slight differences in formatting and content

## Remediation Steps
1. If the notification does not contain the fallback note and you believe some fields are missing or incorrect, check the payload format
2. The payload can be either common schema format or non-common (different scheme between alert types: activity log alerts, log search alerts for Application Insights and log analytics, metric alerts)
3. To see the payload, use a webhook action and send it to your IP to see the result

## Validation
1. Check the email notification for the presence of the fallback note: 'To ensure timely delivery, this email was processed through a secondary notification provider...' If present, the formatting differences are expected and no further action is needed. 2. If the fallback note is absent, verify the alert rule payload format by configuring a webhook action in the action group to send the alert payload to a request bin or your own endpoint. 3. Compare the received payload with the expected schema for the alert type (common schema vs. non-common schema) as documented at https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-common-schema. 4. Confirm that the email content matches the payload fields; if not, adjust the action group email template or switch to common schema if applicable.

## Rollback
1. If the fallback note is present and the formatting differences are acceptable, no rollback is required. 2. If you modified the action group to use common schema and the email formatting worsens, revert the action group settings to use the original non-common schema. 3. If you changed the email template or action group configuration, restore the previous configuration from backup or reapply the original settings. 4. If the issue persists, disable the webhook test action and re-enable the original email action in the action group.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
