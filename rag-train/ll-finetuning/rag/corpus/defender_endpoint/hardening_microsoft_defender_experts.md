# Hardening: Microsoft Defender Experts

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Experts
**Incident Type:** Hardening

## Scenario / Query
How to audit when Defender Experts analyst permissions are created or modified?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft 365 audit log must be enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search the audit log for DefenderExpertsAnalystPermissionCreated activity to identify when an administrator granted one or more role permissions to Defender Experts analysts to investigate incidents or remediate threats.
2. Search the audit log for DefenderExpertsAnalystPermissionModified activity to identify when an administrator modified role permissions for Defender Experts analysts to investigate incidents or remediate threats.

## Validation
1. Confirm Microsoft 365 audit log is enabled: Run `Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) -Operations DefenderExpertsAnalystPermissionCreated -ResultSize 1` in Exchange Online PowerShell. If no results, audit logging may be disabled or no such events occurred. 2. Verify DefenderExpertsAnalystPermissionModified events: Run `Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) -Operations DefenderExpertsAnalystPermissionModified -ResultSize 1`. 3. For each event found, review the AuditData property to confirm the user, role, and timestamp match expected changes.

## Rollback
1. If unauthorized permission creation is detected, remove the assigned role: In Microsoft 365 Defender, go to Settings > Endpoints > Permissions > Roles, locate the role assigned to Defender Experts analysts, and remove the analyst or group. 2. If unauthorized permission modification is detected, revert the role to its previous state: Use the audit log to identify the previous role configuration, then in Microsoft 365 Defender > Settings > Endpoints > Permissions > Roles, edit the role to restore original permissions. 3. If audit log was disabled, enable it: In Microsoft 365 Purview compliance portal, go to Audit > Audit log, and turn on auditing if off.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
