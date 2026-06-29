# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How does DLP handle actions on inbound encrypted emails in Exchange?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy on inbound encrypted emails

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. DLP actions (e.g., block) are taken on inbound encrypted emails that are in scope of a policy.
2. To maintain confidentiality of the encryption, the event won't appear in Activity Explorer or in the Alert.
3. The content of the message won't be accessible to anyone other than the recipient.

## Validation
1. Send a test inbound encrypted email that matches a DLP policy condition (e.g., contains sensitive info like credit card numbers).
2. Verify that the email is blocked or the configured action (e.g., block) is applied by checking the recipient's mailbox (the email should not be delivered).
3. Confirm that the event does NOT appear in Activity Explorer (navigate to Purview > Data Loss Prevention > Activity Explorer, search for the test email's subject or sender; no matching event should be found).
4. Confirm that no alert is generated for this event in the Alerts page (Purview > Data Loss Prevention > Alerts).
5. Verify that the encrypted message content is not accessible to anyone other than the intended recipient (e.g., by attempting to open the encrypted message with a different account).

## Rollback
1. Remove or disable the DLP policy that applies to inbound encrypted emails (Purview > Data Loss Prevention > Policies, select the policy, and choose 'Disable' or 'Delete').
2. Wait for policy propagation (up to 1 hour).
3. Send a test inbound encrypted email again to confirm it is now delivered normally (check recipient's mailbox).
4. Re-enable or recreate the policy if needed, but consider excluding encrypted emails from the policy scope by modifying the policy conditions (e.g., add 'Message is encrypted' exception) to avoid unintended blocking.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
