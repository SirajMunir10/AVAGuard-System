# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to search for Dragon Copilot admin activities in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Dragon Copilot configured

## Symptoms
- Need to audit administrative changes to Dragon Copilot configuration

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search the audit log for Dragon Copilot admin activities using the Activities picker list.
2. Alternatively, run the Search-UnifiedAuditLog -RecordType DragonCopilotAdmin command in Exchange Online PowerShell.

## Validation
1. In the Microsoft 365 Purview compliance portal, navigate to Audit > Search. Under 'Activities', select 'Dragon Copilot admin activities' from the picker list and run a search for the relevant date range. Confirm that expected administrative events appear in the results.
2. Alternatively, connect to Exchange Online PowerShell and run: Search-UnifiedAuditLog -RecordType DragonCopilotAdmin -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date). Verify that the cmdlet returns audit records for Dragon Copilot admin actions.

## Rollback
1. If the audit search returns no results or incorrect data, verify that audit logging is enabled in the Purview portal under Audit > Audit log. If disabled, enable it by clicking 'Start recording user and admin activity'.
2. If the PowerShell command fails, ensure the Exchange Online PowerShell module is installed and you have the required permissions (e.g., Audit Log role). Re-run the command after confirming connectivity and permissions.
3. If the issue persists, refer to the official documentation at https://learn.microsoft.com/en-us/purview/audit-log-activities to confirm the correct RecordType and activity names.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
