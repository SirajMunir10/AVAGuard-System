# Troubleshooting: Automation

**Domain:** Sentinel
**Subdomain:** Automation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I interpret the details shown on the Active playbooks tab in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Playbook type (Standard vs Consumption), trigger kind

## Symptoms
- Playbook shows as enabled or disabled
- Playbook type is Standard or Consumption
- Trigger kind is one of: Microsoft Sentinel Incident/Alert/Entity, Using Microsoft Sentinel Action, Other, or Not initialized

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View the Active playbooks tab to see playbook details including enabled/disabled status, type (Standard/Consumption), and trigger kind.
2. For Standard type playbooks, note they use the LogicApp/Workflow naming convention.
3. Select a playbook to open its Azure Logic Apps page for more details.

## Validation
1. Navigate to Microsoft Sentinel > Automation > Active playbooks tab.
2. Confirm the playbook list displays with columns: Playbook, Status (Enabled/Disabled), Type (Standard/Consumption), Trigger kind.
3. For a Standard playbook, verify the name follows the LogicApp/Workflow naming convention (e.g., 'LogicApp-<name>').
4. Select a playbook and verify it opens the correct Azure Logic Apps page with the expected workflow details.
5. Check that the trigger kind matches one of: Microsoft Sentinel Incident/Alert/Entity, Using Microsoft Sentinel Action, Other, or Not initialized.

## Rollback
1. If the Active playbooks tab does not load or shows incorrect data, refresh the page and verify the user has at least Microsoft Sentinel Contributor role.
2. If a playbook's status is incorrectly shown, use Azure PowerShell or CLI to check the logic app's state: Get-AzLogicApp -ResourceGroupName <rg> -Name <playbook-name> or az logicapp show --name <playbook-name> --resource-group <rg>.
3. If the playbook type or trigger kind is misrepresented, review the logic app definition in Azure Portal > Logic Apps > <playbook> > Workflow > Trigger to confirm the actual trigger configuration.
4. If the Azure Logic Apps page fails to open, ensure the playbook is deployed in the same tenant and region as Microsoft Sentinel, and that the user has Logic App Contributor permissions.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
