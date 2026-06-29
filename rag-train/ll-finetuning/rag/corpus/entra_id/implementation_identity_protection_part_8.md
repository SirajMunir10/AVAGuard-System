# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites and considerations for generating temporary passwords for hybrid users in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Hybrid (cloud and on-premises)
- **Configuration:** Enable password hash synchronization, including the PowerShell script in the Synchronizing temporary passwords section; Enable the Allow on-premises password change to reset user risk setting in Microsoft Entra ID Protection; Enable Self-service password reset; In Active Directory, only select the option User must change password at next logon after enabling everything in the previous bullets

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable password hash synchronization, including the PowerShell script in the Synchronizing temporary passwords section.
2. Enable the Allow on-premises password change to reset user risk setting in Microsoft Entra ID Protection.
3. Enable Self-service password reset.
4. In Active Directory, only select the option User must change password at next logon after enabling everything in the previous bullets.

## Validation
1. Verify password hash synchronization is enabled: Run `Get-ADSyncAADPasswordSyncConfiguration` in the Azure AD Connect PowerShell module and confirm that PasswordHashSync is True for the target domain. 2. Confirm the temporary password script is deployed: Check that the script from the 'Synchronizing temporary passwords' section is scheduled or present in the synchronization pipeline. 3. Validate the 'Allow on-premises password change to reset user risk' setting: In the Entra admin center, go to Identity Protection > User risk policy and ensure the toggle 'Allow on-premises password change to reset user risk' is enabled. 4. Confirm SSPR is enabled: In Entra admin center > Password reset, verify that Self-service password reset is enabled for the relevant users. 5. Check a hybrid user's Active Directory account: Ensure that 'User must change password at next logon' is selected only after all previous steps are enabled, and that the user can sign in with a temporary password and is prompted to change it.

## Rollback
1. Disable password hash synchronization: In Azure AD Connect, uncheck Password Hash Synchronization and run a full sync to revert to federation or pass-through authentication if needed. 2. Remove the temporary password script: Delete or disable the scheduled task or script that synchronizes temporary passwords. 3. Disable 'Allow on-premises password change to reset user risk': In Entra admin center > Identity Protection > User risk policy, turn off the toggle. 4. Disable SSPR: In Entra admin center > Password reset, set self-service password reset to 'None' or disable for the affected users. 5. Clear the 'User must change password at next logon' flag: In Active Directory Users and Computers, uncheck the option for affected users to prevent forced password change on next logon.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
