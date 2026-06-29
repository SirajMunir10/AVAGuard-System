# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I restrict access or encrypt content in Microsoft 365 locations using DLP policies?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with actions: Block Everyone, Block only people outside your organization, Encrypt Email Messages

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure the DLP policy action 'Restrict access or encrypt the content in Microsoft 365 locations' with options: Block Everyone, Block only people outside your organization, or Encrypt Email Messages.
2. For 'Block access for specific external domains or users' (in public preview), specify domains (e.g., partner.com) or user SMTP (e.g., user@example.com). Use Domain IS NOT or User IS NOT for allow lists.
3. When using 'Block access for specific external domains or users', note that if a user or domain appears in both allow and block lists, the block takes effect (most restrictive wins). If a file matches both an allow rule and a block rule, evaluation is across all matching rules: allowed users and domains are permitted, blocked users and domains are denied, and users in neither list are blocked by default.

## Validation
1. Create a test file containing sensitive data (e.g., credit card numbers) and share it with an external user (e.g., user@partner.com).
2. Verify that the external user cannot access the file and receives an access denied message.
3. For 'Block only people outside your organization', confirm that internal users can access the file while external users cannot.
4. For 'Encrypt Email Messages', send a test email with sensitive content to an external recipient and verify the email is automatically encrypted (e.g., shows 'Encrypted' in the recipient's email client).
5. If using 'Block access for specific external domains or users', test with a blocked domain (e.g., blocked.com) and an allowed domain (e.g., allowed.com) to confirm the block takes effect and the allow list works as expected.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies.
2. Locate the DLP policy that was modified and select 'Edit'.
3. In the 'Actions' section, change the action from 'Restrict access or encrypt the content in Microsoft 365 locations' to 'Notify users with email and tip' or remove the action entirely.
4. If specific domains or users were blocked, remove those entries from the 'Block access for specific external domains or users' list.
5. Save the policy and wait for it to propagate (typically up to 1 hour).
6. Confirm that previously blocked external users can now access the content.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
