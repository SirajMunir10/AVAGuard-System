# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How to automate the enablement of analytics rules in Microsoft Sentinel using API and PowerShell?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with connected data sources

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Export the rules to JSON before enabling the rules.
2. Push rules to Microsoft Sentinel via API and PowerShell.

## Validation
1. Run the following PowerShell command to confirm the analytics rules are enabled: Get-AzSentinelAlertRule -ResourceGroupName <ResourceGroupName> -WorkspaceName <WorkspaceName> | Where-Object {$_.Enabled -eq $true}. 2. Verify the count of enabled rules matches the expected number from the exported JSON. 3. Check the rule details (e.g., displayName, severity) against the exported JSON to ensure correct configuration.

## Rollback
1. Disable the newly enabled rules by running: Get-AzSentinelAlertRule -ResourceGroupName <ResourceGroupName> -WorkspaceName <WorkspaceName> | Where-Object {$_.Enabled -eq $true} | ForEach-Object { Update-AzSentinelAlertRule -ResourceGroupName <ResourceGroupName> -WorkspaceName <WorkspaceName> -RuleId $_.Name -Enabled $false }. 2. If the exported JSON is available, re-import the original rule state by running the deployment script with the original JSON file. 3. Confirm rollback by running the validation command and ensuring no rules are enabled.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
