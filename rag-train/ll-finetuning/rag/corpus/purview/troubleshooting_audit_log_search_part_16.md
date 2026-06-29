# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit changes to Teams bot and extension settings?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Unexpected changes to bot or extension permissions in Teams

## Error Codes
N/A

## Root Causes
1. The TeamsTenantSettingChanged operation logs changes to bot and extension settings

## Remediation Steps
1. Search the audit log for TeamsTenantSettingChanged operations
2. Review the Item column for descriptions like 'Org-wide bots', 'Individual bots', 'Extensions or tabs', or 'Side loading of Bots'

## Validation
Search the audit log for TeamsTenantSettingChanged operations with the following command: Search-UnifiedAuditLog -Operations TeamsTenantSettingChanged -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date). Then review the Item column in the results for descriptions such as 'Org-wide bots', 'Individual bots', 'Extensions or tabs', or 'Side loading of Bots' to confirm that changes to bot and extension settings are being logged.

## Rollback
If the audit log search fails or returns no results, verify that audit logging is enabled in the Microsoft 365 compliance center by running: Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled. If it is not enabled, enable it with: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true. Then re-run the search command from the validation step.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
