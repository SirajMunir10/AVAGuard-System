# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How to use PowerShell to search the Exchange admin audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange admin audit logging enabled by default

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Search-UnifiedAuditLog -RecordType ExchangeAdmin command in Exchange Online PowerShell to return only audit records from the Exchange admin audit log.
2. For more information, see Search-UnifiedAuditLog.
3. For information about exporting the search results returned by the Search-UnifiedAuditLog cmdlet to a CSV file, see the 'Tips for exporting and viewing the audit log' section in Export, configure, and view audit log records.

## Validation
1. Connect to Exchange Online PowerShell using 'Connect-ExchangeOnline -UserPrincipalName admin@contoso.com'. 2. Run 'Search-UnifiedAuditLog -RecordType ExchangeAdmin -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date)' and verify that the output contains only records where the 'RecordType' property equals 'ExchangeAdmin'. 3. Confirm that the 'Operations' field includes expected Exchange admin actions (e.g., Set-Mailbox, New-Mailbox). 4. Optionally, export results to CSV using 'Search-UnifiedAuditLog -RecordType ExchangeAdmin -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) | Export-Csv -Path 'ExchangeAdminAudit.csv' -NoTypeInformation' and verify the file contains the expected columns.

## Rollback
1. If the search returns unexpected or incomplete results, verify that the user account has the 'View-Only Audit Logs' or 'Audit Logs' role assigned in the Microsoft 365 Purview compliance portal. 2. Ensure the 'Exchange admin audit logging' setting is enabled by running 'Get-AdminAuditLogConfig | Format-List AdminAuditLogEnabled' in Exchange Online PowerShell; if disabled, enable it with 'Set-AdminAuditLogConfig -AdminAuditLogEnabled $true'. 3. If the cmdlet fails, disconnect and reconnect the session using 'Disconnect-ExchangeOnline' then 'Connect-ExchangeOnline -UserPrincipalName admin@contoso.com'. 4. For persistent issues, refer to the official documentation at https://learn.microsoft.com/en-us/powershell/module/exchange/search-unifiedauditlog for parameter troubleshooting.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/purview/audit-log-activities#exchange-admin-activities>
- <https://learn.microsoft.com/en-us/powershell/module/exchange/search-unifiedauditlog>
