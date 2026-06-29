# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to track creation or deletion of tenant-wide themes in SharePoint?

## Environment Context
- **Tenant Type:** SharePoint
- **Configuration:** Tenant-wide custom themes

## Symptoms
- Custom theme applied across SharePoint sites is missing or changed unexpectedly

## Error Codes
N/A

## Root Causes
1. A SharePoint administrator, global administrator, or brand manager created or deleted a custom theme

## Remediation Steps
1. Check audit log for TenantWideThemeCreated or TenantWideThemeDeleted activity
2. Identify who made the change
3. Reapply the correct custom theme if unauthorized deletion occurred

## Validation
Search the Purview audit log for TenantWideThemeCreated or TenantWideThemeDeleted events within the relevant time range. Use the following PowerShell command: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations 'TenantWideThemeCreated', 'TenantWideThemeDeleted' | Format-Table CreationDate, UserIds, Operations, AuditData. Confirm that the expected creation event exists and that no unauthorized deletion events are present. If a deletion event is found, verify that the theme has been reapplied by running Get-SPOHomeSite and Get-SPOMasterTheme to check the current tenant-wide theme.

## Rollback
If the remediation (reapplying the theme) fails or causes issues, restore the previous custom theme by using Set-SPOMasterTheme with the correct theme palette. First, retrieve the original theme details from a backup or from the audit log's AuditData field. Then run: Set-SPOMasterTheme -ThemePalette (Get-Content -Path 'path_to_backup_theme.json' -Raw). If the theme was deleted and no backup exists, recreate it using Add-SPOMasterTheme with the original parameters. After restoration, verify with Get-SPOMasterTheme.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
