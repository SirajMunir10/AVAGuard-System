# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure the 'Restrict access or encrypt the content' action in a Microsoft Purview DLP policy to block access for specific external domains or users?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with 'Restrict access or encrypt the content' action

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the 'Block access for specific external domains or users' sub-option.
2. Specify external domains to block (e.g., partner.com) or user SMTP addresses (e.g., user@example.com).
3. Optionally, specify allow lists using 'Domain IS NOT' or 'User IS NOT'.
4. Note: Internal users and domains cannot be blocked with this sub-option; use 'Block everyone' for internal users.

## Validation
1. Create a test DLP policy with the 'Restrict access or encrypt the content' action and configure the 'Block access for specific external domains or users' sub-option to block 'partner.com' and 'user@example.com'. 2. Send a test email containing sensitive content (e.g., credit card number) from an internal user to an external recipient at 'partner.com'. 3. Verify that the email is blocked and the sender receives a DLP policy tip or notification indicating the action was taken. 4. Repeat the test with a recipient at 'user@example.com' and confirm the same blocking behavior. 5. Confirm that internal users and domains are not affected by sending a test email to an internal recipient.

## Rollback
1. Navigate to the Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Locate the DLP policy that was modified or created. 3. Edit the policy and remove or disable the 'Restrict access or encrypt the content' action, or change the sub-option to 'Block everyone' or remove the blocked domains/users. 4. Save the policy and allow up to 1 hour for changes to propagate. 5. Verify that previously blocked external recipients can now receive emails containing sensitive content.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
