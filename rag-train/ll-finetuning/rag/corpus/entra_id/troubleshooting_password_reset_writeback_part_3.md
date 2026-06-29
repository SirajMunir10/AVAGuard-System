# Troubleshooting: Password Reset Writeback

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot password reset writeback failures when the PasswordResetFail event is logged?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with on-premises Active Directory
- **Configuration:** Password writeback enabled via Microsoft Entra Connect

## Symptoms
- PasswordResetFail event indicates a user selected a password and the password arrived successfully to the on-premises environment, but setting the password in local Active Directory failed

## Error Codes
N/A

## Root Causes
1. The user's password doesn't meet the age, history, complexity, or filter requirements for the domain
2. The ADMA service account doesn't have the appropriate permissions to set the new password on the user account in question
3. The user's account is in a protected group, such as domain or enterprise admin group, which disallows password set operations

## Remediation Steps
1. Create a new password that meets the domain's age, history, complexity, or filter requirements
2. Ensure the ADMA service account has appropriate permissions to set the new password on the user account
3. If the user's account is in a protected group, remove the account from the protected group or adjust group policy to allow password set operations

## Validation
1. Check the on-premises Active Directory password policy for the user's domain: run 'net accounts /domain' and 'Get-ADDefaultDomainPasswordPolicy -Identity <DomainName> | fl *' to confirm age, history, complexity, and filter requirements. 2. Verify the ADMA service account permissions: run 'Get-ADUser -Identity <ADMA_ServiceAccount> -Properties memberOf' and check that the account is a member of the 'Domain Admins' group or has been delegated the 'Reset Password' permission on the target user's OU. 3. Confirm the user is not in a protected group: run 'Get-ADGroupMember -Identity 'Domain Admins' | Where-Object {$_.distinguishedName -eq (Get-ADUser -Identity <UserUPN>).distinguishedName}' and similarly for 'Enterprise Admins' and 'Schema Admins'. 4. Trigger a new password reset attempt and verify the PasswordResetFail event no longer appears in the Microsoft Entra ID audit logs.

## Rollback
1. If a new password was set that meets policy, revert to the previous password by resetting it in on-premises AD using 'Set-ADAccountPassword -Identity <UserUPN> -Reset -NewPassword (ConvertTo-SecureString -AsPlainText '<OldPassword>' -Force)'. 2. If ADMA permissions were changed, remove the delegated 'Reset Password' permission from the ADMA service account on the affected OU using Active Directory Users and Computers or 'dsrevoke' command. 3. If the user was removed from a protected group, re-add the user to the group using 'Add-ADGroupMember -Identity 'Domain Admins' -Members <UserUPN>' (or the appropriate group). 4. Re-enable password writeback if it was disabled during troubleshooting: in Microsoft Entra Connect, re-check the 'Password writeback' option and run a full sync cycle.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
