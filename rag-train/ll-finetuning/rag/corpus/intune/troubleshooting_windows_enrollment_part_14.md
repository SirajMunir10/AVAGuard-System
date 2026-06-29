# Troubleshooting: Windows Enrollment

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Windows enrollment errors caused by invalid UPN suffix or MDM user scope set to None?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) with on-premises synchronization
- **Configuration:** UPN suffix configuration, MDM user scope in Microsoft Intune

## Symptoms
- Windows devices fail to enroll in Intune
- UPN suffix mismatch between on-premises and cloud

## Error Codes
N/A

## Root Causes
1. Invalid UPN suffix for affected users
2. MDM user scope set to None in Microsoft Intune configuration

## Remediation Steps
1. For a single affected user: Right-click the user in Azure AD, click Properties, on the Account tab, in the UPN suffix drop-down list under User logon name, select a valid UPN suffix such as contoso.com, and then click OK.
2. For multiple affected users: Select the users, in the Action menu, click Properties, on the Account tab, select the UPN suffix check box, select a valid UPN suffix such as contoso.com in the drop-down list, and then click OK.
3. Wait for the next synchronization or force a Delta Sync from the Synchronization Server by running the following commands in an elevated PowerShell prompt: Import-Module ADSync; Start-ADSyncSyncCycle -PolicyType Delta
4. Alternatively, configure Alternate Login ID (review the article before implementing).
5. If MDM user scope is set to None: Sign in to the Azure portal, select Microsoft Entra ID, select Mobility (MDM and MAM), select Microsoft Intune, set MDM user scope to All, or set MDM user scope to Some and select the Groups that can automatically enroll their Windows 10 devices, and set MAM User scope to None.

## Validation
1. Verify that the affected user's UPN suffix now matches a verified domain in Microsoft Entra ID: run `Get-MsolUser -UserPrincipalName <user@domain.com> | Select-Object UserPrincipalName, SignInName` in Azure AD PowerShell. 2. Confirm that the MDM user scope is set correctly: in the Azure portal, go to Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune, and check that 'MDM user scope' is not 'None'. 3. Force a delta sync from the on-premises synchronization server: `Import-Module ADSync; Start-ADSyncSyncCycle -PolicyType Delta`. 4. After sync completes, check the user's UPN in Microsoft Entra ID again to ensure it reflects the change. 5. Attempt a Windows enrollment on an affected device and confirm no enrollment error occurs.

## Rollback
1. If the UPN change was incorrect, revert the user's UPN suffix to the original value: in on-premises Active Directory Users and Computers, open the user's Properties, on the Account tab, select the original UPN suffix from the drop-down list, and click OK. 2. If MDM user scope was changed to 'All' or 'Some' and causes unintended enrollment, set it back to 'None': in the Azure portal, go to Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune, set 'MDM user scope' to 'None', and click Save. 3. Force a delta sync to propagate the rollback: `Import-Module ADSync; Start-ADSyncSyncCycle -PolicyType Delta`. 4. Verify the rollback by checking the user's UPN and MDM user scope in the Azure portal.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
