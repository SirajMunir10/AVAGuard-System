# Troubleshooting: Information Barriers (Status: IBPolicyConflict)

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Information Barriers policy application failures using audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies

## Symptoms
- Information Barriers policy application failure

## Error Codes
- `Status: IBPolicyConflict`

## Root Causes
1. User was included in more than one segment

## Remediation Steps
1. Search in the audit log for <application guid> using PowerShell: $detailedLogs = Search-UnifiedAuditLog -EndDate <yyyy-mm-ddThh:mm:ss> -StartDate <yyyy-mm-ddThh:mm:ss> -RecordType InformationBarrierPolicyApplication -ResultSize 1000 |?{$_.AuditData.Contains(<application guid>)}
2. Check the detailed output from the audit log for the values of the UserId and ErrorDetails fields using: $detailedLogs[1] | FL
3. Fix the issue by updating segment membership using the Set-OrganizationSegment cmdlet together with the UserGroupFilter parameter
4. Reapply Information Barriers policies

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
