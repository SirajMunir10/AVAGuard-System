# Troubleshooting: Audit Logs

**Domain:** Purview
**Subdomain:** Audit Logs
**Incident Type:** Troubleshooting

## Scenario / Query
How to track encrypted message portal activities and determine when external recipients read and forward messages?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Encrypted message portal activity logging enabled

## Symptoms
- Need to monitor external recipient actions on encrypted messages
- Unable to determine when encrypted messages are read or forwarded

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access logs for encrypted messages through the encrypted message portal
2. Enable and use encrypted message portal activity logs as described in Encrypted message portal activity log documentation
3. Use the MessageID field as the key identifier to follow a message through the system
4. Review Recipient field for list of all recipient email addresses
5. Review Sender field for the originating email address
6. Review AuthenticationMethod field to determine authenticating method (OTP, Yahoo, Gmail, or Microsoft)
7. Review AuthenticationStatus field to see if authentication succeeded or failed
8. Review OperationStatus field to see if the indicated operation succeeded or failed
9. Review AttachmentName field for name of the attachment
10. Review OperationProperties field for optional properties like number of OTP passcodes sent or email subject

## Validation
1. Run the following command in Exchange Online PowerShell to search for encrypted message portal activities: Search-UnifiedAuditLog -Operations 'EncryptedMessagePortalActivity' -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date). 2. Verify that the output includes entries with the MessageID field populated. 3. For a sample entry, confirm that the Recipient, Sender, AuthenticationMethod, AuthenticationStatus, OperationStatus, AttachmentName, and OperationProperties fields are present and contain expected values. 4. Check that the OperationProperties field includes details such as number of OTP passcodes sent or email subject. 5. Ensure that the audit log search returns results for the specific encrypted message portal activities you need to monitor.

## Rollback
1. If the encrypted message portal activity logging is causing performance issues or unwanted noise, disable it by running: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $false. 2. Alternatively, if you need to stop only the encrypted message portal activity logging, you can filter out these events in your audit log search queries by excluding the 'EncryptedMessagePortalActivity' operation. 3. To revert to default audit log settings, ensure that no custom audit log policies are applied that specifically include encrypted message portal activities. 4. If you enabled any additional logging via the Purview compliance portal, disable the corresponding audit log entry for encrypted message portal activities under 'Audit' > 'Audit log search' > 'Activities' > 'Encrypted message portal activities'.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/purview/encrypted-message-portal-activity-log>
