# Implementation: Audit Log Retention

**Domain:** Purview
**Subdomain:** Audit Log Retention
**Incident Type:** Implementation

## Scenario / Query
How to create audit log retention policies to retain audit records for activities in services other than Microsoft Entra ID, Exchange, and SharePoint for up to one year?

## Environment Context
- **Tenant Type:** Office 365 or Microsoft 365 Enterprise with E5 licenses
- **Configuration:** Users assigned Office 365 E5 or Microsoft 365 E5 license (or users with a Microsoft Purview Suite or Microsoft 365 E5 eDiscovery and Audit add-on license)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Organizations can also create audit log retention policies to retain audit records for activities in other services for up to one year.
2. For more information, see Manage audit log retention policies

## Validation
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline. 2. Run Get-AuditLogRetentionPolicy to list all audit log retention policies. 3. Verify that a policy exists with the desired service activities (e.g., -RecordType not equal to AzureActiveDirectory, Exchange, SharePoint) and a RetentionDuration of 365 days. 4. Optionally, use Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-365) -EndDate (Get-Date) -RecordType <RecordType> to confirm that audit records older than 90 days are still searchable.

## Rollback
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline. 2. Identify the policy to remove or modify using Get-AuditLogRetentionPolicy. 3. To remove the policy, run Remove-AuditLogRetentionPolicy -Identity "<PolicyName>" -Confirm:$false. 4. To revert the retention duration, run Set-AuditLogRetentionPolicy -Identity "<PolicyName>" -RetentionDuration <OriginalValue>. 5. Verify the change with Get-AuditLogRetentionPolicy.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
