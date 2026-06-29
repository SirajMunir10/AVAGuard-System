# Troubleshooting: Hybrid Join

**Domain:** Entra ID
**Subdomain:** Hybrid Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to retrieve the Primary Refresh Token (PRT) status on a hybrid-joined Windows device?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Hybrid Azure AD joined Windows device

## Symptoms
- AzureAdPrt field is set to NO
- AzureAdPrtUpdateTime is more than four hours

## Error Codes
N/A

## Root Causes
1. Error acquiring the PRT status from Microsoft Entra ID
2. Issue with refreshing the PRT

## Remediation Steps
1. Open a Command Prompt window in the context of the logged-in user.
2. Run dsregcmd /status.
3. Check the 'SSO state' section for the current PRT status.
4. If AzureAdPrt is NO, there was an error acquiring the PRT status from Microsoft Entra ID.
5. If AzureAdPrtUpdateTime is more than four hours, lock and unlock the device to force the PRT refresh, then check whether the time updates.

## Validation
After locking and unlocking the device, run dsregcmd /status again and verify that AzureAdPrtUpdateTime has updated.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
