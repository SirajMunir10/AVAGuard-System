# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How to enable or disable the Fabric Workspace Inbound External Data Share setting and what are the corresponding audit log activities?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Fabric Workspace Inbound External Data Share setting

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. To enable external data shares bypass on the workspace: The admin allowed External Data Shares to access data in workspaces where inbound public network access is restricted. The corresponding audit activity is 'ExternalDataSharesBypassForWorkspaceEnabled'.
2. To disable external data shares bypass on the workspace: The admin blocked External Data Shares from accessing data in workspaces where inbound public network access is restricted. The corresponding audit activity is 'ExternalDataSharesBypassForWorkspaceDisabled'.

## Validation
1. Connect to Microsoft Fabric using PowerShell or the Fabric admin portal. 2. Run the following command to check the current state of the Fabric Workspace Inbound External Data Share setting: `Get-FabricWorkspace -WorkspaceId <WorkspaceId> | Select-Object -Property ExternalDataSharesBypass`. 3. Verify that the `ExternalDataSharesBypass` property is set to `True` if the remediation was to enable, or `False` if the remediation was to disable. 4. Search the Microsoft 365 Purview audit log for the corresponding activity: `Search-UnifiedAuditLog -Operations 'ExternalDataSharesBypassForWorkspaceEnabled'` or `'ExternalDataSharesBypassForWorkspaceDisabled'` to confirm the change was logged.

## Rollback
1. Connect to Microsoft Fabric using PowerShell or the Fabric admin portal. 2. Run the following command to revert the setting: `Set-FabricWorkspace -WorkspaceId <WorkspaceId> -ExternalDataSharesBypass $false` if the remediation was to enable (to disable), or `Set-FabricWorkspace -WorkspaceId <WorkspaceId> -ExternalDataSharesBypass $true` if the remediation was to disable (to enable). 3. Verify the change by checking the property again: `Get-FabricWorkspace -WorkspaceId <WorkspaceId> | Select-Object -Property ExternalDataSharesBypass`. 4. Confirm the rollback is logged in the audit log by searching for the opposite operation: `Search-UnifiedAuditLog -Operations 'ExternalDataSharesBypassForWorkspaceDisabled'` or `'ExternalDataSharesBypassForWorkspaceEnabled'`.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
