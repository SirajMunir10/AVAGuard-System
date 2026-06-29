# Troubleshooting: Password Writeback (80230402)

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback failure due to duplicate user entries across domains?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Password writeback enabled, Azure AD Connect sync

## Symptoms
- Synchronization Engine returned an error hr=80230402
- Message: An attempt to get an object failed because there are duplicated entries with the same anchor

## Error Codes
- `80230402`

## Root Causes
1. Same user ID is enabled in multiple domains (e.g., account and resource forests)
2. Non-unique anchor attribute used (e.g., alias or UPN) shared by two users

## Remediation Steps
1. Ensure no duplicated users exist within your domains
2. Use a unique anchor attribute for each user

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
