# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Azure Monitor alerts when notifications do not perform as expected?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Alert fires as intended but proper notifications don't perform as expected

## Error Codes
N/A

## Root Causes
1. Action group may not be properly configured

## Remediation Steps
1. Test your action group first to ensure it's properly configured
2. Use the information in the rest of the article to troubleshoot your issue

## Validation
1. In the Azure portal, navigate to Monitor > Alerts > Action groups. 2. Select the action group associated with the alert rule. 3. Click 'Test action group' (preview) and select a sample alert type (e.g., 'Administrative') or use an existing alert rule. 4. Confirm that all configured notification channels (email, SMS, voice, push, webhook, ITSM, automation runbook, Azure Function, Logic App, secure webhook) receive the test notification. 5. Check the 'Notifications' tab in the action group for any delivery failures or errors. 6. Verify that the alert rule's 'Actions' tab correctly references the action group and that the alert rule is enabled.

## Rollback
1. If the action group test fails, review the action group configuration: a. For email/SMS/voice, ensure the recipient details are correct and not blocked. b. For webhook, verify the endpoint URI is correct and reachable; check if authentication (e.g., Azure AD, basic auth) is properly set. c. For ITSM, confirm the connection and work item template are valid. d. For automation runbooks, Azure Functions, or Logic Apps, ensure they are published and have the necessary permissions. 2. If the action group is misconfigured, edit the action group in the Azure portal to correct the settings. 3. If the action group is correct but notifications still fail, check Azure Service Health for any known issues with notification delivery. 4. As a last resort, create a new action group with verified settings and update the alert rule to use the new action group.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
