# Troubleshooting: Password Writeback (32009)

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback configuration error 32009 with 'Error getting auth token' at the end of Microsoft Entra Connect installation?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect installation with password writeback enabled

## Symptoms
- At the last step of the Microsoft Entra Connect installation process, an error indicates that password writeback couldn't be configured
- Microsoft Entra Connect Application event log contains error 32009 with the text 'Error getting auth token'

## Error Codes
- `32009`

## Root Causes
1. Incorrect password for the Hybrid Administrator account provided at the beginning of the Microsoft Entra Connect installation process
2. Attempted to use a federated user for the Hybrid Administrator account specified at the beginning of the Microsoft Entra Connect installation process

## Remediation Steps
1. Verify the password for the Hybrid Administrator account is correct
2. Ensure the Hybrid Administrator account is not a federated user

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
