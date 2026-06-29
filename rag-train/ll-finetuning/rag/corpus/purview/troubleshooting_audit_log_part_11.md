# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to detect when a form owner disables anonymous responses in Microsoft Forms?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Anonymous response setting changed unexpectedly
- Form no longer accepts anonymous responses

## Error Codes
N/A

## Root Causes
1. Form owner turned off the setting allowing anyone to respond to the form

## Remediation Steps
1. Search audit log for 'Disabled anyone can respond setting' activity
2. Verify the form owner who performed the action

## Validation
Search the Microsoft 365 Purview audit log for the activity 'Disabled anyone can respond setting' with the following PowerShell command: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations 'Disabled anyone can respond setting' | Format-Table CreationTime, UserIds, Operations, Item. Confirm that the audit log returns the expected event showing the form owner who disabled anonymous responses. Additionally, verify that the form's current anonymous response setting is disabled by checking the form's sharing settings in Microsoft Forms.

## Rollback
If the audit log does not show the expected event or the form owner needs to re-enable anonymous responses, instruct the form owner to sign in to Microsoft Forms, open the affected form, select 'Collect responses' > 'Anyone can respond', and set the toggle to 'On'. After re-enabling, run the validation command again to confirm the audit log captures the 'Enabled anyone can respond setting' activity.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
