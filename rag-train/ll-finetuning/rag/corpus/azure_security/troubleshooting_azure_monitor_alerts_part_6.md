# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
Why am I not receiving alert emails from Azure Monitor?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Alert emails are not being received by users

## Error Codes
N/A

## Root Causes
1. Spam settings of email client (like Outlook, Gmail) may be blocking emails
2. Sender limits, spam settings, or quarantine settings of email server (like Exchange, Microsoft 365, G-suite) may be blocking emails
3. Settings of email security appliance (like Barracuda, Cisco) may be blocking emails
4. Inbox rules may be deleting or moving alert emails to a side folder
5. User may have accidentally unsubscribed from the action group

## Remediation Steps
1. Check spam settings of email client (like Outlook, Gmail)
2. Check sender limits, spam settings, and quarantine settings of email server (like Exchange, Microsoft 365, G-suite)
3. Check settings of email security appliance (like Barracuda, Cisco)
4. Verify that there are no inbox rules that delete those emails or move them to a side folder
5. Check if user accidentally unsubscribed from the action group by editing the action group in the portal and checking the Status column
6. Search email for the unsubscribe confirmation
7. To subscribe again, either use the link in the unsubscribe confirmation email received, or remove the email address from the action group and then add it back again

## Validation
1. In the Azure portal, navigate to Monitor > Alerts > Action groups, select the relevant action group, and verify the 'Status' column for the email address shows 'Enabled'. 2. Ask the user to check their email client's spam/junk folder for emails from azure-noreply@microsoft.com. 3. Ask the user to search their email inbox for 'unsubscribe' or 'Azure Monitor' to locate any unsubscribe confirmation email. 4. Ask the user to review their inbox rules for any rule that deletes or moves emails from azure-noreply@microsoft.com. 5. Ask the user to check with their email server administrator to ensure sender limits, spam settings, or quarantine settings are not blocking emails from azure-noreply@microsoft.com. 6. Ask the user to check their email security appliance (e.g., Barracuda, Cisco) logs for any blocked emails from azure-noreply@microsoft.com.

## Rollback
1. If the user accidentally unsubscribed, re-subscribe by either using the link in the original unsubscribe confirmation email or by removing the email address from the action group and adding it back. 2. If inbox rules were modified, restore the original rules or remove any rule that was deleting/moving the alert emails. 3. If spam settings were changed, revert to the previous settings that were blocking the emails. 4. If email server or security appliance settings were modified, revert those changes to the previous configuration. 5. If the email address was removed and re-added to the action group, no further rollback is needed as the subscription is restored.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
