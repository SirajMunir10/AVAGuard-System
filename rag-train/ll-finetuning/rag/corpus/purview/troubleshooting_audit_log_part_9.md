# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify when a form owner deletes a form in Microsoft Forms using audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Form deleted unexpectedly
- Missing form data

## Error Codes
N/A

## Root Causes
1. Form owner performed a SoftDelete or HardDelete action

## Remediation Steps
1. Search audit log for 'Deleted form' activity
2. Check if action was SoftDelete (form moved to recycle bin) or HardDelete (recycle bin emptied)

## Validation
Search the Microsoft 365 Purview audit log for the 'Deleted form' activity. Use the following PowerShell command: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) -Operations 'Deleted form' -FormType 'Microsoft Forms'. Confirm the audit record shows the form owner's UserId, the ItemName (form name), and the Detail field indicating whether the action was SoftDelete (form moved to recycle bin) or HardDelete (recycle bin emptied). Verify the form is no longer visible in the owner's Forms dashboard or recycle bin if HardDelete.

## Rollback
If the deletion was a SoftDelete, restore the form from the recycle bin within 30 days: In Microsoft Forms, the owner can go to the recycle bin, select the form, and choose 'Restore'. If the deletion was a HardDelete, the form cannot be recovered via the UI; contact Microsoft Support within 14 days to attempt recovery from backup. If the audit log shows unauthorized deletion, reset the form owner's password and revoke suspicious sessions.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
