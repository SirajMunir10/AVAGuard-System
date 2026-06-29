# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to replace Microsoft Sentinel livestreams with alternative automation methods?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use KQL jobs, analytics rules, or playbooks to automate queries and notifications.
2. These alternatives offer persistent query results and support for various messaging platforms.

## Validation
1. Verify that the Microsoft Sentinel workspace exists and is accessible: az monitor log-analytics workspace show --resource-group <resource-group-name> --workspace-name <workspace-name>. 2. Confirm that a KQL job is created and running: az monitor log-analytics workspace table job list --resource-group <resource-group-name> --workspace-name <workspace-name> --table-name <table-name>. 3. Check that an analytics rule is enabled and producing alerts: az sentinel alert-rule list --resource-group <resource-group-name> --workspace-name <workspace-name> --query "[?properties.enabled == true]" --output table. 4. Validate that a playbook is associated with the analytics rule and triggers correctly: az sentinel playbook list --resource-group <resource-group-name> --workspace-name <workspace-name> --query "[?properties.triggerLogicAppId != null]" --output table. 5. Ensure that the alternative automation method (e.g., playbook) sends notifications to the desired messaging platform by checking the Logic App run history: az logic workflow run list --resource-group <resource-group-name> --name <logic-app-name> --query "[?status == 'Succeeded']" --output table.

## Rollback
1. Disable or delete the analytics rule that was created: az sentinel alert-rule delete --resource-group <resource-group-name> --workspace-name <workspace-name> --rule-id <rule-id>. 2. Remove the KQL job if it was created: az monitor log-analytics workspace table job delete --resource-group <resource-group-name> --workspace-name <workspace-name> --table-name <table-name>. 3. Disable or delete the playbook (Logic App) that was associated: az logic workflow delete --resource-group <resource-group-name> --name <logic-app-name>. 4. If the livestream was previously active, re-enable it via the Azure portal or PowerShell: Enable-AzSentinelLivestream -ResourceGroupName <resource-group-name> -WorkspaceName <workspace-name> -LivestreamId <livestream-id>. 5. Verify that the original livestream is running again: Get-AzSentinelLivestream -ResourceGroupName <resource-group-name> -WorkspaceName <workspace-name>.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
