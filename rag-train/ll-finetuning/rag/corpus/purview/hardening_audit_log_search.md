# Hardening: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Hardening

## Scenario / Query
How to monitor changes to Teams security settings like video calling, screen sharing, and content rating?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Unauthorized changes to Teams security settings

## Error Codes
N/A

## Root Causes
1. The TeamsTenantSettingChanged operation logs changes to settings such as video calling, screen sharing, and content rating

## Remediation Steps
1. Search the audit log for TeamsTenantSettingChanged operations
2. Review the Item column for descriptions like 'Video for Skype meetings', 'Screen sharing for Skype meetings', or 'Content rating'

## Validation
Search the audit log for TeamsTenantSettingChanged operations using the Purview compliance portal or Search-UnifiedAuditLog cmdlet. Verify that the Item column contains descriptions such as 'Video for Skype meetings', 'Screen sharing for Skype meetings', or 'Content rating'. Confirm that the audit log captures the expected changes and that the search returns results for the relevant time period.

## Rollback
If the audit log search fails to return expected results, verify that audit logging is enabled in the Microsoft 365 Defender portal under Audit log. If disabled, enable it by toggling the setting. If the search is not returning TeamsTenantSettingChanged events, ensure the user performing the search has the appropriate permissions (e.g., Audit Logs role). If the issue persists, review the audit log retention policy and consider extending the search date range. No direct rollback of the remediation is required as the remediation is a monitoring action.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
