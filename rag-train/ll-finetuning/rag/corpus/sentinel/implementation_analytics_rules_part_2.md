# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How to create a custom scheduled analytics rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Log Analytics

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure you have the Microsoft Sentinel Contributor role, or any other role or set of permissions that includes write permissions on your Log Analytics workspace and its resource group.
2. Have at least a basic familiarity with data science and analysis and the Kusto Query Language.
3. Familiarize yourself with the analytics rule wizard and all the configuration options that are available. For more information, see Scheduled analytics rules in Microsoft Sentinel.

## Validation
1. Verify that the custom scheduled analytics rule is enabled and appears in the list of active rules: run `Get-AzSentinelAlertRule -ResourceGroupName <resource-group> -WorkspaceName <workspace-name> | Where-Object {$_.Kind -eq 'Scheduled' -and $_.Enabled -eq $true}` in Azure PowerShell. 2. Confirm the rule's query executes without errors by running the KQL query from the rule in the Log Analytics workspace's query editor and checking for results. 3. Validate that the rule's frequency and lookback period are set correctly by reviewing the rule properties: `Get-AzSentinelAlertRule -ResourceGroupName <resource-group> -WorkspaceName <workspace-name> -RuleId <rule-id> | Select-Object -Property Frequency, QueryPeriod, TriggerOperator, TriggerThreshold`.

## Rollback
1. Disable the custom scheduled analytics rule to stop it from generating alerts: `Update-AzSentinelAlertRule -ResourceGroupName <resource-group> -WorkspaceName <workspace-name> -RuleId <rule-id> -Enabled $false`. 2. If the rule was created incorrectly, delete it: `Remove-AzSentinelAlertRule -ResourceGroupName <resource-group> -WorkspaceName <workspace-name> -RuleId <rule-id>`. 3. Restore the previous configuration by re-enabling any previously disabled rule or reapplying the original rule settings from a backup.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
