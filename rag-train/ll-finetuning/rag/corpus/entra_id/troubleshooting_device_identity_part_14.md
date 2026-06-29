# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra hybrid join for downlevel Windows devices (Windows 8.1, Windows Server 2008 R2, Windows Server 2012, Windows Server 2012 R2)?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Downlevel Windows devices (Windows 8.1, Windows Server 2008 R2, Windows Server 2012, Windows Server 2012 R2); requires AD FS for federated domains or Seamless SSO for managed domains

## Symptoms
- Microsoft Entra hybrid join fails for downlevel Windows devices
- Same physical device appears multiple times in Microsoft Entra ID when multiple domain users sign-in
- Multiple entries for a device on the user info tab after OS reinstallation or manual re-registration
- Microsoft Entra hybrid join fails after user UPN change

## Error Codes
N/A

## Root Causes
1. Service Connection Point (SCP) configured to point to managed domain name (e.g., contoso.onmicrosoft.com) instead of federated domain name (e.g., contoso.com) for federated domains
2. Seamless SSO not working in private browsing mode on Firefox and Microsoft Edge browsers
3. Seamless SSO not working on Internet Explorer in Enhanced Protected mode or with Enhanced Security Configuration enabled
4. Missing KB4284842 on Windows 7 SP1 or Windows Server 2008 R2 SP1
5. User UPN changed without clearing browser session cookies or signing out, causing old UPN to be sent during join

## Remediation Steps
1. Ensure AD FS is configured for federated domains or Seamless SSO is configured for managed domains
2. Verify SCP configuration points to the correct federated domain name (e.g., contoso.com) for federated domains
3. Install KB4284842 on Windows 7 SP1 or Windows Server 2008 R2 SP1
4. Clear browser session cookies or have user explicitly sign out and remove old UPN after UPN change

## Validation
1. On a downlevel Windows device, open an elevated command prompt and run: `dsregcmd.exe /status`. Verify that the 'AzureAdJoined' field shows 'YES' and the 'DomainName' field matches the federated domain (e.g., contoso.com) or managed domain as appropriate. 2. In the Microsoft Entra admin center, navigate to Identity > Devices > All devices. Search for the device by its hostname. Confirm only one device entry exists and that the 'Join Type' is 'Hybrid Azure AD joined'. 3. For a user whose UPN changed, have the user sign out of all browser sessions, clear cookies, and sign in again. Then run `dsregcmd.exe /status` and verify the 'UserEmail' field reflects the new UPN. 4. On Windows 7 SP1 or Windows Server 2008 R2 SP1, verify that KB4284842 is installed by running `wmic qfe list brief /format:texttable` and checking for the KB number.

## Rollback
1. If SCP was changed, revert the SCP configuration to the previous domain name using the same method (e.g., `Set-ADObject` or Group Policy). 2. If Seamless SSO was enabled, disable it by running `Update-AzureADSSOStatus -Enable $false` in Azure AD PowerShell. 3. If KB4284842 was installed, uninstall it via Control Panel > Programs > View installed updates, or by running `wusa /uninstall /kb:4284842 /quiet /norestart`. 4. If browser cookies were cleared, no rollback is possible; users can re-authenticate normally. 5. If a device was re-registered, remove the duplicate device entry from the Microsoft Entra admin center (Identity > Devices > All devices > select device > Delete) and re-initiate hybrid join via the original method.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-legacy>
