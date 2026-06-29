# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How to work with custom details in the Microsoft Sentinel incident trigger for playbooks?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Analytics rules configured

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the Microsoft Sentinel workspace menu, under Configuration, select Analytics.
2. Follow the steps to create or open an existing scheduled query rule or NRT query rule.
3. On the Set rule logic tab, expand the Custom details section.
4. In the workflow designer, under the Microsoft Sentinel incident trigger, add the built-in action named Parse JSON.
5. Select inside the action's Content parameter, and select the dynamic content list option (lightning icon).
6. From the list, in the incident trigger section, find and select Alert Custom Details.

## Validation
1. Navigate to the Microsoft Sentinel workspace. 2. Under Configuration, select Analytics. 3. Open the scheduled or NRT query rule that was configured. 4. On the Set rule logic tab, expand the Custom details section and verify that the custom details are correctly defined (key-value pairs). 5. Open the associated playbook in Azure Logic Apps. 6. In the workflow designer, locate the Microsoft Sentinel incident trigger. 7. Confirm that a Parse JSON action is present immediately after the trigger. 8. Click on the Parse JSON action and verify that the Content parameter contains the dynamic content 'Alert Custom Details' (from the incident trigger section). 9. Save the playbook and trigger a test incident to confirm that the custom details are parsed correctly.

## Rollback
1. Open the playbook in Azure Logic Apps. 2. In the workflow designer, delete the Parse JSON action that was added. 3. Save the playbook. 4. If custom details were added to the analytics rule, navigate to the rule in Microsoft Sentinel (Analytics > select the rule > Set rule logic tab). 5. Expand the Custom details section and remove any custom details that were added. 6. Save the analytics rule. 7. Verify that the playbook and analytics rule return to their previous state.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
