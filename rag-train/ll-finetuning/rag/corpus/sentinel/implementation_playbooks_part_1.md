# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I create and manage Microsoft Sentinel playbooks based on Azure Logic Apps?

## Environment Context
- **Tenant Type:** Azure or Microsoft Defender portal
- **Configuration:** Microsoft Sentinel in Azure portal or Defender portal; Azure Logic Apps

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a playbook by building a workflow in Azure Logic Apps.
2. Attach the playbook to an automation rule to run automatically when specific alerts are generated or when incidents are created or updated.
3. Run the playbook manually on-demand on specific incidents, alerts, or entities.

## Validation
1. In the Azure portal, navigate to Microsoft Sentinel > Automation > Playbooks tab. Confirm the playbook appears in the list with status 'Enabled'. 2. Open the playbook (Logic App) and verify the workflow designer shows all expected steps and connections are authorized. 3. In Microsoft Sentinel, create a test incident or alert, then manually trigger the playbook from the incident's 'Actions' menu. Verify the playbook runs successfully (check Logic App run history for 'Succeeded' status). 4. If attached to an automation rule, create a matching test alert/incident and confirm the rule triggers the playbook automatically (check Logic App run history for a new run within expected time).

## Rollback
1. In Microsoft Sentinel > Automation > Playbooks tab, select the playbook and click 'Delete' to remove it from Sentinel. 2. In Azure Logic Apps, navigate to the playbook resource, select 'Delete' to remove the Logic App entirely. 3. If the playbook was attached to an automation rule, edit the rule in Microsoft Sentinel > Automation > Rules tab, remove the playbook action, and save. 4. If the playbook was used in any other automation rules or custom actions, repeat step 3 for each rule. 5. Verify no remaining references to the playbook in Sentinel or Logic Apps.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
