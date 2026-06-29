# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit when a form owner connects a form to an Excel workbook?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Form data synced to unexpected Excel workbook
- Unauthorized Excel connection

## Error Codes
N/A

## Root Causes
1. Form owner connected the form to an Excel workbook

## Remediation Steps
1. Search audit log for 'Connected to Excel workbook' activity
2. Review the ExcelWorkbookLink property to identify the associated workbook

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search audit log. 2. Set 'Activities' to 'Connected to Excel workbook' and specify the date range. 3. Run the search and confirm that the 'ExcelWorkbookLink' property in the results shows the expected workbook URL. 4. Verify no unexpected workbook links appear in the results.

## Rollback
1. If the audit log shows an unauthorized Excel workbook link, instruct the form owner to open the form, go to Settings > Responses > Excel workbook, and disconnect the workbook. 2. Alternatively, use PowerShell: `Connect-ExchangeOnline` then `Set-Form -Identity <FormId> -ExcelWorkbookLink $null` to remove the link. 3. Re-run the audit log search to confirm the 'Connected to Excel workbook' activity no longer appears for that form.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
