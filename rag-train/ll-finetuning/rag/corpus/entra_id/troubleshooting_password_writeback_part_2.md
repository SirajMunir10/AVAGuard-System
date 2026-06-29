# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that Microsoft Entra Connect has the required AD DS Reset password permission for password writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Password writeback fails or is not functioning

## Error Codes
N/A

## Root Causes
1. The AD DS account used by Microsoft Entra Connect does not have the Reset password permission on the on-premises user account

## Remediation Steps
1. Sign in to the Microsoft Entra Connect server and start the Synchronization Service Manager by selecting Start > Synchronization Service.
2. Under the Connectors tab, select the on-premises Active Directory Domain Services connector, and then select Properties.
3. In the pop-up window, select Connect to Active Directory Forest and make note of the User name property. This property is the AD DS account used by Microsoft Entra Connect to perform directory synchronization.
4. Sign in to an on-premises domain controller and start the Active Directory Users and Computers application.
5. Select View and make sure the Advanced Features option is enabled.
6. Look for the AD DS user account you want to verify. Right-click the account name and select Properties.
7. In the pop-up window, go to the Security tab and select Advanced.
8. In the Advanced Security Settings for Administrator pop-up window, go to the Effective Access tab.
9. Choose Select a user, select the AD DS account used by Microsoft Entra Connect, and then select View effective access.
10. Scroll down and look for Reset password. If the entry has a check mark, the AD DS account has permission to reset the password of the selected Active Directory user account.

## Validation
If the Reset password entry has a check mark, the AD DS account has permission to reset the password of the selected Active Directory user account.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
