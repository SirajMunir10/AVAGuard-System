# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra device join failures using dsregcmd output, specifically when authentication fails and sync-join fallback behavior is involved?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows 10 1803 or later, registry key Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CDJ with value FallbackToSyncJoin

## Symptoms
- Authentication fails during device join
- Sync-join is attempted as fallback unless explicitly disabled
- Join errors in the authentication phase

## Error Codes
N/A

## Root Causes
1. Token acquisition test fails when user tenant is federated
2. Fallback to sync-join is enabled by default (no registry key or key set to 0x1)
3. Fallback to sync-join is disabled via registry key set to 0x0

## Remediation Steps
1. Check the registry key Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CDJ with value FallbackToSyncJoin
2. Set the value to 0x0 to disable fallback to sync-join, or 0x1 to enable it
3. Review dsregcmd output for Error Phase values: pre-check, discover, auth, join
4. Review Client ErrorCode (HRESULT), Server ErrorCode, Server Message, Https Status, and Request ID for correlation with server-side logs

## Validation
1. Open Command Prompt as Administrator and run 'dsregcmd /status'. 2. In the output, verify that 'AzureAdJoined' is 'YES' and 'DomainJoined' is 'NO' (or appropriate). 3. Check the 'Last Error Phase' field; it should not be 'auth' or 'join'. 4. Confirm 'Client ErrorCode' is 0 (S_OK) and 'Server ErrorCode' is 0. 5. Navigate to registry path 'Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CDJ' and verify that 'FallbackToSyncJoin' DWORD value is set to 0x0 (disabled) if fallback is not desired, or 0x1 (enabled) if fallback is intended. 6. Run 'dsregcmd /join' again and confirm no authentication errors appear.

## Rollback
1. Open Registry Editor as Administrator. 2. Navigate to 'Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CDJ'. 3. If 'FallbackToSyncJoin' was changed, set it back to its original value (0x0 to disable fallback, 0x1 to enable fallback). 4. If the key was deleted, recreate it as a DWORD with the original value. 5. Run 'dsregcmd /leave' to unjoin the device from Microsoft Entra ID. 6. Run 'dsregcmd /join' to reattempt the join with the original fallback behavior. 7. Verify the join outcome using 'dsregcmd /status' and check for any errors.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
