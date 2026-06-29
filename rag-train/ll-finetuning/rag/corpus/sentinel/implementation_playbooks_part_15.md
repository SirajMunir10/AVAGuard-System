# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I configure authentication parameters and select entity triggers when creating a Microsoft Sentinel playbook?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Playbook authentication options

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Based on your selected authentication option, provide the necessary parameter values for the corresponding option.
2. For Tenant ID, select your Microsoft Entra tenant ID.
3. When you finish, select Sign in.
4. If you chose Playbook with entity trigger, select the type of entity you want this playbook to receive as an input.

## Validation
1. In the Microsoft Sentinel playbook creation wizard, confirm that the selected authentication option (e.g., Managed Identity, Service Principal, or Azure AD User) displays the correct Tenant ID matching your Microsoft Entra tenant. 2. If 'Playbook with entity trigger' was chosen, verify that the entity type (e.g., Account, Host, IP, URL, FileHash) is correctly selected and appears in the trigger configuration. 3. After signing in, run the following Azure PowerShell command to confirm the playbook's authentication settings: Get-AzLogicApp -ResourceGroupName <ResourceGroupName> -Name <PlaybookName> | Select-Object -ExpandProperty Definition | ConvertFrom-Json | Select-Object -ExpandProperty triggers. 4. Check that the trigger's 'kind' property matches the expected entity trigger type (e.g., 'SecurityInsightsEntity') and that the 'authentication' section contains the correct tenant ID and authentication parameters.

## Rollback
1. If the authentication parameters are incorrect, navigate to the playbook in the Azure portal, select 'Edit', and re-enter the correct Tenant ID and authentication option. 2. If the entity trigger type is wrong, delete the current trigger and add a new trigger with the correct entity type by selecting 'Add trigger' and choosing 'Microsoft Sentinel Entity' and the appropriate entity. 3. If the playbook fails to authenticate after changes, run: Remove-AzLogicApp -ResourceGroupName <ResourceGroupName> -Name <PlaybookName> -Force, then recreate the playbook using the correct authentication and trigger settings. 4. Alternatively, use the Azure CLI: az logicapp delete --resource-group <ResourceGroupName> --name <PlaybookName>, then redeploy with az logicapp create.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
- <https://learn.microsoft.com/en-us/azure/sentinel/playbook-reference>
- <https://learn.microsoft.com/en-us/azure/sentinel/playbook-triggers-actions>
