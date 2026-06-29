# Troubleshooting: Authentication (AADSTS50126)

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve AADSTS50126: Error validating credentials due to invalid username or password during hybrid join?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** password hash sync enabled

## Symptoms
- Username and password entered by user in Windows LoginUI are incorrect

## Error Codes
- `AADSTS50126`

## Root Causes
1. New password hasn't synced with Microsoft Entra ID after password change
2. Incorrect username or password entered

## Remediation Steps
1. Wait for the Microsoft Entra password sync to finish to acquire a fresh PRT with the new credentials

## Validation
1. On the affected Windows device, sign out and sign in again using the new password. 2. Run 'dsregcmd /status' and verify that 'AzureAdPrt' equals 'YES'. 3. In the Microsoft Entra admin center, navigate to Identity > Devices > All devices, locate the device, and confirm that 'Hybrid Azure AD joined' shows 'Yes' and the 'Last sign-in' time is recent. 4. Check the Microsoft Entra Connect Health dashboard to confirm that the last password hash sync completed successfully within the expected interval.

## Rollback
1. If the PRT is still not acquired, instruct the user to reset their password again and wait for the next password hash sync cycle (default 2 minutes). 2. If the issue persists, verify that password hash synchronization is enabled in Microsoft Entra Connect by running 'Get-ADSyncAADPasswordSyncConfiguration' on the sync server. 3. If sync is disabled, re-enable it using the Microsoft Entra Connect wizard or by running 'Set-ADSyncAADPasswordSyncConfiguration -Enable $true'. 4. As a last resort, force a full password hash sync by running 'Start-ADSyncSyncCycle -PolicyType Delta' on the sync server.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
