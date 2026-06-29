# Incident Response: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Incident Response

## Scenario / Query
How to audit remediation actions in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Suspicious remediation actions added or completed

## Error Codes
N/A

## Root Causes
1. A remediation action was added to the queue (RemediationActionAdded)
2. A remediation action was completed (RemediationActionUpdated)

## Remediation Steps
1. Review the audit log for RemediationActionAdded and RemediationActionUpdated activities
2. Investigate the context of the remediation action and the user who performed it

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a user with the Audit Log or Security Reader role.
2. Navigate to Audit > Search.
3. Set the Date range to cover the incident timeframe.
4. In the Activities list, select 'RemediationActionAdded' and 'RemediationActionUpdated' under the Microsoft Defender for Identity category.
5. Run the search and confirm that the audit log returns entries for both activities.
6. For each returned entry, verify the 'User' field shows the identity of the user who performed the action, and the 'Item' field describes the remediation action details.
7. Optionally, export the audit log results to a CSV file for further analysis.

## Rollback
1. If a remediation action was incorrectly added or completed, identify the specific action from the audit log (e.g., account disable, password reset).
2. Reverse the action manually: for example, if an account was disabled, re-enable it via the Microsoft 365 admin center or Azure AD; if a password was reset, notify the user to set a new password.
3. To prevent recurrence, review and adjust Microsoft Defender for Identity role permissions to ensure only authorized users can add or complete remediation actions.
4. If the audit log is missing expected entries, verify that audit logging is enabled in the Microsoft 365 Defender portal under Settings > Microsoft 365 Defender > Audit log.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
