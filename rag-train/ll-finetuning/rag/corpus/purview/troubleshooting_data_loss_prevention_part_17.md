# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
What happens when a user or domain appears in both allow and block lists in a DLP policy with 'Block access for specific external domains or users'?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with allow and block lists for external domains or users

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
1. A user or domain is listed in both allow and block lists.

## Remediation Steps
1. Understand that the block takes effect (most restrictive wins) when a user or domain appears in both lists.
2. If a file matches both an allow rule and a block rule, evaluation is per rule: allowed users and domains are permitted, blocked users and domains are denied, and users in neither list are blocked by default.

## Validation
1. Create or identify a DLP policy with 'Block access for specific external domains or users' configured. 2. Add the same user or domain to both the allow list and the block list. 3. Simulate a file sharing event to that user/domain. 4. Verify that the file is blocked (the block rule takes precedence). 5. Check the DLP activity explorer to confirm the block action was applied.

## Rollback
1. Remove the conflicting entry from either the allow list or the block list in the DLP policy. 2. If the block was unintended, remove the user/domain from the block list. 3. If the allow was unintended, remove the user/domain from the allow list. 4. Re-test file sharing to confirm the desired behavior (allow or block) is now enforced.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
