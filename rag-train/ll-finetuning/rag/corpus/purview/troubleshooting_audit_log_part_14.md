# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and audit coauthor activities in Microsoft Forms from the audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Coauthor activities recorded with user ID format urn:forms:coauthor#a0b1c2d3@forms.office.com
- User ID includes a hash that differs for different users

## Error Codes
N/A

## Root Causes
1. Coauthor activities are logged with a hashed user ID to anonymize the coauthor's identity

## Remediation Steps
1. Search the audit log for activities with the user ID prefix urn:forms:coauthor#
2. Note that the second part of the User ID is a hash, which differs for different users

## Validation
1. Run the following audit log search command in the Microsoft 365 Purview compliance portal or via Search-UnifiedAuditLog in Exchange Online PowerShell:
   Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -UserIds "urn:forms:coauthor#*"
2. Verify that the returned results include entries with UserId starting with 'urn:forms:coauthor#' and that the second part of the UserId (after '#') is a hash (e.g., a0b1c2d3@forms.office.com).
3. Confirm that the audit log shows coauthor activities (e.g., FormEdited, FormResponded) with the expected hashed user ID format.

## Rollback
1. If the remediation causes unexpected filtering or missing audit data, revert to the default audit log search without the UserId filter:
   Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date)
2. Ensure that no custom audit log retention policies or exclusions were inadvertently applied that could block coauthor activity logging. If any were changed, restore them to the previous configuration.
3. If the issue persists, contact Microsoft Support to verify that the audit log is capturing coauthor activities correctly and that the hashed UserId format is expected behavior.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
