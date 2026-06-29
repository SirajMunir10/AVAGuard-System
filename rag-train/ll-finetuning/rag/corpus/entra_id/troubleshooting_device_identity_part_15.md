# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Entra hybrid join failure after user UPN change on downlevel Windows devices?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Downlevel Windows devices; Seamless SSO configured

## Symptoms
- Microsoft Entra hybrid join fails after user UPN change
- Seamless SSO authentication process breaks

## Error Codes
N/A

## Root Causes
1. Browser session cookies not cleared or user did not explicitly sign out and remove old UPN, causing the join process to send the previous UPN to Microsoft Entra ID

## Remediation Steps
1. Clear browser session cookies
2. User explicitly signs out and removes old UPN

## Validation
1. On the downlevel Windows device, open Internet Explorer and navigate to https://login.microsoftonline.com. 2. Press F12 to open Developer Tools, select the 'Network' tab, and clear the browser cache and cookies via the browser settings (e.g., Tools > Safety > Delete browsing history > check 'Cookies and saved website data' and 'Temporary Internet files'). 3. Close all browser windows. 4. Open a new browser session and navigate to https://portal.azure.com. 5. Sign in with the user's new UPN. 6. Verify that the user can authenticate successfully without being prompted for the old UPN. 7. On the same device, run 'dsregcmd /status' from an elevated command prompt and confirm that 'AzureAdJoined' shows 'YES' and 'DomainJoined' shows 'YES'. 8. In the Microsoft Entra admin center, go to 'Identity > Devices > All devices' and confirm the device appears with the correct user and status 'Hybrid Azure AD joined'.

## Rollback
1. If the remediation fails, instruct the user to sign out of all applications and close all browser sessions. 2. On the downlevel device, open Internet Explorer, go to Tools > Safety > Delete browsing history, and uncheck 'Cookies and saved website data' and 'Temporary Internet files' to restore previous cookies. 3. Restart the device. 4. Have the user sign in with the old UPN to restore the previous authentication state. 5. Re-attempt the hybrid join process using the old UPN to confirm the device returns to its previous joined state. 6. If the issue persists, refer to the official troubleshooting guide at https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-legacy for additional steps.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-legacy>
