# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How to export and view Exchange admin audit log records?

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
1. Select the Download all results option to export the search results and get information about what cmdlet was run, which parameters and parameter values were used, and what objects were affected.
2. For more information, see Export, configure, and view audit log records.
3. Use the Search-UnifiedAuditLog -RecordType ExchangeAdmin command in Exchange Online PowerShell to return only audit records from the Exchange admin audit log.
4. For information about exporting the search results returned by the Search-UnifiedAuditLog cmdlet to a CSV file, see the 'Tips for exporting and viewing the audit log' section in Export, configure, and view audit log records.

## Validation
1. Connect to Exchange Online PowerShell. 2. Run: Search-UnifiedAuditLog -RecordType ExchangeAdmin -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) | Format-Table Operations, UserIds, Parameters, ResultStatus -AutoSize. 3. Confirm that audit records are returned showing cmdlet operations, parameters, and affected objects. 4. Verify that the 'Download all results' option is available in the Purview compliance portal audit log search UI and that exported CSV contains columns: CreationDate, UserIds, Operations, Parameters, ResultStatus.

## Rollback
1. If audit records are not returned, verify that Exchange admin audit logging is enabled by running: Get-AdminAuditLogConfig | Format-List AdminAuditLogEnabled. 2. If disabled, enable it with: Set-AdminAuditLogConfig -AdminAuditLogEnabled $true. 3. If the 'Download all results' option is missing, ensure you have the Audit Logs role in the Purview compliance portal (assign via Compliance Center permissions). 4. If CSV export fails, try exporting a smaller date range or use: Search-UnifiedAuditLog -RecordType ExchangeAdmin -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) | Export-Csv -Path 'ExchangeAdminAudit.csv' -NoTypeInformation.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/purview/audit-log-activities#exchange-admin-activities>
- <https://learn.microsoft.com/en-us/purview/audit-log-activities#tips-for-exporting-and-viewing-the-audit-log>
