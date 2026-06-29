# Migration: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Migration

## Scenario / Query
How do I migrate classic alert-trigger playbooks to automation rules in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel analytics rule with classic alert automation playbooks

## Symptoms
- Playbooks listed under Alert automation (classic) at the bottom of the Automated responses tab
- Cannot add new playbooks to the classic alert automation list as of June 2023

## Error Codes
N/A

## Root Causes
1. Classic alert automation method is deprecated effective March 2026
2. As of June 2023, you can't add playbooks to the classic list

## Remediation Steps
1. Create an automation rule based on the alert created trigger
2. Invoke the playbook from the automation rule
3. Select the ellipsis at the end of the line of the playbook listed under Alert automation (classic)
4. Select Remove
5. See Migrate your Microsoft Sentinel alert-trigger playbooks to automation rules for full instructions

## Validation
1. In the Azure portal, navigate to Microsoft Sentinel > your workspace > Automation > Automation rules tab. Confirm a new automation rule exists with trigger 'When alert is created' and action 'Run playbook' pointing to the migrated playbook. 2. In the same workspace, go to Analytics > select the relevant rule > Automated responses tab. Verify the playbook no longer appears under 'Alert automation (classic)'. 3. Trigger a test alert that matches the rule and confirm the playbook executes successfully by checking the playbook's run history in the Automation > Playbooks tab.

## Rollback
1. In the Azure portal, navigate to Microsoft Sentinel > your workspace > Automation > Automation rules tab. Delete the newly created automation rule by selecting its row and clicking 'Delete'. 2. In the same workspace, go to Analytics > select the relevant rule > Automated responses tab. Under 'Alert automation (classic)', click 'Add/Edit' and re-add the playbook that was removed. 3. Confirm the playbook appears in the classic list and test that it triggers correctly on a new alert.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
- <https://learn.microsoft.com/en-us/azure/sentinel/automate-threat-response-with-automation-rules>
- <https://learn.microsoft.com/en-us/azure/sentinel/migrate-playbooks-to-automation-rules>
