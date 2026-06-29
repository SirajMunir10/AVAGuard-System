# Troubleshooting: Password Reset Writeback

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot password writeback failures when a user-initiated password reset fails?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Password writeback enabled via Microsoft Entra Connect

## Symptoms
- The user's password doesn't meet the age, history, complexity, or filter requirements for the domain

## Error Codes
N/A

## Root Causes
1. The user's password doesn't meet the age, history, complexity, or filter requirements for the domain
2. The ADMA service account doesn't have the appropriate permissions to set the new password on the user account in question
3. The user's account is in a protected group, such as domain or enterprise admins, which disallow password set operations

## Remediation Steps
1. Create a new password that meets the domain's age, history, complexity, or filter requirements
2. Verify the ADMA service account has appropriate permissions to set the new password on the user account
3. If the user's account is in a protected group (e.g., domain or enterprise admins), remove the account from the protected group or use a different account

## Validation
1. Confirm the user's new password meets domain age, history, complexity, and filter requirements by checking the domain password policy (e.g., Get-ADDefaultDomainPasswordPolicy).
2. Verify the ADMA service account permissions: In Active Directory Users and Computers, ensure the account has 'Reset password' and 'Change password' permissions on the user object.
3. Check if the user is a member of a protected group (e.g., Domain Admins, Enterprise Admins) using Get-ADGroupMember or the Active Directory administrative center.
4. Initiate a test password reset from the SSPR portal and confirm success via the Azure AD audit logs (look for 'Password reset success' event).

## Rollback
1. If the password was changed to meet policy, revert to the previous password by resetting it via Active Directory Users and Computers (if known) or by using Set-ADAccountPassword.
2. If ADMA permissions were modified, restore the original permissions using the Delegation of Control Wizard or by reapplying the default permissions from a backup.
3. If the user was removed from a protected group, re-add the user to the group using Add-ADGroupMember.
4. If any configuration changes were made in Microsoft Entra Connect, re-run the configuration wizard to restore the previous settings.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
