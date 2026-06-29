# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify allowed and blocked URL navigation events in Microsoft Edge from audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** WebContentFiltering feature in Microsoft Edge

## Symptoms
- Need to audit specific URL navigation events

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search for Allowed URL Navigation in Microsoft Edge using the operation URLNavigationAllowed.
2. Search for Blocked URL Navigation in Microsoft Edge using the operation URLNavigationBlocked.

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user with the Audit Logs role. 2. Navigate to Solutions > Audit. 3. Under the Search tab, set the Activities filter to 'URLNavigationAllowed' and 'URLNavigationBlocked' (these appear under 'WebContentFiltering' category). 4. Set a date range that covers the period after remediation. 5. Click Search. 6. Verify that the results include entries for 'URLNavigationAllowed' and 'URLNavigationBlocked' with the expected URLs and timestamps. 7. Optionally, use the Search-UnifiedAuditLog PowerShell cmdlet: `Search-UnifiedAuditLog -Operations URLNavigationAllowed,URLNavigationBlocked -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date)` and confirm output contains the relevant events.

## Rollback
1. If the audit search returns no results or incorrect data, verify that the WebContentFiltering feature is enabled in Microsoft Edge (via Group Policy or Intune). 2. Ensure that audit logging is enabled for the tenant (by default it is, but can be verified via the Audit log settings in the Purview portal). 3. If the issue persists, contact Microsoft Support to check for service health or throttling issues. 4. No direct rollback of the search is possible; instead, re-run the search with a broader date range or different filters to confirm data availability.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
