# Troubleshooting: Automation

**Domain:** Sentinel
**Subdomain:** Automation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I view and manage all active playbooks in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Subscription view filter; Microsoft Defender portal onboarding

## Symptoms
- Active playbooks tab shows a predefined filter with onboarded workspace's subscription after onboarding to Microsoft Defender portal

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the Automation > Active playbooks tab to view all playbooks you have access to, filtered by your subscription view.
2. In the Azure portal, edit the subscriptions you're showing from the Directory + subscription menu in the global Azure page header.

## Validation
1. In the Azure portal, navigate to Microsoft Sentinel > Automation > Active playbooks tab.
2. Confirm the subscription filter in the global page header (Directory + subscription menu) shows the correct subscription(s) for the onboarded workspace.
3. Verify that all expected playbooks (e.g., those with access permissions) are listed in the Active playbooks tab.
4. Optionally, run: az resource list --resource-type 'Microsoft.Logic/workflows' --query "[?tags.workspaceId=='<workspace-id>']" to cross-check playbook count.

## Rollback
1. If the subscription filter is incorrect, open the Directory + subscription menu in the Azure portal header and select the original subscription(s) used before the change.
2. If playbooks are missing, verify the user/principal has the required permissions (e.g., Sentinel Contributor, Logic App Contributor) on the Logic Apps resource group.
3. If the issue persists, restore the previous subscription filter and re-onboard the workspace to Microsoft Defender portal following the official guidance.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
