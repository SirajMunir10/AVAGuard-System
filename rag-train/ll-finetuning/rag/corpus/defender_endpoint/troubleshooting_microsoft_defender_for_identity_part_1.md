# Troubleshooting: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit changes to Microsoft Defender for Identity alert notification recipients?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Unexpected changes to security alert notification recipients

## Error Codes
N/A

## Root Causes
1. A recipient was added to the security alerts notification configuration (AlertNotificationsRecipientAdded)
2. A recipient was removed from the security alerts notification configuration (AlertNotificationsRecipientDeleted)

## Remediation Steps
1. Review the audit log for AlertNotificationsRecipientAdded and AlertNotificationsRecipientDeleted activities
2. Verify the recipient changes against authorized administrators

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a Global Administrator or Security Administrator.
2. Navigate to Audit > Search.
3. Set the Date range to cover the period of suspected changes.
4. In the Activities list, select 'AlertNotificationsRecipientAdded' and 'AlertNotificationsRecipientDeleted' under the 'Microsoft Defender for Identity' category.
5. Click Search and review the results for any unexpected recipient additions or removals.
6. For each suspicious entry, note the User who performed the action, the Recipients field, and the timestamp.
7. Cross-reference the identified changes with the list of authorized administrators to confirm whether the changes were approved.

## Rollback
1. If an unauthorized recipient was added, remove that recipient from the security alerts notification configuration:
   - In the Microsoft 365 Defender portal, go to Settings > Identities > Notifications (or the equivalent alert notification settings page).
   - Locate the recipient list and remove the unauthorized email address.
   - Save the changes.
2. If an authorized recipient was incorrectly removed, re-add that recipient:
   - On the same notification settings page, add the missing recipient email address.
   - Save the changes.
3. After making corrections, repeat the validation steps to confirm the recipient list is now correct.
4. If the unauthorized changes persist, investigate the account that performed the activity (e.g., review sign-in logs, reset credentials, or revoke permissions) and consider raising a support ticket with Microsoft.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
