# Troubleshooting: Password Reset

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix password writeback failure due to incorrect Hybrid Administrator account or federated user?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Password reset fails for federated, pass-through authentication, or password-hash-synchronized users
- Error indicates a service problem

## Error Codes
N/A

## Root Causes
1. Incorrect password for the Hybrid Administrator account provided at the beginning of the Microsoft Entra Connect installation process
2. Attempted to use a federated user for the Hybrid Administrator account specified at the beginning of the Microsoft Entra Connect installation process

## Remediation Steps
1. Make sure that you're not using a federated account for the Hybrid Administrator you specified at the beginning of the installation process
2. Ensure the password specified is correct

## Validation
1. Sign in to the Microsoft Entra Connect server as an administrator. 2. Open Microsoft Entra Connect and select 'View current configuration'. 3. Verify that the Hybrid Administrator account listed under 'User sign-in' is not a federated user (i.e., its UPN domain is not federated). 4. Test the password of the Hybrid Administrator account by running: `Test-ADSyncAzureADConnectivity -AzureADCredential (Get-Credential)` and entering the Hybrid Administrator credentials. 5. Initiate a password reset for a test user and confirm no writeback error appears in the Microsoft Entra Connect event logs (Event ID 6329 or 3100).

## Rollback
1. If the remediation fails, re-run the Microsoft Entra Connect wizard and select 'Change the Azure AD account' to revert to the previous Hybrid Administrator account. 2. If the account was changed, restore the original Hybrid Administrator account by running: `Set-ADSyncAzureADAccount -AzureADCredential (Get-Credential)` with the original credentials. 3. Verify password writeback functionality by testing a password reset for a non-administrator user and checking for success in the Microsoft Entra admin center under 'Password reset' audit logs.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
