# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to evaluate Microsoft Entra hybrid join status when a device fails to join?

## Environment Context
- **Tenant Type:** Hybrid (federated or managed domains)
- **Configuration:** AD FS or Microsoft Entra seamless single sign-on

## Symptoms
- Device was not Microsoft Entra hybrid joined
- Attempt to do Microsoft Entra hybrid join fails

## Error Codes
N/A

## Root Causes
1. Misconfigured AD FS or Microsoft Entra ID
2. Network issues
3. Autoworkplace.exe is unable to silently authenticate with Microsoft Entra ID or AD FS
4. Missing or misconfigured AD FS (for federated domains)
5. Missing or misconfigured Microsoft Entra seamless single sign-on (for managed domains)
6. Multifactor authentication (MFA) is enabled/configured for the user and WIAORMULTIAUTHN isn't configured at the AD FS server
7. Home realm discovery (HRD) page is waiting for user interaction, which prevents autoworkplace.exe from silently requesting a token
8. AD FS and Microsoft Entra URLs are missing in IE's intranet zone on the client
9. Network connectivity issues preventing autoworkplace.exe from reaching AD FS or the Microsoft Entra URLs
10. Autoworkplace.exe requires the client to have direct line of sight to the organization's on-premises AD domain controller
11. https://autologon.microsoftazuread-sso.com isn't present on the device's IE intranet settings (for Microsoft Entra seamless single sign-on)
12. The internet setting 'Do not save encrypted pages to disk' is checked

## Remediation Steps
1. Click on the 'Join' button to attempt Microsoft Entra hybrid join
2. Review the failure details shown after the failed join attempt

## Validation
1. On the affected device, open a PowerShell console as Administrator and run: dsregcmd /status. Verify that 'AzureAdJoined' is 'YES' and 'DomainJoined' is 'YES'. 2. In the output, check that 'Device Name' matches the on-premises computer name and 'DomainName' matches the on-premises domain. 3. Run: dsregcmd /status | findstr 'SSO State' and confirm 'AzureAdPrt' is 'YES'. 4. Sign in to https://portal.azure.com, navigate to 'Microsoft Entra ID' > 'Devices' > 'All devices', and confirm the device appears with 'Hybrid Azure AD joined' as the join type.

## Rollback
1. On the affected device, open a PowerShell console as Administrator and run: dsregcmd /leave. 2. Restart the device. 3. If the device was manually registered in Microsoft Entra ID, sign in to https://portal.azure.com, go to 'Microsoft Entra ID' > 'Devices' > 'All devices', locate the device, and select 'Delete' to remove it. 4. Verify the device no longer appears in the Microsoft Entra devices list and that dsregcmd /status shows 'AzureAdJoined: NO'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-legacy>
