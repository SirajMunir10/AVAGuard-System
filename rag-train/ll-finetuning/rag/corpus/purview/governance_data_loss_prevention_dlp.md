# Governance: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Governance

## Scenario / Query
A user reports that a DLP policy designed to block sharing of credit card numbers is not triggering for emails sent to external recipients. The policy is configured with a low priority and no user override options. How can a Microsoft Purview administrator verify the policy is applied correctly and identify why it is not blocking the emails?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** DLP policy 'Credit Card Block' with scope set to Exchange, priority 3, and action 'Block' with no override.

## Symptoms
- Emails containing credit card numbers are sent to external recipients without being blocked or generating a policy tip.
- DLP reports show zero matches for the 'Credit Card Block' policy over the past 7 days.

## Error Codes
N/A

## Root Causes
1. The DLP policy may not be enabled or deployed to all mailboxes.
2. The policy priority might be lower than another policy that allows the action.
3. The sensitive info type for credit card numbers may not be correctly configured or detected.

## Remediation Steps
1. 1. Verify the policy is enabled: In the Microsoft Purview compliance portal, go to Data loss prevention > Policies, select the policy, and check its status.
2. 2. Check policy priority: Ensure the policy has a higher priority (lower number) than any conflicting policies.
3. 3. Test the policy using the built-in DLP test functionality: In the policy, use the 'Test' option to simulate sending an email with credit card data.
4. 4. Review DLP activity explorer: Navigate to Data loss prevention > Activity explorer and filter by the policy name to see if any matches were recorded.
5. 5. Confirm the sensitive info type is active: Go to Data classification > Sensitive info types and ensure 'Credit Card Number' is published and not disabled.
6. 6. Check for policy tips: Ensure the policy is configured to show policy tips in supported apps (Outlook on the web).

## Validation
After remediation, send a test email containing a valid credit card number (e.g., 4111 1111 1111 1111) to an external recipient. Verify the email is blocked and a policy tip is displayed in Outlook on the web.

## Rollback
If the policy change causes unintended blocking, revert the policy action to 'Notify only' or disable the policy temporarily.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-create-policy>
- <https://learn.microsoft.com/en-us/purview/dlp-test-policy>
