# Troubleshooting: Password Reset (ADUserAccountLockedOut)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback failure due to a locked on-premises Active Directory account?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with SSPR writeback
- **Configuration:** Password writeback enabled

## Symptoms
- Password reset or change operation fails
- Event indicating account is locked out on-premises

## Error Codes
- `ADUserAccountLockedOut`

## Root Causes
1. User account locked out on-premises due to too many change or reset password operations in a short period

## Remediation Steps
1. Unlock the account and try the operation again

## Validation
1. Verify the on-premises AD account lockout status by running 'Get-ADUser -Identity <username> -Properties LockedOut | Select-Object LockedOut' in an elevated PowerShell session on a domain controller or management workstation with AD module. 2. Confirm the account is unlocked by checking that LockedOut returns False. 3. Initiate a test password reset or change from the Microsoft Entra admin center or SSPR portal for the same user. 4. Check the Entra ID audit logs for a successful password writeback event (e.g., 'Password writeback completed successfully') within a few minutes. 5. Verify the user can authenticate with the new password on-premises.

## Rollback
1. If the account becomes locked again or the writeback fails, re-lock the on-premises AD account by running 'Set-ADUser -Identity <username> -LockedOut $true' in an elevated PowerShell session. 2. Notify the user that the password reset operation has been rolled back and their account is locked for security. 3. Escalate to on-premises AD administrators to investigate the root cause of repeated lockouts (e.g., misconfigured applications, scripts, or sync issues). 4. If needed, disable password writeback temporarily via Entra ID > Password reset > On-premises integration > 'No' to prevent further writeback attempts until the issue is resolved.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
