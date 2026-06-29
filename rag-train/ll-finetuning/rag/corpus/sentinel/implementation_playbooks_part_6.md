# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How to create and deploy a Microsoft Sentinel playbook using the Azure portal?

## Environment Context
- **Tenant Type:** Azure tenant with Microsoft Sentinel enabled
- **Configuration:** Consumption workflow designer for Azure Logic Apps

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the Review and create tab, review your configuration choices, and select Create playbook.
2. After deployment completes, your playbook opens in the Consumption workflow designer for Azure Logic Apps.
3. On the designer, select the Microsoft Sentinel trigger, if not already selected.
4. On the Create connection pane, follow these steps to provide the required information to connect to Microsoft Sentinel.
5. For Authentication, select from the following methods: OAuth, Service principal, or Managed identity.
6. Based on your selected authentication option, provide the necessary parameter values for the corresponding option.
7. For Tenant ID, select your Microsoft Entra tenant ID.
8. When you finish, select Sign in.

## Validation
1. Navigate to the Azure portal and open Microsoft Sentinel. 2. Select 'Automation' from the left menu, then 'Playbook templates' tab. 3. Verify the newly created playbook appears in the list. 4. Open the playbook and confirm it opens in the Consumption workflow designer for Azure Logic Apps. 5. In the designer, verify the Microsoft Sentinel trigger is present and configured. 6. Check the connection pane to ensure the authentication method (OAuth, Service principal, or Managed identity) is correctly set and the Tenant ID matches your Microsoft Entra tenant ID. 7. Run a test trigger to confirm the playbook executes without errors.

## Rollback
1. In the Azure portal, navigate to the resource group where the playbook was deployed. 2. Locate the Logic App resource corresponding to the playbook. 3. Select 'Delete' to remove the playbook. 4. Confirm the deletion. 5. If the playbook was created from a template, you may also delete any associated connections or API connections created during deployment. 6. Verify the playbook no longer appears in Microsoft Sentinel under 'Automation' > 'Playbook templates'.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
