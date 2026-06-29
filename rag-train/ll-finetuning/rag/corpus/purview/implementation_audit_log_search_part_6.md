# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to get started with searching the audit log in Microsoft Purview?

## Environment Context
- **Tenant Type:** large tenant with high number of users
- **Configuration:** Audit solution card must be available in Microsoft Purview portal

## Symptoms
- Audit solution card not displayed in Microsoft Purview portal
- Search jobs in large tenants may take up to 48 hours to complete

## Error Codes
N/A

## Root Causes
1. Audit solution card may not be visible if not selected from 'View all solutions'
2. Broadly-scoped Search jobs in large tenants with high number of users can take up to 48 hours

## Remediation Steps
1. Sign in to the Microsoft Purview portal
2. Select the Audit solution card
3. If the Audit solution card isn't displayed, select View all solutions and then select Audit from the Core section
4. On the Search page, configure the following search criteria as applicable: Date and time range (UTC), Keyword Search, Admin Units, Activities - friendly names

## Validation
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com).
2. Verify that the Audit solution card is displayed on the home page. If not, select 'View all solutions' and confirm that 'Audit' appears under the Core section.
3. Click the Audit card to open the Search page.
4. Configure a test search with a narrow date/time range (e.g., last 24 hours) and a specific activity (e.g., 'User logged in').
5. Run the search and confirm that results are returned within a reasonable time (note: for large tenants, results may take up to 48 hours; if no results appear immediately, wait and re-run after 48 hours).
6. Verify that the search results include expected audit records and that the search job status shows as completed.

## Rollback
1. If the Audit solution card is still not visible after following the remediation steps, ensure the user has the necessary permissions (e.g., Audit Log role or View-Only Audit Logs role).
2. If the search job fails or returns no results, reduce the scope of the search (e.g., use a shorter date range, fewer activities, or filter by admin unit).
3. If the issue persists, clear browser cache and cookies, then re-sign in to the Purview portal.
4. As a last resort, contact Microsoft Support for tenant-specific configuration issues.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
