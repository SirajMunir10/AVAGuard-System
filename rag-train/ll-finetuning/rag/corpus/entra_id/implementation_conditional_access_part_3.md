# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
A Conditional Access policy targeting all cloud apps and requiring MFA is not being applied to guest users. What configuration step is missing?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Conditional Access policy configured with 'All cloud apps' and 'Require multifactor authentication' grant control, but guest users are not prompted for MFA.

## Symptoms
- Guest users can access applications without being prompted for MFA
- Conditional Access policy appears enabled but does not apply to external identities

## Error Codes
N/A

## Root Causes
1. The Conditional Access policy does not include 'External users' in the 'Users and groups' assignment
2. By default, Conditional Access policies apply only to members of the tenant, not to guest users, unless explicitly included

## Remediation Steps
1. Edit the Conditional Access policy and under 'Users and groups', select 'Select users and groups' and then check 'Guest or external users'
2. Choose the appropriate external user type (e.g., B2B collaboration guest users) and apply the policy

## Validation
Sign in as a guest user and verify that the MFA prompt appears when accessing a cloud app covered by the policy

## Rollback
Remove the 'Guest or external users' selection from the policy assignments

## References
- Microsoft Learn: 'Common Conditional Access policy: Require multifactor authentication for all users' - https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-all-users-mfa
