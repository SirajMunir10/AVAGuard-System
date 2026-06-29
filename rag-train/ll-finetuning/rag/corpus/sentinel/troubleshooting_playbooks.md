# Troubleshooting: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Troubleshooting

## Scenario / Query
How to prevent entity playbooks from failing when triggered without an incident ID?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel entity trigger playbooks

## Symptoms
- Playbook fails to run to completion when triggered in a scenario unconnected to an incident, such as threat hunting
- Incident ARM ID field is populated with a null value

## Error Codes
N/A

## Root Causes
1. Entity playbooks using the Incident ARM ID field are triggered without an incident ID, causing the field to be null

## Remediation Steps
1. In your workflow, preceding the first action that refers to the Incident ARM ID field, add a Condition action
2. In the Condition pane, on the condition row, select the left Choose a value field, and then select the dynamic content option (lightning icon)
3. From the dynamic content list, under Microsoft Sentinel incident, use the search box to find and select Incident ARM ID
4. If the output doesn't appear in the list, next to the trigger name, select See more
5. In the middle field, from the operator list, select is not equal to
6. In the right Choose a value field, and select the expression editor option (function icon)
7. In the editor, enter null, and select Add
8. Prescribe a different set of actions to take if the field has a null value, due to the playbook not being run from an incident

## Validation
1. Open the playbook in Azure Logic Apps Designer. 2. Locate the Condition action added before the first action that references the Incident ARM ID field. 3. Confirm the left operand is set to the dynamic content 'Incident ARM ID' from the Microsoft Sentinel incident connector. 4. Confirm the operator is 'is not equal to'. 5. Confirm the right operand is the expression 'null'. 6. Verify that the True branch contains the original actions (those that require an incident ID) and the False branch contains alternative actions (e.g., logging, termination) for when Incident ARM ID is null. 7. Trigger the playbook from a non-incident context (e.g., threat hunting) and confirm it completes without error, executing the False branch. 8. Trigger the playbook from an incident and confirm it executes the True branch successfully.

## Rollback
1. Open the playbook in Azure Logic Apps Designer. 2. Delete the Condition action added during remediation. 3. Reconnect the trigger directly to the first action that references the Incident ARM ID field. 4. Save the playbook. 5. Test the playbook by triggering it from an incident to ensure it runs as before. 6. If the playbook still fails, restore from a previous version using the 'Version history' option in the Logic Apps blade, selecting the last known working version.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
