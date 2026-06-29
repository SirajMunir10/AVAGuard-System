# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I block access for specific external domains or users in a DLP policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with 'Block access for specific external domains or users' sub-option

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the 'Block access for specific external domains or users' sub-option to block external access by domain (e.g., partner.com) or by user SMTP (e.g., user@example.com).
2. Specify allow lists by using Domain IS NOT or User IS NOT.
3. Internal users and domains cannot be blocked with this sub-option; use 'Block everyone' for internal users.
4. If a user or domain appears in both allow and block lists, the block takes effect (most restrictive wins). If a file matches both an allow rule and a block rule, evaluation is across all matching rules: allowed users and domains are permitted, blocked users and domains are denied, and users in neither list are blocked by default.

## Validation
1. Create a test file containing sensitive data (e.g., credit card numbers) and share it with an external user from a blocked domain (e.g., user@partner.com).
2. Attempt to access the file from that external account; verify that access is denied and a DLP policy tip or block notification is shown.
3. Create a test file and share it with an external user from an allowed domain (e.g., user@allowed.com) that is not in the block list; verify that access is permitted.
4. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies, select the policy, and review the 'Access by external users' settings to confirm the blocked domains/users are listed under 'Block access for specific external domains or users' and allowed domains/users are listed under 'Allow access for specific external domains or users'.
5. Use the DLP Alerts dashboard to confirm no unexpected alerts were generated for allowed users.

## Rollback
1. In the Microsoft Purview compliance portal, go to Data Loss Prevention > Policies and select the policy that was modified.
2. Under 'Access by external users', clear the entries in the 'Block access for specific external domains or users' field and the 'Allow access for specific external domains or users' field, or remove the specific domains/users that were added.
3. Alternatively, set the policy to 'Block everyone' or 'Allow everyone' as needed to revert to the previous state.
4. Save the policy and wait for replication (up to 24 hours).
5. Verify that external users who were previously blocked can now access shared content (if intended) and that no unintended access is granted.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
