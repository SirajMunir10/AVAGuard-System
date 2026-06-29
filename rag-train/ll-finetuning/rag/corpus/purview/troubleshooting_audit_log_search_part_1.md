# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that audit log search is turned on for Microsoft 365 or Office 365 enterprise organizations?

## Environment Context
- **Tenant Type:** Microsoft 365 or Office 365 enterprise
- **Configuration:** UnifiedAuditLogIngestionEnabled property

## Symptoms
- Unable to search audit log
- UnifiedAuditLogIngestionEnabled property shows False in Security & Compliance PowerShell

## Error Codes
N/A

## Root Causes
1. Audit log search may be turned off
2. Running Get-AdminAuditLogConfig in Security & Compliance PowerShell instead of Exchange Online PowerShell

## Remediation Steps
1. Run the following command in Exchange Online PowerShell: Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled
2. Ensure the value of UnifiedAuditLogIngestionEnabled is True

## Validation
The value of True for the UnifiedAuditLogIngestionEnabled property indicates that audit log search is turned on.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
