# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I attach a playbook to an analytics rule or automation rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure or Microsoft Defender portal
- **Configuration:** Microsoft Sentinel in Azure portal or Defender portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Attach the playbook to an analytics rule or automation rule.
2. Alternatively, run the playbook manually on specific incidents, alerts, or entities.

## Validation
1. In Microsoft Sentinel, navigate to Automation > Automation rules. Select the rule you modified or created. Confirm the playbook is listed under 'Actions' with the correct trigger (e.g., 'When incident is created').
2. Alternatively, go to Analytics > Active rules, select the rule, and under 'Automated response' verify the playbook is attached.
3. Trigger a test incident or alert that meets the rule criteria. Check the playbook's run history in the playbook resource (Logic Apps) under 'Runs history' to confirm successful execution.
4. For manual playbook execution: Open an incident, click 'Actions' > 'Run playbook', and verify the playbook appears in the list and runs without error.

## Rollback
1. In Microsoft Sentinel, go to Automation > Automation rules. Select the rule where the playbook is attached, click 'Edit', and remove the playbook action. Save the rule.
2. For analytics rule attachment: Navigate to Analytics > Active rules, select the rule, click 'Edit'. In the 'Automated response' tab, remove the playbook. Save the rule.
3. If the playbook was attached via an automation rule, delete the automation rule entirely if it was created solely for this playbook.
4. Verify removal by checking that the playbook no longer appears in the rule's actions and that no automated runs occur for new incidents/alerts.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
