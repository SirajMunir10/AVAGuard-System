# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and investigate Universal Print management activities in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Universal Print service enabled

## Symptoms
- Unexpected changes to printer shares or access controls
- Unregistered connectors or printers
- Suspicious modifications to tenant print settings

## Error Codes
N/A

## Root Causes
1. Unauthorized user actions on Universal Print resources
2. Misconfiguration of printer shares or pull-print printers
3. Connector registration issues

## Remediation Steps
1. Search the audit log for activities such as ShareCreated, ShareDeleted, ShareAccessControlGroupAdded, ShareAccessControlUserAdded, ShareAccessControlAllowAllEnabled, ShareAccessControlAllowAllDisabled, PrinterSettingsModified, ShareSettingsModified, PullPrintPrinterSettingsModified, TenantPrintSettingsModified, ConnectorRegistered, PrinterRegistered, PrinterSwapped, ReportDownloaded, PullPrintPrinterCreated, PullPrintPrinterDeleted, PullPrintPrinterMemberAdded, PullPrintPrinterMemberRemoved, PullPrintPrinterIncludeAllPrintersEnabled, PullPrintPrinterIncludeAllPrintersDisabled
2. Review the audit log entries for the specific activity to identify the user, timestamp, and affected resource
3. Take corrective action based on the activity, such as reverting unauthorized changes or re-registering connectors

## Validation
1. Connect to Exchange Online PowerShell: Connect-ExchangeOnline -UserPrincipalName admin@contoso.com
2. Search the audit log for Universal Print activities: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations ShareCreated, ShareDeleted, ShareAccessControlGroupAdded, ShareAccessControlUserAdded, ShareAccessControlAllowAllEnabled, ShareAccessControlAllowAllDisabled, PrinterSettingsModified, ShareSettingsModified, PullPrintPrinterSettingsModified, TenantPrintSettingsModified, ConnectorRegistered, PrinterRegistered, PrinterSwapped, ReportDownloaded, PullPrintPrinterCreated, PullPrintPrinterDeleted, PullPrintPrinterMemberAdded, PullPrintPrinterMemberRemoved, PullPrintPrinterIncludeAllPrintersEnabled, PullPrintPrinterIncludeAllPrintersDisabled -ResultSize 1000
3. Verify that the audit log returns entries for the expected activities and that no unauthorized activities appear after remediation.
4. For each suspicious entry, confirm the user, timestamp, affected resource, and that corrective actions (e.g., reverting changes) have been applied.

## Rollback
1. If the audit log search fails or returns unexpected results, re-run the search with broader date range or without operation filters: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-30) -EndDate (Get-Date) -Operations ShareCreated, ShareDeleted, ShareAccessControlGroupAdded, ShareAccessControlUserAdded, ShareAccessControlAllowAllEnabled, ShareAccessControlAllowAllDisabled, PrinterSettingsModified, ShareSettingsModified, PullPrintPrinterSettingsModified, TenantPrintSettingsModified, ConnectorRegistered, PrinterRegistered, PrinterSwapped, ReportDownloaded, PullPrintPrinterCreated, PullPrintPrinterDeleted, PullPrintPrinterMemberAdded, PullPrintPrinterMemberRemoved, PullPrintPrinterIncludeAllPrintersEnabled, PullPrintPrinterIncludeAllPrintersDisabled -ResultSize 5000
2. If corrective actions (e.g., reverting changes) caused issues, restore the previous configuration using the audit log details: For example, if a share was deleted, recreate it with the original settings from the audit log entry.
3. If a connector was unregistered, re-register it using the connector setup instructions from the Universal Print admin center.
4. If tenant print settings were modified, reset them to the previous values documented in the audit log.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
