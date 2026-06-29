# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How do I search for specific activities in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search the audit log in the Microsoft Purview portal.
2. Select one of the links in the 'In this article' list to go directly to a specific product table.
3. Use the friendly name displayed in the Activities drop-down list or the corresponding operation name in PowerShell commands.

## Validation
1. In the Microsoft Purview portal, navigate to Audit > Search. 2. From the Activities drop-down list, select a specific activity (e.g., 'Deleted file') and set a date range. 3. Run the search and confirm that results display the expected events. 4. Alternatively, run the PowerShell command: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations 'FileDeleted' and verify that the output contains the expected audit records.

## Rollback
1. If the search returns no results or incorrect data, verify that audit logging is enabled: in the Purview portal, go to Audit > Audit retention policies and ensure 'Audit logging' is turned on. 2. If using PowerShell, run: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true. 3. Check that the user performing the search has the 'Audit Logs' role assigned in the Purview portal under Roles & scopes. 4. If the issue persists, clear the browser cache or use an InPrivate/Incognito session to access the Purview portal.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
