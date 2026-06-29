# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How do I use the Translation view in Communication Compliance to review messages in different languages?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Displayed language setting in Microsoft 365 subscription

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Translation view in Communication Compliance.
2. The view automatically converts message text to the language configured in the Displayed language setting in the Microsoft 365 subscription for each reviewer.
3. This conversion includes the text for the policy match and everything included in the conversation view (up to five messages before and five messages after the policy match).

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with appropriate permissions. 2. Navigate to Communication Compliance > Policies and select a policy with messages in a language different from the reviewer's displayed language. 3. Open a message flagged by the policy. 4. In the message details pane, click the 'Translation' tab or toggle. 5. Verify that the message text (policy match and up to five messages before and after) is displayed in the language configured in the Microsoft 365 subscription's 'Displayed language' setting for the reviewer. 6. Confirm that the translated text is readable and corresponds to the original message content.

## Rollback
1. If the Translation view does not display correctly or causes confusion, revert to the original language view by clicking the 'Original' tab or toggle in the message details pane. 2. If the issue persists, sign out and sign back into the compliance portal to reset the session. 3. If the problem is related to the 'Displayed language' setting, navigate to Microsoft 365 admin center > Settings > Org settings > Language and adjust the displayed language to a supported option. 4. If translation still fails, clear browser cache and cookies, then retry. 5. As a last resort, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
