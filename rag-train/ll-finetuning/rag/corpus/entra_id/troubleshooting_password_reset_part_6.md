# Troubleshooting: Password Reset (CryptoError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve CryptoError during SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** SSPR writeback

## Symptoms
- Error generating the password encryption key or decrypting a password that arrives from the cloud service

## Error Codes
- `CryptoError`

## Root Causes
1. Problem with your environment

## Remediation Steps
1. Look at the details of your event log to learn more about how to resolve this problem
2. Try disabling and then re-enabling the password writeback service

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
