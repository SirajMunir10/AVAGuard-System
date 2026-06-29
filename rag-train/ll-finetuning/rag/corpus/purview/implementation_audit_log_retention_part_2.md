# Implementation: Audit Log Retention

**Domain:** Purview
**Subdomain:** Audit Log Retention
**Incident Type:** Implementation

## Scenario / Query
How to determine the default retention period for Audit (Standard) logs based on the generation date?

## Environment Context
- **Tenant Type:** Office 365 or Microsoft 365 Enterprise
- **Configuration:** Audit (Standard) logs

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Audit (Standard) logs generated before October 17, 2023 are retained for 90 days.
2. Audit (Standard) logs generated on or after October 17, 2023 follow the new default retention of 180 days.

## Validation
1. Use Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-181) -EndDate (Get-Date).AddDays(-1) to verify that logs older than 180 days are not returned for events generated on or after October 17, 2023. 2. Use Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-91) -EndDate (Get-Date).AddDays(-1) to confirm logs older than 90 days are not returned for events generated before October 17, 2023. 3. Check the audit log retention policy in the Microsoft Purview compliance portal: Audit > Audit retention policies to ensure no custom policies override the default.

## Rollback
1. If the default retention period is incorrectly applied, create a custom audit retention policy in the Microsoft Purview compliance portal (Audit > Audit retention policies) to set the desired retention period (e.g., 90 days for all logs). 2. Use New-AuditConfigurationPolicy -RetentionDuration 90 -Scope All to enforce a 90-day retention for all audit logs. 3. Monitor the change using Get-AuditConfigurationPolicy to confirm the policy is active.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
