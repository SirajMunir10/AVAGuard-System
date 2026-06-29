# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I create a playbook in Microsoft Sentinel using a Consumption logic app?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Consumption logic app type

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the trigger, which includes an incident, alert, or entity trigger, so that the Create playbook wizard appears.
2. On the Basics tab, provide the following information: For Subscription and Resource group, select the values you want from their respective lists. The Region value is set to the same region as the associated Log Analytics workspace. For Playbook name, enter a name for your playbook.
3. To monitor this playbook's activity for diagnostic purposes, select Enable diagnostics logs in Log Analytics, and then select a Log Analytics workspace unless you already selected a workspace.
4. Select Next: Connections >.
5. On the Connections tab, we recommend leaving the default values, which configure a logic app to connect to Microsoft Sentinel with a managed identity.
6. To continue, select Next: Review and create >.

## Validation
1. In the Azure portal, navigate to Microsoft Sentinel > Automation > Playbooks tab. Confirm the playbook appears in the list with the expected name and status 'Enabled'. 2. Open the playbook resource in Logic Apps Designer and verify the trigger is set to a Microsoft Sentinel incident, alert, or entity trigger. 3. On the playbook's Overview page, confirm the subscription, resource group, and region match the values specified during creation. 4. If diagnostic logs were enabled, navigate to the associated Log Analytics workspace and run: `union * | where ResourceProvider == 'MICROSOFT.LOGIC' | where ResourceId contains '<playbook-name>' | take 10` to confirm log entries are being collected. 5. Test the playbook by triggering a sample incident or alert and verify the playbook runs successfully (check the Runs history in the playbook's Overview page).

## Rollback
1. In the Azure portal, navigate to Microsoft Sentinel > Automation > Playbooks tab. 2. Select the playbook you created. 3. On the playbook's Overview page, select 'Delete' and confirm the deletion. 4. If diagnostic logs were enabled, optionally delete the diagnostic setting from the playbook's Diagnostic settings page to stop log ingestion. 5. Verify the playbook no longer appears in the Playbooks list and that no runs are in progress.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
