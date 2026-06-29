# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I add actions to a Microsoft Sentinel playbook workflow?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel playbook with Logic Apps

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the plus sign (+) on the designer to add actions, logical conditions, loops, or switch case conditions.
2. In the Add an action pane, browse or search for services, applications, systems, control flow actions, and more.
3. After entering search terms or selecting the resource, choose from the available actions in the results list.
4. When selecting inside a field, use Dynamic content (lightning icon) to choose from available outputs from preceding actions, including the Microsoft Sentinel trigger (e.g., attributes of an alert or incident, values and attributes of all mapped entities and custom details).
5. Use the Expression editor (function icon) to choose from a library of functions to add more logic to the workflow.

## Validation
1. Open the playbook in Logic Apps Designer. 2. Verify that the new action appears in the workflow with the correct configuration. 3. Trigger the playbook with a test incident or alert. 4. Confirm that the action executes as expected (e.g., check run history for successful completion). 5. Validate that dynamic content and expressions used are correctly resolved in the action inputs.

## Rollback
1. Open the playbook in Logic Apps Designer. 2. Delete the added action by selecting the ellipsis (...) on the action and choosing 'Delete'. 3. Reconnect any subsequent actions that depended on the deleted action's outputs. 4. Save the playbook. 5. Re-test the playbook to ensure it returns to the previous working state.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
