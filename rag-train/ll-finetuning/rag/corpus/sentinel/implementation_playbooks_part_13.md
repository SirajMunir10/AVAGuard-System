# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I add a Microsoft Sentinel trigger to a playbook in Azure Logic Apps?

## Environment Context
- **Tenant Type:** Azure tenant with Microsoft Sentinel enabled
- **Configuration:** Logic Apps designer, Microsoft Sentinel connector

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the designer, select Add a trigger to open the Add a trigger pane.
2. Find the Microsoft Sentinel triggers, which include: Microsoft Sentinel entity, Microsoft Sentinel alert, Microsoft Sentinel incident.
3. Select the trigger that you want to use for your playbook. This example continues with the Microsoft Sentinel entity trigger.
4. On the designer, select the trigger, if not already selected.
5. On the Create connection pane, provide the required information to connect to Microsoft Sentinel.
6. For Authentication, select from the following methods: OAuth, Service principal, or Managed identity. For optimal security, Microsoft recommends using a managed identity for authentication when possible.
7. Based on your selected authentication option, provide the necessary parameter values for the corresponding option.
8. For Tenant ID, select your Microsoft Entra tenant ID.
9. When you finish, select Sign in.

## Validation
1. In the Logic Apps designer, confirm that the Microsoft Sentinel trigger (e.g., 'Microsoft Sentinel entity') appears as the first step in the workflow. 2. Verify that the trigger connection shows a green checkmark and the status 'Connected'. 3. Run a test by triggering the playbook (e.g., manually or via a sample alert/incident) and confirm that the playbook execution log shows a successful trigger invocation. 4. Check that the trigger output contains the expected fields (e.g., entity properties, alert details, or incident information) in the run history.

## Rollback
1. In the Logic Apps designer, delete the Microsoft Sentinel trigger step by selecting the trigger and choosing 'Delete'. 2. If a new connection was created, navigate to the Logic Apps resource's 'API connections' blade, find the Sentinel connection, and delete it. 3. Revert any changes to the playbook's authentication method (e.g., if you switched from managed identity to service principal, switch back to the original method). 4. If the playbook was previously working with a different trigger, re-add that original trigger and reconfigure its connection parameters.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
