# Troubleshooting: Password Reset (AuthTokenError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve AuthTokenError during SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** SSPR writeback, Microsoft Entra Connect

## Symptoms
- Couldn't get an authorization token for the Hybrid Administrator account specified during Microsoft Entra Connect setup

## Error Codes
- `AuthTokenError`

## Root Causes
1. Bad username or password specified for the Hybrid Administrator account
2. Hybrid Administrator account specified is federated

## Remediation Steps
1. Rerun the configuration with the correct username and password
2. Ensure that the administrator is a managed (cloud-only or password-synchronized) account

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
