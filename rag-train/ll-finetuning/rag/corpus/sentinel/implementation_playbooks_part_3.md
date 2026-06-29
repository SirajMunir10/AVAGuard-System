# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites and required Azure roles to create and manage playbooks in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel playbook prerequisites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure you have an Azure account and subscription. If you don't have a subscription, sign up for a free Azure account.
2. To create and manage playbooks, you need access to Microsoft Sentinel with one of the following Azure roles: Consumption Logic App Contributor (Edit and manage logic apps), Consumption Logic App Operator (Read, enable, and disable logic apps), Standard Logic Apps Standard Operator (Enable, resubmit, and disable workflows), Standard Logic Apps Standard Developer (Create and edit workflows), Standard Logic Apps Standard Contributor (Manage all aspects of a workflow).
3. For more information, see the following documentation: Access to logic app operations Microsoft Sentinel playbook prerequisites.
4. Before you create your playbook, we recommend that you read Azure Logic Apps for Microsoft Sentinel playbooks.

## Validation
1. Confirm that the Azure account has an active subscription: `az account show --output table` (verify 'state' is 'Enabled').
2. Verify the user has the required role assignments for the subscription or resource group containing Microsoft Sentinel: `az role assignment list --assignee <user-principal-name> --output table | findstr /i "Logic App"` (should show one of: 'Consumption Logic App Contributor', 'Consumption Logic App Operator', 'Standard Logic Apps Standard Operator', 'Standard Logic Apps Standard Developer', 'Standard Logic Apps Standard Contributor').
3. Confirm Microsoft Sentinel is enabled in the workspace: `az sentinel show --workspace-name <workspace-name> --resource-group <resource-group-name>` (should return workspace details).
4. Test playbook creation by navigating to Microsoft Sentinel > Automation > Create > Playbook and verifying the UI loads without errors.

## Rollback
1. If the user lacks required roles, assign the appropriate role: `az role assignment create --assignee <user-principal-name> --role "<role-name>" --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group-name>` (replace <role-name> with one of the five listed roles).
2. If the subscription is disabled, reactivate it via Azure portal (Subscriptions > select subscription > 'Reactivate') or contact billing support.
3. If Microsoft Sentinel is not enabled, enable it: `az sentinel enable --workspace-name <workspace-name> --resource-group <resource-group-name>`.
4. If playbook creation fails due to missing Logic Apps provider, register the provider: `az provider register --namespace 'Microsoft.Logic'`.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
