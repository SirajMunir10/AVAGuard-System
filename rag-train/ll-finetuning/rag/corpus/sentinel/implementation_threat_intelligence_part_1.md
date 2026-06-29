# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
What prerequisites are required to manage threat intelligence in Microsoft Sentinel?

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
1. Ensure the user account has Microsoft Sentinel Contributor or higher role assigned.
2. Install the Threat Intelligence solution in Microsoft Sentinel.
3. Enable the relevant connectors as described in Use STIX/TAXII to import and export threat intelligence in Microsoft Sentinel.

## Validation
1. Confirm the user account has Microsoft Sentinel Contributor role or higher: run 'az role assignment list --assignee <userPrincipalName> --scope /subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/Microsoft.OperationalInsights/workspaces/<workspaceName> --output table' and verify the role includes 'Microsoft Sentinel Contributor' or 'Microsoft Sentinel Responder' or 'Microsoft Sentinel Contributor'.
2. Verify the Threat Intelligence solution is installed: in the Azure portal, navigate to Microsoft Sentinel > Content hub, search for 'Threat Intelligence', and confirm its status is 'Installed'.
3. Check that the required connectors are enabled: go to Microsoft Sentinel > Data connectors, search for 'Threat Intelligence - TAXII' and 'Threat Intelligence - Upload Indicators API', and verify each shows 'Connected'.

## Rollback
1. Remove the Threat Intelligence solution: in Microsoft Sentinel > Content hub, select the 'Threat Intelligence' solution, click 'Uninstall', and confirm.
2. Disable the connectors: in Microsoft Sentinel > Data connectors, select each connector (e.g., 'Threat Intelligence - TAXII', 'Threat Intelligence - Upload Indicators API'), click 'Disconnect', and confirm.
3. Remove elevated role assignments: run 'az role assignment delete --assignee <userPrincipalName> --role "Microsoft Sentinel Contributor" --scope /subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/Microsoft.OperationalInsights/workspaces/<workspaceName>' to revert the user's role to the previous assignment.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
