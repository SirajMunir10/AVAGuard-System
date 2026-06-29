# Troubleshooting: Password Reset Writeback

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot password change writeback failures when the ChangePasswordFail event is logged?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with on-premises Active Directory
- **Configuration:** Password writeback enabled via Microsoft Entra Connect

## Symptoms
- ChangePasswordFail event indicates a user selected a password and the password arrived successfully to the on-premises environment, but setting the password in local Active Directory failed

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
1. Verify that the user's new password meets the domain's age, history, complexity, and filter requirements by checking the local Active Directory password policy (e.g., using `net accounts /domain` or reviewing GPO).
2. Confirm the ADMA service account has the necessary permissions by checking its membership in the appropriate groups (e.g., Domain Admins or a custom group with 'Reset Password' and 'Change Password' permissions on the user object).
3. If the user is in a protected group (e.g., Domain Admins, Enterprise Admins), verify the group membership and ensure the account is removed or the policy allows password set operations.
4. Trigger a password change for the user and monitor the Microsoft Entra Connect event logs for a successful writeback (look for 'ChangePasswordSuccess' event).

## Rollback
1. If the password change fails due to domain policy, revert to the previous password (if known) or set a compliant password via Active Directory Users and Computers.
2. If the ADMA service account lacks permissions, restore its previous group memberships or grant the minimum required permissions (e.g., 'Reset Password' and 'Change Password' on the affected user object).
3. If the user was removed from a protected group, re-add the user to the original protected group using Active Directory administrative tools.
4. After any rollback action, re-run the password change test and confirm the 'ChangePasswordFail' event no longer appears.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
