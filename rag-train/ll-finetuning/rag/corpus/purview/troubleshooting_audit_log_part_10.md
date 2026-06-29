# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit when a form owner shares a form for copying via template link?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Form shared without authorization
- Unexpected template link generation

## Error Codes
N/A

## Root Causes
1. Form owner selected to generate the template URL

## Remediation Steps
1. Search audit log for 'Allowed share form for copy' activity
2. Review event details for form owner action

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with appropriate permissions. 2. Navigate to Audit > Audit log search. 3. Set the Activities filter to 'Allowed share form for copy'. 4. Set the Date range to cover the incident period. 5. Click Search. 6. In the results, locate the event where the form owner generated the template URL. 7. Select the event and review the details to confirm the form owner's action is recorded. 8. Verify that the 'Item' field shows the form name and the 'User' field shows the form owner's UPN.

## Rollback
1. If the audit log does not show the expected 'Allowed share form for copy' activity, verify that audit logging is enabled in the Microsoft 365 Defender portal (https://security.microsoft.com/auditlogsearch). 2. If audit logging is disabled, enable it by running: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true in Exchange Online PowerShell. 3. If the activity is still missing, check the Microsoft 365 Service Health Dashboard for any known issues with audit log ingestion. 4. As a last resort, contact Microsoft Support to investigate missing audit events.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
