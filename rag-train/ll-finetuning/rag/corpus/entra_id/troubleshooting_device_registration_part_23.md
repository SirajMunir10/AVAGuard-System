# Troubleshooting: Device Registration (0x801c03f2)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot a device registration failure with HTTP 400 status, client error 0x801c03f2, and server message 'The device object by the given id isn't found' during a sync-join?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Fallback to Sync-Join: ENABLED; Registration Type: sync; Error Phase: join

## Symptoms
- HTTP Status 400
- Client ErrorCode: 0x801c03f2
- Server ErrorCode: DirectoryError
- Server Message: The device object by the given id (aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb) isn't found.

## Error Codes
- `0x801c03f2`
- `DirectoryError`

## Root Causes
1. The device object referenced by the given ID is not found in the directory.

## Remediation Steps
N/A

## Validation
1. On the affected device, open Command Prompt as Administrator and run 'dsregcmd /status'. Verify that 'AzureAdJoined' shows 'YES' and 'DomainJoined' shows 'YES'. 2. Confirm that the device is listed in the Entra ID portal under 'Devices' > 'All devices' and that the 'Join Type' is 'Hybrid Azure AD joined'. 3. Run 'dsregcmd /status' and check that the 'DeviceId' matches the ID that was previously missing. 4. Verify that the device can authenticate by running 'dsregcmd /status' and ensuring 'Last PSS Sign In Time' is recent.

## Rollback
1. If the remediation fails, remove the device from Entra ID by running 'dsregcmd /leave' on the device as Administrator. 2. Restart the device. 3. Re-initiate the sync-join by running 'dsregcmd /join' as Administrator. 4. If issues persist, disable 'Fallback to Sync-Join' temporarily by setting the registry key 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CDJ' > 'FallbackToSyncJoin' to 0, then re-enable after troubleshooting.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
