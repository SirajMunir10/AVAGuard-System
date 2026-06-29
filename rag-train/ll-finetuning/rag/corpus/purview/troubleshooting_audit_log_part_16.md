# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate restore task details requests in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- User requested details of a restore task by its identifier

## Error Codes
N/A

## Root Causes
1. User programmatically accessed GetRestoreTaskDetails

## Remediation Steps
1. Review the audit log for GetRestoreTaskDetails activity
2. Verify user permissions and access controls

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with appropriate permissions (e.g., Audit Logs or View-Only Audit Logs role).
2. Navigate to Audit > Search audit log.
3. Set the 'Activities' filter to 'GetRestoreTaskDetails' (under the 'Backup' category).
4. Set the 'Start date' and 'End date' to cover the time of the reported incident.
5. Click 'Search' and confirm that the audit log returns entries for 'GetRestoreTaskDetails' activity, including the user who performed the action, the target restore task identifier, and the timestamp.
6. Verify that the audit records show the expected user and that the activity is logged with the correct details (e.g., 'Item' field contains the restore task ID).
7. Optionally, export the audit log results to a CSV file for further analysis.

## Rollback
1. If the audit log search reveals unauthorized or unexpected 'GetRestoreTaskDetails' activity, review the affected user's permissions in the Microsoft 365 Defender portal or Azure AD.
2. Remove or modify the user's access to the 'GetRestoreTaskDetails' operation by adjusting role assignments (e.g., remove the 'Backup Reader' or 'Backup Operator' role if assigned).
3. If the issue is due to a misconfigured application or script, revoke the application's permissions or update the script to use a service principal with least privilege.
4. To prevent recurrence, consider enabling alert policies for 'GetRestoreTaskDetails' activity (e.g., create a custom alert in the Microsoft 365 Defender portal).
5. If the audit log was inadvertently cleared or missing, restore from a backup of the audit log (if available) or re-enable audit logging if it was disabled (though this is unlikely given the context).

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
