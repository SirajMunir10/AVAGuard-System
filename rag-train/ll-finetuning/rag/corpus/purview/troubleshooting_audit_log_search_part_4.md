# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
Why are audit records not appearing in audit log search results after an event occurs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Audit records are not returned in the results of an audit log search after an event occurs

## Error Codes
N/A

## Root Causes
1. For core services (such as Exchange, SharePoint, OneDrive, and Teams), audit record availability is typically 60 to 90 minutes after an event occurs
2. For other services, audit record availability might be longer
3. Some issues that are unavoidable (such as a server outage) might occur outside of the audit service that delays the availability of audit records

## Remediation Steps
1. Wait for the typical availability window of 60 to 90 minutes for core services
2. For other services, allow additional time for audit record availability
3. Check for any server outages that might affect the audit service

## Validation
1. Wait at least 90 minutes after the event occurred. 2. Run an audit log search in the Microsoft Purview compliance portal (https://compliance.microsoft.com/auditlogsearch) for the specific event time and user. 3. Verify that the expected audit records appear in the search results. 4. If records still do not appear, check the Microsoft 365 Service Health Dashboard (https://admin.microsoft.com/Adminportal/Home#/servicehealth) for any reported outages or advisories related to the audit service.

## Rollback
1. If audit records still do not appear after the recommended wait time, extend the wait period by an additional 30–60 minutes for non-core services. 2. If a server outage is identified, wait for the service to be restored as indicated by the Service Health Dashboard. 3. No configuration changes were made, so no direct rollback is required; continue monitoring the audit log search results periodically until records appear.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
