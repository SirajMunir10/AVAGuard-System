# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify changes to Teams tenant settings in the audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Changes to Teams org-wide settings are not visible in audit log search results

## Error Codes
N/A

## Root Causes
1. The TeamsTenantSettingChanged operation is logged when a global admin changes Teams settings in the Microsoft 365 admin center

## Remediation Steps
1. Search the audit log for the TeamsTenantSettingChanged operation
2. Review the Item column for a description of the setting that was changed (shown in parentheses)

## Validation
1. Sign in to the Microsoft 365 Purview compliance portal (https://compliance.microsoft.com) as a global admin. 2. Navigate to Audit > Audit log search. 3. Set the Activities filter to 'TeamsTenantSettingChanged'. 4. Set the Date range to cover the time period when the change was made. 5. Click Search. 6. In the results, select a record and review the Item column to confirm it contains a description of the setting that was changed (e.g., 'Allow private meetings (True)'). 7. Verify that the record includes the user who made the change and the timestamp.

## Rollback
1. If the TeamsTenantSettingChanged operation is not appearing in audit log search results, verify that audit logging is enabled in the Microsoft 365 admin center: go to Security & Compliance > Audit log > Turn on auditing. 2. If audit logging is already enabled, ensure the user performing the search has the 'Audit Logs' role in the Purview compliance portal (e.g., Audit Logs or View-Only Audit Logs). 3. If the change was made outside the Microsoft 365 admin center (e.g., via PowerShell or Teams admin center), note that the TeamsTenantSettingChanged operation may not be logged; instead, search for other activities such as 'Set-CsTenant' or 'Set-CsTeamsMeetingPolicy'. 4. If the change is still not found, contact Microsoft Support to investigate potential data latency or ingestion issues.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
