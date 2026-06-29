# Governance: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Governance

## Scenario / Query
How to audit report and notification configuration changes in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Report scheduling modified unexpectedly
- Security alerts or health issues notifications configuration changed

## Error Codes
N/A

## Root Causes
1. A report's scheduling was modified (ReporterConfigurationUpdated)
2. The security alerts or health issues notifications configuration was modified (NotificationConfigurationUpdated)

## Remediation Steps
1. Review the audit log for ReporterConfigurationUpdated and NotificationConfigurationUpdated activities
2. Verify the changes against authorized administrators

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a Global Administrator or Security Administrator.
2. Navigate to Audit > Search.
3. Set the Date range to cover the period of the suspected changes.
4. In the Activities list, search for and select 'ReporterConfigurationUpdated' and 'NotificationConfigurationUpdated'.
5. Click Search and review the results. Confirm that the only entries present correspond to authorized administrators and that the changes match expected configurations.
6. For each suspicious entry, expand the details to verify the user, IP address, and changed properties.
7. Optionally, export the audit log results for record-keeping.

## Rollback
1. If an unauthorized change is detected, identify the specific configuration that was altered from the audit log details.
2. For report scheduling changes: In Microsoft Defender for Identity, navigate to Configuration > Reports and manually restore the correct schedule for each affected report.
3. For notification changes: In Microsoft Defender for Identity, navigate to Configuration > Notifications and restore the correct settings for security alerts and health issues notifications.
4. If the change was made by a compromised account, immediately reset the account's credentials and revoke any active sessions.
5. After restoring, re-run the validation steps to confirm the correct configuration is in place.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
