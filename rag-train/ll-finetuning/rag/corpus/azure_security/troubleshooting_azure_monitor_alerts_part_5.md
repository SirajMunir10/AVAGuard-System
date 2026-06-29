# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
I didn't receive the expected email for an Azure Monitor alert that fired in the portal.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Fired alert visible in Azure portal
- Expected email notification not received

## Error Codes
N/A

## Root Causes
1. Alert email suppressed by an alert processing rule
2. Action type 'Email Azure Resource Manager Role' not assigned at subscription scope or not of type User or Group
3. Email server or mailbox blocking external emails from Azure Monitor sender addresses
4. Inbox rules or spam filter deleting or moving alert emails

## Remediation Steps
1. Click on the fired alert in the portal and look at the history tab for suppressed action groups to check if the email was suppressed by an alert processing rule.
2. If the action type is 'Email Azure Resource Manager Role', ensure the role assignment is at the subscription scope and of type User or Group, not at resource or resource group level.
3. Allow emails from these sender addresses in email filtering and spam prevention services: azure-noreply@microsoft.com, azureemail-noreply@microsoft.com, alerts-noreply@mail.windowsazure.com.
4. Test by adding a regular work email address (not a mailing list) to the action group to see if alerts arrive.
5. Verify that there are no inbox rules that delete those emails or move them to a side folder, for example, rules catching specific senders or specific words in the subject.

## Validation
1. In the Azure portal, navigate to Monitor > Alerts, select the fired alert, and review the History tab to confirm no action group was suppressed by an alert processing rule. 2. If the action group uses 'Email Azure Resource Manager Role', verify the role assignment is at the subscription scope and assigned to a User or Group (not a service principal or managed identity). 3. Check the mailbox's spam or junk folder for emails from azure-noreply@microsoft.com, azureemail-noreply@microsoft.com, or alerts-noreply@mail.windowsazure.com. 4. Temporarily add a personal work email (not a distribution list) to the action group and trigger a test alert to confirm delivery. 5. Review inbox rules for any filters that delete or move emails containing 'Azure Monitor' or the sender addresses above.

## Rollback
1. If an alert processing rule was suppressing the email, either disable the rule or modify its scope to exclude the affected action group. 2. If the 'Email Azure Resource Manager Role' assignment was changed, reassign the role at the subscription scope to the original User or Group. 3. If email filtering was modified, restore the original allow/block list settings for the sender addresses. 4. Remove any test email addresses added to the action group. 5. Revert any inbox rules that were disabled or changed during troubleshooting.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
