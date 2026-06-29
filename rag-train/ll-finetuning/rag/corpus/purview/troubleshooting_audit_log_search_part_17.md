# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit changes to Teams meeting scheduling settings?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Changes to private or channel meeting scheduling permissions

## Error Codes
N/A

## Root Causes
1. The TeamsTenantSettingChanged operation logs changes to meeting scheduling settings

## Remediation Steps
1. Search the audit log for TeamsTenantSettingChanged operations
2. Review the Item column for descriptions like 'Private meeting scheduling' or 'Channel meeting scheduling'

## Validation
Search the audit log for TeamsTenantSettingChanged operations and verify that the Item column contains descriptions such as 'Private meeting scheduling' or 'Channel meeting scheduling'. Use the following command: Search-UnifiedAuditLog -Operations TeamsTenantSettingChanged -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) | Select-Object CreationDate, UserIds, Operations, Item | Format-Table -AutoSize

## Rollback
If the audit log search fails or returns unexpected results, verify that audit logging is enabled by running: Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled. If disabled, enable it with: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true. Then re-run the search command. If the issue persists, check the source documentation at https://learn.microsoft.com/en-us/purview/audit-log-activities for additional troubleshooting steps.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
