# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to differentiate between PagePrefetched and PageViewed events in SharePoint and OneDrive audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- PagePrefetched events logged without corresponding PageViewed events
- Uncertainty whether a user actually navigated to a page

## Error Codes
N/A

## Root Causes
1. PagePrefetched indicates a client request for page content to improve performance, not definitive user navigation; a ClientViewSignaled event indicates actual rendering

## Remediation Steps
1. Check for ClientViewSignaled events to confirm user navigation
2. Note that some clients may log prefetched activities as PageViewed events instead

## Validation
1. Run a unified audit log search for the user and time range in question. Filter by workload 'SharePoint' or 'OneDrive' and look for 'ClientViewSignaled' events. If present, the user navigated to the page. 2. Check for 'PagePrefetched' events and confirm they are not accompanied by a 'PageViewed' event. 3. Verify that 'PageViewed' events are logged only when a user actually navigates to a page, not during prefetch operations.

## Rollback
1. If validation shows that 'ClientViewSignaled' events are missing but user navigation is still suspected, review client-side telemetry or browser logs to confirm actual page rendering. 2. If 'PageViewed' events are incorrectly logged due to prefetch, adjust client or server settings to prevent prefetch from triggering 'PageViewed' events. 3. If needed, contact Microsoft Support for further investigation into audit log inconsistencies.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
