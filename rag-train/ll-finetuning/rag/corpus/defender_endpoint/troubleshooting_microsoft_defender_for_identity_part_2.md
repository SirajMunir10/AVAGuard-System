# Troubleshooting: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit changes to Microsoft Defender for Identity health issues notification recipients?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Unexpected changes to health issues notification recipients

## Error Codes
N/A

## Root Causes
1. A recipient was added to the health issues notification configuration (MonitoringAlertNotificationRecipientAdded)
2. A recipient was removed from the health issues notification configuration (MonitoringAlertNotificationRecipientDeleted)

## Remediation Steps
1. Review the audit log for MonitoringAlertNotificationRecipientAdded and MonitoringAlertNotificationRecipientDeleted activities
2. Verify the recipient changes against authorized administrators

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a user with the Audit Log or Security Reader role.
2. Navigate to Audit > Search.
3. Set the Date range to cover the period of the unexpected change.
4. In the Activities list, select 'Added recipient to health issue notification' (MonitoringAlertNotificationRecipientAdded) and 'Removed recipient from health issue notification' (MonitoringAlertNotificationRecipientDeleted).
5. Click Search and review the results. Confirm that each entry shows the user who performed the action, the affected sensor or workspace, and the recipient email address.
6. Cross-reference the user who performed the action with the list of authorized administrators. Ensure that only approved personnel made changes.
7. If no audit entries appear for the unexpected change, verify that audit logging is enabled in the Microsoft 365 Purview compliance portal (https://compliance.microsoft.com) under Audit > Audit log.

## Rollback
1. If an unauthorized recipient was added, sign in to the Microsoft 365 Defender portal as a user with the Security Administrator role.
2. Navigate to Settings > Identities > Health issues notification recipients.
3. Remove the unauthorized recipient email address from the list.
4. If an authorized recipient was incorrectly removed, add the correct recipient email address back to the list.
5. To prevent recurrence, review and update administrative role assignments to ensure only authorized users have permissions to modify health issue notification settings.
6. Optionally, create a custom audit log search alert for MonitoringAlertNotificationRecipientAdded and MonitoringAlertNotificationRecipientDeleted activities to notify security operations of future changes.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
