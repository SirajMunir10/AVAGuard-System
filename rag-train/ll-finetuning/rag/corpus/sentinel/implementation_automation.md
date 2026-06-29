# Implementation: Automation

**Domain:** Sentinel
**Subdomain:** Automation
**Incident Type:** Implementation

## Scenario / Query
How do I create a new playbook in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure or Defender portal
- **Configuration:** Microsoft Sentinel workspace with Automation enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Defender portal or in the Azure portal, go to your Microsoft Sentinel workspace.
2. On the workspace menu, under Configuration, select Automation.
3. From the top menu, select Create, and then select one of the following options: If you're creating a Consumption playbook, select one of the following options, depending on the trigger you want to use, and then follow the steps for a Consumption logic app: Playbook with incident trigger, Playbook with alert trigger, Playbook with entity trigger. This guide continues with the Playbook with entity trigger. If you're creating a Standard playbook, select Blank playbook and then follow the steps for the Standard logic app type.

## Validation
1. In the Defender portal or Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under Configuration, select Automation. 3. Verify the new playbook appears in the playbooks list. 4. Select the playbook and confirm its status is 'Enabled' and the trigger type matches what was selected (e.g., incident, alert, or entity trigger). 5. Optionally, run a test by triggering the playbook with a sample alert or incident to ensure it executes successfully.

## Rollback
1. In the Defender portal or Azure portal, go to your Microsoft Sentinel workspace. 2. Under Configuration, select Automation. 3. Locate the newly created playbook in the list. 4. Select the playbook and choose 'Delete' from the top menu or context menu. 5. Confirm the deletion to remove the playbook and revert to the previous state.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
