# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify security risks detected during incoming calls in Microsoft Teams?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Security risk detected during an incoming call in Microsoft Teams

## Error Codes
N/A

## Root Causes
1. Security risk detected during an incoming call in Microsoft Teams, such as brand, domain, or user impersonation

## Remediation Steps
1. Search for SecurityRiskInCallDetected activity in audit log
2. Review the details of the detected security risk

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user with the Audit Log role. 2. Navigate to Solutions > Audit or go directly to https://compliance.microsoft.com/auditlogsearch. 3. Under the Search tab, set the Date range to cover the time of the reported incident. 4. In the Activities list, search for and select 'SecurityRiskInCallDetected' (under the 'Security' category). 5. Click Search and verify that one or more audit log entries appear. 6. Select an audit log entry and review the Details pane to confirm the 'SecurityRiskInCallDetected' activity, including the risk type (e.g., brand impersonation, domain impersonation, user impersonation) and the affected user or call details.

## Rollback
1. If the audit log search returns no results or incorrect data, verify that Audit Log Search is enabled in the Microsoft 365 Defender portal (https://security.microsoft.com/auditlogsearch?view=auditlogsearch) under 'Audit log search' settings. 2. Ensure the user performing the search has the 'Audit Logs' role assigned in the Microsoft Purview compliance portal (Roles & scopes > Permissions > Audit Log role). 3. If the activity is not listed, confirm that the tenant has the required Microsoft 365 E5/A5/G5 or Microsoft 365 E5/A5/G5 Compliance license. 4. If the issue persists, run the following PowerShell command to search for the same activity: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations 'SecurityRiskInCallDetected' | Format-Table CreationDate, UserIds, Operations, AuditData. 5. If no results are still found, contact Microsoft Support with the tenant ID and time range of the incident.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
