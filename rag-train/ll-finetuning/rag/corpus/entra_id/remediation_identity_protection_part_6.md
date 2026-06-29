# Remediation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Remediation

## Scenario / Query
How to require a password change for risky users in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Allow on-premises password change to reset user risk setting must be enabled for hybrid users with on-premises or hybrid-joined Windows devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For cloud users and hybrid users with Microsoft Entra-joined devices: Perform a secure password change after a successful MFA sign-in. Users must already be registered for MFA.
2. For hybrid users with on-premises or hybrid-joined Windows devices: Perform a secure password change through the Ctrl-Alt-Delete screen on their Windows device. The Allow on-premises password change to reset user risk setting must be enabled.
3. If the User must change password at next logon setting is enabled in Active Directory, the user is prompted to change their password the next time they sign in.

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky users. 3. Confirm the user's risk level is now 'None' or 'Low' and the risk state is 'Remediated'. 4. For hybrid users with on-premises or hybrid-joined Windows devices, verify the 'Allow on-premises password change to reset user risk' setting is enabled: Go to Protection > Identity Protection > Settings > General, and ensure the toggle is turned on. 5. For cloud users, confirm the user has completed a secure password change after a successful MFA sign-in and that MFA registration is active.

## Rollback
1. If the password change was performed in error, an administrator can reset the user's password to a temporary password via the Microsoft Entra admin center: Users > All users > select the user > Reset password. 2. If the 'Allow on-premises password change to reset user risk' setting was incorrectly enabled, disable it: Protection > Identity Protection > Settings > General, turn off the toggle. 3. If the user was incorrectly prompted to change password at next logon due to Active Directory settings, clear the 'User must change password at next logon' flag in Active Directory Users and Computers for that user.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
