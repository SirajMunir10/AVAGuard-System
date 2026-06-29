# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I create a Standard playbook in Microsoft Sentinel using Azure Logic Apps?

## Environment Context
- **Tenant Type:** Azure tenant with Microsoft Sentinel enabled
- **Configuration:** Standard logic app plan, Application Insights disabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Under Application Insights, set Enable Application Insights to No.
2. To apply tags to this logic app for resource categorization and billing purposes, select Next: Tags >. Otherwise, select Review + create.
3. On the Review + create tab, review your configuration choices, and select Create.
4. After deployment completes, select Go to resource, which opens your logic app resource.
5. On your logic app menu, under Workflows, select Workflows.
6. On the Workflows page toolbar, select Add.
7. In the New workflow pane, provide a meaningful name for Workflow Name.
8. For State type, select Stateful. Microsoft Sentinel doesn't support the use of stateless workflows as playbooks.
9. When you finish, select Create.
10. Select the workflow to open the workflow Overview page.
11. On the workflow menu, under Developer, select Designer to start building your workflow by adding a trigger.

## Validation
1. In the Azure portal, navigate to the resource group containing the Standard logic app. 2. Select the logic app resource. 3. Under Settings, select Identity and confirm System assigned managed identity is enabled. 4. Under Workflows, select Workflows and verify the workflow named with State type Stateful exists. 5. Select the workflow, then under Developer select Designer and confirm the trigger is present. 6. Under Monitoring, select Diagnostic settings and verify no Application Insights is configured.

## Rollback
1. In the Azure portal, navigate to the resource group containing the Standard logic app. 2. Select the logic app resource. 3. Under Workflows, select Workflows. 4. Select the workflow created during remediation, then select Delete and confirm. 5. Under Overview, select Delete to remove the entire logic app resource and confirm. 6. If tags were applied, remove them by selecting Tags, deleting each tag, and saving.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
