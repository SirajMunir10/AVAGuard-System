# Governance: Migration

**Domain:** Sentinel
**Subdomain:** Migration
**Incident Type:** Governance

## Scenario / Query
How do I plan the transition from Microsoft Sentinel in the Azure portal to the Microsoft Defender portal before the March 31, 2027 deadline?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Azure portal
- **Configuration:** Transition to Defender portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Start planning your transition to the Defender portal to ensure a smooth transition.
2. Take advantage of the unified security operations experience offered by Microsoft Defender.

## Validation
1. Confirm that the Microsoft Sentinel instance is accessible from the Microsoft Defender portal by navigating to https://security.microsoft.com and verifying that the Sentinel data sources, analytics rules, and incidents appear under the 'Microsoft Sentinel' section.
2. Run the following Azure CLI command to check the Sentinel workspace provisioning state: az resource show --resource-group <workspace-rg> --name <workspace-name> --resource-type Microsoft.OperationalInsights/workspaces --query properties.provisioningState -o tsv. Ensure the output is 'Succeeded'.
3. Validate that all custom analytics rules are still active by running: az security insight alert-rule list --resource-group <workspace-rg> --workspace-name <workspace-name> --query "[?properties.enabled==true].name" -o tsv. Compare the list with your pre-transition inventory.
4. Verify that incident creation and management workflows function correctly by creating a test incident from a simulated alert and confirming it appears in both the Azure portal and Defender portal.

## Rollback
1. If the transition fails or causes issues, revert to the Azure portal by disabling the Defender portal integration: Navigate to the Sentinel workspace in the Azure portal, select 'Settings' > 'Microsoft Defender XDR integration', and set the toggle to 'Off'.
2. Use Azure CLI to disable the integration: az security insight entity-query update --resource-group <workspace-rg> --workspace-name <workspace-name> --name 'MicrosoftDefenderATP' --properties '{"properties":{"enabled":false}}'.
3. Restore any custom configurations (e.g., analytics rules, automation rules) from a backup if they were modified during the transition. Use the Azure portal or PowerShell to re-import rules from a saved ARM template.
4. Confirm the Sentinel workspace is fully operational in the Azure portal by running: az monitor log-analytics workspace show --resource-group <workspace-rg> --workspace-name <workspace-name> --query provisioningState -o tsv. Ensure it returns 'Succeeded'.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
