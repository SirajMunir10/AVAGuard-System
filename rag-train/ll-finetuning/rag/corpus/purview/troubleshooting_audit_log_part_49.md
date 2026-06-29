# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to find when a user requests site admin permissions in audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- User requests to be added as a site collection administrator

## Error Codes
N/A

## Root Causes
1. User initiated a request for full control permissions for the site collection and all subsites

## Remediation Steps
1. Search for all activities in the audit log
2. Look for the activity 'Requested site admin permissions' with the operation 'SiteAdminChangeRequest'

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search audit log. 2. Set the 'Activities' filter to 'Requested site admin permissions' (operation 'SiteAdminChangeRequest'). 3. Set the date range to cover the incident timeframe. 4. Run the search and confirm that entries with the user's UPN and the activity 'Requested site admin permissions' appear. 5. Verify that the 'Item' field shows the site URL and that the 'Operation' field is 'SiteAdminChangeRequest'.

## Rollback
1. If the audit search returns no results, verify that audit logging is enabled in the Microsoft 365 Defender portal > Audit log search. 2. If disabled, enable audit log search via PowerShell: `Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true`. 3. Wait up to 24 hours for logs to populate, then re-run the search. 4. If the activity is still missing, check that the user's license includes audit log retention (e.g., E5/A5/G5). 5. As a last resort, contact Microsoft Support to investigate missing audit records.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
