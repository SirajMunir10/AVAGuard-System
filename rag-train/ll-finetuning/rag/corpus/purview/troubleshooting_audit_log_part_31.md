# Troubleshooting: Audit Log (ResultStatus.Failure)

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify failed roster creation operations in Microsoft Planner audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- RosterCreated operation shows ResultStatus.Failure or ResultStatus.AuthorizationFailure

## Error Codes
- `ResultStatus.Failure`
- `ResultStatus.AuthorizationFailure`

## Root Causes
1. Failed roster creation results in ObjectId being null and MemberIds being an empty string

## Remediation Steps
1. Check the ObjectId and MemberIds fields in audit records for RosterCreated failures

## Validation
Search the unified audit log for RosterCreated operations with ResultStatus of Failure or AuthorizationFailure. Use Search-UnifiedAuditLog -Operations RosterCreated -ResultSize 1000 | Where-Object {$_.ResultStatus -eq 'Failure' -or $_.ResultStatus -eq 'AuthorizationFailure'} | Format-List AuditData. Confirm that the AuditData JSON for each failed record contains ObjectId set to null and MemberIds set to an empty string. If no such records exist, the remediation is successful.

## Rollback
No rollback is required because the remediation is read-only verification. If the verification reveals that the issue persists, re-enable audit logging by running Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true and ensure the audit log search is properly configured per https://learn.microsoft.com/en-us/purview/audit-log-enable-disable.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
