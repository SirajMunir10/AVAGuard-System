# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate Office on Demand enablement in SharePoint?

## Environment Context
- **Tenant Type:** SharePoint
- **Configuration:** Office on Demand

## Symptoms
- Users unable to access latest Office desktop applications from SharePoint
- Office on Demand feature enabled or disabled unexpectedly

## Error Codes
N/A

## Root Causes
1. Site administrator enabled Office on Demand

## Remediation Steps
1. Review audit log for OfficeOnDemandSet activity
2. Identify the site administrator who made the change
3. Reconfigure Office on Demand settings if needed

## Validation
1. Run the following command in the Security & Compliance PowerShell to search the audit log for OfficeOnDemandSet events in the last 90 days: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) -Operations OfficeOnDemandSet -ResultSize 1000 | Format-Table CreationTime, UserIds, Operations, SiteUrl. 2. Confirm that the output shows the expected reconfiguration activity (e.g., the site administrator who made the change and the corrected settings). 3. Verify that users can now access the latest Office desktop applications from SharePoint by navigating to a document library and selecting 'Open in Desktop App'.

## Rollback
1. If the remediation fails or causes issues, identify the original OfficeOnDemandSet audit log entry to retrieve the previous configuration. 2. Re-run the same OfficeOnDemandSet operation with the original settings by having the site administrator or a global admin use the SharePoint Online Management Shell: Set-SPOTenant -OfficeOnDemandEnabled $true (or $false as needed). 3. Confirm the rollback by repeating the validation steps to ensure the audit log shows the reversal and users experience the original behavior.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
