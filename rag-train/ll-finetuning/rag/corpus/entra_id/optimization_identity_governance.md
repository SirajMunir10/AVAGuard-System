# Optimization: Identity Governance

**Domain:** Entra ID
**Subdomain:** Identity Governance
**Incident Type:** Optimization

## Scenario / Query
How can I reduce the number of stale guest accounts in my Entra ID tenant to improve security and reduce licensing costs?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Guest user accounts that have not signed in for more than 90 days

## Symptoms
- Guest accounts that have not been used for extended periods remain active
- High number of guest accounts in the tenant
- Potential security risk from dormant external identities

## Error Codes
N/A

## Root Causes
1. No automated review or lifecycle policy for guest accounts
2. Lack of periodic access reviews for external identities

## Remediation Steps
1. Create an access review for guest users with a duration of 90 days and auto-apply results to remove inactive guests
2. Configure a lifecycle workflow in Entra ID Identity Governance to automatically disable or delete guest accounts that have not signed in for 90 days

## Validation
Run a report of guest users with last sign-in older than 90 days and verify that the access review or lifecycle workflow has removed or disabled them.

## Rollback
If a guest account was removed in error, a global administrator can re-invite the guest user through the Entra ID portal or PowerShell.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-plan>
