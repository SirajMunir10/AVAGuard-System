# Troubleshooting: Password Reset Writeback (ADUserAccountDisabled)

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot ADUserAccountDisabled event in SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback configuration

## Symptoms
- Attempted to reset or change password for an account that is disabled on-premises

## Error Codes
- `ADUserAccountDisabled`

## Root Causes
1. Account is disabled on-premises

## Remediation Steps
1. Enable the account and try the operation again

## Validation
1. Verify the on-premises user account is enabled: Run 'Get-ADUser -Identity <username> | Select-Object Enabled' in Active Directory module for Windows PowerShell. 2. Confirm the account is not disabled: Ensure the output shows 'True' for the Enabled property. 3. Test SSPR writeback: Initiate a password reset from the Microsoft Entra admin center for the same user and confirm no ADUserAccountDisabled error appears.

## Rollback
1. If enabling the account causes unintended access, disable the account again: Run 'Disable-ADAccount -Identity <username>' in Active Directory module for Windows PowerShell. 2. Revert any other changes made during remediation (e.g., group memberships or permissions). 3. Notify the user that the account remains disabled and SSPR writeback will continue to fail for that account.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
