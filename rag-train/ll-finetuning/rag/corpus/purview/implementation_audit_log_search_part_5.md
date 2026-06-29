# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to enable auditing for Power BI activities in the audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Power BI admin portal

## Symptoms
- Power BI activities are not appearing in audit log search results

## Error Codes
N/A

## Root Causes
1. Auditing is not enabled in the Power BI admin portal

## Remediation Steps
1. Enable auditing in the Power BI admin portal
2. See the 'Audit logs' section in Power BI admin portal for instructions

## Validation
1. Sign in to the Power BI admin portal (https://app.powerbi.com/admin-portal) as a Global Admin or Power BI Admin.
2. Navigate to 'Tenant settings' > 'Audit logs'.
3. Verify that the 'Audit logs' toggle is set to 'Enabled'.
4. Wait up to 24 hours for audit data to propagate.
5. Run a unified audit log search in the Microsoft 365 Defender portal (https://security.microsoft.com/auditlogsearch) with the following parameters:
   - Date range: Last 24 hours
   - Activities: Select 'Power BI activities' or specific Power BI operations.
   - Users: Leave blank to include all users.
6. Execute the search and confirm that Power BI activities appear in the results.

## Rollback
1. Sign in to the Power BI admin portal (https://app.powerbi.com/admin-portal) as a Global Admin or Power BI Admin.
2. Navigate to 'Tenant settings' > 'Audit logs'.
3. Set the 'Audit logs' toggle to 'Disabled'.
4. Confirm the change by selecting 'Apply'.
5. Note that disabling audit logging will stop the collection of Power BI audit events, and existing audit logs will be retained according to your organization's retention policy.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
