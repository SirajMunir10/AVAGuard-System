# Implementation: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Implementation

## Scenario / Query
A security administrator enabled the 'Log Analytics agent should be installed on your Windows-based Azure Arc machines' recommendation in Microsoft Defender for Cloud, but after 24 hours the agent status still shows 'Not installed' for all Arc-enabled servers. What configuration step was missed?

## Environment Context
- **Tenant Type:** Enterprise (Azure Arc hybrid environment)
- **Configuration:** Azure Arc-enabled servers with Windows OS; Log Analytics workspace linked to Defender for Cloud; no Azure Policy assignment for the built-in 'Deploy Log Analytics agent to Windows Azure Arc machines' initiative.

## Symptoms
- Defender for Cloud recommendation 'Log Analytics agent should be installed on your Windows-based Azure Arc machines' remains in 'Unhealthy' state for all Arc resources.
- Agent status in Azure Arc resource blade shows 'Not installed'.
- No errors in Azure Activity Log related to agent deployment.

## Error Codes
N/A

## Root Causes
1. The built-in policy initiative 'Deploy Log Analytics agent to Windows Azure Arc machines' was not assigned to the scope containing the Arc machines. The recommendation in Defender for Cloud only detects the missing agent but does not deploy it; a corresponding Azure Policy assignment is required for automatic deployment.

## Remediation Steps
1. Navigate to Azure Policy and assign the built-in initiative 'Deploy Log Analytics agent to Windows Azure Arc machines' (policy definition ID: /providers/Microsoft.Authorization/policySetDefinitions/...).
2. Set the assignment scope to the management group or subscription containing the Arc-enabled servers.
3. Configure the Log Analytics workspace parameter to match the workspace used by Defender for Cloud.
4. After assignment, the policy will deploy the Log Analytics agent to all non-compliant Arc machines within the evaluation cycle (typically 30 minutes).

## Validation
After policy assignment, verify that the Defender for Cloud recommendation status changes to 'Healthy' for the Arc machines and that the Log Analytics agent appears as 'Installed' in the Azure Arc resource blade.

## Rollback
Remove the policy assignment from the scope. The agent will not be automatically uninstalled; manual uninstallation via the Azure Arc machine's Control Panel or script is required if removal is desired.

## References
- <https://learn.microsoft.com/en-us/azure/azure-arc/servers/manage-agent#install-the-log-analytics-agent>
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-arc>
