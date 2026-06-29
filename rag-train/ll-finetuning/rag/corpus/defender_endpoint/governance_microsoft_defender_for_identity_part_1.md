# Governance: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Governance

## Scenario / Query
How to audit workspace configuration changes in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Workspace created or deleted unexpectedly
- Alert threshold configuration changed

## Error Codes
N/A

## Root Causes
1. The workspace was created (WorkspaceCreated)
2. The workspace was deleted (WorkspaceDeleted)
3. The alerts thresholds configuration was updated (WorkspaceAlertThresholdLevelUpdated)

## Remediation Steps
1. Review the audit log for WorkspaceCreated, WorkspaceDeleted, and WorkspaceAlertThresholdLevelUpdated activities
2. Ensure only authorized administrators can modify workspace settings

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a Global Administrator or Audit Administrator.
2. Navigate to Audit > Search.
3. Set the Date range to cover the period of the unexpected changes.
4. In the Activities list, select the following activities under the Microsoft Defender for Identity category:
   - WorkspaceCreated
   - WorkspaceDeleted
   - WorkspaceAlertThresholdLevelUpdated
5. Run the search and confirm that the audit log entries for these activities are present and match the expected changes.
6. Verify that the User field for each entry shows only authorized administrators (e.g., Global Administrators, Security Administrators).
7. If no unexpected entries are found, the remediation is successful.

## Rollback
1. If an unauthorized workspace was created: Contact Microsoft Support to delete the unauthorized workspace and restore the previous workspace configuration from backup or recreate it using documented settings.
2. If a workspace was deleted: Contact Microsoft Support to restore the deleted workspace from the Microsoft Defender for Identity service (note: workspace deletion may be irreversible; if so, recreate the workspace with the same configuration and reconnect sensors).
3. If alert thresholds were changed: Revert the threshold values to the previous known good configuration by editing the workspace settings in Microsoft Defender for Identity (https://portal.azure.com/#blade/Microsoft_Azure_DefenderforIdentity/WorkspaceSettings).
4. After restoration, re-run the audit log search to confirm no further unauthorized changes occur.
5. Review and tighten role assignments to ensure only authorized administrators have permissions to modify workspace settings.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
