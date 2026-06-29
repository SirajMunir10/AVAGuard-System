# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How do I use the Translation view to convert message text in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Displayed language setting configured in the Microsoft 365 subscription for each reviewer

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The Translation view automatically converts message text to the language configured in the Displayed language setting in the Microsoft 365 subscription for each reviewer
2. This conversion includes the text for the policy match and everything included in the conversation view (up to five messages before and five messages after the policy match)

## Validation
1. Sign in to the Microsoft 365 Purview compliance portal as a reviewer. 2. Navigate to Communication Compliance > Policies and open a policy with matched messages. 3. Select a message that triggered a policy match. 4. In the message details pane, locate the Translation view option (e.g., a translate icon or language selector). 5. Click the Translation view and verify that the message text is converted to the language specified in your Displayed language setting (e.g., if Displayed language is French, confirm the text appears in French). 6. Expand the conversation view to confirm that up to five messages before and five messages after the policy match are also translated to the same language.

## Rollback
1. If the Translation view does not display correctly or causes confusion, close the Translation view by toggling it off (e.g., clicking the translate icon again or selecting 'Original' language). 2. Verify that the original message text is restored. 3. If the issue persists, clear the browser cache and sign out of the compliance portal, then sign back in. 4. As a last resort, contact Microsoft Support to investigate potential issues with the Displayed language setting or Translation feature.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
