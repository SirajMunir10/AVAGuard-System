# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle accidental unsubscription from an action group in Azure Monitor?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- User accidentally unsubscribed from an action group
- All members from a distribution list are unsubscribed when one user unsubscribes

## Error Codes
N/A

## Root Causes
1. User clicked the unsubscribe link in an alert email
2. Distribution list behavior: unsubscribing affects all members of the distribution list

## Remediation Steps
1. To subscribe again, either use the link in the unsubscribe confirmation email received, or remove the email address from the action group and then add it back again
2. Work-around: add the email address of all users in the action group individually (one action group can contain up to 1000 email addresses) so that if a specific user wants to unsubscribe, they can do so without affecting other users

## Validation
1. Check the action group's email recipients in the Azure portal: navigate to Monitor > Alerts > Action groups, select the affected action group, and verify the email address is listed under 'Email'. 2. Send a test alert to the action group and confirm the user receives the email notification. 3. If the user was re-added, ask them to check their inbox for the test alert.

## Rollback
1. If re-adding the email address fails or causes duplicate notifications, remove the email address from the action group via the Azure portal: Monitor > Alerts > Action groups > select the action group > delete the email entry. 2. If the user needs to be re-subscribed, provide them with the original unsubscribe confirmation email link to re-subscribe, or re-add the email address individually. 3. If the distribution list behavior is problematic, remove the distribution list email and add individual user email addresses (up to 1000) as a workaround.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
