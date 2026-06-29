# Troubleshooting: Password Writeback (hr=800700CE)

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix password writeback failure with error hr=800700CE indicating filename or extension is too long?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Password writeback enabled

## Symptoms
- User attempts to reset a password or unlock an account with password writeback enabled, and the operation fails
- Event in the Microsoft Entra Connect event log contains: 'Synchronization Engine returned an error hr=800700CE, message=The filename or extension is too long' after the unlock operation occurs

## Error Codes
- `hr=800700CE`

## Root Causes
1. The Active Directory account for Microsoft Entra Connect has a password longer than 256 characters

## Remediation Steps
1. Find the Active Directory account for Microsoft Entra Connect and reset the password so that it contains no more than 256 characters
2. Open the Synchronization Service from the Start menu
3. Browse to Connectors and find the Active Directory Connector
4. Select it and then select Properties
5. Browse to the Credentials page and enter the new password
6. Select OK to close the page

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
