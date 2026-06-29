# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How do I use PowerShell to search the audit log with operation names that contain a period?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Some operation names contain a period (.).

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Include the period in the operation name when specifying it in a PowerShell command.
2. Use double quotation marks (" ") to contain the operation name.

## Validation
Run the following PowerShell command to confirm that audit log entries with operation names containing a period are returned: Search-UnifiedAuditLog -Operations "FileAccessed", "FileModified" -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) | Format-Table CreationDate, Operations, UserIds, -AutoSize. Then verify that the output includes entries where the Operations field contains a period (e.g., "File.Uploaded").

## Rollback
If the remediation causes unexpected results, revert to the previous method by removing the double quotation marks around the operation name and escaping the period with a backtick (`) character. For example, use Search-UnifiedAuditLog -Operations File`.Uploaded instead of Search-UnifiedAuditLog -Operations "File.Uploaded". Then run the same validation command to confirm the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
