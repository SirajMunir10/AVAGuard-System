# Troubleshooting: Automation

**Domain:** Sentinel
**Subdomain:** Automation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I view run history and edit a playbook from the Azure Logic Apps page?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Permissions to edit playbook

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select a playbook to open its Azure Logic Apps page.
2. On the Azure Logic Apps page: View a log of all times the playbook ran.
3. View run results, including successes and failures and other details.
4. If you have the relevant permissions, open the workflow designer in Azure Logic Apps to edit the playbook directly.

## Validation
1. Navigate to Azure Sentinel > Automation > Playbooks. 2. Select a playbook to open its Azure Logic Apps page. 3. Under 'Run history', confirm that a log of all runs is displayed, including timestamps, status (success/failure), and other details. 4. If permissions allow, click 'Edit' to open the workflow designer and verify the playbook can be modified.

## Rollback
1. If run history is not visible, ensure the playbook has been triggered at least once; if not, trigger it manually. 2. If unable to edit, verify you have Contributor or Owner permissions on the Logic App; if not, request the necessary role assignment. 3. If the playbook page fails to load, check Azure Service Health for any ongoing outages. 4. If changes were made in error, use the workflow designer to revert to a previous version via 'Version history' in Azure Logic Apps.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
