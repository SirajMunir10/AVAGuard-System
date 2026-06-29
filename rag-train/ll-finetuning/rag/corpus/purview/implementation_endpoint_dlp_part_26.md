# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to configure website groups in Endpoint DLP with proper URL syntax to assign different policy actions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP website groups configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Add a maximum of 100 websites into a single group
2. Create a maximum of 150 groups
3. Do not include networking protocol (e.g., https:// or file://) as part of the URL
4. Use *. as a wildcard to specify all domains or all subdomains
5. Use / as a terminator at the end of a URL to scope to that specific site only
6. When adding a URL without a terminating slash mark (/), that URL is scoped to that site and all subsites
7. Only add *. to the beginning of a domain
8. The / terminator is only supported at the end of a domain
9. This syntax applies to all http/https websites

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Website groups.
2. Verify that each group contains no more than 100 websites.
3. Confirm that the total number of groups does not exceed 150.
4. For each URL entry, ensure no networking protocol (e.g., https://, file://) is included.
5. Check that wildcards are used only as '*.domain.com' at the beginning of a domain.
6. Validate that a terminating slash (/) is used only at the end of a domain to scope to that specific site.
7. Confirm that URLs without a terminating slash scope to the site and all subsites.
8. Test policy assignment by applying different actions to groups and verifying enforcement on endpoints.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Website groups, select the group(s) that need to be reverted.
2. Remove or edit the incorrectly configured URL entries to match the correct syntax (remove protocol prefixes, adjust wildcards, add/remove terminating slashes as needed).
3. If a group exceeds 100 websites, split the URLs into additional groups (up to 150 groups total).
4. Reassign the original policy actions to the corrected groups.
5. Test that the rollback restores previous DLP behavior by verifying policy actions on endpoints.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
