# Troubleshooting: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit health issue modifications in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Health issues modified unexpectedly

## Error Codes
N/A

## Root Causes
1. A health issue was modified (MonitoringAlertUpdated)

## Remediation Steps
1. Review the audit log for MonitoringAlertUpdated activities
2. Verify the changes against authorized administrators

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a user with the Audit Log or Security Reader role.
2. Navigate to 'Audit' under 'Solutions' > 'Audit'.
3. Set the 'Date' range to cover the time of the unexpected health issue modification.
4. In the 'Activities' filter, search for and select 'MonitoringAlertUpdated' (listed under 'Microsoft Defender for Identity' activities).
5. Run the search and confirm that the audit log returns entries showing the 'MonitoringAlertUpdated' activity.
6. For each returned entry, verify the 'User' field shows an authorized administrator and the 'Item' field details the specific health issue that was modified.
7. If no entries appear, confirm that audit logging is enabled in the Microsoft 365 Defender portal under 'Settings' > 'Microsoft 365 Defender' > 'Audit log'.

## Rollback
1. If the audit log reveals that an unauthorized or incorrect modification was made to a health issue, identify the specific health issue from the audit log entry.
2. Sign in to the Microsoft 365 Defender portal with appropriate permissions (Security Administrator or Global Administrator).
3. Navigate to 'Settings' > 'Microsoft Defender for Identity' > 'Health issues'.
4. Locate the affected health issue and manually revert its configuration to the previous known good state (e.g., change the alert severity, status, or suppression settings as needed).
5. If the health issue cannot be reverted via the portal, contact Microsoft Support for assistance in restoring the default configuration.
6. As a preventive measure, review and update administrative role assignments to ensure only authorized users can modify health issues.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
